// ── SHARED NAV + FOOTER INJECTOR ──
// Include this script in every page: <script src="components.js"></script>
// Then call: injectNav('home') and injectFooter() at bottom of body

function injectNav(activePage) {
  const nav = `
  <nav class="navbar">
    <a href="index.html" class="nav-logo">
      <div class="logo-icon">✈</div>
      <span>WanderLust</span>
    </a>
    <ul class="nav-links">
      <li><a href="index.html" class="${activePage === 'home' ? 'active' : ''}">Home</a></li>
      <li><a href="about.html" class="${activePage === 'about' ? 'active' : ''}">About Us</a></li>
      <li><a href="destinations.html" class="${activePage === 'destinations' ? 'active' : ''}">Destinations</a></li>
      <li><a href="packages.html" class="${activePage === 'packages' ? 'active' : ''}">Packages</a></li>
      <li><a href="contact.html" class="nav-cta ${activePage === 'contact' ? 'active' : ''}">Contact Us</a></li>
    </ul>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </nav>
  <div class="mobile-menu" id="mobileMenu">
    <a href="index.html">🏠 Home</a>
    <a href="about.html">👥 About Us</a>
    <a href="destinations.html">🗺 Destinations</a>
    <a href="packages.html">📦 Packages</a>
    <a href="contact.html">📩 Contact Us</a>
  </div>`;
  document.body.insertAdjacentHTML('afterbegin', nav);

  // Hamburger toggle
  document.getElementById('hamburger').addEventListener('click', () => {
    document.getElementById('mobileMenu').classList.toggle('open');
  });
}

function injectFooter() {
  const footer = `
  <footer>
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="logo-text">✈ WanderLust</span>
        <p>Your trusted partner for unforgettable travel experiences. We craft journeys that go beyond destinations — we create stories you'll tell forever.</p>
        <div class="footer-social">
          <a href="#" aria-label="Facebook">f</a>
          <a href="#" aria-label="Instagram">ig</a>
          <a href="#" aria-label="Twitter">tw</a>
          <a href="#" aria-label="YouTube">yt</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <ul>
          <li><a href="destinations.html">Destinations</a></li>
          <li><a href="packages.html">Travel Packages</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Support</h4>
        <ul>
          <li><a href="#">FAQ</a></li>
          <li><a href="#">Cancellation Policy</a></li>
          <li><a href="#">Travel Insurance</a></li>
          <li><a href="#">Visa Help</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Newsletter</h4>
        <p style="font-size:0.85rem; margin-bottom:0.8rem;">Get travel deals & inspiration straight to your inbox.</p>
        <div class="newsletter-form">
          <input type="email" placeholder="your@email.com">
          <button>Go</button>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 WanderLust Agency. All rights reserved.</span>
      <span>Made with ❤️ for adventurers</span>
    </div>
  </footer>`;
  document.body.insertAdjacentHTML('beforeend', footer);
}

// ── SCROLL TO TOP BUTTON ──
function injectScrollTopBtn() {
  // Create the button
  const btn = document.createElement('button');
  btn.className = 'scroll-top-btn';
  btn.setAttribute('aria-label', 'Scroll to top');
  btn.innerHTML = '&#8679;'; // ↑ arrow
  document.body.appendChild(btn);

  // Show/hide based on scroll position
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  });

  // Smooth scroll to top on click
  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// Auto-run when components.js loads
injectScrollTopBtn();
