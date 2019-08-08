from html.parser import HTMLParser
from urllib.parse import urljoin

class LinkFinder(HTMLParser):

    def _init_(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for(attribute, value) in attrs:
                if attribute == 'href':
                    url = urljoin(self.base_url, value)
                    self.links.add(url)

    def handle_endtag(self, tag):
        pass

    def error(self, message):
        pass
