import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://drive.google.com/drive/folders/1TtmxKSn7LV-QxiDCzwbrXRts8nHeVvgE'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

matches = re.findall(r'aria-label="([^"]+)".*?ssk=[\'"][^:]+:[^:]+:([a-zA-Z0-9_-]{25,})', html)
for label, fid in matches:
    print(f"{label} ===> {fid}")
