import requests
print('Extracting URLs...')
a=open('URLS_SCRAPS.txt').read().split('\n')
for url in a:
    sites=requests.get(url,verify=False).text
    open('URLS_COMBO.txt','a').write(sites+'\n')
quit()
