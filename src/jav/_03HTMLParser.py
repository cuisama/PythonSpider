'''
Created on 2018/09/28

@author: 8LB11L2
'''
from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    
    
    def _get_urls(self, url, soup):
#         soup.find_all("div",class_="video",)
        return None
        
    
    def _get_data(self, url, soup):
        nodes = soup.find_all("a",href=re.compile("\.\/\?v=javli\w*"))
        res = []
        for node in nodes:
            res.append((node["title"], node["href"]))
        return res
    
    
    def do(self, html, url):
        if html is None or url is None:
            return
        
        soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
        
        new_urls = self._get_urls(url, soup)
        new_data = self._get_data(url, soup)
        
        return new_data, new_urls
    
    



