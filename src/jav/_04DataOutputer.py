'''
Created on 2018/09/28

@author: 8LB11L2
'''
from jav.Model import Video

class DataOutPuter(object):
    
    def __init__(self):
        self.datas = set()

    def collect_data(self, data):
        if data is None:
            return
        
        for item in data:
            self.datas.add(item)
#             print(item)
        
    def console(self):
        for item in self.datas:
            print(item)


    def file(self):
        f = open("jav.txt", "w", encoding='utf-8')
        for item in self.datas:
            f.write(str(item) + '\n')
        f.close()
    
    def db_sqlserver(self):
        pass
    
    def db_sqlite(self):
        pass

