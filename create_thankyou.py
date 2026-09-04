import os
import re

doc_dir = r'C:\Users\anand singh\Documents\digitaldas-landing'
ipath = os.path.join(doc_dir, 'index.html')

with open(ipath, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract logo Data URI from index.html
logo_match = re.search(r'src="(data:image/png;base64,[^"]+)"', index_html)
logo_uri = logo_match.group(1) if logo_match else 'assets/logo.png'

meta_pixel_code = """  <!-- Meta Pixel Code -->
  <script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'PASTE_YOUR_PIXEL_ID_HERE');
  fbq('track', 'PageView');
  </script>
  <noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=PASTE_YOUR_PIXEL_ID_HERE&ev=PageView&noscript=1"
  /></noscript>
  <!-- End Meta Pixel Code -->"""

# Add Meta Pixel Code to index.html <head> if not present
if 'PASTE_YOUR_PIXEL_ID_HERE' not in index_html:
    head_pos = index_html.find('</head>')
    index_html = index_html[:head_pos] + meta_pixel_code + '\n' + index_html[head_pos:]

# Update handleFormSubmit redirect logic in index.html
old_success_block = """        if (response.status === 200 && data.success) {
          // Confirmed Success: Fire dataLayer Event & Render In-Page Thank-You Card
          trackEvent('lead_form_submit', 'primary_form');
          
          const submittedName = nameInput.value.trim();
          const formContainer = document.getElementById('form-container');
          formContainer.innerHTML = `
            <div class="text-center py-8 px-4 bg-white rounded-2xl border border-[#e8a13c]/40 shadow-card-soft animate-on-scroll is-visible">
              <div class="w-16 h-16 rounded-full bg-[#e8a13c]/20 text-[#e8a13c] flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 stroke-current fill-none" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
              </div>
              <h3 class="text-2xl font-extrabold text-[#1a1815] tracking-tight mb-2">Thank You, ${submittedName}!</h3>
              <p class="text-sm text-[#6c665a] max-w-md mx-auto mb-6">
                We have received your project details. Senior Strategist from Digital Das will call you within 24 hours.
              </p>
              <a href="https://wa.me/916387812688?text=Hi%20Digital%20Das%2C%20I%20want%20to%20discuss%20a%20project" 
                 target="_blank" 
                 rel="noopener noreferrer"
                 aria-label="WhatsApp Digital Das"
                 onclick="trackEvent('whatsapp_click', 'thank_you_card')"
                 class="inline-flex items-center justify-center gap-2 h-12 px-6 rounded-xl bg-[#e8a13c] hover:bg-[#d48f2b] text-black font-extrabold text-sm transition-all shadow-md min-h-[44px] min-w-[44px] focus:outline-none focus:ring-2 focus:ring-[#e8a13c]">
                <svg class="w-4 h-4 fill-current text-black" viewBox="0 0 24 24">
                  <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
                </svg>
                <span>Instant Chat on WhatsApp</span>
              </a>
            </div>
          `;
        }"""

new_success_block = """        if (response.status === 200 && data.success) {
          // Confirmed Success: Fire dataLayer Event & Redirect to /thank-you
          trackEvent('lead_form_submit', 'primary_form');
          sessionStorage.setItem('lead_pending', 'true');
          window.location.href = 'thank-you.html';
        }"""

if old_success_block in index_html:
    index_html = index_html.replace(old_success_block, new_success_block)

with open(ipath, 'w', encoding='utf-8') as f:
    f.write(index_html)

thank_you_html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  
  <title>Thank You — Digital Das</title>
  <meta name="robots" content="noindex, nofollow" />
  <meta name="author" content="Digital Das" />

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="{logo_uri}" />

{meta_pixel_code}

  <!-- Google Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            gold: {{
              DEFAULT: '#e8a13c',
              hover: '#d48f2b',
              light: '#fdf8ef',
              dark: '#9a6417'
            }},
            dark: {{
              base: '#0d0c0a',
              end: '#241a0e',
              card: '#15110c',
              cardAlt: '#211a12',
              border: '#3a3226',
              muted: '#c9c2b4'
            }},
            cream: {{
              DEFAULT: '#f7f3ec',
              card: '#f4f0e8',
              border: '#e6dfd0',
              muted: '#6c665a'
            }}
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'Inter', 'system-ui', 'sans-serif'],
          }},
          boxShadow: {{
            'gold-glow': '0 0 25px -5px rgba(232, 161, 60, 0.25)',
            'card-soft': '0 10px 30px -10px rgba(0, 0, 0, 0.08)',
            'dark-card': '0 12px 32px -8px rgba(0, 0, 0, 0.5)'
          }}
        }}
      }}
    }}
  </script>

  <style>
    html, body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #0d0c0a;
      color: #1a1815;
      overflow-x: hidden;
      -webkit-tap-highlight-color: transparent;
    }}
  </style>
