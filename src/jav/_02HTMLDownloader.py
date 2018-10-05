'''
Created on 2018/09/28

@author: 8LB11L2
'''
import urllib.request
# from jav.Model import Video
from jav.Util import fn_timer

# exist_urls = Video.select(Video.url).dicts()

class HtmlDownloader(object):
    
    @fn_timer
    def do(self, url):
        if url is None:
            return None
        
#         if len(Video.select(Video.title).where(Video.url==url).dicts()) > 0:
#             return None
        print("    " + url)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        req = urllib.request.Request(url, headers={"User-Agent":user_agent})
        res = urllib.request.urlopen(req, timeout=3)
        if res.code != 200:
            return None
        html = res.read().decode("utf-8")
        return html
        
    
    



