from googletrans import Translator
from chatbot.spellcheck import SpellCheck

class translate():

    sc = SpellCheck()
    translator = Translator()
    language = "en"

    def transToEn(self, sentence):

        if self.language == "en":
            return sentence
        else:
            return self.translator.translate(sentence,dest = "en", src=self.language)

    def googleTrans(self, sentence):

        if self.language == "en":
            return sentence
        else:
            translation = self.translator.translate(sentence,dest = self.language, src=self.language)
            return(translation.text)

    def setLanguage(self, language):

        if language.lower() == "dutch":
            self.language = "nl"
            return "Language changed: Dutch"
        elif language.lower() == "arabic":
            self.language = "ar"
            return "Language changed: Arabic"
        elif language.lower() == "spanish":
            self.language = "es"
            return "Language changed: Spanish"
        elif language.lower() == "korean":
            self.language = "ko"
            return "Language changed: Korean"
        elif language.lower() == "english":
            self.language = "en"
            return "Language changed: English"
        else:
            return("Please enter a valid language: Korean, Arabic, Spanish, Dutch, English")
