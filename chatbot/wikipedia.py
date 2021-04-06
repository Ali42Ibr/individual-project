import wikipedia
import nltk
class WikiPedia():



    def getDefinition(self, sentence):

        tries = 0
        x = nltk.word_tokenize(sentence)
        w=0

        while tries < 4: #since wikipedia has many different idintefiers for webpages, this while loop tries different forms of the sentence to get an accurate match
            try:
                if(tries == 0):
                    return(wikipedia.summary(sentence + "(mood)",sentences = 1)) #attempts to put the word "mood" in the sentence to avoid other sorts of non related words
                    break   #also prints the summary of the found webpage, first 3 sentences only as it will be too big otherwise.
                elif(tries == 1):
                    return(wikipedia.summary(x[len(x)-1],sentences = 1)) #attemtps to only use the last word in the sentence
                    break
                elif (tries == 2): #attempts to use the first word in the sentence
                    return(wikipedia.summary(x[0],sentences = 1))
                    break
                elif (tries == 3): #uses wikipedias suggest to get another similar word and then searches in wikipedia
                    w = wikipedia.suggest(sentence)
                    return(summary(w,sentences = 1))
                    break
                tries = tries + 1
            except: #since an error is produced if there are too many results found, exception must be used
                 tries = tries + 1

        if tries == 4: #returns false if no information was found
            return False
