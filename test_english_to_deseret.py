from unittest import TestCase
from english_to_deseret import EnglishToDeseret

class TestEnglishToDeseret(TestCase):

    def setUp(self):
        self.deseret = EnglishToDeseret()

    def test_translate(self):

        deseret_word = self.deseret.translate('hello')
        self.assertEquals(deseret_word, u'\U00010410\U00010407\U00010422\U00010404')

        deseret_word = self.deseret.translate('world')
        self.assertEquals(deseret_word, u'\U0001040e\U0001040a\U00010421\U00010422\U00010414')

        deseret_word = self.deseret.translate('hello world')
        self.assertEquals(deseret_word, u'\U00010410\U00010407\U00010422\U00010404 \U0001040e\U0001040a\U00010421\U00010422\U00010414')

        deseret_word = self.deseret.translate('hello, world')
        self.assertEquals(deseret_word, u'\U00010410\U00010407\U00010422\U00010404, \U0001040e\U0001040a\U00010421\U00010422\U00010414')

    def test_translate_word(self):

        deseret_word = self.deseret.translate('jellies')
        print deseret_word
        self.assertEquals(deseret_word, u'\U00010416\U00010407\U00010422\U00010400\U0001041e')

        print deseret_word
        deseret_word = self.deseret.translate('horse')
        self.assertEquals(deseret_word, u'\U00010410\U00010403\U00010421\U0001041d')

        deseret_word = self.deseret.translate('horses')
        self.assertEquals(deseret_word, u'\U00010410\U00010403\U00010421\U0001041d\U0001041e')

        deseret_word = self.deseret.translate('buys')
        self.assertEquals(deseret_word, u'\U00010412\U0001040c\U0001041e')

        deseret_word = self.deseret.translate('candies')
        self.assertEquals(deseret_word, u'\U00010417\U00010408\U00010424\U00010414\U00010400\U0001041e')

        deseret_word = self.deseret.translate('buses')
        self.assertEquals(deseret_word,  u'\U00010412\U0001040a\U0001041d\U0001040a\U0001041e')

        deseret_word = self.deseret.translate('biking')
        self.assertEquals(deseret_word, u'\U00010412\U0001040c\U00010417\U00010400\U00010425')

        deseret_word = self.deseret.translate('digging')
        self.assertEquals(deseret_word, u'\U00010414\U00010406\U00010418\U00010400\U00010425')

        deseret_word = self.deseret.translate('runs')
        self.assertEquals(deseret_word, u'\U00010421\U0001040a\U00010424\U0001041e')

        deseret_word = self.deseret.translate('seeing')
        self.assertEquals(deseret_word, u'\U0001041d\U00010400\U00010400\U00010425')

        deseret_word = self.deseret.translate('Deseret')
        self.assertEquals(deseret_word, u'\U00010414\U00010407\U0001041d\U00010400\U00010421\U00010407\U00010413')

    def test_get_ipa_word(self):

        ipa_word = self.deseret.get_ipa_word('hello')
        self.assertEquals(ipa_word, "h/E/'l/oU/")

    def test_get_deseret_word(self):

        ipa_word = self.deseret.get_ipa_word('hello')
        deseret_word = self.deseret.get_deseret_word(ipa_word)
        self.assertEquals(deseret_word,  u'\U00010410\U00010407\U00010422\U00010404')

    def test_check_plural(self):
        # self.fail()
        self.failUnless(True);