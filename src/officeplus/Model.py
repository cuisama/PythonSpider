'''
Created on 2018/10/04

@author: 8LB11L2
'''
import re
from peewee import TextField, CharField, SqliteDatabase,\
    Model, IntegerField, CompositeKey

db = SqliteDatabase("officeplus.db")

class Url(Model):
    id = IntegerField(unique=True)
    url = CharField(unique=True, max_length=100)
    state = IntegerField(default=0)
    class Meta:
        database = db
        table_name = 'url'
        primary_key = CompositeKey('url')

class Doc(Model):
    
    id = IntegerField(unique=True)    #key
    title = TextField()
    url = CharField(unique=True, primary_key=True, max_length=100)
    page_number = CharField(max_length=10)
    size = CharField(max_length=20)
    proportion = CharField(max_length=5) #比例
    purpose = TextField() #用途
    style = TextField() #风格
    chart = TextField() #图表
    type = CharField(max_length=5) #文件类型
    genres = TextField() #分类
    class Meta:
        database = db
        table_name = 'doc'


    tag = re.compile("<.*?>")
    

db.connect()
tables = db.get_tables()
if 'doc' not in tables:
    db.create_tables([Doc,])    
    
if 'url' not in tables:
    db.create_tables([Url,])