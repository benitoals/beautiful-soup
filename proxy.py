'''
Created on 7 de mar de 2017

@author: benito
'''
import requests
url = 'https://www.hide-my-ip.com/pt/proxylist.shtml'
proxies = { 'http' : '213.251.139.236:8080'}

try:
    r = requests.get(url, proxies=proxies)
    print(r.status_code)
except requests.exceptions.ConnectionError as e:
    print(str(e))