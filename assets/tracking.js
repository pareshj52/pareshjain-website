/* Site-wide tracking for every page. Paste IDs here once; all pages load this file.
   META_PIXEL:       Meta Events Manager > Data sources > your Pixel > ID (numbers only)
   GOOGLE_ADS:       Google Ads > Goals > Conversions > tag set-up, e.g. 'AW-123456789'
   GOOGLE_ADS_LEAD:  the lead conversion's send_to value, e.g. 'AW-123456789/AbCdEfGh'   */
window.PJ = { GA4: 'G-XV39SFSW40', META_PIXEL: '', GOOGLE_ADS: '', GOOGLE_ADS_LEAD: '' };

window.dataLayer = window.dataLayer || [];
function gtag(){ dataLayer.push(arguments); }

(function(){
  var deny  = {ad_storage:'denied', ad_user_data:'denied', ad_personalization:'denied', analytics_storage:'denied'};
  var grant = {ad_storage:'granted', ad_user_data:'granted', ad_personalization:'granted', analytics_storage:'granted'};
  var tz = ''; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch(e) {}
  var saved = null; try { saved = localStorage.getItem('pj_consent'); } catch(e) {}
  PJ.eu = /^Europe\//.test(tz);
  PJ.consent = saved;

  // Google Consent Mode v2: ask first in the EEA, UK and Switzerland; allowed elsewhere.
  gtag('consent', 'default', Object.assign({
    region: ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','GB','CH'],
    wait_for_update: 500
  }, deny));
  gtag('consent', 'default', grant);
  if (saved === 'granted') gtag('consent', 'update', grant);
  else if (saved === 'denied') gtag('consent', 'update', deny);

  var s = document.createElement('script');
  s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + PJ.GA4;
  document.head.appendChild(s);
  gtag('js', new Date());
  gtag('config', PJ.GA4);
  if (PJ.GOOGLE_ADS) gtag('config', PJ.GOOGLE_ADS);

  PJ.loadPixel = function(){
    if (!PJ.META_PIXEL || window.fbq) return;
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', PJ.META_PIXEL); fbq('track', 'PageView');
  };
  PJ.setConsent = function(v){
    try { localStorage.setItem('pj_consent', v); } catch(e) {}
    PJ.consent = v;
    gtag('consent', 'update', v === 'granted' ? grant : deny);
    if (v === 'granted') PJ.loadPixel();
  };
  // Meta Pixel loads straight away outside Europe; in Europe only after "Accept".
  if (!PJ.eu || saved === 'granted') PJ.loadPixel();
})();
