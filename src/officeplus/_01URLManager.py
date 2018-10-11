'''
Created on 2018/10/04

@author: 8LB11L2
'''
# from os import path
from officeplus.Model import Url
from Util.com import tm
import json



class UrlManager(object):
    
    old_urls = set()
    new_urls = set()
    
    #init data
    
    with open("Cats_WORD_.json",'r',encoding='utf-8') as f:
        data = json.load(f)["Templates"]
    for doc in data:
        new_urls.add((doc["Title"],"http://www.officeplus.cn" + doc["Download"]))
    
    def __init__(self, lock):
        self.lock = lock

    res = Url.select()
    for u in res :
        if u.state == 1:
            old_urls.add(u.url)
        else: 
            new_urls.add(u.url)
            
    def add_new_url(self, _url):
        if _url not in self.old_urls and _url not in self.new_urls:
            Url.create(url = _url)
            self.new_urls.add(_url)
    
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        
        for url in urls:
            self.add_new_url(url)

    
    def has_new_url(self):
        return len(self.new_urls) > 0
    
    __index = 1 
    
    def get_new_url(self,num):
#         self.lock.acquire()
        print("[%s] exec %s: %s" % (num, self.__index, tm()))#threading.currentThread().idents
        self.__index += 1
        url = self.new_urls.pop()
        self.old_urls.add(url)
#         self.lock.release()
        return url

    

    
    
    
    
    
    
    
    
    
    



