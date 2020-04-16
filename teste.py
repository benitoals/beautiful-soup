'''
Created on 5 de mar de 2017

@author: benito
'''
from bs4 import BeautifulSoup
import requests

# with open('arquivo.html', 'r') as f:
#     soupt_string = BeautifulSoup(f.read(), 'html.parser')
# print(soupt_string)

# r = requests.get('http://www.google.com')
# soup = BeautifulSoup(r.text, 'lxml')
# print(soup)

# with open('arquivo.html', 'r') as f:
#     soup_string = BeautifulSoup(f.read(), 'html5lib')
# print(soup_string)

# with open('arquivo.html', 'r') as f:
#     soup = BeautifulSoup(f, 'lxml')
# 
# tag = soup.title
# print(tag)
# 
# print(tag.name)
# 
# tag = soup.p
# 
# print(tag)

# with open('arquivo.html', 'r') as f:
#     soup = BeautifulSoup(f, 'html.parser')
# 
# print(soup.p['class'])
# 
# print(soup.p.attrs)
# 
# print(soup.a['href'])
# 
# print(soup.a.get('href'))


with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')

# print(soup.prettify())
# print(soup.get_text())
# print(soup.p.get_text())
# print(soup.p.string)
# print(soup.p.b.string)


