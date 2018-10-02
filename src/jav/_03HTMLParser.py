'''
Created on 2018/09/28

@author: 8LB11L2
'''
from bs4 import BeautifulSoup
import re

from jav.Model import Video

class HtmlParser(object):
    
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
        
    
    def _get_data(self, url, soup):
        if re.search("\/\?v=javli",url) is None:
            return None
        print(url)
        datas = []
        
        title = soup.find("div", id="video_title").find("a",href=re.compile("\?v=javli\w*")).text
        
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
        
        x = self._format(title, url, number, date, length, director, maker, label, review, genres, cast)
        m = Video(x)
#         Video.create(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10])
        Video.create(title = x[0], url = x[1], number = x[2], date = x[3], length = x[4], director = x[5], maker = x[6], label = x[7], review = x[8], genres = x[9], cast = x[10])
        datas.append(m)   
        
        return datas
    
    
    def do(self, html, url):
        if html is None or url is None:
            return None, None
        
        soup = BeautifulSoup(html,"html.parser")
        
        new_urls = self._get_urls(url, soup)
        new_data = self._get_data(url, soup)
        
        return new_data, new_urls
    
    _tag = re.compile("<.*?>")
    
    def _format(self, title, url, number, date, length, director, maker, label, review, genres, cast):
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
        return _title, _url, _number, _date, _length, _director, _maker, _label, _review, _genres, _cast
    



