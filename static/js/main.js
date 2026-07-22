/* Özdemir Teknik Servis — küçük etkileşimler (harici bağımlılık yok) */
(function () {
  "use strict";

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
