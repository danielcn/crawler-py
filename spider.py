import urllib
from link_finder import LinkFinder
from general import*


class Spider:

    # Class varibles (shared ammong all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def _init_(self, project_name, base_url):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue_file.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'

        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def  boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider,project_name, Spider_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.clawler:
            print(thread_name + 'now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled: ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spide.gether_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.updates_files()
