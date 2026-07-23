"""Servis talebi formu — spam korumalı basit ModelForm."""
from django import forms

from .models import ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    # Honeypot: gerçek kullanıcıya görünmez (CSS ile ekran dışına alınır),
    # botlar genelde her alanı doldurduğu için bu alan doluysa spam sayılır.
    website = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={
        "class": "hp", "tabindex": "-1", "autocomplete": "off", "aria-hidden": "true",
    }))

    class Meta:
        model = ServiceRequest
        fields = ["name", "phone", "device", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Adınız Soyadınız", "autocomplete": "name",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "05xx xxx xx xx", "autocomplete": "tel", "inputmode": "tel",
            }),
            "device": forms.Select(),
            "message": forms.Textarea(attrs={
                "placeholder": "Arızayı kısaca anlatın (opsiyonel)", "rows": 4,
            }),
        }

    def is_spam(self):
        """Honeypot alanı doluysa bot kaydıdır — kaydetmeden sessizce yut."""
        return bool(self.cleaned_data.get("website"))
