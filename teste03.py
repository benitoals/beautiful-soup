'''
Created on 5 de mar de 2017

@author: benito
'''
from bs4 import BeautifulSoup
from bs4.element import Tag

with open('arquivo03.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# print(soup.div.next_element.next_element)
# print(soup.li.previous_element.previous_element)

# for e in soup.ul.next_elements:
#     if isinstance(e, Tag):
#         print(e)
for e in soup.li.previous_elements:
    print(repr(e))