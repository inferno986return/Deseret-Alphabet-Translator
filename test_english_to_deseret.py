# coding: utf-8
from unittest import TestCase
from english_to_deseret import EnglishToDeseret


class TestEnglishToDeseret(TestCase):

    def setUp(self):
        self.english = EnglishToDeseret()

    def test_translate(self):

        english_word = self.english.translate(u'𐐐𐐇𐐢𐐄')
        self.assertEquals(english_word, 'hello')

        english_word = self.english.translate('world')
        self.assertEquals(english_word, u'\u6657\u66570;&#66593;&#66594;&#66580;')

        english_word = self.english.translate('hello world')
        self.assertEquals(english_word, u'&#66576;&#66567;&#66594;&#66564; &#66574;&#66570;&#66593;&#66594;&#66580;')

        english_word = self.english.translate('hello, world')
        self.assertEquals(english_word, u'&#66576;&#66567;&#66594;&#66564;, &#66574;&#66570;&#66593;&#66594;&#66580;')

    def test_translate_word(self):

        english_word = self.english.translate('jellies')
        self.assertEquals(english_word, u'&#66582;&#66567;&#66594;&#66560;&#66590;')

        english_word = self.english.translate('horse')
        self.assertEquals(english_word, u'&#66576;&#66563;&#66593;&#66589;')

        english_word = self.english.translate('horses')
        self.assertEquals(english_word, u'&#66580;&#66565;&#66586;&#66593;&#66570;&#66590;')

        english_word = self.english.translate('buys')
        self.assertEquals(english_word, u'&#66578;&#66572;&#66590;')

        english_word = self.english.translate('candies')
        self.assertEquals(english_word, u'&#66583;&#66568;&#66596;&#66580;&#66560;&#66590;')

        english_word = self.english.translate('buses')
        self.assertEquals(english_word,  u'&#66578;&#66570;&#66589;&#66570;&#66590;')

        english_word = self.english.translate('biking')
        self.assertEquals(english_word, u'&#66578;&#66572;&#66583;&#66560;&#66597;')

        english_word = self.english.translate('digging')
        self.assertEquals(english_word, u'&#66580;&#66566;&#66584;&#66560;&#66597;')

        english_word = self.english.translate('runs')
        self.assertEquals(english_word, u'&#66593;&#66570;&#66596;&#66590;')

        english_word = self.english.translate('seeing')
        self.assertEquals(english_word, u'&#66589;&#66560;&#66560;&#66597;')

        english_word = self.english.translate('Deseret')
        self.assertEquals(english_word, u'&#66580;&#66567;&#66590;&#66570;&#66593;&#66567;&#66579;')

    def test_get_ipa_word(self):

        ipa_word = self.english.get_ipa_word(u'𐐐𐐇𐐢𐐄')
        self.assertEquals(ipa_word, "hEloU")

    def test_get_english_word(self):

        ipa_word = self.english.get_ipa_word('hello')
        english_word = self.english.get_english_word(ipa_word)
        self.assertEquals(english_word, u'&#66576;&#66567;&#66564;')

    def test_check_plural(self):
        self.fail()