from translate import Translator


class SentenceIsNotWithinLimitsException(Exception):
    pass


class Translate:
    def __init__(self, dest_language, sentence):
        self.dest_language = dest_language
        self.sentence = sentence

    @staticmethod
    def sentence_length_is_within_limits(sentence) -> bool:
        if len(sentence) > 100:
            return False
        else:
            return True

    @property
    def translate_sentence(self):
        translation_setup = Translator(to_lang=self.dest_language)

        if self.sentence_length_is_within_limits(self.sentence):
            translation = translation_setup.translate(self.sentence)
        else:
            SentenceIsNotWithinLimitsException("Your sentence is over 100 words characters long, please provide a "
                                               "shorter sentence")

        return translation
