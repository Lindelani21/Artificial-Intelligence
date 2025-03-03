import speech_recognition as sr
import pyttsx3
import os 
import openai
from dotenv import load_dotenv


load_dotenv()
AI_KEY = os.getenv('AI_KEY')
openai.api_key = AI_KEY

def SpeechToText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

speech = sr.Recognizer()

def RecordText():
    while(1):
        try:
            with sr.Microphone() as source:

                speech.adjust_for_ambient_noise(source, duration=0.2)
                print("I'm listening")
                audio = speech.listen(source)
                myText = speech.recognize_amazon

                return myText
      
        except sr.RequestError as ex:
            print("Could not request results; {0}".format(ex))
        except sr.UnknownValueError:
            print("Unknown error occured")

def sendToAi(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
        
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = []
while(1):
    text = RecordText()
    messages.append({"role": "user", "content": text})
    response = sendToAi(messages)
    SpeechToText(response)
    print("response")


