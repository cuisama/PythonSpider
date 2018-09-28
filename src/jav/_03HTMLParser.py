'''
Created on 2018/09/28

@author: 8LB11L2
'''
from bs4 import BeautifulSoup
import re

from jav.Model import Video


class HtmlParser(object):
    
    
    def _get_urls(self, url, soup):
        nodes = soup.find_all("a",href=re.compile("vl_update.php\?&mode=&page=\d+"))
        urls = []
        for node in nodes:
            pass
            # urls.append("http://www.o23g.com/cn/" + node["href"])
        return urls
        
    
    def _get_data(self, url, soup):
        nodes = soup.find_all("a",href=re.compile("\.\/\?v=javli\w*"))
        res = []
        for node in nodes:
            m = Video(node["title"], node["href"])
            res.append(m)
        return res
    
    
    def do(self, html, url):
        if html is None or url is None:
            return
        
        soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
        
        new_urls = self._get_urls(url, soup)
        new_data = self._get_data(url, soup)
        
        return new_data, new_urls
    
    



