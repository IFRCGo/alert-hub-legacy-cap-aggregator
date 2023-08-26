# Generated by Django 4.2.3 on 2023-08-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_feed', '0011_alter_alertinfoarea_altitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageinfo',
            name='language',
            field=models.CharField(blank=True, choices=[('ab', 'ab - Abkhazian'), ('aa', 'aa - Afar'), ('af', 'af - Afrikaans'), ('ak', 'ak - Akan'), ('sq', 'sq - Albanian'), ('am', 'am - Amharic'), ('ar', 'ar - Arabic'), ('an', 'an - Aragonese'), ('hy', 'hy - Armenian'), ('as', 'as - Assamese'), ('av', 'av - Avaric'), ('ae', 'ae - Avestan'), ('ay', 'ay - Aymara'), ('az', 'az - Azerbaijani'), ('bm', 'bm - Bambara'), ('ba', 'ba - Bashkir'), ('eu', 'eu - Basque'), ('be', 'be - Belarusian'), ('bn', 'bn - Bengali'), ('bh', 'bh - Bihari languages'), ('bi', 'bi - Bislama'), ('bs', 'bs - Bosnian'), ('br', 'br - Breton'), ('bg', 'bg - Bulgarian'), ('my', 'my - Burmese'), ('ca', 'ca - Catalan'), ('ch', 'ch - Chamorro'), ('ce', 'ce - Chechen'), ('zh', 'zh - Chinese'), ('cu', 'cu - Church Slavic'), ('cv', 'cv - Chuvash'), ('kw', 'kw - Cornish'), ('co', 'co - Corsican'), ('cr', 'cr - Cree'), ('hr', 'hr - Croatian'), ('cs', 'cs - Czech'), ('da', 'da - Danish'), ('dv', 'dv - Dhivehi'), ('nl', 'nl - Dutch'), ('dz', 'dz - Dzongkha'), ('en', 'en - English'), ('eo', 'eo - Esperanto'), ('et', 'et - Estonian'), ('ee', 'ee - Ewe'), ('fo', 'fo - Faroese'), ('fj', 'fj - Fijian'), ('fi', 'fi - Finnish'), ('fr', 'fr - French'), ('ff', 'ff - Fulah'), ('gl', 'gl - Galician'), ('lg', 'lg - Ganda'), ('ka', 'ka - Georgian'), ('de', 'de - German'), ('gn', 'gn - Guarani'), ('gu', 'gu - Gujarati'), ('ht', 'ht - Haitian'), ('ha', 'ha - Hausa'), ('he', 'he - Hebrew'), ('hz', 'hz - Herero'), ('hi', 'hi - Hindi'), ('ho', 'ho - Hiri Motu'), ('hu', 'hu - Hungarian'), ('is', 'is - Icelandic'), ('io', 'io - Ido'), ('ig', 'ig - Igbo'), ('id', 'id - Indonesian'), ('ia', 'ia - Interlingua (International Auxiliary Language Association)'), ('ie', 'ie - Interlingue'), ('iu', 'iu - Inuktitut'), ('ik', 'ik - Inupiaq'), ('ga', 'ga - Irish'), ('it', 'it - Italian'), ('ja', 'ja - Japanese'), ('jv', 'jv - Javanese'), ('kl', 'kl - Kalaallisut'), ('kn', 'kn - Kannada'), ('kr', 'kr - Kanuri'), ('ks', 'ks - Kashmiri'), ('kk', 'kk - Kazakh'), ('km', 'km - Khmer'), ('ki', 'ki - Kikuyu'), ('rw', 'rw - Kinyarwanda'), ('ky', 'ky - Kirghiz'), ('kv', 'kv - Komi'), ('kg', 'kg - Kongo'), ('ko', 'ko - Korean'), ('kj', 'kj - Kuanyama'), ('ku', 'ku - Kurdish'), ('lo', 'lo - Lao'), ('la', 'la - Latin'), ('lv', 'lv - Latvian'), ('li', 'li - Limburgan'), ('ln', 'ln - Lingala'), ('lt', 'lt - Lithuanian'), ('lu', 'lu - Luba-Katanga'), ('lb', 'lb - Luxembourgish'), ('mk', 'mk - Macedonian'), ('mg', 'mg - Malagasy'), ('ms', 'ms - Malay (macrolanguage)'), ('ml', 'ml - Malayalam'), ('mt', 'mt - Maltese'), ('gv', 'gv - Manx'), ('mi', 'mi - Maori'), ('mr', 'mr - Marathi'), ('mh', 'mh - Marshallese'), ('el', 'el - Modern Greek (1453-)'), ('mn', 'mn - Mongolian'), ('na', 'na - Nauru'), ('nv', 'nv - Navajo'), ('ng', 'ng - Ndonga'), ('ne', 'ne - Nepali (macrolanguage)'), ('nd', 'nd - North Ndebele'), ('se', 'se - Northern Sami'), ('no', 'no - Norwegian'), ('nb', 'nb - Norwegian Bokmål'), ('nn', 'nn - Norwegian Nynorsk'), ('ny', 'ny - Nyanja'), ('oc', 'oc - Occitan (post 1500)'), ('oj', 'oj - Ojibwa'), ('or', 'or - Oriya (macrolanguage)'), ('om', 'om - Oromo'), ('os', 'os - Ossetian'), ('pi', 'pi - Pali'), ('pa', 'pa - Panjabi'), ('fa', 'fa - Persian'), ('pl', 'pl - Polish'), ('pt', 'pt - Portuguese'), ('ps', 'ps - Pushto'), ('qu', 'qu - Quechua'), ('ro', 'ro - Romanian'), ('rm', 'rm - Romansh'), ('rn', 'rn - Rundi'), ('ru', 'ru - Russian'), ('sm', 'sm - Samoan'), ('sg', 'sg - Sango'), ('sa', 'sa - Sanskrit'), ('sc', 'sc - Sardinian'), ('gd', 'gd - Scottish Gaelic'), ('sr', 'sr - Serbian'), ('sh', 'sh - Serbo-Croatian'), ('sn', 'sn - Shona'), ('ii', 'ii - Sichuan Yi'), ('sd', 'sd - Sindhi'), ('si', 'si - Sinhala'), ('sk', 'sk - Slovak'), ('sl', 'sl - Slovenian'), ('so', 'so - Somali'), ('nr', 'nr - South Ndebele'), ('st', 'st - Southern Sotho'), ('es', 'es - Spanish'), ('su', 'su - Sundanese'), ('sw', 'sw - Swahili (macrolanguage)'), ('ss', 'ss - Swati'), ('sv', 'sv - Swedish'), ('tl', 'tl - Tagalog'), ('ty', 'ty - Tahitian'), ('tg', 'tg - Tajik'), ('ta', 'ta - Tamil'), ('tt', 'tt - Tatar'), ('te', 'te - Telugu'), ('th', 'th - Thai'), ('bo', 'bo - Tibetan'), ('ti', 'ti - Tigrinya'), ('to', 'to - Tonga (Tonga Islands)'), ('ts', 'ts - Tsonga'), ('tn', 'tn - Tswana'), ('tr', 'tr - Turkish'), ('tk', 'tk - Turkmen'), ('tw', 'tw - Twi'), ('ug', 'ug - Uighur'), ('uk', 'uk - Ukrainian'), ('ur', 'ur - Urdu'), ('uz', 'uz - Uzbek'), ('ve', 've - Venda'), ('vi', 'vi - Vietnamese'), ('vo', 'vo - Volapük'), ('wa', 'wa - Walloon'), ('cy', 'cy - Welsh'), ('fy', 'fy - Western Frisian'), ('wo', 'wo - Wolof'), ('xh', 'xh - Xhosa'), ('yi', 'yi - Yiddish'), ('yo', 'yo - Yoruba'), ('za', 'za - Zhuang'), ('zu', 'zu - Zulu')], default='en-US', null=True),
        ),
    ]
