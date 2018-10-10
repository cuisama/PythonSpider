'''
Created on 2018/09/28

@author: 8LB11L2
'''
from jav import _01URLManager, _02HTMLDownloader, _03HTMLParser, _04DataOutputer
import traceback
from jav.Model import Url
import threading

class SpiderMan(object):
    
    def __init__(self, lock):
        self.urls = _01URLManager.UrlManager(lock)
        self.downloader = _02HTMLDownloader.HtmlDownloader()
        self.parser = _03HTMLParser.HtmlParser(lock)
        self.outputer = _04DataOutputer.DataOutPuter()
    
    def crawl(self,th_num):
        
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url(th_num)
                html = self.downloader.do(new_url)
                new_datas, new_urls = self.parser.do(html, new_url)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_datas)
                #TODO
#                 if len(self.outputer.datas) > 20:
#                     break
#                 Url.update(state=1).where(Url.url == new_url).execute()
            except Exception:
                print('traceback.print_exc():', traceback.print_exc())
#                 Url.update(state=2).where(Url.url == new_url).execute()

        print("end")
#         self.outputer.file()
    



if __name__ == '__main__':
    root_url = "http://www.o23g.com/cn/vl_update.php?&mode=&page="   # "http://www.j20a.com/cn/"
    lock = threading.Lock()
    spider_man = SpiderMan(lock)
#     TODO
#     spider_man.urls.add_new_url(root_url)
    th = []
    for i in range(0,100):
        t = threading.Thread(target=spider_man.crawl, args=(i,))
        th.append(t)
        t.start()
    for t in th:
        t.join()
#         spider_man.crawl()
    
    