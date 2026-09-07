import os

doc_dir = r'C:\Users\anand singh\Documents\digitaldas-landing'

old_yt = "https://youtube.com/@Dastalks."
new_yt = "https://www.youtube.com/channel/UCEYRS7mxRPVP7qPHsnbD23g"

old_addr_text = "<span>First Floor, B-3/11, Vibhuti Khand, Gomti Nagar, Lucknow – 226010</span>"
new_addr_text = "<span>Head Office : First Floor, B-3/11, Vibhuti Khand, Gomti Nagar – 226010</span>"

files_to_update = [
    os.path.join(doc_dir, 'index.html'),
    os.path.join(doc_dir, 'thank-you.html'),
    os.path.join(doc_dir, 'thank-you', 'index.html'),
    os.path.join(r'C:\Users\anand singh\.gemini\antigravity\scratch\digital-das-landing-page', 'index.html')
]

for fp in files_to_update:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update YouTube URLs
        content = content.replace(old_yt, new_yt)
        
        # 2. Update Head Office Address text
        content = content.replace(old_addr_text, new_addr_text)
        
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated:', fp)
