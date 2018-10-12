'''
Created on 2018/09/28

@author: 8LB11L2
'''
from jav.Model import Video, db

class DataOutPuter(object):
    
    def __init__(self,lock):
        self.datas = set()
        self._data = {}
        self.lock = lock

    #收集数据存在内存datas
    def collect_data(self, data):
        if data is None:
            return
        
        for item in data:
            self.datas.add(item)

    #收集数据到_data,100就往数据库插            
    def collect_data_to_db(self, data):
        if data is None:
            return
        
        self.lock.acquire()
        for key in data:
            self._data[key] = data[key]
        
        self.db(10)
        self.lock.release()
        
    def console(self):
        for item in self.datas:
            print(item)


    def file(self):
        f = open("jav.txt", "w", encoding='utf-8')
        for item in self.datas:
            f.write(str(item) + '\n')
        f.close()
    
    def db(self,num = 100):
        if len(self._data) >= num:
            print (len(self._data))
            try:
                with db.atomic():
                    for key in self._data:
                        print (key,self._data[key])
                        x = self._data[key]
    #                     Video().update(img = self._data[key]).where(Video.url == key, Video.img == None).execute()
                        Video.create(title = x[0], url = x[1], number = x[2], date = x[3], length = x[4], director = x[5], maker = x[6], label = x[7], review = x[8], genres = x[9], cast = x[10], img = x[11])
    #                     Url.update(state=1).where(Url.url == x[1]).execute()
            except Exception as err:
                if "UNIQUE constraint failed" in str(err):
                    print(err)
                else:
                    self.lock.release()
                    raise RuntimeError(err)
                    
            self._data = {}
#         Video().update(img = _img).where(Video.url == url, Video.img == None).execute()
    
    def db_sqlserver(self):
        pass
    
    def db_sqlite(self):
        pass

