/* Özdemir Teknik Servis — küçük etkileşimler (harici bağımlılık yok) */
(function () {
  "use strict";

  // Açılış animasyonu: erken kapatma + bitince DOM'dan temizle
  var splash = document.getElementById("splash");
  if (splash) {
    var removeSplash = function () {
      if (splash && splash.parentNode) splash.parentNode.removeChild(splash);
    };
    var killSplash = function () {
      splash.classList.add("is-hiding");
      window.removeEventListener("scroll", killSplash);
      window.removeEventListener("wheel", killSplash);
      window.removeEventListener("touchstart", killSplash);
      window.removeEventListener("keydown", killSplash);
      splash.removeEventListener("click", killSplash);
      setTimeout(removeSplash, 450);
    };
    // Doğal bitişte de kaldır (animasyon ~3.05s'de biter)
    setTimeout(removeSplash, 3300);
    window.addEventListener("scroll", killSplash, { passive: true });
    window.addEventListener("wheel", killSplash, { passive: true });
    window.addEventListener("touchstart", killSplash, { passive: true });
    window.addEventListener("keydown", killSplash);
    splash.addEventListener("click", killSplash);
  }

  // Kaydırınca beliren öğeler
  var revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          var el = e.target;
          var delay = parseInt(el.getAttribute("data-delay") || "0", 10);
          el.style.transitionDelay = delay + "ms";
          el.classList.add("is-visible");
          obs.unobserve(el);
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // Hafif paralaks (hero arka plan çizgileri)
  var parallaxEls = document.querySelectorAll("[data-parallax]");
  if (parallaxEls.length) {
    var ticking = false;
    window.addEventListener(
      "scroll",
      function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () {
          var y = window.scrollY;
          parallaxEls.forEach(function (el) {
            var f = parseFloat(el.getAttribute("data-parallax"));
            el.style.transform = "translateY(" + (y * f).toFixed(1) + "px)";
          });
          ticking = false;
        });
      },
      { passive: true }
    );
  }
})();
