import pyttsx3
import speech_recognition as sr
from datetime import date
import webbrowser
import datetime
from pynput.keyboard import Key, Controller
import pyautogui
import os
from os import listdir
from os.path import isfile, join
import smtplib
import wikipedia
import Gesture_Controller
from threading import Thread


# -------------Object Initialization---------------
today = date.today()
r = sr.Recognizer()
keyboard = Controller()

engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


# ----------------Variables------------------------
file_exp_status = False
path = ''
files =[]
is_awake = True             #Bot status

# ------------------Functions----------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  

    print("I am Proton Sir and now fully awake! Please tell me how may I help you")
    speak("I am Proton Sir and now fully awake! Please tell me how may I help you")


with sr.Microphone() as source:             #setting microphone parameters
        #r.adjust_for_ambient_noise(source)
        r.energy_threshold = 500            #threshold on amplitude of audio signals to pick
        r.dynamic_energy_threshold = False  #disabling auto tuning of energy threshold


def record_audio(): #to recognize, returns string
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)

        try:
            #print('Starting Audio Recognition')
            voice_data = r.recognize_google(audio)
            #print('Recognising')
        except sr.RequestError:
            print('Sorry my Service is down... Plz try later')
        except sr.UnknownValueError:
            print("Couldn't Recognize that... Does that even make sense ")
        #print(voice_data)

        return voice_data.lower()


def respond(voice_data):    #to executes commands, string containing command as input 
    global path, file_exp_status, files, is_awake
    print(voice_data)
    voice_data.replace('proton','')
    #print(voice_data)

    if is_awake==False:
        if 'wake up' in voice_data in voice_data:
            is_awake = True
            wish()

    # STATIC CONTROLS
    elif 'hello' in voice_data:
        wish()

    elif 'what is your name' in voice_data:
        print('My name is Proton!')
        speak('My name is Proton!')

    elif 'date' in voice_data:
        print(today.strftime("%B %d, %Y"))
        speak(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        print(str(datetime.datetime.now()).split(" ")[1].split('.')[0])
        speak(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

    elif 'search' in voice_data:
        speak('Searching for ' + voice_data.split('search')[1])
        url = 'https://google.com/search?q=' + voice_data.split('search')[1]
        try:
            webbrowser.get().open(url)
            speak('This is what I found Sir')
        except:
            speak('Please check your Internet')

    elif 'location' in voice_data:
        location_status = True
        if location_status == True:
            print('Which place are you looking for ?')
            speak('Which place are you looking for ?')
            temp_audio = record_audio()
            speak('Locating...')
            url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
            try:
                webbrowser.get().open(url)
                speak('This is what I found Sir')
            except:
                speak('Please check your Internet')

    elif ('bye' in voice_data) or ('by' in voice_data):
        print(voice_data)
        print("Good bye Sir! Have a nice day.")
        speak("Good bye Sir! Have a nice day.")
        is_awake = False
        
    # DYNAMIC CONTROLS
    elif 'launch gesture recognition' in voice_data:
        gc = Gesture_Controller.Gest_Ctrl()
        Gesture_Controller.Gest_Ctrl.gc_mode = 1
        t = Thread(target = gc.start)
        t.start()

    elif 'stop gesture recognition' in voice_data:
        if Gesture_Controller.Gest_Ctrl.gc_mode:
            Gesture_Controller.Gest_Ctrl.gc_mode = 0
        else: print('Gesture recognition is already inactive')
        
    elif 'copy' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        speak('Copied')
          
    elif 'page' in voice_data or 'pest'  in voice_data or 'paste' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        speak('Pasted')

    # File Navigation Start
    elif 'list' in voice_data:
        counter = 0
        path = 'C://'
        files = listdir(path)
        for f in files:
            counter+=1
            print(str(counter) + ':  ' + f)
        file_exp_status = True
        speak('These are the files in your root directory')
        
    elif file_exp_status == True:
        counter = 0   
        if 'open' in voice_data:
            if isfile(join(path,files[int(voice_data.split(' ')[-1])-1])):
                os.startfile(path + files[int(voice_data.split(' ')[-1])-1])
                file_exp_status = False
            else:
                try:
                    path = path + files[int(voice_data.split(' ')[-1])-1] + '//'
                    files = listdir(path)
                    for f in files:
                        counter+=1
                        print(str(counter) + ':  ' + f)
                    speak('Opened Successfully')
                    
                except:
                    print('You do not have permission to access this folder')
                    speak('You do not have permission to access this folder')
                                    
        if 'back' in voice_data:
            if path == 'C://':
                print('Sorry, this is the root directory')
                speak('Sorry, this is the root directory')
            else:
                a = path.split('//')[:-2]
                path = '//'.join(a)
                path += '//'
                files = listdir(path)
                for f in files:
                    counter+=1
                    print(str(counter) + ':  ' + f)
                speak('ok')
                   
    else: 
        print('I am not functioned to do this !')

# ------------------Driver Code--------------------
wish()
while True:
    voice_data = record_audio()
    if 'proton' in voice_data:
        #voice_data=voice_data[voice_data.find('proton'):]
        respond(voice_data)