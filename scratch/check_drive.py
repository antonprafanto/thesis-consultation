import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

for url in [
    'https://drive.google.com/drive/folders/1TtmxKSn7LV-QxiDCzwbrXRts8nHeVvgE',
    'https://drive.google.com/drive/folders/17X94D0gTLHhMCUQF0pITm8FodYac4NCD'
]:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            found = set(re.findall(r'[\w\- ]+\.(?:docx?|pdf)', html))
            print(f"URL: {url}")
            print("Found files:", found)
    except Exception as e:
        print(f"Error {url}: {e}")
