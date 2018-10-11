'''
Created on 2018/10/04

@author: 8LB11L2
'''
import urllib.request
from Util.com import fn_timer

class HtmlDownloader(object):
    
    @fn_timer
    def do(self, url):
        if url is None:
            return None
        
#         if len(Video.select(Video.title).where(Video.url==url).dicts()) > 0:
#             return None
        print("    " + url[0],url[1])
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        req = urllib.request.Request(url[1], headers={"User-Agent":user_agent})
        res = urllib.request.urlopen(req, timeout=3600)
        if res.code != 200:
            return None
        data = res.read()
        with open("doc/"+url[0]+".docx", "wb") as code:     
            code.write(data)
        return None
        
    
    



