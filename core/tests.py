from django.test import TestCase
from django.urls import reverse

from .models import ServiceRequest


class PublicPageTests(TestCase):
    def test_public_pages_render(self):
        routes = [
            reverse("core:index"),
            reverse("core:services"),
            reverse("core:works"),
            reverse("core:reviews"),
            reverse("core:service_request"),
            reverse("core:contact"),
            reverse("core:service_detail", args=["klima-servisi"]),
            reverse("core:service_detail", args=["kombi-servisi"]),
            reverse("core:service_detail", args=["beyaz-esya-servisi"]),
        ]

        for route in routes:
            with self.subTest(route=route):
                self.assertEqual(self.client.get(route).status_code, 200)

    def test_unknown_service_returns_404(self):
        response = self.client.get(
            reverse("core:service_detail", args=["bilinmeyen-servis"])
        )
        self.assertEqual(response.status_code, 404)

    def test_homepage_is_shortened_and_links_to_service_request(self):
        response = self.client.get(reverse("core:index"))
        self.assertContains(response, reverse("core:service_request"))
        self.assertNotContains(response, "<form", html=False)


class ServiceRequestTests(TestCase):
    def test_valid_request_is_saved_and_redirected(self):
        response = self.client.post(
            reverse("core:service_request"),
            {
                "name": "Test Kullanıcı",
                "phone": "0500 000 00 00",
                "device": "klima",
                "message": "Soğutmuyor",
                "website": "",
            },
        )

        self.assertRedirects(
            response,
            f"{reverse('core:service_request')}?talep=ok",
            fetch_redirect_response=False,
        )
        self.assertEqual(ServiceRequest.objects.count(), 1)

    def test_honeypot_submission_is_not_saved(self):
        response = self.client.post(
            reverse("core:service_request"),
            {
                "name": "Bot",
                "phone": "0500 000 00 00",
                "device": "klima",
                "message": "",
                "website": "https://spam.example",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ServiceRequest.objects.count(), 0)
