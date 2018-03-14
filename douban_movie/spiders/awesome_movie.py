# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import MovieItem
import re
class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):

    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    rules = (
        
        Rule(LinkExtractor(allow=('/?from=subject-page')),callback='parse_movie_item',follow=True),
        # Rule(LinkExtractor(allow=('movie.douban.com/subject/\d\d\d\d\d\d\d')),follow=True),
        # Rule(LinkExtractor(allow=('from=subject-page"')),callback='parse_movie_item'),


    )


    def parse_movie_item(self, response):
        "TODO: 解析 item"
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.css('title::text').extract()[0][0:-5].strip()
        summary_text = response.css('span[property="v:summary"]::text').extract_first()
        item['summary']=re.sub('\s','',summary_text)
        item['score'] = response.css('strong[property="v:average"]::text').extract()[0]
        return item

    def parse_start_url(self, response):
        yield self.parse_movie_item(response)


    def parse_page(self, response):
        yield self.parse_movie_item(response)



# conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
# conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
# conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
# conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
# conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
# conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/

# conda config --set show_channel_urls yes