(function () {
  var root = document.documentElement;
  var btn = document.getElementById('langToggle');
  if (btn) btn.addEventListener('click', function () {
    var next = root.dataset.lang === 'hi' ? 'en' : 'hi';
    root.dataset.lang = next;
    root.lang = next;
    try { localStorage.setItem('lang', next); } catch (e) {}
  });
})();
