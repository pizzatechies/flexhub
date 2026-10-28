// Mobile menu, sticky-nav border, scroll reveal and screenshot lightbox.
(() => {
  const nav = document.querySelector('.nav');
  const links = document.querySelector('.nav-links');
  document.querySelector('.menu-btn')?.addEventListener('click', () => links.classList.toggle('open'));
  links?.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => links.classList.remove('open')));
  const onScroll = () => nav?.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const io = 'IntersectionObserver' in window
    ? new IntersectionObserver((entries) => entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.12 })
    : null;
  document.querySelectorAll('.reveal').forEach((el) => (io ? io.observe(el) : el.classList.add('in')));

  const box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.innerHTML = '<img alt="">';
  document.body.appendChild(box);
  const close = () => box.classList.remove('open');
  box.addEventListener('click', close);
  document.addEventListener('keydown', (e) => e.key === 'Escape' && close());
  document.querySelectorAll('img.zoom').forEach((img) => img.addEventListener('click', () => {
    box.querySelector('img').src = img.src;
    box.querySelector('img').alt = img.alt;
    box.classList.add('open');
  }));

  // Pricing: switch every plan between monthly and annual rates.
  document.querySelectorAll('.billing-toggle').forEach((toggle) => toggle.addEventListener('click', (e) => {
    const btn = e.target.closest('button[data-period]');
    if (!btn) return;
    const period = btn.dataset.period;
    toggle.querySelectorAll('button').forEach((b) => b.classList.toggle('on', b === btn));
    const scope = toggle.closest('section') || document;
    scope.querySelectorAll('.plan-price, .plan-per').forEach((el) => { el.textContent = el.dataset[period]; });
    scope.querySelectorAll('.plan-cta').forEach((a) => { a.href = a.dataset[period]; });
  }));

  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
