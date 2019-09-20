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

    elif 'Amy' in command:
        talkToMe('What\'s the matter sir?')
        matter = myCommand()
        if 'tired' in matter:
            talkToMe('Would you like me to set an alarm')
            o1 = myCommand()
            if 'yes' in o1:
                talkToMe()
            if 'no' in o1:
                talkToMe('Owh, what else can I do')
        elif 'sad' in matter:
            talkToMe('I can open up a playlist so you can zone out')
            o2 = myCommand()
            if 'yes' in o2:
                url = 'https://open.spotify.com/playlist/3fXi8ZOs5jiVP4E8VeaOIe'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
        elif 'happy' in matter:
            talkToMe('I\'m glad to hear that, if you need me I will be here')
        elif 'you help' in matter:
            talkToMe('In what way could I help?')
            o3 = myCommand()
        elif 'don\'t know' in matter:
            talkToMe()

    elif 'you there' in command:
        talkToMe('Yes ' + str(x) + ', at your service')

    elif 'set alarm' in command:
        talkToMe('For when should the alarm be set')
        alarm = myCommand()

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
        talkToMe('Would you like to open a genre, choose from your presets or just open spotify?')
        time.sleep(3)
        open = myCommand().strip
        if 'genre' in open:
            talkToMe('what genre?')
            genre = myCommand()
            url = 'https://open.spotify.com/view/' + genre + '-page'
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
        elif 'Presets' in open:
            talkToMe('which playlist would you like?')
            playlist = myCommand()
            if 'random' in playlist:
                url = 'https://open.spotify.com/playlist/2jXdNcw5VtwEzR2eTsOg7M'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
            elif 'calm' in playlist:
                url = 'https://open.spotify.com/playlist/3fXi8ZOs5jiVP4E8VeaOIe'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
            elif 'dance' in playlist:
                url = 'https://open.spotify.com/playlist/0X3Lki36sx0W1TksjA14Tx'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
            elif 'workout' in playlist:
                url = 'https://open.spotify.com/playlist/37i9dQZF1DX76t638V6CA8'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
            elif 'rap' in playlist:
                url = 'https://open.spotify.com/playlist/4ISsZf8PzRtNgf6LQpby5q'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)


        elif 'just' in open:
            url = 'https://open.spotify.com/browse/featured'
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)


    elif 'set the mood' in command:
        winsound.PlaySound('LGIO', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    elif 'intruder' in command:
        talkToMe('Who is in my swamp?')
        time.sleep(2)
        winsound.PlaySound('shrek', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

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
            talkToMe('It is a school day today')
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

webbrowser.open('jarvis.html')
talkToMe('Hello sir, My name is Amy, if you need something, just let me know.')
time.sleep(3)

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
