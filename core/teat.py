import urllib3
# scheme='https',
# netloc='https://libraries.io',
http = urllib3.PoolManager()
r = http.request('GET', 'https://libraries.io')

print(r.status)