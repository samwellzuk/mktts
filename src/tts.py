# -*-coding: utf-8 -*-
# Created by samwell
from gtts import lang

tts_languages = sorted(lang.tts_langs().items(), key=lambda d: d[1])

