'''
Created on 2018/09/28

@author: 8LB11L2
'''
import urllib.request
from jav.Model import Video

# exist_urls = Video.select(Video.url).dicts()

class HtmlDownloader(object):
    
    
    def do(self, url):
        if url is None:
            return None
        
        if len(Video.select(Video.title).where(Video.url==url).dicts()) > 0:
            return None
        
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        req = urllib.request.Request(url, headers={"User-Agent":user_agent})
        res = urllib.request.urlopen(req)
        if res.code != 200:
            return None
        html = res.read().decode("utf-8")
        return html
        
    
    



