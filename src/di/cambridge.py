# -*-coding: utf-8 -*-
# Created by samwell
from urllib.parse import urljoin

from scrapy import Selector

_dict_ui_path = [
    ('us', 'dictionary', 'english'),
    ('es', 'diccionario', 'ingles'),
    ('es-LA', 'dictionary', 'english'),
    ('fr', 'dictionnaire', 'anglais'),
    ('pl', 'dictionary', 'english'),
    ('pt', 'dicionario', 'ingles'),
    ('ru', 'словарь', 'английский'),
    ('de', 'worterbuch', 'englisch'),
    ('fr', 'dictionnaire', 'anglais'),
    ('it', 'dizionario', 'inglese'),
    ('ko', '사전', '영어'),
    ('tr', 'sözlük', 'ingilizce'),
    ('ja', 'dictionary', 'english'),
    ('vi', 'dictionary', 'english'),
    ('zhs', '词典', '英语'),
    ('zht', '詞典', '英語'),
]


class Cambridge(object):
    @property
    def home(self):
        return 'https://dictionary.cambridge.org/dictionary/'

    def check_url(self, url):
        """
        :param url: QUrl
        :return: bool,queryword
        """
        if url.host() != 'dictionary.cambridge.org':
            return False, None
        sparts = url.path().split('/')
        if (len(sparts) == 4 or len(sparts) == 5) and sparts[0] == '' and not sparts[-1].endswith('.html'):
            if len(sparts) == 4:
                if sparts[1] == 'dictionary' and sparts[2] == 'english':
                    return True, sparts[3]
            else:
                for lantype, dictname, dicttype in _dict_ui_path:
                    if lantype == sparts[1] and dictname == sparts[2] and dicttype == sparts[3]:
                        return True, sparts[4]
        return False, None

    def parse_html(self, dictword, html):
        sel = Selector(text=html)
        ciddict = {}
        cidlist = sel.xpath('//div[@data-id="cald4"]//div[@class="cid"]')
        for cid in cidlist:
            id = cid.xpath('@id').get()
            if id.startswith('cald4-'):
                ciddict[id] = cid.xpath('..')

        if not dilist:
            return False
        for di in dilist:
            dihead = di.xpath('div[contains(@class,"dpos-h")]')
            # 词
            word = dihead.xpath('.//*[contains(@class,"dpos-h_hw")]/span/text()').get()
            # 词性
            pos = ','.join(dihead.xpath('.//span[contains(@class,"dpos")]/text()').getall())
            # 可数性
            gram = ''.join(dihead.xpath('.//span[contains(@class,"dgram")]/descendant-or-self::text()').getall())
            # 发音
            mp3path = dihead.xpath(
                './/span[contains(@class,"%s")]//source[@type="audio/mpeg"]/@src' %
                self.langkey).get()
            # 音标
            pron = ''.join(dihead.xpath(
                './/span[contains(@class,"%s")]//span[contains(@class,"dipa")]/descendant-or-self::text()' %
                self.langkey).getall())

            mp3 = urljoin(self.home, mp3path)

            dihead = di.xpath('div[contains(@class,"dpos-h")]')
        return True


class CambridgeUK(Cambridge):
    def __init__(self):
        self.langkey = 'uk'

    @property
    def name(self):
        return 'cambridge_uk'

    @property
    def displayname(self):
        return "Cambridge Advanced Learner's Dictionary (UK)"

    @property
    def language(self):
        return 'en'

    @property
    def default_ttslang(self):
        return 'en-uk'


class CambridgeUS(Cambridge):
    def __init__(self):
        self.langkey = 'us'

    @property
    def name(self):
        return 'cambridge_us'

    @property
    def displayname(self):
        return "Cambridge Advanced Learner's Dictionary (US)"

    @property
    def language(self):
        return 'en'

    @property
    def default_ttslang(self):
        return 'en-us'
