import urllib.request, re

# Fetch the main JS bundle and search for API endpoint patterns
url = 'https://www.usaswimming.org/assets/index-06d7cf2c.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
r = urllib.request.urlopen(req, timeout=15)
js = r.read().decode(errors='ignore')
print(f'Bundle size: {len(js)} chars')

# Look for fetch/endpoint patterns
patterns = re.findall(r'["\`](/[a-zA-Z0-9/_-]*(?:api|times|rank|search|swim)[a-zA-Z0-9/_?=&-]*)["\`]', js)
print('\nAPI-like paths found:')
for p in sorted(set(patterns))[:30]:
    print(' ', p)
