'''
Created on 2018/09/28

@author: 8LB11L2
'''
# from os import path
from jav.Model import Url, Video
from jav.Util import tm

class UrlManager(object):
    
    old_urls = set()
    new_urls = set()
    
    def __init__(self, lock):
        self.lock = lock
    
#     从文件读URL
#     if path.isfile("urls.txt"):
#         f = open("urls.txt","r")
#         for line in f:
#             line = line[1:-1]
#             urls = line.strip().replace(" ","").replace("'","").split(",")
#         for u in urls:
#             new_urls.add(u)
# #             Url.create(url=u)
#         f.close()

#     res = Url.select()
    res = Video.select(Video.url).where(Video.img == None)
    for u in res :
#         if u.state == 1:
#             old_urls.add(u.url)
#         else: 
        new_urls.add(u.url)
            
    def add_new_url(self, _url):
        if _url not in self.old_urls:
            if _url not in self.new_urls:
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
#     lock = threading.Lock()
    
    def get_new_url(self,num):
#         self.lock.acquire()
        print("[%s] exec %s: %s" % (num, self.__index, tm()))#threading.currentThread().idents
        self.__index += 1
        url = self.new_urls.pop()
        self.old_urls.add(url)
#         self.lock.release()
        return url

    

    
    
    
    
    
    
    
    
    
    



