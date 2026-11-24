// Génère les visuels noir et jaune des prestations qui n'ont pas encore de photo réelle.
// Usage : node src/make_illustrations.js   (nécessite Playwright + Chromium), puis python3 src/make_webp.py
// Dès qu'une vraie photo de chantier existe, la déposer dans src/assets/img/ sous le même nom.
const { chromium } = require('playwright');
const path = require('path');
const out = path.join(__dirname, 'assets', 'img');
const I = {
  tank: '<rect x="3" y="8" width="18" height="11" rx="3"/><path d="M8 8V5h3v3M3 14h18"/>',
  camera: '<rect x="3" y="7" width="12" height="10" rx="2"/><path d="m15 11 6-3v8l-6-3"/><circle cx="9" cy="12" r="2"/>',
  grease: '<path d="M4 10h16v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4v-6ZM8 10V7M16 10V7M12 4v3"/><path d="M8 14h8" stroke-dasharray="2 2"/>',
  pump: '<rect x="6" y="9" width="12" height="11" rx="2"/><path d="M12 9V3M9 6l3-3 3 3M9 14h6"/>',
  wrench: '<path d="M14.7 6.3a4 4 0 0 0-5.2 5.2L4 17l3 3 5.5-5.5a4 4 0 0 0 5.2-5.2l-2.4 2.4-2.6-.6-.6-2.6 2.6-2.2Z"/>',
  truck: '<path d="M2 7h11v9H2zM13 10h4l3 3v3h-7"/><circle cx="6" cy="17.5" r="1.8"/><circle cx="16.5" cy="17.5" r="1.8"/>',
};
const items = [
  ['fosse-septique', 'tank', 'Vidange de fosse septique', 'Fosse toutes eaux · micro-station · bac dégraisseur'],
  ['inspection-camera', 'camera', 'Inspection caméra', 'Diagnostic des canalisations sans casse'],
  ['bac-a-graisse', 'grease', 'Bac à graisse', 'Restaurants · commerces · collectivités'],
  ['pompe-relevage', 'pump', 'Pompe de relevage', 'Dépannage · nettoyage · remplacement'],
  ['travaux-assainissement', 'wrench', "Travaux d'assainissement", "Réparation · raccordement au tout-à-l'égout"],
  ['pompage', 'truck', 'Pompage & aspiration', 'Camion aspirateur · cuves · sous-sols inondés'],
];
const html = (ic, t, sub) => `<html><head><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&family=Inter:wght@600&display=swap" rel="stylesheet"></head>
<body style="margin:0;width:1200px;height:720px;background:radial-gradient(ellipse 700px 500px at 85% 10%,rgba(34,197,94,.16),transparent 60%),#111;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:30px;font-family:'Space Grotesk',sans-serif;position:relative;overflow:hidden">
<div style="width:250px;height:250px;border-radius:50%;background:#22c55e;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 18px rgba(34,197,94,.14)">
<svg width="150" height="150" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">${I[ic]}</svg></div>
<div style="color:#fff;font-size:58px;font-weight:700;letter-spacing:-.02em;text-align:center">${t}</div>
<div style="color:#22c55e;font-family:Inter,sans-serif;font-weight:600;font-size:26px;letter-spacing:.04em">${sub}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:26px;background:repeating-linear-gradient(-45deg,#22c55e 0 22px,#111 22px 44px)"></div></body></html>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 720 } });
  for (const [f, ic, t, sub] of items) {
    await p.setContent(html(ic, t, sub), { waitUntil: 'networkidle' }).catch(() => {});
    await p.screenshot({ path: path.join(out, f + '.jpg'), type: 'jpeg', quality: 85 });
  }
  await b.close();
})();
