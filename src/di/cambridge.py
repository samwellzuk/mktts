# -*-coding: utf-8 -*-
# Created by samwell


class CambridgeUK(object):
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
    def tts_language(self):
        return 'en-uk'

    @property
    def home(self):
        return 'https://dictionary.cambridge.org/dictionary/'

    def check_url(self, url):
        """
        :param url: QUrl
        :return: bool
        """
        return True

    def parse_url(self, url):
        pass

    def parse_html(self, usrl, html):
        return


class CambridgeUS(object):
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
    def tts_language(self):
        return 'en-us'

    @property
    def home(self):
        return 'https://dictionary.cambridge.org/dictionary/'

    def check_url(self, url):
        """
        :param url: QUrl
        :return: bool
        """
        return True

    def parse_url(self, url):
        pass

    def parse_html(self, usrl, html):
        return
