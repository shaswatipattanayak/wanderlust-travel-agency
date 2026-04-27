// ── WANDERLUST MAIN SCRIPT ──
// Handles: scroll animations, image lazy loading, smooth interactions

document.addEventListener('DOMContentLoaded', () => {

  // ── SCROLL REVEAL ──
  // Add .reveal to any element to animate it in on scroll
  const revealEls = document.querySelectorAll(
    '.feature-card, .dest-full-card, .pkg-card, .testimonial-card, .team-card, .value-card, .gallery-item, .s-stat, .stat-box'
  );

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        // Staggered delay based on position
        const delay = (entry.target.dataset.delay || 0) * 80;
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, delay);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  revealEls.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(28px)';
    el.style.transition = 'opacity 0.55s ease, transform 0.55s ease';
    el.dataset.delay = i % 4; // stagger within rows
    observer.observe(el);
  });

  // ── COUNTER ANIMATION for stats ──
  const counters = document.querySelectorAll('.stat-box .number, .s-stat .num');
  const countObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        countObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(el => countObserver.observe(el));

  function animateCounter(el) {
    const text = el.textContent;
    const num = parseFloat(text.replace(/[^0-9.]/g, ''));
    const suffix = text.replace(/[0-9.,]/g, '');
    if (!num) return;

    let start = 0;
    const duration = 1500;
    const step = timestamp => {
      if (!start) start = timestamp;
      const progress = Math.min((timestamp - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease out cubic
      const current = Math.floor(eased * num);
      el.textContent = (num % 1 !== 0 ? current.toFixed(1) : current) + suffix;
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = text; // ensure exact final value
    };
    requestAnimationFrame(step);
  }

  // ── NAVBAR SCROLL EFFECT ──
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 60) {
        navbar.style.boxShadow = '0 4px 24px rgba(0,0,0,0.25)';
      } else {
        navbar.style.boxShadow = 'none';
      }
    });
  }

  // ── NEWSLETTER FORM ──
  const newsletterBtn = document.querySelector('.newsletter-form button');
  const newsletterInput = document.querySelector('.newsletter-form input');
  if (newsletterBtn && newsletterInput) {
    newsletterBtn.addEventListener('click', () => {
      const val = newsletterInput.value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (emailRegex.test(val)) {
        newsletterBtn.textContent = '✓';
        newsletterBtn.style.background = '#22C55E';
        newsletterInput.value = '';
        newsletterInput.placeholder = 'You\'re subscribed!';
        setTimeout(() => {
          newsletterBtn.textContent = 'Go';
          newsletterBtn.style.background = '';
          newsletterInput.placeholder = 'your@email.com';
        }, 3000);
      } else {
        newsletterInput.style.borderColor = '#EF4444';
        setTimeout(() => newsletterInput.style.borderColor = '', 2000);
      }
    });
  }

});