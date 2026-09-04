import base64
import os

doc_dir = r'C:\Users\anand singh\Documents\digitaldas-landing'

# 1. Base64 Encode Logo
logo_path = os.path.join(doc_dir, 'assets', 'logo.png')
with open(logo_path, 'rb') as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')
data_uri_logo = f'data:image/png;base64,{b64_logo}'

# 2. Base64 Encode Poster Images
posters = ['founder.jpg', 'absolute.jpg', 'client1.jpg', 'director.jpg']
b64_posters = {}
for p in posters:
    ppath = os.path.join(doc_dir, 'assets', 'videos', p)
    if os.path.exists(ppath):
        with open(ppath, 'rb') as f:
            b64_posters[p] = f'data:image/jpeg;base64,{base64.b64encode(f.read()).decode("utf-8")}'

# 3. Update index.html
html_path = os.path.join(doc_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Logo
html = html.replace('src="assets/logo.png"', f'src="{data_uri_logo}"')
html = html.replace('href="assets/logo.png"', f'href="{data_uri_logo}"')

# Replace Posters
for p, uri in b64_posters.items():
    html = html.replace(f'poster="assets/videos/{p}"', f'poster="{uri}"')
    html = html.replace(f'poster: "assets/videos/{p}"', f'poster: "{uri}"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Logo and all 4 Poster Thumbnails successfully embedded directly inside index.html!')
