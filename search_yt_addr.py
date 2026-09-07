import os

doc_dir = r'C:\Users\anand singh\Documents\digitaldas-landing'

for root, dirs, files in os.walk(doc_dir):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                for idx, line in enumerate(lines, 1):
                    if 'youtube.com' in line.lower() or 'vibhuti khand' in line.lower() or 'first floor' in line.lower() or 'streetaddress' in line.lower():
                        rel = os.path.relpath(fp, doc_dir)
                        print(f'{rel} (Line {idx}): {line.strip()}')
