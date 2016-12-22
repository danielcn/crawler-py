from HTMLParser import HTMLParser
from urlparse import urlparse

class LinkFinder(HTMLParser):

    def _init_(self):
        super(self)._init_()

    def handle_starttag(self, tag, atts):
        print(tag)

    def error(self, message):
        pass

finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Paser me!<h1></body></html>')
