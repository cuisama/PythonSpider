'''
Created on 2018/09/28

@author: 8LB11L2
'''


class UrlManager(object):
    
    old_urls = set()
    new_urls = set()
    
    def add_new_url(self, url):
        if url not in self.old_urls:
            self.new_urls.add(url)
    
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        
        for url in urls:
            self.add_new_url(url)

    
    def has_new_url(self):
        return len(self.new_urls) > 0

    
    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    

    
    
    
    
    
    
    
    
    
    



