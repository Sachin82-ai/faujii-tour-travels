(function () {
  var items = document.querySelectorAll('.g-item');
  document.querySelectorAll('.filter').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.filter').forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active');
      items.forEach(function (i) {
        i.style.display = (b.dataset.filter === 'all' || i.dataset.cat === b.dataset.filter) ? '' : 'none';
      });
    });
  });
  var lb = document.getElementById('lightbox');
  if (!lb) return;
  document.querySelectorAll('.g-img').forEach(function (img) {
    img.addEventListener('click', function () {
      lb.querySelector('img').src = img.src;
      lb.classList.add('open');
    });
  });
  lb.addEventListener('click', function () { lb.classList.remove('open'); });
})();
