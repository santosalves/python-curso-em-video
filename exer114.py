import urllib.request

try:
    URL = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('O site Pudim está acessível.')


