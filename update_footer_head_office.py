import os
import urllib.parse

doc_dir = r'C:\Users\anand singh\Documents\digitaldas-landing'
scratch_dir = r'C:\Users\anand singh\.gemini\antigravity\scratch\digital-das-landing-page'

new_addr_text = "First Floor, B - 3, 11, Vibhuti Khand, Gomti Nagar, Lucknow, Uttar Pradesh 226010"
maps_query = urllib.parse.quote_plus(new_addr_text)
new_maps_url = f"https://maps.google.com/?q={maps_query}"

old_footer_block = """          <div class="text-[11px] text-[#c9c2b4]/80">
            <span class="font-bold text-[#e8a13c]">Branch Office:</span> 
            <a href="https://maps.google.com/?q=D-217+B,+First+Floor,+Vibhuti+Khand,+Gomti+Nagar,+Lucknow+226010" 
               target="_blank" 
               rel="noopener noreferrer" 
               class="hover:text-white underline ml-1 focus:outline-none focus:ring-2 focus:ring-[#e8a13c] rounded">
              D-217 B, First Floor, Vibhuti Khand, Gomti Nagar, Lucknow – 226010
            </a>
          </div>"""

new_footer_block = f"""          <div class="text-[11px] text-[#c9c2b4]/80">
            <span class="font-bold text-[#e8a13c]">Head Office:</span> 
            <a href="{new_maps_url}" 
               target="_blank" 
               rel="noopener noreferrer" 
               class="hover:text-white underline ml-1 focus:outline-none focus:ring-2 focus:ring-[#e8a13c] rounded">
              {new_addr_text}
            </a>
          </div>"""

files_to_update = [
    os.path.join(doc_dir, 'index.html'),
    os.path.join(doc_dir, 'thank-you.html'),
    os.path.join(doc_dir, 'thank-you', 'index.html'),
    os.path.join(scratch_dir, 'index.html')
]

for fp in files_to_update:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_footer_block in content:
            content = content.replace(old_footer_block, new_footer_block)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Successfully updated footer in:', fp)
        else:
            print('Old footer block not matched in:', fp)
