'''
Created on 7 de mar de 2017

@author: benito
'''
import requests
from bs4 import BeautifulSoup

# url = 'http://www.submarino.com.br'
#  
#  
# s = requests.Session() 
# s.get(url)
#  
# # cookie = s.cookies.get_dict()
# # print(cookie)
#  
# busca = 'notebook'
# url = 'http://www.submarino.com.br/busca/?conteudo={0}' . format(busca)
#  
# r = s.get(url)
# with open('submarino.html', 'w', encoding='utf-8') as f:
#     f.write(r.text)


# r = requests.get('http://www.google.com', allow_redirects=False)
# print(r.history)

# r = requests.get('http://www.google.com', timeout=(1, 1))
# print(r.url)

# url = 'h.com'
# 
# try:
#     r = requests.get(url)  
# except requests.exceptions.RequestException as e:
#     print ('RequestException')
#     print(str(e))

# url = 'http://compras.dados.gov.br'
# cnpj = '07689002000189'
# 
# url = '{0}:8080/contratos/v1/contratos.json?cnpj_contratada={1}'.format(url, cnpj)
# 
# r = requests.get(url)
# print(r.json()['_embedded']['contratos'][0]['objeto'])

# url = 'http://st3.depositphotos.com/11426354/14157/i/1600/depositphotos_141577094-stock-photo-beautiful-woman-in-train.jpg'
# 
# r = requests.get(url)
# 
# with open('img.jpg', 'wb') as f:
#     f.write(r.content)

# url = 'http://httpbin.org/basic-auth/user/passwd'
# 
# r = requests.get(url)
# print(r.status_code)
# 
# r = requests.get(url, auth=('user', 'passwd'))
# print(r.status_code)








