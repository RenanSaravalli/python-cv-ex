#Crie um código em python que teste se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=51')
except:
    print('Não consegui acessar o youtube.')
else:
    print('Consegui acessar o youtube')
    #print(site.read()) vai mostrar o conteúdo do site