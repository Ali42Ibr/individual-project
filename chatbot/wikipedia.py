import wikipedia

class WikiPedia():



    def getDefinition(self, sentence):

        sentence = "What is depression"
        tries = 0
        x = nltk.word_tokenize(sentence)
        w=0

        w = wikipedia.page(sentence + "(mood)")

        while tries < 4:
            try:
                if(tries == 0):
                    w = wikipedia.page(sentence + "(mood)")
                    print(1)
                    print(w.summary)
                    continue
                elif(tries == 1):
                    w = wikipedia.page(x[len(x)-1])
                    print(w.summary)
                    print(2)
                    break
                elif (tries == 2):
                    w = wikipedia.page(x[0])
                    print(3)
                    print(w.summary)
                    break
                elif (tries == 3):
                    w = wikipedia.suggest(sentence)
                    print(4)
                    print(w.summary)
                    break

                tries = tries+1
            except Exception as e:
                 tries = tries + 1
