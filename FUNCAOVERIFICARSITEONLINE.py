import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=50')
except urllib.erro.URLERROR:
    print('ERRO NAO FUNCIONOU')
else:
    print('FUNCIONOU')
    print(site.read())