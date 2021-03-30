from googletrans import Translator


class translate():


    translator = Translator()
    language = "en"

    def transToEn(self, sentence): #translates from any language to english, but only if language being typed is the one set in setLanguage

        translation = self.translator.translate(sentence,dest = "en", src = self.language)
        return (translation.text)

    def googleTrans(self, sentence): #translates from english to the set language

        translation = self.translator.translate(sentence,dest = self.language)
        return(translation.text)

    def setLanguage(self, language): #sets the language

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
