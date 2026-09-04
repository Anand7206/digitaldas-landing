import urllib.request
import os
import uuid
import ssl

doc_dir = r'C:\Users\anand singh\Documents\digitaldas-landing'
vdir = os.path.join(doc_dir, 'assets', 'videos')

ctx = ssl._create_unverified_context()

def upload_file_catbox(file_path):
    filename = os.path.basename(file_path)
    boundary = '----WebKitFormBoundary' + uuid.uuid4().hex
    
    with open(file_path, 'rb') as f:
        file_data = f.read()

    body = []
    body.append(f'--{boundary}\r\nContent-Disposition: form-data; name="reqtype"\r\n\r\nfileupload\r\n'.encode('utf-8'))
    body.append(f'--{boundary}\r\nContent-Disposition: form-data; name="fileToUpload"; filename="{filename}"\r\nContent-Type: video/mp4\r\n\r\n'.encode('utf-8'))
    body.append(file_data)
    body.append(f'\r\n--{boundary}--\r\n'.encode('utf-8'))
    
    payload = b''.join(body)
    
    req = urllib.request.Request(
        'https://catbox.moe/user/api.php',
        data=payload,
        headers={
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    )
    
    with urllib.request.urlopen(req, context=ctx) as response:
        res_text = response.read().decode('utf-8').strip()
        return res_text

videos = ['founder.mp4', 'absolute.mp4', 'client1.mp4', 'director.mp4']
cdn_urls = {}

for vf in videos:
    vpath = os.path.join(vdir, vf)
    if os.path.exists(vpath):
        print(f'Uploading {vf} ({round(os.path.getsize(vpath)/(1024*1024), 2)} MB) to CDN...')
        try:
            url = upload_file_catbox(vpath)
            if url.startswith('http'):
                cdn_urls[vf] = url
                print(f'✅ [SUCCESS] {vf} -> {url}')
            else:
                print(f'❌ [ERROR] {vf}: {url}')
        except Exception as e:
            print(f'❌ [EXCEPT] {vf}: {e}')

print('\n=== CDN URL DICTIONARY ===')
for k, v in cdn_urls.items():
    print(f'"{k}": "{v}",')
