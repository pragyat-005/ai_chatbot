import os
import openai
import sys
import win32com.client
import speech_recognition as sr
import pyaudio
import webbrowser
from wikipedia import languages
import subprocess
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
import requests
import json
import datetime

speaker=win32com.client.Dispatch("SAPI.SpVoice")
for i, voice in enumerate(speaker.GetVoices()):
    print(f"{i}: {voice.GetDescription()}")


speaker.Voice = speaker.GetVoices().Item(0)

r=sr.Recognizer()
pause_threshold=0.5

def say(text):
    print(text)
    speaker.Speak(f"{text}")



def take():

    with sr.Microphone() as source:
            audio=r.listen(source)
            query=r.recognize_google(audio, language='en-In')
            print(f"you said : {query}")
            return query

if __name__=="__main__":
    say("alex")

while True:

    print("listening...")
    query=take()

      # used to access files through programme
    if "chat".lower() in query.lower():
        chatStr= ""
        def talk(query):
            global chatStr
            print(chatStr)
            openai.api_key = "your api key"
            chatStr += f"User:{query}\n BOT:"
            response =client.chat.completions.create(
                prompt=chatStr,
                model="deepseek/deepseek-chat",
            )


            say(response["choices"][0]["text"])
            chatStr += f"{response['choices'][0]['text']}\n"
            return response["choices"][0]["text"]




    if "hi".lower() in query.lower():
        say("hi, how may i help you?")



    if "hello".lower() in query.lower():
        say("hello, how may i help you?")

    if "thank you".lower() in query.lower():
        say("my pleasure")

    if "thankyou".lower() in query.lower():
        say("my pleasure")

    if "name".lower() in query.lower():
        say("my name is alex")

    if "time" in query:
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        speaker.speak(f" {hour}:{minute}")

    if "Google".lower() in query.lower():  # add more sites
        speaker.speak("Opening google...")
        webbrowser.open("https://www.google.com")

    if "youtube".lower() in query.lower():
        say("Opening youtube...")
        webbrowser.open("https://www.youtube.com")

    if "college website".lower() in query.lower():
        say("opening UIT website...")
        webbrowser.open("https://www.hpuniv.ac.in/university-detail/home.php?uiit")

    if "wikipedia".lower() in query.lower():
        say("Opening wikipedia...")
        webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")


    if "Steven".lower() in query.lower():
        while True:
         print("ASK ANYTHING")
         question = takeCommand()
         client = OpenAI(api_key="your api key",
                         base_url="your base url")

         chat = client.chat.completions.create(
             model="deepseek/deepseek-chat",
             messages=[
                 {
                     "role": "user",
                     "content": f"{question} short "
                 }
             ]
         )

         print(chat.choices[0].message.content)  # only response is printed
         say(chat.choices[0].message.content)

    if "temperature".lower() in query.lower():
        say("what is your city")
        print("listening")
        City = take()

        BASE_URL = "your base url"
        API_KEY = "your api key"
        CITY = (City)


        def kelvin_to_celsius_fahrenheit(kelvin):
            celsius = kelvin - 273.15
            fahrenheit = (9 / 5) * celsius + 32
            return celsius, fahrenheit


        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

        response = requests.get(url).json()

        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        say(f"Temperature in {CITY} is {temp_celsius:.2f}degree celsius")





