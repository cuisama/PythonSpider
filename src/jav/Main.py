'''
Created on 2018/09/28

@author: 8LB11L2
'''
from jav import _01URLManager, _02HTMLDownloader, _03HTMLParser, _04DataOutputer


class SpiderMan(object):
    
    def __init__(self):
        self.urls = _01URLManager.UrlManager()
        self.downloader = _02HTMLDownloader.HtmlDownloader()
        self.parser = _03HTMLParser.HtmlParser()
        self.outputer = _04DataOutputer.DataOutPuter()
    
    def crawl(self, root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html = self.downloader.do(new_url)
                res, new_urls = self.parser.do(html, new_url)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(res)
            except:
                print("error")

        print("end")
        self.outputer.file()
    



if __name__ == '__main__':
    root_url = "http://www.o23g.com/cn/vl_update.php"   # "http://www.j20a.com/cn/"
    spider_man = SpiderMan()
    spider_man.crawl(root_url)
    
    