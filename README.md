# Özdemir Teknik Servis — Django Sitesi

Denizli Pamukkale merkezli klima, kombi ve beyaz eşya teknik servisi için
çok sayfalı kurumsal web sitesi.

## Sayfalar

- `/` — kısa, dönüşüm odaklı ana sayfa
- `/hizmetler/` — tüm hizmetler ve satış-montaj bilgileri
- `/hizmetler/klima-servisi/`
- `/hizmetler/kombi-servisi/`
- `/hizmetler/beyaz-esya-servisi/`
- `/calismalarimiz/` — çalışma galerisi
- `/yorumlar/` — müşteri değerlendirmeleri
- `/servis-talebi/` — servis talep formu
- `/iletisim/` — adres, telefon ve harita

## Yerel kurulum

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
# source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Site: `http://127.0.0.1:8000`

## İçerik düzenleme

- İşletme bilgileri, hizmetler, yorumlar ve SSS: `core/views.py`
- URL yapısı: `core/urls.py`
- Ortak navbar, footer ve sabit iletişim barı: `templates/base.html`
- Sayfa şablonları: `templates/`
- Renkler ve tüm görsel stiller: `static/css/style.css`
- Etkileşimler: `static/js/main.js`

Servis talebi kayıtları Django admin panelinde `/admin/` altında tutulur.

## Test

```bash
python manage.py check
python manage.py test core
```

## Canlı ortam

Gerekli ortam değişkenleri:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS=alanadi.com,www.alanadi.com`
- `DJANGO_CSRF_TRUSTED=https://alanadi.com,https://www.alanadi.com`

Güncelleme sonrasında:

```bash
git pull --ff-only origin main
.venv/bin/python manage.py collectstatic --noinput
sudo systemctl restart ozdemir
```
