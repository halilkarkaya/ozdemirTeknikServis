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

  // Sayaç şeridi: görününce 0'dan hedef değere say
  var statEls = document.querySelectorAll(".stat-no[data-count]");
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function formatStat(n, decimals, prefix, suffix) {
    var s = decimals > 0 ? n.toFixed(decimals).replace(".", ",") : String(Math.round(n));
    return prefix + s + suffix;
  }

  function animateStat(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduceMotion || !isFinite(target)) {
      el.textContent = formatStat(target, decimals, prefix, suffix);
      return;
    }
    var duration = 1400;
    var start = null;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
      el.textContent = formatStat(target * eased, decimals, prefix, suffix);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if (statEls.length) {
    if ("IntersectionObserver" in window) {
      var statIo = new IntersectionObserver(
        function (entries, obs) {
          entries.forEach(function (e) {
            if (!e.isIntersecting) return;
            animateStat(e.target);
            obs.unobserve(e.target);
          });
        },
        { threshold: 0.4 }
      );
      statEls.forEach(function (el) { statIo.observe(el); });
    } else {
      statEls.forEach(animateStat);
    }
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
