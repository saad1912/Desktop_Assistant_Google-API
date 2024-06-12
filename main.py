import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


#Taking voice from system

#'sapi5' allows the use of SAPI5-compatible voices installed on your system.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


#print(voices) #returns a list object
#print(voices[0].id) #retutns the ID behind the voice
#print(len(voices)) #Length is two. 0:Male, 1:Female


engine.setProperty('voice', voices[0].id) #Setting Male voice for Desktop Application
engine.setProperty('rate', 150)#Speed percent (defaul is 200 words per minute)


#Speak function
def speak(text):
    '''This function takes text and returns voice

    Args: 
        text (_type_) : string
    '''
    engine.say(text)
    engine.runAndWait()


#Speech recognition function

def takeCommand():
    """this function will take voice as input and returns text
    """
    #Speech recognition object
    r = sr.Recognizer() 
    #Access microphone
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 #Amount of time (in seconds) the recognizer will wait for a pause in speech before considering the end of a phrase.
        audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Please say that again")
            return "None"
        return query
    
print("ok")

            





