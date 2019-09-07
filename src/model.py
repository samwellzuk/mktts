# -*-coding: utf-8 -*-
# Created by samwell


class Word(object):
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else ''
        self.title_text = kwargs['title_text'] if 'title_text' in kwargs else ''
        self.title_voices = kwargs['title_voices'] if 'title_voices' in kwargs and kwargs['title_voices'] else []
        self.content_text = kwargs['content_text'] if 'content_text' in kwargs else ''
        self.content_voices = kwargs['content_voices'] if 'content_voices' in kwargs and kwargs['content_voices'] else []


class QueryWords(object):
    def __init__(self, **kwargs):
        self.data_path = kwargs['data_path'] if 'data_path' in kwargs else ''
        self.tts_lang = kwargs['tts_lang'] if 'tts_lang' in kwargs else ''
        self.query_word = kwargs['query_word'] if 'query_word' in kwargs else ''
        self.words = [Word(**wobj) for wobj in kwargs['words']] if 'words' in kwargs and kwargs['words'] else []
