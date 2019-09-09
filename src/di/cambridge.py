# -*-coding: utf-8 -*-
# Created by samwell


class Cambridge(object):
    def __init__(self):
        pass

    @property
    def home(self):
        return 'https://dictionary.cambridge.org/dictionary/'

    def check_url(self, url):
        """
        :param url: QUrl
        :return: bool,queryword
        """
        return False, None

    def parse_html(self, dictword, html):
        return


class CambridgeUK(Cambridge):
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
