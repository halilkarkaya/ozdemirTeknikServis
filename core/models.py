"""
Servis talebi modeli — sitedeki "Servis Talebi" formundan gelen kayıtlar.

Django admin panelinden (/admin/) görülür ve yönetilir; ayrı bir e-posta/SMS
altyapısı gerektirmez.
"""
from django.db import models


class ServiceRequest(models.Model):
    DEVICE_CHOICES = [
        ("klima", "Klima"),
        ("kombi", "Kombi"),
        ("beyaz_esya", "Beyaz Eşya"),
        ("diger", "Diğer"),
    ]

    name = models.CharField("Ad Soyad", max_length=80)
    phone = models.CharField("Telefon", max_length=20)
    device = models.CharField("Cihaz", max_length=20, choices=DEVICE_CHOICES, default="klima")
    message = models.TextField("Arıza / Not", blank=True)
    created_at = models.DateTimeField("Geliş Tarihi", auto_now_add=True)
    handled = models.BooleanField("İlgilenildi", default=False)

    class Meta:
        verbose_name = "Servis Talebi"
        verbose_name_plural = "Servis Talepleri"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.get_device_display()}) — {self.created_at:%d.%m.%Y %H:%M}"