</head>
<body class="bg-[#0d0c0a] text-[#1a1815] antialiased selection:bg-[#e8a13c] selection:text-black min-h-screen flex flex-col justify-between">

  <!-- HEADER -->
  <header id="main-header" class="fixed top-0 left-0 right-0 z-50 bg-[#0d0c0a]/85 backdrop-blur-md h-[64px] flex items-center px-4 md:px-8 border-b border-[#3a3226]/50">
    <div class="max-w-7xl mx-auto w-full flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3 group focus:outline-none rounded-lg p-1" aria-label="Digital Das Homepage">
        <div class="bg-[#f7f3ec] p-0.5 rounded-full inline-flex items-center justify-center shadow-sm">
          <img src="{logo_uri}" width="40" height="40" alt="Digital Das" class="w-[34px] h-[34px] md:w-[40px] md:h-[40px] aspect-square rounded-full object-contain" />
        </div>
        <span class="text-white font-extrabold text-lg md:text-xl tracking-tight leading-none">Digital Das</span>
      </a>

      <a href="https://wa.me/916387812688?text=Hi%20Digital%20Das%2C%20I%20want%20to%20discuss%20a%20project" 
         target="_blank" rel="noopener noreferrer" aria-label="WhatsApp Digital Das"
         class="h-11 px-4 md:px-5 rounded-full bg-[#e8a13c] hover:bg-[#d48f2b] text-black font-bold text-sm flex items-center justify-center gap-2 transition-all transform active:scale-95 shadow-md shadow-[#e8a13c]/20">
        <span>Talk to Us</span>
      </a>
    </div>
  </header>

  <!-- THANK YOU CONTENT CARD -->
  <main class="pt-32 pb-20 px-4 md:px-8 flex-grow flex items-center justify-center">
    <div class="max-w-xl w-full bg-[#f4f0e8] border border-[#e6dfd0] rounded-3xl p-8 md:p-12 text-center shadow-card-soft">
      <div class="w-16 h-16 rounded-full bg-[#e8a13c]/20 text-[#e8a13c] flex items-center justify-center mx-auto mb-6">
        <svg class="w-8 h-8 stroke-current fill-none" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold text-[#1a1815] tracking-tight mb-3">Thank you!</h1>
      <p class="text-base sm:text-lg text-[#6c665a] leading-relaxed mb-8 max-w-md mx-auto">
        We've received your details. Our team will get back to you within 24 hours.
      </p>
      <a href="index.html" 
         class="inline-flex items-center justify-center gap-2 h-14 px-8 rounded-xl bg-[#e8a13c] hover:bg-[#d48f2b] text-black font-extrabold text-base transition-all transform active:scale-95 shadow-lg shadow-[#e8a13c]/25">
        <svg class="w-5 h-5 stroke-current fill-none" stroke-width="2.5" viewBox="0 0 24 24"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
        <span>Back to Home</span>
      </a>
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-[#0d0c0a] text-white py-12 border-t border-[#3a3226]/60">
    <div class="max-w-7xl mx-auto px-4 md:px-8">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-[#3a3226]/40">
        <div class="flex flex-col items-center md:items-start text-center md:text-left">
          <div class="flex items-center gap-3 mb-2">
            <div class="bg-[#f7f3ec] p-0.5 rounded-full inline-flex items-center justify-center shadow-sm">
              <img src="{logo_uri}" width="56" height="56" alt="Digital Das Logo" class="w-[56px] h-[56px] aspect-square rounded-full object-contain" />
            </div>
            <span class="text-white font-extrabold text-xl tracking-tight">Digital Das</span>
          </div>
          <p class="text-xs text-[#c9c2b4] max-w-sm mb-2">
            Lucknow's premier performance digital marketing & software agency. Turning clicks into revenue since 2015.
          </p>
        </div>
      </div>
      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between text-xs text-[#c9c2b4]/70 gap-2">
        <p>© 2026 Digital Das. All rights reserved.</p>
        <p>Lucknow, Uttar Pradesh, India • info@digitaldas.com</p>
      </div>
    </div>
  </footer>

  <!-- META PIXEL SINGLE LEAD EVENT GUARD -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      function fireLeadEvent() {{
        if (typeof fbq === 'function') {{
          if (sessionStorage.getItem('lead_pending') && !sessionStorage.getItem('lead_fired')) {{
            fbq('track', 'Lead');
            sessionStorage.setItem('lead_fired', 'true');
            sessionStorage.removeItem('lead_pending');
            console.log('[Meta Pixel] Lead event fired successfully on /thank-you');
          }}
        }} else {{
          setTimeout(fireLeadEvent, 100);
        }}
      }}
      fireLeadEvent();
    }});
  </script>
</body>
</html>
"""

# Write thank-you.html
ty_path = os.path.join(doc_dir, 'thank-you.html')
with open(ty_path, 'w', encoding='utf-8') as f:
    f.write(thank_you_html)

# Write thank-you/index.html
ty_dir = os.path.join(doc_dir, 'thank-you')
os.makedirs(ty_dir, exist_ok=True)
ty_sub_path = os.path.join(ty_dir, 'index.html')
with open(ty_sub_path, 'w', encoding='utf-8') as f:
    f.write(thank_you_html)

print('thank-you.html, thank-you/index.html, and index.html successfully updated!')
