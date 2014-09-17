from unittest import TestCase
from deseret import Deseret

class TestDeseret(TestCase):

    def setUp(self):
        self.deseret = Deseret()

    def test_translate(self):

        deseret_word = self.deseret.translate('hello')
        self.assertEquals(deseret_word,  u'&#66576;&#66567;&#66594;&#66564;')

        deseret_word = self.deseret.translate('world')
        self.assertEquals(deseret_word, u'&#66574;&#66570;&#66593;&#66594;&#66580;')

        deseret_word = self.deseret.translate('hello world')
        self.assertEquals(deseret_word, u'&#66576;&#66567;&#66594;&#66564; &#66574;&#66570;&#66593;&#66594;&#66580;')

        deseret_word = self.deseret.translate('hello, world')
        self.assertEquals(deseret_word, u'&#66576;&#66567;&#66594;&#66564;, &#66574;&#66570;&#66593;&#66594;&#66580;')

    def test_translate_word(self):

        deseret_word = self.deseret.translate('jellies')
        self.assertEquals(deseret_word, u'&#66582;&#66567;&#66594;&#66560;&#66590;')

        deseret_word = self.deseret.translate('horse')
        self.assertEquals(deseret_word, u'&#66576;&#66563;&#66593;&#66589;')

        deseret_word = self.deseret.translate('horses')
        self.assertEquals(deseret_word, u'&#66580;&#66565;&#66586;&#66593;&#66570;&#66590;')

        deseret_word = self.deseret.translate('buys')
        self.assertEquals(deseret_word, u'&#66578;&#66572;&#66590;')

        deseret_word = self.deseret.translate('candies')
        self.assertEquals(deseret_word, u'&#66583;&#66568;&#66596;&#66580;&#66560;&#66590;')

        deseret_word = self.deseret.translate('buses')
        self.assertEquals(deseret_word,  u'&#66578;&#66570;&#66589;&#66570;&#66590;')

        deseret_word = self.deseret.translate('biking')
        self.assertEquals(deseret_word, u'&#66578;&#66572;&#66583;&#66560;&#66597;')

        deseret_word = self.deseret.translate('digging')
        self.assertEquals(deseret_word, u'&#66580;&#66566;&#66584;&#66560;&#66597;')

        deseret_word = self.deseret.translate('runs')
        self.assertEquals(deseret_word, u'&#66593;&#66570;&#66596;&#66590;')

        deseret_word = self.deseret.translate('seeing')
        self.assertEquals(deseret_word, u'&#66589;&#66560;&#66560;&#66597;')

        deseret_word = self.deseret.translate('Deseret')
        self.assertEquals(deseret_word, u'&#66580;&#66567;&#66590;&#66570;&#66593;&#66567;&#66579;')

    def test_get_ipa_word(self):

        ipa_word = self.deseret.get_ipa_word('hello')
        self.assertEquals(ipa_word, "h/E/'l/oU/")

    def test_get_deseret_word(self):

        ipa_word = self.deseret.get_ipa_word('hello')
        deseret_word = self.deseret.get_deseret_word(ipa_word)
        self.assertEquals(deseret_word, u'&#66576;&#66567;&#66564;')

    def test_check_plural(self):
        self.fail()