import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS


GOOGLE_API_KEY = "AIzaSyBASVDhRfM4-uIik19j9ISEavzdZGd3q6g"
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

def voice_input():
    """this function will take voice as input and returns text
    """
    #Speech recognition object
    r = sr.Recognizer() 
    #Access microphone
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source, timeout = 5)

        try:
            print("Recognizing....")
            text = r.recognize_google(audio, language = 'en-in')
            print(f"You said: {text}\n")

            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def text_to_speech(text):
    #Create a gTTS object
    tts = gTTS(text=text, lang="en")

    #Saving audio as mp3
    tts.save("speech.mp3")

def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_text)
    result = response.text

    return result