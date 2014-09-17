import json
import re

class Deseret:

    pron_dict = {}
    ipa_to_deseret = {}

    def __init__(self):

        with open("ipa_to_deseret.json", "r") as json_file:
            self.ipa_to_deseret = json.load(json_file)
            json_file.close()

        print(self.ipa_to_deseret)
        print(self.ipa_to_deseret["@"])

        for pron_filename in ["mobypron.unc", "custompron.unc"]:
            pron_file = open(pron_filename, "r")
            for line in pron_file:
                entry = line.split(" ")
                self.pron_dict[entry[0].lower()] = entry[1].strip()

            pron_file.close()

        print "Finished initializaing Deseret class."

    def translate(self, english):

        translation = ""
        for english_word in re.findall('([^a-zA-z]+|[a-zA-Z]+)', english, re.DOTALL):
            translation += self.translate_word(english_word)

        return translation.strip()

    def translate_word(self, english_word):

        translation = ""

        ipa_word = self.get_ipa_word(english_word)
        if ipa_word:
            translation = self.get_deseret_word(ipa_word)
        else:
            ipa_word = self.try_alternate_endings(english_word)
            if ipa_word:
                translation += self.get_deseret_word(ipa_word)
            else:
                translation += english_word

        return translation

    def try_alternate_endings(self, english_word):
        """Get string of IPA fragments that can be converted into Deseret Alphabet characters"""

        ipa_word = None
        if english_word[-3:] == "ies":
            ipa_word = self.get_ipa_word(english_word[:-3] + "y")       # e.g., "candies"
            if ipa_word:
                ipa_word += "/z"

        if not ipa_word and english_word[-2:] == "es":
            ipa_word = self.get_ipa_word(english_word[:-2])             # e.g., "buses"
            if ipa_word:
                ipa_word += "/@z"
            else:
                ipa_word = self.get_ipa_word(english_word[:-1])         # e.g., "horses"
                if ipa_word:
                    ipa_word += "/z"

        if not ipa_word and english_word[-3:] == "ing":
            ipa_word = self.get_ipa_word(english_word[:-3])             # e.g., "seeing"
            if ipa_word:
                ipa_word += "/iN"
            else:
                ipa_word = self.get_ipa_word(english_word[:-3] + "e")   # e.g., "biking"
                if ipa_word:
                    ipa_word += "/iN"
                else:
                    ipa_word = self.get_ipa_word(english_word[:-4])     # e.g., "digging"
                    if ipa_word:
                        ipa_word += "/iN"

        if not ipa_word and english_word[-1:] == "s":                   # e.g., "runs"
            ipa_word = self.get_ipa_word(english_word[:-1])
            if ipa_word:
                ipa_word += "/z"

        if not ipa_word and english_word[-2:] == "ly":
            ipa_word = self.get_ipa_word(english_word[:-2])
            if ipa_word:
                ipa_word += "/l/i/"

        if not ipa_word and english_word[-2:] == "ed":
            ipa_word = self.get_ipa_word(english_word[:-2])
            if ipa_word:
                ipa_word += "@d"

        if not ipa_word and english_word[-1:] == "d":
            ipa_word = self.get_ipa_word(english_word[:-1])
            if ipa_word:
                ipa_word += "d"

        if not ipa_word and english_word[-2:] == "er":
            ipa_word = self.get_ipa_word(english_word[:-2])
            if ipa_word:
                ipa_word += "@r"

        if not ipa_word and english_word[-1:] == "r":
            ipa_word = self.get_ipa_word(english_word[:-1])
            if ipa_word:
                ipa_word += "r"

        return ipa_word

    def get_ipa_word(self, english_word):

        if not english_word:
            return None
        english_word = re.sub('[\',\\.]', '', english_word)
        return self.pron_dict.get(english_word.lower(), None)

    def get_deseret_word(self, ipa_word):

        deseret_word = ""

        ipa_word = re.sub('[\',]', '', ipa_word)

        ipa_syllables = ipa_word.split('/')

        for ipa_syllable in ipa_syllables:
            ipa_syllable = ipa_syllable.strip()

            if not ipa_syllable:
                continue

            deseret_char = self.ipa_to_deseret.get(ipa_syllable, None)

            if deseret_char:
                deseret_word += "&#%s;" % deseret_char
            else:
                # no match for full syllable; process as a cluster of consonants
                for ipa_char in ipa_syllable:
                    deseret_char = self.ipa_to_deseret.get(ipa_char, None)
                    if deseret_char:
                        deseret_word += "&#%s;" % deseret_char
                    else:
                        print "Unrecognized IPA syllable: %s" % ipa_syllable

        return deseret_word


