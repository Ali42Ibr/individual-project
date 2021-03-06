from chatbot.chatbot import ChatBot
from chatbot.spellcheck import SpellCheck
from chatbot.translate import translate
import PySimpleGUI as sg
import sys
import subprocess

# Define the window's contents
sg.theme('Dark2')
layout = [[sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(80,10))],
          [sg.Text('Your Input')],
          [sg.InputText(key='i', size=(40, 2))],
          [sg.Button('SUBMIT', bind_return_key=True), sg.Button('EXIT')]]

def __main__():

    # Create the window
    window = sg.Window('Calm Bot', layout, default_element_size=(50, 3),finalize=True)
    cb = ChatBot()
    ta = translate()
    sc = SpellCheck()
    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!")
    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: What language do your prefer we speak in? To change this language at any time please type: Change language")
    cb.extractQuotes('posQuotes.txt') #we establish the posQuotes in the object
    cb.extractQuotes('negQuotes.txt') #we establish the negQuotes in the object
    exitWords = ['bye', 'quit', 'exit', 'see ya', 'good bye'] #Exit the chat bot with common salutations

    exitError = sc.errorHandlingArray(exitWords) # correcting for errors
    try:
        while(True):    #run a loop to keep prompting the user for input
            event, values = window.read()
            print("You: "+ values['i'])
            languageInput = (values['i']) #userInput in any language
            userInput = ta.transToEn(languageInput) #converting to english to use in chatbot properly

            window.FindElement('i').Update('')
            window['-ML1-' + sg.WRITE_ONLY_KEY].print("You: "+languageInput, end='\n')
            if event == sg.WIN_CLOSED or event == 'EXIT':
                break
            if sc.errorHandlingArray(userInput.lower()) in exitError: #allows for words like "exiting" or "exited" to work, as well as many other cases
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: " + ta.googleTrans("It was really nice talking to you!"), end='\n')
                print("Calm Bot: " + ta.googleTrans("It was really nice talking to you!"))
                break
            elif sc.errorHandlingArray(userInput.lower()) == sc.errorHandlingArray("change language"): #changes language if user asks
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: " + ta.googleTrans("What language do you want? Choose from English, Dutch, Spanish, Arabic, and Korean"))
                event, values = window.read()
                print(ta.googleTrans("You: ") + values['i'])
                languageInput = (values['i']) #userInput in any language
                userInput = ta.transToEn(languageInput) #converting to english to use in chatbot properly
                window.FindElement('i').Update('')
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("You: "+ ta.googleTrans(userInput), end='\n')
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm bot: " + ta.googleTrans(ta.setLanguage(userInput.lower())))


            else:
                if cb.helloMessage(userInput) != None:  #if hello returns nothing, output a quote
                    out=("Calm Bot: " + ta.googleTrans(cb.helloMessage(userInput)))
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print(out, end='\n')
                else:
                    out = ("Calm Bot: " + ta.googleTrans(cb.botResponse(userInput)))
                    print(out)
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print(out, end='\n')
                    # See if user wants to quit or window was closed
                    if event == sg.WINDOW_CLOSED or event == 'EXIT':
                        break
    except Exception as e:
        print(e)
        window.close()
        sys.exit()
    window.close()
    sys.exit()

__main__()
