'''
Created on 2018/09/28

@author: 8LB11L2
'''


class DataOutPuter(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        for item in data:
            self.datas.append(item)
        
    def console(self):
        for item in self.datas:
            print(item[1],item[0])
    
    



