'''
Created on 7 de mar de 2017

@author: benito
'''
import requests
from bs4 import BeautifulSoup

# url = 'https://www.youtube.com/results?'
# 
# payload = {'search_query':'como fazer strogonoff de frangos'}
# 
# r = requests.get(url, params=payload)
# 
# with open('youtube.html', 'wb') as f:
#     f.write(r.content)

# url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
# 
# payload = {'relaxation' : '12240000' , 'tipoCEP': 'ALL', 'semelhante': 'N' }
# 
# response = requests.post(url, data=payload)
# 
# with open('correios.html', 'wb') as f:
#     f.write(response.content)

# url = 'http://www.google.com'
# r = requests.get(url)
# # print(r.status_code)
# # 
# # if r.status_code == requests.codes.ok:
# #     soup = BeautifulSoup(r.text, 'html.parser')
# print(r.request.headers)

url = 'http://michaelis.uol.com.br/busca?'

payload = {'r':'0','f':'0','t':'0','palavra':'talk'}




header = {'Referer'  :  'http://michaelis.uol.com.br/',
'Upgrade-Insecure-Requests'  :  '1',
'Accept'   : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'User-Agent'  :  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'}

r = requests.get(url=url, params=payload, headers = header)

soup = BeautifulSoup(r.text, 'lxml')

div = soup.find('div' ,{'id': 'content'})

print(div.get_text())

with open('michaelis.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
# print(r.request.headers)

