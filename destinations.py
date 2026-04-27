<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Destinations | WanderLust</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <style>
    .dest-section {
      padding: 4rem 2rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    .dest-controls {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 2.5rem;
    }

    .dest-count {
      color: var(--gray);
      font-size: 0.9rem;
    }

    .dest-count span {
      color: var(--deep);
      font-weight: 700;
    }

    .dest-all-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.5rem;
    }

    .dest-full-card {
      background: white;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(12,27,51,0.06);
      transition: transform 0.3s, box-shadow 0.3s;
      display: none;
    }

    .dest-full-card.visible {
      display: block;
    }

    .dest-full-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 16px 40px rgba(12,27,51,0.12);
    }

    .dest-full-card img {
      width: 100%;
      height: 220px;
      object-fit: cover;
      transition: transform 0.5s;
    }

    .dest-full-card:hover img { transform: scale(1.05); }

    .dest-full-card .card-body { padding: 1.5rem; }

    .dest-full-card .card-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.8rem;
    }

    .dest-full-card h3 {
      font-family: 'Playfair Display', serif;
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--deep);
      margin-bottom: 0.5rem;
    }

    .dest-full-card p {
      color: var(--gray);
      font-size: 0.88rem;
      line-height: 1.6;
      margin-bottom: 1.2rem;
    }

    .dest-full-card .card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .price-from {
      font-size: 0.78rem;
      color: var(--gray);
    }

    .price-from strong {
      display: block;
      font-family: 'Playfair Display', serif;
      font-size: 1.3rem;
      color: var(--fire);
      font-weight: 900;
    }

    .region-badge {
      padding: 4px 12px;
      border-radius: 50px;
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 0.5px;
    }

    .region-asia { background: rgba(255,154,60,0.12); color: #C2570A; }
    .region-europe { background: rgba(14,165,233,0.12); color: #0369A1; }
    .region-africa { background: rgba(34,197,94,0.12); color: #15803D; }
    .region-americas { background: rgba(168,85,247,0.12); color: #7C3AED; }
    .region-oceania { background: rgba(236,72,153,0.12); color: #BE185D; }

    .no-results {
      text-align: center;
      padding: 4rem 2rem;
      grid-column: 1/-1;
      display: none;
    }

    .no-results.show { display: block; }
    .no-results h3 { font-size: 1.3rem; color: var(--deep); margin-bottom: 0.5rem; }
    .no-results p { color: var(--gray); }

    /* Map CTA */
    .map-cta {
      background: linear-gradient(135deg, var(--deep) 0%, var(--moss) 100%);
      border-radius: 24px;
      padding: 3rem;
      text-align: center;
      margin: 3rem 0;
      position: relative;
      overflow: hidden;
    }

    .map-cta::before {
      content: '🌍';
      position: absolute;
      font-size: 12rem;
      opacity: 0.05;
      top: -2rem;
      right: -2rem;
    }

    .map-cta h3 {
      font-family: 'Playfair Display', serif;
      font-size: 2rem;
      font-weight: 900;
      color: white;
      margin-bottom: 0.8rem;
    }

    .map-cta p { color: rgba(255,255,255,0.6); margin-bottom: 1.5rem; }

    /* ── AI RESULT CARD ── */
    .ai-card {
      background: white;
      border-radius: 24px;
      overflow: hidden;
      box-shadow: 0 8px 40px rgba(12,27,51,0.1);
      display: grid;
      grid-template-columns: 1fr 1.5fr;
      min-height: 320px;
      border: 2px solid rgba(255,77,28,0.12);
      animation: fadeUp 0.5s ease both;
    }

    .ai-card-img { position: relative; overflow: hidden; }
    .ai-card-img img { width: 100%; height: 100%; object-fit: cover; }
    .ai-card-img .ai-badge {
      position: absolute; top: 14px; left: 14px;
      background: linear-gradient(135deg, var(--fire), var(--sun));
      color: white; font-size: 0.72rem; font-weight: 700;
      letter-spacing: 1px; text-transform: uppercase;
      padding: 5px 14px; border-radius: 50px;
    }

    .ai-card-body {
      padding: 2rem 2.5rem;
      display: flex; flex-direction: column; justify-content: center;
    }
    .ai-card-body .ai-label {
      font-size: 0.72rem; font-weight: 700; letter-spacing: 2px;
      text-transform: uppercase; color: var(--fire); margin-bottom: 0.4rem;
    }
    .ai-card-body h2 {
      font-family: 'Playfair Display', serif; font-size: 2rem;
      font-weight: 900; color: var(--deep); margin-bottom: 0.5rem;
    }
    .ai-card-body .ai-region {
      display: inline-block; background: var(--sand); color: var(--gray);
      font-size: 0.78rem; font-weight: 600; padding: 3px 12px;
      border-radius: 50px; margin-bottom: 1rem;
    }
    .ai-card-body .ai-desc {
      color: var(--gray); font-size: 0.9rem; line-height: 1.75; margin-bottom: 1.2rem;
    }
    .ai-highlights { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.5rem; }
    .ai-highlights span {
      background: rgba(255,77,28,0.07); color: var(--fire);
      font-size: 0.78rem; font-weight: 600; padding: 4px 12px;
      border-radius: 50px; border: 1px solid rgba(255,77,28,0.15);
    }
    .ai-card-footer { display: flex; gap: 0.8rem; align-items: center; flex-wrap: wrap; }
    .ai-note { font-size: 0.75rem; color: rgba(107,114,128,0.75); display: flex; align-items: center; gap: 5px; }

    /* Spinner */
    .ai-spinner {
      width: 44px; height: 44px;
      border: 3px solid rgba(255,77,28,0.15);
      border-top-color: var(--fire);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      margin: 0 auto;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* Autocomplete dropdown */
    .search-bar-wrap { position: relative; max-width: 380px; flex: 1; min-width: 240px; }
    .search-dropdown {
      position: absolute; top: calc(100% + 4px); left: 0; right: 0;
      background: white; border-radius: 16px;
      box-shadow: 0 8px 28px rgba(12,27,51,0.13);
      z-index: 200; overflow: hidden; display: none;
      border: 1px solid rgba(0,0,0,0.06);
    }
    .search-dropdown.open { display: block; }
    .dropdown-item {
      padding: 10px 18px; cursor: pointer; font-size: 0.88rem;
      color: var(--deep); display: flex; align-items: center;
      gap: 10px; transition: background 0.15s;
    }
    .dropdown-item:hover { background: var(--sand); }
    .dropdown-item .match { font-weight: 700; color: var(--fire); }
    .dropdown-item .sub { color: var(--gray); font-size: 0.78rem; }
    .dropdown-divider {
      font-size: 0.72rem; font-weight: 700; letter-spacing: 1.5px;
      text-transform: uppercase; color: var(--gray); padding: 8px 18px 4px;
      background: var(--sand);
    }

    .no-results.show { display: block; }

    @media (max-width: 768px) {
      .ai-card { grid-template-columns: 1fr; }
      .ai-card-img { height: 200px; }
    }
  </style>
</head>
<body>

<script src="components.js"></script>
<script>injectNav('destinations');</script>

<!-- PAGE HERO -->
<div class="page-hero" style="background-image:url('https://images.unsplash.com/photo-1488085061387-422e29b40080?auto=format&fit=crop&w=1600&q=80'); background-size:cover; background-position:center;">
  <div style="position:absolute;inset:0;background:rgba(12,27,51,0.65);"></div>
  <div style="position:relative;z-index:1;text-align:center;padding:0 1.5rem;">
    <span class="page-hero-tag">Explore</span>
    <h1>The World Awaits</h1>
    <p>150+ handpicked destinations across 6 continents. Find yours.</p>
  </div>
</div>

<!-- ── DESTINATIONS ── -->
<section class="dest-section">
  <!-- Controls -->
  <div class="dest-controls">
    <div class="search-bar-wrap">
      <div class="search-bar">
        <input type="text" id="destSearch" placeholder="Search any destination..." oninput="onSearchInput()" onkeydown="onSearchKey(event)" autocomplete="off">
        <button onclick="triggerSearch()"><i class="fas fa-search"></i></button>
      </div>
      <div class="search-dropdown" id="searchDropdown"></div>
    </div>
    <div class="filter-tabs" id="filterTabs">
      <button class="filter-tab active" onclick="setFilter('all', this)">All</button>
      <button class="filter-tab" onclick="setFilter('asia', this)">🌏 Asia</button>
      <button class="filter-tab" onclick="setFilter('europe', this)">🏰 Europe</button>
      <button class="filter-tab" onclick="setFilter('africa', this)">🌍 Africa</button>
      <button class="filter-tab" onclick="setFilter('americas', this)">🗺 Americas</button>
      <button class="filter-tab" onclick="setFilter('oceania', this)">🌊 Oceania</button>
    </div>
    <div class="dest-count">Showing <span id="visibleCount">12</span> destinations</div>
  </div>

  <!-- Grid -->
  <div class="dest-all-grid" id="destGrid">

    <div class="dest-full-card visible" data-region="asia" data-name="bali indonesia">
      <img src="https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=600&q=80" alt="Bali">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-asia">Asia</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.9</span>
        </div>
        <h3>Bali, Indonesia</h3>
        <p>Tropical paradise with ancient temples, lush rice terraces, and world-class surf breaks.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$899</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="europe" data-name="santorini greece">
      <img src="https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=600&q=80" alt="Santorini">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-europe">Europe</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.8</span>
        </div>
        <h3>Santorini, Greece</h3>
        <p>Iconic whitewashed villages perched on volcanic cliffs above the stunning Aegean Sea.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$1,199</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="asia" data-name="tokyo japan">
      <img src="https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=600&q=80" alt="Tokyo">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-asia">Asia</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 5.0</span>
        </div>
        <h3>Tokyo, Japan</h3>
        <p>Where ancient temples meet neon-lit streets — the most electrifying city on Earth.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$1,499</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="americas" data-name="patagonia chile argentina">
      <img src="https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&w=600&q=80" alt="Patagonia">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-americas">Americas</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.9</span>
        </div>
        <h3>Patagonia, Chile</h3>
        <p>Glaciers, granite peaks, and raw wilderness at the bottom of the world.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$2,199</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="africa" data-name="serengeti tanzania safari">
      <img src="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=600&q=80" alt="Serengeti">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-africa">Africa</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.9</span>
        </div>
        <h3>Serengeti, Tanzania</h3>
        <p>Witness the great wildebeest migration across Africa's most iconic savanna.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$2,899</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="europe" data-name="amalfi coast italy">
      <img src="https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=600&q=80" alt="Amalfi">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-europe">Europe</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.8</span>
        </div>
        <h3>Amalfi Coast, Italy</h3>
        <p>Clifftop villages, lemon groves, and sapphire waters along Italy's most dramatic coastline.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$1,399</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="oceania" data-name="new zealand fjordland milford">
      <img src="https://images.unsplash.com/photo-1507699622108-4be3abd695ad?auto=format&fit=crop&w=600&q=80" alt="New Zealand">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-oceania">Oceania</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 5.0</span>
        </div>
        <h3>Fjordland, New Zealand</h3>
        <p>Middle-earth comes alive with soaring fiords, glowworm caves, and volcanic lakes.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$1,899</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="asia" data-name="rajasthan india">
      <img src="https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=600&q=80" alt="Rajasthan">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-asia">Asia</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.7</span>
        </div>
        <h3>Rajasthan, India</h3>
        <p>Golden deserts, medieval forts, and the most vivid colours you'll ever photograph.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$799</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="americas" data-name="machu picchu peru">
      <img src="https://images.unsplash.com/photo-1587595431973-160d0d94add1?auto=format&fit=crop&w=600&q=80" alt="Machu Picchu">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-americas">Americas</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.9</span>
        </div>
        <h3>Machu Picchu, Peru</h3>
        <p>The lost Inca city in the clouds — one of humanity's most awe-inspiring achievements.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$1,699</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="africa" data-name="morocco marrakech sahara">
      <img src="https://images.unsplash.com/photo-1539020140153-e479b8fbe0cb?auto=format&fit=crop&w=600&q=80" alt="Morocco">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-africa">Africa</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.8</span>
        </div>
        <h3>Marrakech, Morocco</h3>
        <p>Ancient medinas, Sahara dunes, and spice-scented souks — sensory overload in the best way.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$999</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="europe" data-name="iceland northern lights aurora">
      <img src="https://images.unsplash.com/photo-1531366936337-7c912a4589a7?auto=format&fit=crop&w=600&q=80" alt="Iceland">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-europe">Europe</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 4.9</span>
        </div>
        <h3>Iceland</h3>
        <p>Chase the Northern Lights across volcanic landscapes, geysers, and midnight sun.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$1,599</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <div class="dest-full-card visible" data-region="oceania" data-name="maldives islands overwater bungalow">
      <img src="https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=600&q=80" alt="Maldives">
      <div class="card-body">
        <div class="card-meta">
          <span class="region-badge region-oceania">Oceania</span>
          <span style="color:var(--gold);font-size:0.82rem;">★ 5.0</span>
        </div>
        <h3>Maldives</h3>
        <p>Overwater bungalows, crystal lagoons, and the purest turquoise waters on the planet.</p>
        <div class="card-footer">
          <div class="price-from">From<strong>$2,499</strong></div>
          <a href="packages.html" class="btn btn-primary" style="padding:9px 20px;font-size:0.82rem;">View Package</a>
        </div>
      </div>
    </div>

    <!-- No results: AI-powered fallback -->
    <div class="no-results" id="noResults">
      <!-- State 1: Searching spinner -->
      <div id="aiSearching" style="display:none; text-align:center; padding:3rem 1rem; grid-column:1/-1;">
        <div class="ai-spinner"></div>
        <p style="color:var(--gray); margin-top:1rem; font-size:0.95rem;">Finding travel info for <strong id="searchingFor"></strong>…</p>
      </div>

      <!-- State 2: AI result card -->
      <div id="aiResultCard" style="display:none; grid-column:1/-1;"></div>

      <!-- State 3: Hard not found (shown only if AI also fails) -->
      <div id="hardNotFound" style="display:none; text-align:center; padding:3rem 1rem;">
        <div style="font-size:3rem; margin-bottom:1rem;">🌐</div>
        <h3 style="color:var(--deep); font-size:1.2rem; margin-bottom:0.4rem;">Destination not found</h3>
        <p style="color:var(--gray); margin-bottom:1.2rem;">We couldn't find travel info for this place. Our experts can still plan a custom trip!</p>
        <a href="contact.html" class="btn btn-primary" style="font-size:0.88rem; padding:10px 24px;">Talk to an Expert</a>
      </div>
    </div>
  </div>

  <!-- Map CTA -->
  <div class="map-cta">
    <h3>Can't Find What You're Looking For?</h3>
    <p>Our travel experts can plan a custom trip to literally anywhere on Earth.</p>
    <a href="contact.html" class="btn btn-primary"><i class="fas fa-paper-plane"></i> Talk to an Expert</a>
  </div>
</section>

<script>injectFooter();</script>
<script src="script.js"></script>
<script>
// ── DESTINATION DATA (for local matching & autocomplete) ──
const LOCAL_DESTS = [
  { name: 'Bali, Indonesia',      region: 'asia',     keywords: ['bali','indonesia','ubud','kuta','seminyak'] },
  { name: 'Santorini, Greece',    region: 'europe',   keywords: ['santorini','greece','oia','greek'] },
  { name: 'Tokyo, Japan',         region: 'asia',     keywords: ['tokyo','japan','kyoto','osaka','japanese'] },
  { name: 'Patagonia, Chile',     region: 'americas', keywords: ['patagonia','chile','argentina','torres del paine'] },
  { name: 'Serengeti, Tanzania',  region: 'africa',   keywords: ['serengeti','tanzania','safari','africa'] },
  { name: 'Amalfi Coast, Italy',  region: 'europe',   keywords: ['amalfi','italy','italian','positano','rome'] },
  { name: 'Fjordland, New Zealand',region:'oceania',  keywords: ['new zealand','fjordland','milford','nz'] },
  { name: 'Rajasthan, India',     region: 'asia',     keywords: ['rajasthan','india','jaipur','udaipur','delhi','mumbai','goa','bhubaneswar','odisha'] },
  { name: 'Machu Picchu, Peru',   region: 'americas', keywords: ['machu picchu','peru','inca','cusco'] },
  { name: 'Marrakech, Morocco',   region: 'africa',   keywords: ['morocco','marrakech','sahara','casablanca'] },
  { name: 'Iceland',              region: 'europe',   keywords: ['iceland','reykjavik','northern lights','aurora'] },
  { name: 'Maldives',             region: 'oceania',  keywords: ['maldives','maldivian','atoll'] },
];

let currentFilter = 'all';
let debounceTimer = null;
let currentQuery = '';

// ── FILTER TABS ──
function setFilter(region, btn) {
  currentFilter = region;
  document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  filterLocalCards(document.getElementById('destSearch').value.toLowerCase());
}

// ── LOCAL CARD FILTER ──
function filterLocalCards(query) {
  const cards = document.querySelectorAll('.dest-full-card');
  let count = 0;
  cards.forEach(card => {
    const name = card.dataset.name;
    const region = card.dataset.region;
    const matchRegion = currentFilter === 'all' || region === currentFilter;
    const matchQuery = !query || name.includes(query);
    if (matchRegion && matchQuery) { card.classList.add('visible'); count++; }
    else { card.classList.remove('visible'); }
  });
  document.getElementById('visibleCount').textContent = count;
  return count;
}

// ── AUTOCOMPLETE ──
function onSearchInput() {
  const query = document.getElementById('destSearch').value.trim();
  currentQuery = query;

  // Reset AI result area when user types again
  hideAIStates();
  document.getElementById('noResults').classList.remove('show');

  if (query.length < 2) {
    closeDropdown();
    filterLocalCards('');
    return;
  }

  const q = query.toLowerCase();
  const suggestions = LOCAL_DESTS.filter(d =>
    d.keywords.some(k => k.includes(q)) || d.name.toLowerCase().includes(q)
  );

  const dropdown = document.getElementById('searchDropdown');

  if (suggestions.length > 0) {
    dropdown.innerHTML = suggestions.slice(0, 5).map(s => `
      <div class="dropdown-item" onclick="selectSuggestion('${s.name}', '${s.region}')">
        <span style="font-size:1.1rem;">${regionEmoji(s.region)}</span>
        <div>
          <div class="match">${s.name}</div>
          <div class="sub">${capitalize(s.region)}</div>
        </div>
      </div>`).join('');

    // Also add "Search globally" option
    dropdown.innerHTML += `
      <div class="dropdown-divider">Or search globally</div>
      <div class="dropdown-item" onclick="triggerSearch()">
        <span style="font-size:1.1rem;">🌐</span>
        <div>
          <div>Find info for <strong>"${query}"</strong></div>
          <div class="sub">AI-powered search</div>
        </div>
      </div>`;
    dropdown.classList.add('open');
  } else {
    // No local match — show only global option
    dropdown.innerHTML = `
      <div class="dropdown-item" onclick="triggerSearch()">
        <span style="font-size:1.1rem;">🌐</span>
        <div>
          <div>Search for <strong>"${query}"</strong></div>
          <div class="sub">Find travel info with AI</div>
        </div>
      </div>`;
    dropdown.classList.add('open');
  }

  // Live filter local cards
  filterLocalCards(q);

  // Debounce AI search for unknown destinations
  clearTimeout(debounceTimer);
  if (suggestions.length === 0) {
    debounceTimer = setTimeout(() => triggerSearch(), 1200);
  }
}

function selectSuggestion(name, region) {
  document.getElementById('destSearch').value = name;
  closeDropdown();
  const q = name.toLowerCase();
  // Filter by region too
  currentFilter = region;
  document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
  const count = filterLocalCards(q);
  document.getElementById('visibleCount').textContent = count;
  if (count === 0) triggerSearch();
}

function onSearchKey(e) {
  if (e.key === 'Enter') { closeDropdown(); triggerSearch(); }
  if (e.key === 'Escape') closeDropdown();
}

function closeDropdown() {
  document.getElementById('searchDropdown').classList.remove('open');
}

// Close dropdown on outside click
document.addEventListener('click', e => {
  if (!e.target.closest('.search-bar-wrap')) closeDropdown();
});

// ── TRIGGER SEARCH (local + AI fallback) ──
function triggerSearch() {
  clearTimeout(debounceTimer);
  closeDropdown();
  const query = document.getElementById('destSearch').value.trim();
  if (!query) return;

  const q = query.toLowerCase();
  const localCount = filterLocalCards(q);
  document.getElementById('visibleCount').textContent = localCount;

  if (localCount === 0) {
    // Show AI search
    aiSearchDestination(query);
  } else {
    hideAIStates();
    document.getElementById('noResults').classList.remove('show');
  }
}

// ── SMART SEARCH using Wikipedia + Unsplash (works on localhost, no API key needed) ──
async function aiSearchDestination(query) {
  const noResults = document.getElementById('noResults');
  noResults.classList.add('show');
  noResults.style.display = 'block';

  document.getElementById('aiSearching').style.display = 'block';
  document.getElementById('aiResultCard').style.display = 'none';
  document.getElementById('hardNotFound').style.display = 'none';
  document.getElementById('searchingFor').textContent = query;

  try {
    // Step 1: Wikipedia search to find the best matching article
    const searchUrl = `https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=${encodeURIComponent(query + ' city travel tourism')}&format=json&origin=*&srlimit=3`;
    const searchRes = await fetch(searchUrl);
    const searchData = await searchRes.json();
    const results = searchData.query?.search || [];

    if (results.length === 0) {
      showHardNotFound(); return;
    }

    // Step 2: Get extract + page image from the best result
    const pageTitle = results[0].title;
    const summaryUrl = `https://en.wikipedia.org/w/api.php?action=query&titles=${encodeURIComponent(pageTitle)}&prop=extracts|pageimages|categories&exintro=true&explaintext=true&pithumbsize=800&format=json&origin=*`;
    const summaryRes = await fetch(summaryUrl);
    const summaryData = await summaryRes.json();

    const pages = summaryData.query?.pages || {};
    const page = Object.values(pages)[0];

    if (!page || page.missing) { showHardNotFound(); return; }

    // Step 3: Parse and clean the extract
    const rawExtract = page.extract || '';
    // Take first 3 sentences, clean up
    const sentences = rawExtract.replace(/\n+/g, ' ').split(/(?<=[.!?])\s+/);
    const description = sentences.slice(0, 3).join(' ').substring(0, 400);

    if (description.length < 30) { showHardNotFound(); return; }

    // Step 4: Determine region from page title / content
    const region = detectRegion(page.title + ' ' + description);

    // Step 5: Extract country name (simple heuristic from title or description)
    const country = extractCountry(page.title, description);

    // Step 6: Smart highlight tags — extract key nouns/topics from description
    const highlights = extractHighlights(description, query);

    // Step 7: Image — use Wikipedia's page image if available, else Unsplash
    let imgUrl = '';
    if (page.thumbnail?.source) {
      imgUrl = page.thumbnail.source;
    } else {
      // Fallback: Unsplash random travel photo for the query
      imgUrl = `https://images.unsplash.com/1600x900/?${encodeURIComponent(query + ' travel landmark')}`;
    }

    // Step 8: Build best-time guess from description keywords
    const bestTime = guessBestTime(description);

    document.getElementById('aiSearching').style.display = 'none';

    const highlightTags = highlights.map(h => `<span>${h}</span>`).join('');

    const card = document.getElementById('aiResultCard');
    card.innerHTML = `
      <div class="ai-card">
        <div class="ai-card-img">
          <img 
            src="${imgUrl}" 
            alt="${pageTitle}"
            onerror="this.src='https://images.unsplash.com/photo-1488085061387-422e29b40080?auto=format&fit=crop&w=800&q=80'"
          >
          <span class="ai-badge">🌐 Live Result</span>
        </div>
        <div class="ai-card-body">
          <div class="ai-label">Destination Found</div>
          <h2>${pageTitle}</h2>
          <span class="ai-region">📍 ${region}${country ? ' · ' + country : ''}</span>
          <p class="ai-desc">${description}</p>
          <div class="ai-highlights">${highlightTags}</div>
          <div class="ai-highlights" style="margin-top:-0.5rem; margin-bottom:1rem;">
            <span>🗓 Best time to visit: ${bestTime}</span>
          </div>
          <div class="ai-card-footer">
            <a href="contact.html?dest=${encodeURIComponent(pageTitle)}" class="btn btn-primary" style="padding:10px 24px; font-size:0.85rem;">
              <i class="fas fa-paper-plane"></i> Plan This Trip
            </a>
            <a href="https://en.wikipedia.org/wiki/${encodeURIComponent(pageTitle)}" target="_blank" class="btn btn-outline" style="color:var(--deep); border-color:#E5E7EB; padding:10px 18px; font-size:0.82rem;">
              Read More
            </a>
          </div>
          <p class="ai-note" style="margin-top:0.8rem;">✦ Info sourced from Wikipedia · Our experts can plan this trip for you</p>
        </div>
      </div>`;
    card.style.display = 'block';

  } catch (err) {
    document.getElementById('aiSearching').style.display = 'none';
    document.getElementById('hardNotFound').style.display = 'block';
    console.error('Search error:', err);
  }
}

// ── HELPER: Show hard not found state ──
function showHardNotFound() {
  document.getElementById('aiSearching').style.display = 'none';
  document.getElementById('hardNotFound').style.display = 'block';
}

// ── HELPER: Detect world region from text ──
function detectRegion(text) {
  const t = text.toLowerCase();
  if (/india|china|japan|korea|thailand|vietnam|indonesia|bali|singapore|sri lanka|nepal|bhutan|myanmar|cambodia|malaysia|odisha|bhubaneswar|rajasthan|mumbai|delhi|goa|kerala/.test(t)) return 'Asia';
  if (/france|germany|italy|spain|greece|uk|england|portugal|netherlands|switzerland|austria|sweden|norway|denmark|finland|poland|czech|hungary|croatia/.test(t)) return 'Europe';
  if (/africa|kenya|tanzania|nigeria|ghana|ethiopia|egypt|morocco|south africa|uganda|zimbabwe|mozambique|madagascar|serengeti/.test(t)) return 'Africa';
  if (/usa|united states|canada|mexico|brazil|argentina|chile|peru|colombia|ecuador|venezuela|cuba|caribbean|amazon|patagonia/.test(t)) return 'Americas';
  if (/australia|new zealand|fiji|samoa|tonga|papua|pacific|polynesia|micronesia|maldives/.test(t)) return 'Oceania';
  if (/dubai|uae|saudi|qatar|bahrain|kuwait|oman|jordan|israel|turkey|iran|iraq|lebanon/.test(t)) return 'Middle East';
  return 'World';
}

// ── HELPER: Extract country from title/text ──
function extractCountry(title, text) {
  const countryList = ['India','China','Japan','France','Italy','Germany','Spain','Greece','USA','Brazil','Australia','New Zealand','Morocco','Egypt','Kenya','Thailand','Indonesia','Mexico','Canada','Turkey','UAE','Peru','Chile','Argentina','Portugal','Netherlands','Switzerland','Sweden','Norway','Tanzania','South Africa'];
  for (const c of countryList) {
    if (title.includes(c) || text.includes(c)) return c;
  }
  // Try last word of title if it looks like a country
  const parts = title.split(',');
  if (parts.length > 1) return parts[parts.length - 1].trim();
  return '';
}

// ── HELPER: Extract smart highlight tags from description ──
function extractHighlights(text, query) {
  const defaults = ['Historic Sites', 'Local Cuisine', 'Cultural Heritage', 'Nature & Parks'];
  const tags = [];
  const t = text.toLowerCase();

  const checks = [
    [/temple|shrine|mosque|church|cathedral|mandir/, '🛕 Temples'],
    [/beach|coast|ocean|sea|bay|shore/, '🏖 Beaches'],
    [/mountain|peak|hill|trek|hiking/, '🏔 Mountains'],
    [/museum|gallery|art|history|heritage/, '🏛 Museums'],
    [/food|cuisine|restaurant|market|street food/, '🍜 Local Food'],
    [/festival|culture|tradition|dance|music/, '🎭 Culture'],
    [/wildlife|safari|animal|bird|forest|jungle/, '🦁 Wildlife'],
    [/river|lake|waterfall|garden|park/, '🌿 Nature'],
    [/palace|fort|castle|monument|ruins/, '🏰 Monuments'],
    [/shopping|bazaar|market|souvenir/, '🛍 Shopping'],
    [/nightlife|club|bar|entertainment/, '🌙 Nightlife'],
    [/spa|wellness|yoga|retreat/, '🧘 Wellness'],
  ];

  for (const [re, label] of checks) {
    if (re.test(t)) tags.push(label);
    if (tags.length >= 4) break;
  }

  // Fill remaining with defaults
  let di = 0;
  while (tags.length < 4 && di < defaults.length) {
    if (!tags.includes(defaults[di])) tags.push(defaults[di]);
    di++;
  }

  return tags.slice(0, 4);
}

// ── HELPER: Guess best time from description text ──
function guessBestTime(text) {
  const t = text.toLowerCase();
  if (/october|november|december|january|february|march/.test(t)) return 'Oct – Mar';
  if (/april|may|june|july|august|september/.test(t)) return 'Apr – Sep';
  if (/winter/.test(t)) return 'Winter (Dec–Feb)';
  if (/summer/.test(t)) return 'Summer (Jun–Aug)';
  if (/monsoon|rainy/.test(t)) return 'Avoid Monsoon Season';
  return 'Year-round';
}

function hideAIStates() {
  document.getElementById('aiSearching').style.display = 'none';
  document.getElementById('aiResultCard').style.display = 'none';
  document.getElementById('hardNotFound').style.display = 'none';
}

// ── HELPERS ──
function regionEmoji(r) {
  return { asia:'🌏', europe:'🏰', africa:'🌍', americas:'🗺', oceania:'🌊' }[r] || '📍';
}
function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

// ── URL PARAMS (from homepage search) ──
const params = new URLSearchParams(window.location.search);
if (params.get('q')) {
  document.getElementById('destSearch').value = params.get('q');
  triggerSearch();
}
</script>
</body>
</html>