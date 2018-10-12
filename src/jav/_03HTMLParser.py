'''
Created on 2018/09/28

@author: 8LB11L2
'''
from bs4 import BeautifulSoup
import re

from jav.Util import fn_timer

class HtmlParser(object):
    
    def __init__(self, lock):
        self.lock = lock
    
    @fn_timer
    def _get_urls(self, url, soup):
#         if re.search("vl_update.php\?&mode=&page=",url) is None:
#             return None
        
        urls = []

        nodes = soup.find_all("a",href=re.compile("vl_update.php\?&mode=&page=\d+"))
        for node in nodes:
            urls.append("http://www.o23g.com/cn/" + node["href"])
        
        nodes = soup.find_all("a",href=re.compile("\.\/\?v=javli\w*"))
        for node in nodes:
            urls.append("http://www.o23g.com/cn/" + node["href"][2:])
            
        nodes = soup.find_all("a",href=re.compile("vl_star.php\?s="))
        for node in nodes:
            urls.append("http://www.o23g.com/cn/" + node["href"])
        
        nodes = soup.find_all("a",href=re.compile("vl_star.php\?&mode=&s=\w*?&page=\d+"))
        for node in nodes:
            urls.append("http://www.o23g.com" + node["href"])
        
        return urls
        
    @fn_timer
    def _get_data(self, url, soup):
        if re.search("\/\?v=javli",url) is None:
            return None
        
        datas = {}
        
        title = soup.find("div", id="video_title").find("a",href=re.compile("\?v=javli\w*")).text
        _img = soup.find("img",id="video_jacket_img")["src"]
        
        video_info = soup.find("div",id="video_info")
        number = video_info.find("div",id="video_id").find("td",class_="text").text
        date = video_info.find("div",id="video_date").find("td",class_="text").text
        length = video_info.find("div",id="video_length").find("span",class_="text").text
        director = video_info.find("div",id="video_director").find("a")
        maker = video_info.find("div",id="video_maker").find("a")
        label = video_info.find("div",id="video_label").find("a")
        video_review = video_info.find("div",id="video_review")
        review = video_review and video_review.find("span",class_="score").text
        genres = video_info.find("div",id="video_genres").find_all("a")
        cast = video_info.find("div",id="video_cast").find_all("a")
#         m = Video(title, url, number, date, length, director, maker, label, review, genres, cast)
        
        x = self._format(title, url, number, date, length, director, maker, label, review, genres, cast, _img)
        
        datas[url] = x 
        
        return datas #返回一个字典
    
    
    
    
    def do(self, html, url):
        if html is None or url is None:
            return None, None
        
        soup = BeautifulSoup(html,"html.parser")
        
        new_urls = self._get_urls(url, soup)
        new_data = self._get_data(url, soup)
        
        return new_data, new_urls
    
    _tag = re.compile("<.*?>")
    
    def _format(self, title, url, number, date, length, director, maker, label, review, genres, cast, img):
        _title = title
        _url = url
        _number = number
        _date = date
        _length = length
        _director = director and director.text or ""
        _maker = maker and maker.text or ""
        _label = label and label.text or ""
        _review = review or ""
        _genres = genres and self._tag.sub("",str(genres)) or ""
        _cast = cast and self._tag.sub("",str(cast)) or ""
        _img = img
        return _title, _url, _number, _date, _length, _director, _maker, _label, _review, _genres, _cast, _img
    



