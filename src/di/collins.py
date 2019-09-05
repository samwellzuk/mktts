# -*-coding: utf-8 -*-
# Created by samwell


class Collins(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'collins'

    @property
    def displayname(self):
        return 'Collins Dictionary'

    @property
    def home(self):
        return 'https://www.collinsdictionary.com/dictionary/english'

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
