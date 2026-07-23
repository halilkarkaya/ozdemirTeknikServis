"""
Tek sayfalık tanıtım sitesinin görünümü (view).

Sitenin tüm metin içeriği burada, tek yerde toplanmıştır; şablon (index.html)
bu verileri döngülerle basar. Böylece hizmet, yorum, SSS gibi içerikleri
düzenlemek için HTML'e dokunmanıza gerek kalmaz — sadece bu dosyayı düzenleyin.
"""
from django.shortcuts import render

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
        "title": "Klima Bakım & Tamir",
        "desc": "Periyodik bakım, gaz dolumu, derin temizlik ve arıza onarımı. "
                "Montaj ve sökme-takma dahil.",
    },
    {
        "icon": "flame",
        "title": "Kombi Bakım & Tamir",
        "desc": "Tüm markalarda yıllık bakım, petek temizliği, sıcak su ve basınç "
                "arızaları. Aynı gün servis.",
    },
    {
        "icon": "washer",
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

HERO_IMAGE = {
    "img": "img/hero-klima-salon.jpg",
    "alt": "Modern aydınlık salonda panel üzerine monte duvar tipi split klima",
    "credit": "Caroline Badran / Unsplash",
}


def index(request):
    context = {
        "b": BUSINESS,
        "services": SERVICES,
        "sales": SALES,
        "steps": STEPS,
        "brands": BRANDS,
        "gallery": GALLERY,
        "hero_image": HERO_IMAGE,
        "testimonials": TESTIMONIALS,
        "faq": FAQ,
    }
    return render(request, "index.html", context)
