# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JapaneseverbconjugatorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JapaneseVerb(scrapy.Item):
    verb = scrapy.Field()
    verb_class = scrapy.Field()
    stem = scrapy.Field()
    te_form = scrapy.Field()
    infinitive = scrapy.Field()
    english = scrapy.Field()

    #Present Indicative
    present_indicative_plain_positive = scrapy.Field()
    present_indicative_plain_negative = scrapy.Field()
    present_indicative_polite_positive = scrapy.Field()
    present_indicative_polite_negative = scrapy.Field()

    #Past Indicative
    past_indicative_plain_positive = scrapy.Field()
    past_indicative_plain_negative = scrapy.Field()
    past_indicative_polite_positive = scrapy.Field()
    past_indicative_polite_negative = scrapy.Field()

    #Volitional
    volitional_plain_positive = scrapy.Field()
    volitional_plain_negative = scrapy.Field()
    volitional_polite_positive = scrapy.Field()
    volitional_polite_negative = scrapy.Field()

    #Imperative
    imperative_plain_positive = scrapy.Field()
    imperative_plain_negative = scrapy.Field()
    imperative_polite_positive = scrapy.Field()
    imperative_polite_negative = scrapy.Field()

    #Past Presumptive
    past_presumptive_plain_positive = scrapy.Field()
    past_presumptive_plain_negative = scrapy.Field()
    past_presumptive_polite_positive = scrapy.Field()
    past_presumptive_polite_negative = scrapy.Field()

    #Present Progressive
    present_progressive_plain_positive = scrapy.Field()
    present_progressive_plain_negative = scrapy.Field()
    present_progressive_polite_positive = scrapy.Field()
    present_progressive_polite_negative = scrapy.Field()

    #Past Progressive
    past_progressive_plain_positive = scrapy.Field()
    past_progressive_plain_negative = scrapy.Field()
    past_progressive_polite_positive = scrapy.Field()
    past_progressive_polite_negative = scrapy.Field()

    #Provisional Conditional eba
    provisional_conditional_plain_positive = scrapy.Field()
    provisional_conditional_plain_negative = scrapy.Field()
    provisional_conditional_polite_positive = scrapy.Field()
    provisional_conditional_polite_negative = scrapy.Field()

    #Conditional
    conditional_plain_positive = scrapy.Field()
    conditional_plain_negative = scrapy.Field()
    conditional_polite_positive = scrapy.Field()
    conditional_polite_negative = scrapy.Field()

    #Potential
    potential_plain_positive = scrapy.Field()
    potential_plain_negative = scrapy.Field()
    potential_polite_positive = scrapy.Field()
    potential_polite_negative = scrapy.Field()

    #Causative
    causative_plain_positive = scrapy.Field()
    causative_plain_negative = scrapy.Field()
    causative_polite_positive = scrapy.Field()
    causative_polite_negative = scrapy.Field()

    #Passive
    passive_plain_positive = scrapy.Field()
    passive_plain_negative = scrapy.Field()
    passive_polite_positive = scrapy.Field()
    passive_polite_negative = scrapy.Field()