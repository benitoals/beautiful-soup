'''
Created on 5 de mar de 2017

@author: benito
'''
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
import requests

with open('arquivo.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# print(soup.title)
# print(soup.head.title)
# print(soup.a)
# print(soup.a.img)
# print(soup.td)
# print(soup.tr)
# print(soup.tr.td)
# 
# print(soup.td.attrs)
# print(soup.td['class'])
# print(soup.td['class'][0])

# print(soup.table.contents)
# print(type(soup.contents))
# print(len(soup.contents))
# print(soup.table.contents[1])
# print(soup.table.contents[1].span)
# print(soup.table.contents[1].span.string)
# print(soup.table.contents[3].td)
# 
# for child in soup.table.contents:
#     if child.name == 'tr':
#         print(child)

# print(type(soup.children))

# for child in soup.footer.children:
#     print(child)

# for child in soup.footer.p.children:
#     if child.name == 'a':
#         print(child.get('href'))

# print(len(list(soup.children)))
# print(len(list(soup.descendants)))



# for tag in soup.descendants:
#     if isinstance(tag, NavigableString):
#         print(tag)
#     else:
#         print(tag.name)
        
# for tag in soup.descendants:
#     if isinstance(tag, Tag):
#         print(tag)

# for string in soup.aside.strings:
#     print(repr(string))

# for string in soup.aside.stripped_strings:
#     print(repr(string))

# tag_title = soup.title
# print(tag_title.parent)
# 
# print(soup.td.parent)

# print(soup.td.parent.parent)

# for pai in soup.p.parents:
#     print(pai.name)

# print(soup.nex_sibling)

# print(soup.td.next_sibling.next_sibling)

# for sibling in soup.p.next_siblings:
#     print(repr(sibling))

for sibling in soup.p.previous_siblings:
    print(repr(sibling))