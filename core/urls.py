from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("hizmetler/", views.services_page, name="services"),
    path("hizmetler/<slug:slug>/", views.service_detail, name="service_detail"),
    path("calismalarimiz/", views.works, name="works"),
    path("yorumlar/", views.reviews, name="reviews"),
    path("servis-talebi/", views.service_request, name="service_request"),
    path("iletisim/", views.contact, name="contact"),
]
