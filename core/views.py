"""Özdemir Teknik Servis sayfaları ve ortak içerik verileri."""
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ServiceRequestForm

# ── İletişim / işletme bilgileri ────────────────────────────────────────────
BUSINESS = {
    "name": "Özdemir Teknik Servis",
    "phone_display": "0507 123 33 31",
    "phone_e164": "+905071233331",
    "whatsapp_plain": "https://wa.me/905071233331",
    "whatsapp_text": (
        "https://wa.me/905071233331?text="
        "Merhaba%2C%20ar%C4%B1za%20%2F%20bak%C4%B1m%20i%C3%A7in"
        "%20bilgi%20almak%20istiyorum."
    ),
    "address": "15 Mayıs Mah., Gazi Mustafa Kemal Blv. No:105 D:15, Pamukkale / Denizli",
    "region": "Pamukkale / Denizli",
    "hours": "24 saat açık — her gün",
    "rating": "5,0",
    "review_count": 85,
    "maps_query": (
        "%C3%96zdemir%20Teknik%20Servis%2C%20Gazi%20Mustafa%20Kemal%20"
        "Bulvar%C4%B1%20No%3A105%2C%20Pamukkale%2C%20Denizli"
    ),
}
BUSINESS["maps_embed"] = (
    "https://maps.google.com/maps?q=" + BUSINESS["maps_query"] +
    "&z=15&hl=tr&output=embed"
)
BUSINESS["maps_directions"] = (
    "https://www.google.com/maps/dir/?api=1&destination=" + BUSINESS["maps_query"]
)
BUSINESS["maps_search"] = (
    "https://www.google.com/maps/search/?api=1&query=" + BUSINESS["maps_query"]
)

# ── Hizmetler ───────────────────────────────────────────────────────────────
SERVICES = [
    {
        "icon": "ac",
        "slug": "klima-servisi",
        "title": "Klima Bakım & Tamir",
        "desc": "Periyodik bakım, gaz dolumu, derin temizlik ve arıza onarımı. "
                "Montaj ve sökme-takma dahil.",
    },
    {
        "icon": "flame",
        "slug": "kombi-servisi",
        "title": "Kombi Bakım & Tamir",
        "desc": "Tüm markalarda yıllık bakım, petek temizliği, sıcak su ve basınç "
                "arızaları. Aynı gün servis.",
    },
    {
        "icon": "washer",
        "slug": "beyaz-esya-servisi",
        "title": "Beyaz Eşya Tamir & Bakım",
        "desc": "Çamaşır ve bulaşık makinesi, buzdolabı, fırın arızaları. "
                "Orijinal parça, işçilik garantili.",
    },
]

SALES = [
    {
        "title": "Klima Satışı",
        "desc": "İhtiyacınıza uygun inverter klima seçimi, ücretsiz keşif ve montaj "
                "dahil anahtar teslim kurulum.",
        "highlight": True,
    },
    {
        "title": "Kombi Satışı",
        "desc": "Yoğuşmalı kombi modelleri, eski cihaz sökümü ve yeni cihaz "
                "montajıyla birlikte teslim.",
        "highlight": False,
    },
]

# ── Çalışma süreci ──────────────────────────────────────────────────────────
STEPS = [
    {
        "no": "01",
        "title": "Arayın ya da yazın",
        "desc": "Telefonla veya WhatsApp'tan ulaşın, arızanızı kısaca anlatın. "
                "7/24 dönüş yapıyoruz.",
    },
    {
        "no": "02",
        "title": "Aynı gün yerinde tespit",
        "desc": "Denizli genelinde kapınıza gelir, arızayı yerinde tespit eder, "
                "işleme başlamadan net fiyat veririz.",
    },
    {
        "no": "03",
        "title": "Garantili teslim",
        "desc": "Onarım biter, cihazınız çalışır halde teslim edilir. İşçilik ve "
                "parça garantisi bizden.",
    },
]

BRANDS = (
    "Arçelik · Vestel · Bosch · Siemens · Samsung · LG · Daikin · "
    "Mitsubishi Electric · Vaillant · Demirdöküm · Baymak · ECA · Ferroli · "
    "Protherm ve diğerleri"
)

# ── Güven şeridi (sayaçlar) — hepsi sitede zaten geçen doğrulanabilir değerler
STATS = [
    {"value": 5.0, "decimals": 1, "prefix": "", "suffix": "", "label": "Google puanı"},
    {"value": 85, "decimals": 0, "prefix": "", "suffix": "+", "label": "mutlu müşteri yorumu"},
    {"value": 24, "decimals": 0, "prefix": "", "suffix": "", "label": "saat kesintisiz hizmet"},
    {"value": 100, "decimals": 0, "prefix": "%", "suffix": "", "label": "garantili işçilik"},
]

