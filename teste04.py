'''
Created on 5 de mar de 2017

@author: benito
'''
from bs4 import BeautifulSoup
from bs4.element import Tag

with open('arquivo04.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# tag = soup.find('li')
# print(tag)

# tag = soup.find(string='bear')
# print(tag)

# tag = soup.find(id='primaryconsumers')
# print(tag)

# tag = soup.find(attrs={'class':'primaryconsumerlist'})
# print(tag)

# tag = soup.find(class_='primaryconsumerlist')
# print(tag)

# tag = soup.find('li', attrs={'class':'producerlist'})
# print(tag)

# tag = soup.ul.li.find('li')
# print(tag)

def is_secondary_consumers(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer.li.div.string)