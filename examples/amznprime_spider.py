import re

from datetime import date
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapies.items import ScrapiesItem
from scrapies.custom_filters import amznprimeFilter


class AmznprimeSpider(CrawlSpider):
    name = 'amznprime_spider'
    allowed_domains = ['amazon.com']
    start_urls = ['http://www.amazon.com/s/ref=sr_pg_1?rh=n%3A2858778011%2Cp_85%3A2470955011&bbn=2864549011&sort=csrank&ie=UTF8&qid=1395326334&lo=none']
    rules = [ Rule(SgmlLinkExtractor(allow=(r'.*amazon.com/s/ref=sr_pg_(0-9)*?.*')),follow=True), Rule(SgmlLinkExtractor(allow=(r'.*?s=instant-video&ie=UTF8&.*')),callback='parse_item')]

    def parse_item(self, response):
        hxs = Selector(response)
        i = ScrapiesItem()
        head = hxs.xpath('//div[@id="dv-dp-main-content"]')
        data = hxs.xpath('//div[@class="aiv-container-limited"]')
        i['request_url'] = response.url.encode('utf-8')
        i['i_d'] = response.url.split('/')[5].encode('utf-8')
        year = head.xpath('./h1[@id="aiv-content-title"]/span[@class="release-year"]/text()').extract()
        if year == []:
            i['release_year'] = 'Unavailable'.encode('utf-8')
        else:
            i['release_year'] = year[0]
        i['cast'] = list(set(data.xpath('.//tr[contains(th,"Starring")]/td/a/text()').extract()) | set(data.xpath('.//tr[contains(th,"Supporting actors")]/td/a/text()').extract()))
        genres = []
        for g in data.xpath('.//tr[contains(th,"Genres")]/td/a/text()').extract():
            genres.append(g.strip('\n '))
        i['genre'] = genres
        if data.xpath('.//tr/th[@text="Captions and Subtitles"]').extract() is not None:
            i['has_subtitles'] = 'TRUE'.encode('utf-8')
        else:
            i['has_subtitles'] = 'FALSE'.encode('utf-8')
        i['description'] = hxs.xpath('//div[@class="dv-simple-synopsis dv-extender"]/p/text()').extract()
        i['user_rating_count'] = hxs.xpath('.//span[@id="ratingCountText"]/text()').extract()
        i['user_rating_average'] = hxs.xpath('//div[@id="avgRating"]/span/text()').extract()
        i['user_rating_max'] = str(5)
        ctypes = []
        opts = hxs.xpath('//div[@id="dv-side-box-container"]//h5/text()').extract()
        for opt in opts:
            if "Watch for $0.00 with" in opt:
                ctypes.append('SVOD'.encode('utf-8'))
            if "Rent" in opt:
                ctypes.append('RENT'.encode('utf-8'))
            if "Buy" in opt:
                ctypes.append('KEEP'.encode('utf-8'))
        i['consumption_type'] = ctypes
        if hxs.xpath('//span[@class="num-of-seasons"]/text()').extract() == []:
            i['content_type'] = 'FILM'.encode('utf-8')
            i['title'] = head.xpath('./h1[@id="aiv-content-title"]/text()').extract()[0].strip('\n ').encode('utf-8')
            rating = head.xpath('./h1[@id="aiv-content-title"]/span[@class="content-rating "]/text()').extract()
            if rating == []:
                i['rating'] = 'Unavailable'.encode('utf-8')
            else:
                i['rating'] = rating[0]
            i['director'] = data.xpath('.//tr[contains(th,"Director")]/td/text()').extract()[0].strip('\n ')
            i['studio'] = data.xpath('.//tr[contains(th,"Studio")]/td/text()').extract()[0].strip('\n ')
            i['episode_count'] = 'N/A'.encode('utf-8')
            i['network'] = 'N/A'.encode('utf-8')
        else:
            i['content_type'] = 'SERIES'.encode('utf-8')
            title = head.xpath('./h1[@id="aiv-content-title"]/text()').extract()[0].strip('\n ')
            title += ' '+head.xpath('.//div[@class="dv-dropdown-single-dark"]/text()').extract()[0].strip('\n ')
            i['title'] = title.encode('utf-8')
            i['network'] = data.xpath('.//tr[contains(th,"Network")]/td/text()').extract()[0].strip('\n ')
            eps = hxs.xpath('//div[@class="aiv-container-limited episode-list"]//ul/li/div[@class="dv-extender"]//a/text()').extract()
            c = 0
            for ep in eps:
                if re.match(r'[0-9]*\..*',ep):
                    c += 1
            i['episode_count'] = str(c).encode('utf-8')
            i['director'] = 'Unavailable'.encode('utf-8')
            i['network'] = 'N/A'.encode('utf-8')
        i['site_language'] = 'en'.encode('utf-8')
        i['meta_vendor'] = 'Allion USA'.encode('utf-8')
        i['meta_site'] = 'amazon'.encode('utf-8')
        i['meta_geo'] = 'COM'.encode('utf-8')
        today = date.today()
        month = today.month
        if month < 10:
            month = '0'+str(month)
        else:
            month = str(month)
        day = today.day
        if day < 10:
            day = '0'+str(day)
        else:
            day = str(day)
        i['meta_pull_date'] = str(today.year)+month+day
        return i
