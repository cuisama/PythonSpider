
class Video(object):

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __str__(self):
        return  self.url + " " +self.title

    def __eq__(self, other):
        if isinstance(other, Video):
            return (self.title == other.title) and (self.url == other.url)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.title) + hash(self.title)