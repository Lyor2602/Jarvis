import time
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import pyaudio
from playsound import playsound
import winsound
from weather import Weather, Unit
import subprocess
from datetime import datetime
from datetime import date
import datetime
import requests
from bs4 import BeautifulSoup




def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('audio.mp3')


#listens for commands
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ready...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("you said: " + command)

        #loop back to continue listening

    except sr.UnknownValueError:
        print("I didn't quite catch that")
        command = myCommand()

    return command

    #if statements
def assistant(command):

    x = 'sir'

    if 'I\'m home' in command:
        talkToMe('Welcome back ' + str(x) + ', what can I do')

    elif 'you there' in command:
        talkToMe('Yes ' + str(x) + ', at your service')

    elif 'sir' in command:
        talkToMe('what should I call you then?')
        x = myCommand()
        talkToMe('okay ' + str(x))

    elif 'let\'s work' in command:
        winsound.PlaySound('BIB', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    elif 'play music' in command:
        talkToMe('what song would you like')
        song = myCommand()
        if 'Black' in song:
            winsound.PlaySound('BIB', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        elif 'sunflower' in song:
            winsound.PlaySound('Sun', winsound.SND_FILENAME | winsound.SND_ASYNC| winsound.SND_LOOP)
        elif 'body' in song:
            winsound.PlaySound('Body', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        elif 'Love' in song:
            winsound.PlaySound('Love', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    elif 'stop' in command:
        winsound.PlaySound(None, winsound.SND_ASYNC)

    elif 'Netflix' in command:
        talkToMe('What show would you like to see?')
        show = myCommand()
        url = 'https://www.netflix.com/search?q=' + show
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        assistant(myCommand())

    elif 'close all' in command:
        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)

    elif 'lights' in command:
        talkToMe('what would you like me to do with the lights?')
        light = myCommand()
        talkToMe('Sorry, the lights are not set up just yet')

    elif 'Spotify' in command:
        url = 'https://open.spotify.com/browse/featured'
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif 'set the mood' in command:
        winsound.PlaySound('LGIO', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    elif 'schedule' in command:
        schedule = []
        if not schedule:
            talkToMe("your schedule is empty")
            time.sleep(2)
            talkToMe('would you like me to add something')
            option = myCommand()
            if 'yes' in option:
                talkToMe('what should I add')
                note = myCommand()
                schedule.append(note)
        if schedule:
            talkToMe('Coming up you have, ' + str(schedule))
            time.sleep(3)
            talkToMe('Would you like me to add something?')
            schedule = myCommand()
            if 'add' in schedule:
                talkToMe('what should I add')
                note = myCommand()
                schedule.append(note)
                talkToMe('Noted')

    elif 'leave us alone' in command:
        talkToMe('are you sure')
        option = myCommand()
        if 'yes' in option:
            os.system("shutdown.exe /h")

    elif 'we did it' in command:
        winsound.PlaySound('Pull', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    elif 'what should I do' in command:
        talkToMe('you tell me')

    elif 'good morning' in command:
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        talkToMe('Goodmorning daddy')
        time.sleep(1)
        talkToMe('It is ' + str(dt_string))
        time.sleep(7)
        if date.today().weekday() < 5:
            talkToMe('Holiday bitches')
        elif date.today().weekday() > 5:
            talkToMe('enjoy your weekend')



    elif 'news' in command:
        result = requests.get("https://www.bbc.com/news/world")
        src = result.content
        y = BeautifulSoup(src, 'lxml')

        c = y.find("h3").findAll(text=True, recursive=False)

        for i in c:
            talkToMe("today\'s top story is, " + str(i))

    elif 'time' in command:
        now = datetime.datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        talkToMe('the time is, ' + str(dt_string))

    elif 'thank you' in command:
        talkToMe('No problem ' + str(x))



    elif 'open Reddit' in command:
        url = 'https://www.reddit.com'
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif 'search' in command:
        talkToMe('What should I search for')
        link = myCommand()
        url = 'https://www.google.com/search?q=' + link
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)


    elif 'what\'s up' in command:
        talkToMe('Chillin bro')

    elif 'email' in command:
        talkToMe('who is the recipient')
        recipient = myCommand()

        if 'john' in recipient:
            talkToMe("what should i say")
            content = myCommand()

            mail = smptlib.SMTP('smtp.gmail.com', 587)

            mail.ehlo()

            mail.starttls()

            mail.login('109771@st-maartenscollege.nl', '')

            mail.sendmail('PERSON NAME', 'EMAILaddress@email.com', content)

            mail.close()

            talkToMe('Email sent')

    elif 'exit' in command:
            exit()
    else:
        print("what do you mean with " + command)

while True:
    stop = False
    while stop == False:
        rn = str(datetime.datetime.now().time())
        if rn > "09:30:00.000000" and rn < "09:30:30.000000":
            stop = True
            winsound.PlaySound('Morning', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            time.sleep(25)
        elif rn > "09:30:30.000000" and rn < "23:30:00.000000":
            stop = True
            assistant(myCommand())
