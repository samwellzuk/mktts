# -*-coding: utf-8 -*-
# Created by samwell
import gtts
import gtts.lang

"""
af Afrikaans
sq Albanian
ar Arabic
hy Armenian
bn Bengali
bs Bosnian
ca Catalan
zh-cn Chinese (Mandarin/China)
zh-tw Chinese (Mandarin/Taiwan)
hr Croatian
cs Czech
da Danish
nl Dutch
en English
en-au English (Australia)
en-ca English (Canada)
en-gh English (Ghana)
en-in English (India)
en-ie English (Ireland)
en-nz English (New Zealand)
en-ng English (Nigeria)
en-ph English (Philippines)
en-za English (South Africa)
en-tz English (Tanzania)
en-uk English (UK)
en-gb English (UK)
en-us English (US)
eo Esperanto
et Estonian
tl Filipino
fi Finnish
fr French
fr-ca French (Canada)
fr-fr French (France)
de German
el Greek
gu Gujarati
hi Hindi
hu Hungarian
is Icelandic
id Indonesian
it Italian
ja Japanese
jw Javanese
kn Kannada
km Khmer
ko Korean
la Latin
lv Latvian
mk Macedonian
ml Malayalam
mr Marathi
my Myanmar (Burmese)
ne Nepali
no Norwegian
pl Polish
pt Portuguese
pt-br Portuguese (Brazil)
pt-pt Portuguese (Portugal)
ro Romanian
ru Russian
sr Serbian
si Sinhala
sk Slovak
es Spanish
es-es Spanish (Spain)
es-us Spanish (United States)
su Sundanese
sw Swahili
sv Swedish
ta Tamil
te Telugu
th Thai
tr Turkish
uk Ukrainian
ur Urdu
vi Vietnamese
cy Welsh
"""
tts_languages = sorted(gtts.lang.tts_langs().items(), key=lambda d: d[1])


def trans_tts(text, lang, fpath):
    ttsobj = gtts.gTTS(text, lang=lang, lang_check=False)
    ttsobj.save(fpath)
