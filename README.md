# Özdemir Teknik Servis — Django Sitesi

Denizli Pamukkale merkezli klima / kombi / beyaz eşya tamir-bakım ve satış
firması için tek sayfalık tanıtım sitesi. Django ile sunulur; tüm metin içeriği
`core/views.py` içinde tek yerde toplanmıştır.

## Kurulum ve çalıştırma

```bash
# 1) (önerilir) sanal ortam
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 2) bağımlılıklar
pip install -r requirements.txt

# 3) veritabanı (oturum/admin için; içerik veritabanı kullanmaz)
python manage.py migrate

# 4) geliştirme sunucusu
python manage.py runserver
```

Ardından tarayıcıdan http://127.0.0.1:8000 adresini açın.

## İçeriği düzenleme

- **Metinler** (hizmetler, yorumlar, SSS, adımlar, markalar, iletişim):
  `core/views.py` — HTML'e dokunmadan buradan düzenleyin.
- **Marka rengi:** `static/css/style.css` içindeki `:root { --accent: #C42B2B }`.
- **Fotoğraflar:** `static/img/` (bkz. `CREDITS.md`).
- **Logo:** `static/logo/` ve şablondaki `templates/_logo.html`.
- **Şablon düzeni:** `templates/index.html`.

## Yapı

```
django-site/
├─ manage.py
├─ requirements.txt
├─ ozdemir_servis/        # proje ayarları (settings, urls, wsgi/asgi)
├─ core/                  # uygulama: view + içerik verisi
├─ templates/             # index.html + _logo.html
└─ static/                # css, js, img, logo
```

## Canlıya (production) çıkış notları

`ozdemir_servis/settings.py` geliştirme için hazırdır. Yayınlarken:

1. Ortam değişkenleri: `DJANGO_SECRET_KEY` (rastgele gizli anahtar),
   `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS=alanadi.com,www.alanadi.com`.
2. `python manage.py collectstatic` çalıştırın.
3. Statik dosyaları bir web sunucusu (Nginx) veya WhiteNoise ile sunun;
   uygulamayı Gunicorn/uWSGI arkasında çalıştırın.

## Notlar

- Telefon numarası `0507 123 33 31` örnek olarak alınmıştır; `core/views.py`
  içindeki `BUSINESS` sözlüğünden güncelleyin.
- Sayfa, yerel SEO için `HVACBusiness` ve `FAQPage` schema.org yapısal verilerini
  içerir (Google zengin sonuçları).
```
