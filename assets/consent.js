/* Cookie-Einwilligung für Google Analytics 4.
   GA (gtag.js) wird erst nach „Akzeptieren“ geladen. Vorher werden keine Analysedaten gesendet.
   Footer-Links mit data-consent-open öffnen die Auswahl erneut (Widerruf). */
(function () {
  var GA_ID = 'G-LTG3V4SS14';
  var KEY = 'rmh_consent_ga_v1';
  var loaded = false;

  window.dataLayer = window.dataLayer || [];

  function read() {
    try { return window.localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function write(value) {
    try { window.localStorage.setItem(KEY, value); } catch (e) { /* ohne Speicher: Auswahl gilt nur für diese Seite */ }
  }

  var state = read();

  // gtag-Aufrufe der Seiten: ohne Einwilligung verworfen, Weiterleitungs-Callbacks laufen trotzdem sofort.
  window.gtag = function () {
    if (state === 'granted') {
      window.dataLayer.push(arguments);
      return;
    }
    var params = arguments[2];
    if (params && typeof params.event_callback === 'function') {
      params.event_callback();
    }
  };

  function loadGA() {
    if (loaded) { return; }
    loaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.gtag('js', new Date());
    window.gtag('config', GA_ID);
  }

  function clearGACookies() {
    var host = window.location.hostname;
    var domains = ['', host, '.' + host, '.' + host.split('.').slice(-2).join('.')];
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (name === '_ga' || name.indexOf('_ga_') === 0) {
        domains.forEach(function (d) {
          document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + (d ? '; domain=' + d : '');
        });
      }
    });
  }

  var banner;

  function hide() {
    if (banner) { banner.remove(); banner = null; }
  }

  function decide(value) {
    var before = state;
    state = value;
    write(value);
    hide();
    if (value === 'granted') {
      loadGA();
      return;
    }
    clearGACookies();
    if (before === 'granted') {
      window.location.reload();
    }
  }

  function privacyHref() {
    var el = document.querySelector('a[href$="datenschutz.html"]');
    return el ? el.getAttribute('href') : '/datenschutz.html';
  }

  function show() {
    if (banner) { return; }
    if (!document.getElementById('rmh-consent-style')) {
      var css = document.createElement('style');
      css.id = 'rmh-consent-style';
      css.textContent =
        '.rmh-consent{position:fixed;left:12px;right:12px;bottom:12px;z-index:1000;max-width:640px;margin:0 auto;' +
        'background:#151a20;color:#eef3f5;border:1px solid #2a333d;border-radius:16px;padding:18px 18px 16px;' +
        'box-shadow:0 20px 60px rgba(0,0,0,.45);font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif;font-size:14.5px;line-height:1.5}' +
        '.rmh-consent p{margin:0 0 14px;color:#d4dce2}' +
        '.rmh-consent strong{color:#fff}' +
        '.rmh-consent a{color:#98f2c5}' +
        '.rmh-consent .rmh-row{display:flex;gap:10px}' +
        '.rmh-consent button{flex:1;min-height:46px;border-radius:12px;font:inherit;font-weight:700;cursor:pointer;border:1px solid #3fcf8e}' +
        '.rmh-consent .rmh-no{background:transparent;color:#eef3f5}' +
        '.rmh-consent .rmh-yes{background:#3fcf8e;color:#07120c}' +
        '.rmh-consent button:focus-visible{outline:3px solid #98f2c5;outline-offset:2px}';
      document.head.appendChild(css);
    }
    banner = document.createElement('div');
    banner.className = 'rmh-consent';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-live', 'polite');
    banner.setAttribute('aria-label', 'Cookie-Einstellungen');
    banner.innerHTML =
      '<p><strong>Darf ich messen, wie die Seite genutzt wird?</strong> Mit deiner Einwilligung nutze ich Google Analytics. ' +
      'Dabei werden Cookies gesetzt und Nutzungsdaten an Google übertragen, auch in die USA. Ohne Einwilligung passiert das nicht. ' +
      'Du kannst deine Wahl jederzeit über „Cookie-Einstellungen“ unten auf der Seite ändern. ' +
      '<a href="' + privacyHref() + '">Datenschutzerklärung</a></p>' +
      '<div class="rmh-row"><button type="button" class="rmh-no">Ablehnen</button>' +
      '<button type="button" class="rmh-yes">Akzeptieren</button></div>';
    banner.querySelector('.rmh-no').addEventListener('click', function () { decide('denied'); });
    banner.querySelector('.rmh-yes').addEventListener('click', function () { decide('granted'); });
    document.body.appendChild(banner);
  }

  if (state === 'granted') {
    loadGA();
  }

  function init() {
    if (state !== 'granted') { clearGACookies(); }
    document.querySelectorAll('[data-consent-open]').forEach(function (el) {
      el.addEventListener('click', function (event) { event.preventDefault(); show(); });
    });
    if (state !== 'granted' && state !== 'denied') { show(); }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
