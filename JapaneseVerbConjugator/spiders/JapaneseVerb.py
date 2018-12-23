# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

from JapaneseVerbConjugator.items import JapaneseVerb

class JapaneseverbSpider(CrawlSpider):
    name = 'JapaneseVerb'
    # allowed_domains = ['http://japaneseverbconjugator.com']
    start_urls = [
        'http://www.japaneseverbconjugator.com/JVerbList.asp',
        ]

    rules = (
        Rule(LinkExtractor(allow=('VerbDetails', )), callback='parse_verb'),
    )

    def parse_verb(self, response):
        if re.search('VerbDetails', response.url):
            verb = JapaneseVerb()

            a = response.xpath('//h1/span[@class="JScript"]/text()').extract()
            verb['verb'] = a

            count = 0
            if len(a) == 0:
                count = -1

            table = response.xpath('//table')[0]

            # This is to process first part of table body
            trs = table.xpath('.//tr')

            #PROCESS TRS[0]
            verb['verb_class'] = self.get_process_one(trs[0])

            #PROCESS TRS[1]
            verb['stem'] = self.get_process_one(trs[1])

            #PROCESS TRS[2]
            verb['te_form'] = self.get_process_one(trs[2])

            #PROCESS TRS[3]
            verb['infinitive'] = self.get_process_one(trs[3])

            #Process English
            verb['english'] = self.get_english(trs)

            #Present Indicative
            verb['present_indicative_plain_positive'], verb['present_indicative_plain_negative'] = self.get_process_plain(trs[7+count])
            verb['present_indicative_polite_positive'], verb['present_indicative_polite_negative'] = self.get_process_polite(trs[8+count])

            #Volitional
            a, b = self.get_process_plain(trs[10+count])
            verb['volitional_plain_positive'], verb['volitional_plain_negative'] = self.split_volitional(a+b)
            a, b = self.get_process_polite(trs[11+count])
            verb['volitional_polite_positive'], verb['volitional_polite_negative'] = self.split_volitional(a+b)

            #Imperative
            verb['imperative_plain_positive'], verb['imperative_plain_negative'] = self.get_process_plain(trs[13+count])
            verb['imperative_polite_positive'], verb['imperative_polite_negative'] = self.get_process_polite(trs[14+count])

            #Past Indicative
            verb['past_indicative_plain_positive'], verb['past_indicative_plain_negative'] = self.get_process_plain(trs[15+count])
            verb['past_indicative_polite_positive'], verb['past_indicative_polite_negative'] = self.get_process_polite(trs[16+count])
            
            #Past Presumptive
            a, b = self.get_process_plain(trs[17+count])
            verb['past_presumptive_plain_positive'], verb['past_presumptive_plain_negative'] = self.split_past_presumptive(a+b)
            verb['past_presumptive_polite_positive'], verb['past_presumptive_polite_negative'] = self.get_process_polite(trs[18+count])

            #Present Progressive
            a, b = self.get_process_plain(trs[19+count])
            verb['present_progressive_plain_positive'] = a + b
            verb['present_progressive_polite_positive'], verb['present_progressive_polite_negative'] = self.get_process_polite(trs[20+count])

            #Past Progressive
            a, b = self.get_process_plain(trs[21+count])
            verb['past_progressive_plain_positive'] = a + b
            verb['past_progressive_polite_positive'], verb['past_progressive_polite_negative'] = self.get_process_polite(trs[22+count])

            #Provisional Conditional eba
            verb['provisional_conditional_plain_positive'], verb['provisional_conditional_plain_negative'] = self.get_process_plain(trs[23+count])
            verb['provisional_conditional_polite_positive'], verb['provisional_conditional_polite_negative'] = self.get_process_polite(trs[24+count])

            #Conditional
            verb['conditional_plain_positive'], verb['conditional_plain_negative'] = self.get_process_plain(trs[25+count])
            verb['conditional_polite_positive'], verb['conditional_polite_negative'] = self.get_process_polite(trs[26+count])

            #Potential
            verb['potential_plain_positive'], verb['potential_plain_negative'] = self.get_process_plain(trs[27+count])
            verb['potential_polite_positive'], verb['potential_polite_negative'] = self.get_process_polite(trs[28+count])

            #Causative
            verb['causative_plain_positive'], verb['causative_plain_negative'] = self.get_process_plain(trs[29+count])
            verb['causative_polite_positive'], verb['causative_polite_negative'] = self.get_process_polite(trs[30+count])

            #Passive
            verb['passive_plain_positive'], verb['passive_plain_negative'] = self.get_process_plain(trs[31+count])
            verb['passive_polite_positive'], verb['passive_polite_negative'] = self.get_process_polite(trs[32+count])

            return verb

        else:
            print('Not verb details')
            print(response.url)
            return None
        
    def get_process_one(self, response):
        words = response.xpath('.//td/text() | .//td/span/text()').extract()
        real_verb = []

        for word in words:
            # if re.match('Verb Class', word):
            #     continue
            a = re.sub(r'\r+|\n+|\t+|\s+', ' ', word)
            real_verb.append(a)
            
        return ''.join(real_verb).strip()

    def get_english(self, response):
        words = response.xpath('.//td[@class="Meaning"]/text()')
        return [x.strip() for x in words.extract_first().split(',')]

    def get_process_plain(self, response):
        words = [tr.strip() for tr in response.xpath('.//td/span/text() | .//td/a[@class="JScript"]/text()').extract()]
        temp = []

        for word in words:
            if word == '':
                continue
            temp.append(word)

        A = []
        B = []
        
        # return temp
        if (len(temp) % 2) == 0:
            A, B = self.split_list(temp)
        else:
            A = temp

        return A, B

    def get_process_polite(self, response):
        words = [tr.strip() for tr in response.xpath('.//td/span/text() | .//td/a[@class="JScript"]/text()').extract()]
        temp = []

        for word in words:
            if word == '':
                continue
            temp.append(word)

        A = []
        B = []
        
        # return temp
        if (len(temp) % 2) == 0:
            A, B = self.split_list(temp)
        else:
            A = temp

        return A, B

    def split_list(self, a_list):
        half = len(a_list)//2
        return a_list[:half], a_list[half:]

    def split_volitional(self, a_list):
        one_third = len(a_list)//3
        return a_list[:2*one_third], a_list[2*one_third:]

    def split_past_presumptive(self, a_list):
        if len(a_list) > 4:
            return a_list[:-2], a_list[-2:]
        elif len(a_list) > 2 :
            return a_list[:-1], a_list[-1:]
        else:
            return a_list, []
