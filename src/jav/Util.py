'''
Created on 2018/10/04

@author: 8LB11L2
'''

import time
from functools import wraps
 
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("[%ss] [%s]" %(str(t1-t0), function.__name__))
        return result
    return function_timer

def tm():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())