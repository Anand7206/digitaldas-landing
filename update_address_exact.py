import os
import urllib.parse

doc_dir = r'C:\Users\anand singh\Documents\digitaldas-landing'
scratch_dir = r'C:\Users\anand singh\.gemini\antigravity\scratch\digital-das-landing-page'

new_addr_text = "First Floor, B - 3, 11, Vibhuti Khand, Gomti Nagar, Lucknow, Uttar Pradesh 226010"

# Files to update
target_files = [
    os.path.join(doc_dir, 'index.html'),
    os.path.join(doc_dir, 'thank-you.html'),
    os.path.join(doc_dir, 'thank-you', 'index.html'),
    os.path.join(scratch_dir, 'index.html')
]

for fp in target_files:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace text inside spans
        content = content.replace(
            "<span>Head Office : First Floor, B-3/11, Vibhuti Khand, Gomti Nagar – 226010</span>",
            f"<span>Head Office : {new_addr_text}</span>"
        )
        content = content.replace(
            "<span>First Floor, B-3/11, Vibhuti Khand, Gomti Nagar, Lucknow – 226010</span>",
            f"<span>Head Office : {new_addr_text}</span>"
        )

        # Replace Google Maps href query parameter
        maps_query = urllib.parse.quote_plus(new_addr_text)
        new_maps_url = f"https://maps.google.com/?q={maps_query}"
        
        # Replace old google maps URLs
        old_maps_urls = [
            "https://maps.google.com/?q=First+Floor,+B-3/11,+Vibhuti+Khand,+Gomti+Nagar,+Lucknow+226010",
            "https://maps.google.com/?q=First+Floor,+B-3/11,+Vibhuti+Khand,+Gomti+Nagar,+Lucknow+226010"
        ]
        for ourl in old_maps_urls:
            content = content.replace(ourl, new_maps_url)

        # Replace JSON-LD schema streetAddress
        content = content.replace(
            '"streetAddress": "First Floor, B-3/11, Vibhuti Khand, Gomti Nagar"',
            '"streetAddress": "First Floor, B - 3, 11, Vibhuti Khand, Gomti Nagar"'
        )
        content = content.replace(
            '"streetAddress": "First Floor, B-3/11, Vibhuti Khand, Gomti Nagar – 226010"',
            '"streetAddress": "First Floor, B - 3, 11, Vibhuti Khand, Gomti Nagar"'
        )

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated:', fp)