# ── Galeri (fotoğraflar static/img altında; kredi bilgisi CREDITS.md'de) ─────
GALLERY = [
    {"img": "img/galeri-klima.jpg", "alt": "Duvar tipi split klima ünitesi",
     "credit": "Zulfugar Karimov / Unsplash"},
    {"img": "img/galeri-kombi.jpg", "alt": "Kombi ve tesisat bakımı",
     "credit": "Timur Shakerzianov / Unsplash"},
    {"img": "img/galeri-beyaz-esya.jpg", "alt": "Çamaşır makinesi servisi",
     "credit": "Oli Woodman / Unsplash"},
    {"img": "img/galeri-aletler.jpg", "alt": "Teknik servis el aletleri",
     "credit": "Barn Images / Unsplash"},
]

# ── Müşteri yorumları (Google) ──────────────────────────────────────────────
TESTIMONIALS = [
    {
        "name": "Ertuğrul K.",
        "tag": "Yerel Rehber",
        "text": "Kombi bakımı için anlaştık. Yarım saat gibi kısa bir sürede tüm "
                "bakımı yaptılar ve sıcak su problemini çözdüler. Gönül rahatlığıyla "
                "tercih edebilirsiniz.",
    },
    {
        "name": "Hatice Ç.",
        "tag": "",
        "text": "Klima temizliği ve bakımı yaptırdım. İşini bu kadar titizlikle yapan "
                "bir firmaya denk gelmedim. Bundan sonra tek tercihimiz.",
    },
    {
        "name": "Melisa A.",
        "tag": "",
        "text": "Hem hızlı hem de çok ilgiliydiler, sorunum kısa sürede çözüldü. "
                "Gönül rahatlığıyla tavsiye ederim.",
    },
]

# ── Sık sorulan sorular ─────────────────────────────────────────────────────
FAQ = [
    {
        "q": "Aynı gün gelebiliyor musunuz?",
        "a": "Evet. 24 saat açığız; Pamukkale ve Merkezefendi'deki çağrıların büyük "
             "bölümüne aynı gün gidiyoruz. Acil durumlarda telefonla arayın, en hızlı "
             "şekilde yönlendirelim.",
    },
    {
        "q": "Fiyat nasıl belirleniyor?",
        "a": "Arıza yerinde tespit edilir ve işleme başlamadan önce net fiyat "
             "bildirilir. Onayınız olmadan hiçbir işlem yapılmaz, sürpriz ücret çıkmaz.",
    },
    {
        "q": "Garanti veriyor musunuz?",
        "a": "Evet. İşçiliğimiz ve taktığımız parçalar garantilidir. Sattığımız klima "
             "ve kombiler ise resmi distribütör garantisiyle, montaj dahil teslim edilir.",
    },
    {
        "q": "Hangi marka ve bölgelere bakıyorsunuz?",
        "a": "Arçelik'ten Daikin'e, Vaillant'tan Bosch'a tüm markaların klima, kombi ve "
             "beyaz eşyalarına bakıyoruz. Merkez Pamukkale olmak üzere Denizli genelinde "
             "yerinde servis veriyoruz.",
    },
]

