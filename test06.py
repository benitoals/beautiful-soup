'''
Created on 6 de mar de 2017

@author: benito
'''
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
      
# primaryconsumers = soup.find_all(class_='primaryconsumerlist')
# primaryconsumer = primaryconsumers[0]
# print(primaryconsumer)

# parente_ul = primaryconsumer.find_parents('ul')
# print(parente_ul)

# parent_ul = primaryconsumer.find_parent('ul')
# print(parent_ul)

# producers = soup.find(id='quaternaryconsumers')
# next_sibling = producers.find_previous_sibling()
# print(next_sibling)

# producers = soup.find(id ='quaternatryconsumers')
# previous_siblings = producers.fin
# print(previous_siblings)

# 
# 
# producers = soup.find(id='producers')
# tag_next = producers.find_next()
# print(tag_next)

# producers = soup.find(id='producers')
# tag_next = producers.find_all_next()
# print(tag_next)

producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_all_previous()
print(tag_previous)