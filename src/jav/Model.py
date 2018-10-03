import re
from peewee import TextField, CharField, SqliteDatabase,\
    Model, IntegerField

db = SqliteDatabase("jav.db")

class Url(Model):
    url = CharField(max_length=100)
    state = IntegerField(default=0)
    class Meta:
        database = db
        table_name = 'url'

class Video(Model):
    
#     id = IntegerField(unique=True,auto=True)    #key
    title = TextField()
    url = CharField(max_length=60)
    number = CharField(max_length=10)
    date = CharField(max_length=20)
    length = CharField(max_length=5)
    director = TextField()
    maker = TextField()
    label = TextField()
    review = CharField(max_length=5)
    genres = TextField()
    cast = TextField()
    class Meta:
        database = db
        table_name = 'video'


    tag = re.compile("<.*?>")

#     def __init__(self, title, url, number, date, length, director, maker, label, review, genres, cast):
#         self.title = title
#         self.url = url
#         self.number = number
#         self.date = date
#         self.length = length
#         self.director = director and director.text or ""
#         self.maker = maker and maker.text or ""
#         self.label = label and label.text or ""
#         self.review = review or ""
#         self.genres = genres and self.tag.sub("",str(genres)) or ""
#         self.cast = cast and self.tag.sub("",str(cast)) or ""

    
    def __str__(self):
#         return  self.url + " " +self.title
        return self.title + " " + self.url + " " + self.number + " " + self.date + " " + self.length + " " + self.director + " " + self.maker + " " + self.label + " " + self.review + " " + str(self.genres) + " " + str(self.cast)

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.title) + hash(self.title)

db.connect()
tables = db.get_tables()
if 'video' not in tables:
    db.create_tables([Video,])    
#     Video.create(title = "_title", url = "_url", number = "_number", date = "_date", length = "_len", director = "_director", maker = "_maker", label = "_label", review = "_review", genres = "_genres", cast = "_cast")
if 'url' not in tables:
    db.create_tables([Url,])