SERVICE_DETAILS = {
    "klima-servisi": {
        "eyebrow": "Klima Servisi",
        "headline": "Klimanız daha sessiz, temiz ve verimli çalışsın",
        "lead": (
            "Denizli genelinde split klima bakım, arıza tespiti, gaz dolumu, "
            "derin temizlik, montaj ve sökme-takma hizmeti."
        ),
        "features": [
            "İç ve dış ünite detaylı temizlik",
            "Gaz basıncı ve kaçak kontrolü",
            "Elektrik bağlantıları ve drenaj testi",
            "Montaj, sökme ve yer değişikliği",
            "Tüm markalarda arıza tespiti",
            "İşçilik ve değişen parça garantisi",
        ],
        "issues": [
            "Yeterince soğutmuyor veya ısıtmıyor",
            "Su akıtıyor ya da kötü koku yapıyor",
            "Yüksek sesle çalışıyor",
            "Sık sık kapanıyor veya hata kodu veriyor",
        ],
        "faq": [
            {
                "q": "Klima bakımı ne sıklıkla yapılmalı?",
                "a": "Ev tipi klimalarda yılda en az bir kez, yoğun kullanılan cihazlarda sezon öncesi ve sonrası bakım öneriyoruz.",
            },
            {
                "q": "Klima gazı her bakımda doldurulur mu?",
                "a": "Hayır. Gaz seviyesi ölçülür; eksilme varsa önce kaçak kontrolü yapılır, ardından ihtiyaç kadar dolum uygulanır.",
            },
        ],
        "image": "img/galeri-klima.jpg",
        "image_alt": "Duvar tipi split klima bakım hizmeti",
    },
    "kombi-servisi": {
        "eyebrow": "Kombi Servisi",
        "headline": "Sıcak su ve ısınma sorunlarını aynı gün çözelim",
        "lead": (
            "Kombi yıllık bakımı, petek temizliği, basınç ve sıcak su arızaları "
            "için Denizli genelinde yerinde teknik servis."
        ),
        "features": [
            "Yanma odası ve eşanjör temizliği",
            "Genleşme tankı ve basınç kontrolü",
            "Sıcak su ve kalorifer devresi testi",
            "Petek ve tesisat temizliği",
            "Parça değişiminden önce net fiyat",
            "Garantili işçilik",
        ],
        "issues": [
            "Sıcak su gelmiyor veya dalgalanıyor",
            "Kombi basıncı sürekli düşüyor",
            "Petekler eşit ısınmıyor",
            "Cihaz ses yapıyor veya hata kodu veriyor",
        ],
        "faq": [
            {
                "q": "Kombi bakımı ne zaman yapılmalı?",
                "a": "Yılda bir kez, tercihen kış sezonu başlamadan önce yapılması cihazın güvenli ve verimli çalışmasına yardımcı olur.",
            },
            {
                "q": "Petek temizliği her yıl gerekli mi?",
                "a": "Her yıl şart değildir. Isınma dengesizliği, alt kısımların soğuk kalması veya yüksek tüketim varsa kontrol edilmelidir.",
            },
        ],
        "image": "img/galeri-kombi.jpg",
        "image_alt": "Kombi ve tesisat bakım hizmeti",
    },
    "beyaz-esya-servisi": {
        "eyebrow": "Beyaz Eşya Servisi",
        "headline": "Günlük hayatı durduran arızaları hızlıca giderelim",
        "lead": (
            "Çamaşır ve bulaşık makinesi, buzdolabı ve fırın arızalarında "
            "yerinde tespit, onarım ve garantili parça değişimi."
        ),
        "features": [
            "Yerinde arıza tespiti",
            "Onay öncesi net fiyat bilgisi",
            "Uygun ve garantili parça kullanımı",
            "Su alma ve tahliye sorunları",
            "Soğutma ve ısıtma arızaları",
            "İşlem sonrası çalışma testi",
        ],
        "issues": [
            "Makine su almıyor veya boşaltmıyor",
            "Buzdolabı yeterince soğutmuyor",
            "Fırın ısıtmıyor veya sigorta attırıyor",
            "Cihaz ses yapıyor ya da programı tamamlamıyor",
        ],
        "faq": [
            {
                "q": "Arıza evde tamir edilebilir mi?",
                "a": "Arızaların büyük bölümü yerinde giderilir. Atölye işlemi gerekirse cihazın durumu ve süreç önceden açıklanır.",
            },
            {
                "q": "Değişen parçaya garanti veriliyor mu?",
                "a": "Evet. Kullanılan parça ve yapılan işçilik için işlem türüne göre garanti bilgisi teslim sırasında paylaşılır.",
            },
        ],
        "image": "img/galeri-beyaz-esya.jpg",
        "image_alt": "Beyaz eşya bakım ve onarım hizmeti",
    },
}

HERO_IMAGE = {
    "img": "img/hero-klima-salon.jpg",
    "alt": "Modern aydınlık salonda panel üzerine monte duvar tipi split klima",
    "credit": "Caroline Badran / Unsplash",
}


def _site_context(active_page="", **extra):
    context = {
        "b": BUSINESS,
        "services": SERVICES,
        "sales": SALES,
        "steps": STEPS,
        "brands": BRANDS,
        "stats": STATS,
        "gallery": GALLERY,
        "hero_image": HERO_IMAGE,
        "testimonials": TESTIMONIALS,
        "faq": FAQ,
        "active_page": active_page,
    }
    context.update(extra)
    return context


def index(request):
    # Eski ana sayfa formuna gönderilen kayıtları yeni form sayfasına yönlendir.
    if request.method == "POST":
        return service_request(request)
    return render(request, "index.html", _site_context("home"))


def services_page(request):
    return render(request, "services.html", _site_context("services"))


def service_detail(request, slug):
    summary = next((item for item in SERVICES if item["slug"] == slug), None)
    detail = SERVICE_DETAILS.get(slug)
    if summary is None or detail is None:
        raise Http404("Hizmet bulunamadı")
    service = {**summary, **detail}
    return render(
        request,
        "service_detail.html",
        _site_context("services", service=service),
    )


def works(request):
    return render(request, "works.html", _site_context("works"))


def reviews(request):
    return render(request, "reviews.html", _site_context("reviews"))


def service_request(request):
    form = ServiceRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        if not form.is_spam():
            form.save()
        return redirect(f"{reverse('core:service_request')}?talep=ok")

    return render(
        request,
        "service_request.html",
        _site_context(
            "request",
            form=form,
            talep_ok=request.GET.get("talep") == "ok",
        ),
    )


def contact(request):
    return render(request, "contact.html", _site_context("contact"))
