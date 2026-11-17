/* Small cookie notice. Shown to visitors in Europe (EEA/UK) until they choose,
   and to anyone who clicks "Change cookie choice" on the privacy page. */
(function(){
  if (!window.PJ) return;
  function show(){
    if (document.getElementById('pj-consent')) return;
    var st = document.createElement('style');
    st.textContent = '#pj-consent{position:fixed;left:1rem;right:1rem;bottom:1rem;z-index:60;max-width:30rem;background:#141830;color:#fff;border-radius:1rem;padding:1.1rem 1.2rem;box-shadow:0 20px 50px -20px rgba(0,0,0,.6);font:inherit;font-size:.95rem;line-height:1.45}'
      + '#pj-consent p{margin:0 0 .85rem;color:#DCE0EE}#pj-consent a{color:#fff}'
      + '#pj-consent .r{display:flex;gap:.6rem;flex-wrap:wrap}#pj-consent button{font:inherit;font-weight:600;cursor:pointer;min-height:2.6rem;padding:0 1.1rem;border-radius:999px;border:1.5px solid #fff;background:transparent;color:#fff}'
      + '#pj-consent button.y{background:#FF9E2C;border-color:#FF9E2C;color:#141830}#pj-consent button:focus-visible{outline:3px solid #FF9E2C;outline-offset:2px}'
      + '@media (max-width:820px){#pj-consent{bottom:5rem}}';
    document.head.appendChild(st);
    var d = document.createElement('div');
    d.id = 'pj-consent'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-label', 'Cookie choice');
    d.innerHTML = '<p>I use cookies to see which pages help and whether ads bring enquiries. Nothing is sold. <a href="/privacy.html">Privacy</a></p>'
      + '<div class="r"><button type="button" class="y" data-v="granted">Accept</button><button type="button" data-v="denied">Decline</button></div>';
    d.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      PJ.setConsent(b.getAttribute('data-v'));
      d.remove();
    });
    document.body.appendChild(d);
  }
  PJ.showConsent = show;
  if (PJ.eu && !PJ.consent) show();
})();
