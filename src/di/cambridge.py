# -*-coding: utf-8 -*-
# Created by samwell


class Cambridge(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'Cambridge Dictionary'

    @property
    def home(self):
        return 'https://dictionary.cambridge.org/dictionary/'

    def check_url(self, url):
        """
        :param url: QUrl
        :return: bool
        """
        return True

    def parse_html(self, usrl, html):
        return


# -*-coding: utf-8 -*-
# Created by samwell


class Cambridge(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'cambridge'

    @property
    def displayname(self):
        return 'Cambridge Dictionary'

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
