import speech_recognition as sr
from time import ctime
from datetime import date
import webbrowser
import time
import datetime
from pynput.keyboard import Key, Controller
import pyautogui
import os
from os import listdir
from os.path import isfile, join

# Object Initialization
today = date.today()
r = sr.Recognizer()
keyboard = Controller()

# Variables
is_awake = False
file_exp_status = False
path = ''
files = []


# Main Code
with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration = 1 )  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.energy_threshold = 400 # to set energy threshold manually
        r.dynamic_energy_threshold = False   # sets energy threshold dynamically
        r.dynamic_energy_adjustment_damping = 0.15 #represents approximately the fraction of the current energy threshold that is retained after one second of dynamic threshold adjustment
        r.dynamic_energy_adjustment_ratio = 1.5
        r.pause_threshold = 0.8

def record_audio(ask = False):
    print('Energy Threshold =',r.energy_threshold)
    with sr.Microphone() as source:
        if ask:
            print(ask)
        voice_data = ''
        
        try:
            print('listening')
            #audio = r.listen(source, timeout = 3, phrase_time_limit = 3)
            audio = r.listen(source, phrase_time_limit= 4)
            print('recognizing')
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            print('Sorry my Service is down... Plz try later') 
        except sr.UnknownValueError:
            print("Couldn't Recognize that... Does that even make sense ")
        except Exception:
            print('timeout')
    return voice_data.lower()

def respond(voice_data):
    global path, file_exp_status, files, is_awake
   
    #INVOKE
    if is_awake==False:
        if 'wake up' in voice_data and 'proton' in voice_data:
            is_awake = True
            print("I am awake, How may I help you?")
    elif 'sleep' in voice_data and 'proton' in voice_data:
        is_awake = False
        print("It was nice talking to you !")
    elif 'proton' in voice_data.lower():
        voice_data=voice_data[voice_data.find('proton'):]
        print('After detecting Proton ',voice_data)
        if 'what is your name' in voice_data:
            print('My name is Proton!')
        elif 'date' in voice_data:
            print(today.strftime("%B %d, %Y"))
        elif 'time' in voice_data:
            print(str(datetime.datetime.now()).split(" ")[1].split('.')[0])
        elif 'search' in voice_data:
            search = record_audio('What do you want to Search ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            print('This is what I found for ' + search)
        elif 'location' in voice_data:
            location = record_audio('Which place are you looking for ?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            
        elif 'copy' in voice_data:
            with keyboard.pressed(Key.ctrl):
                keyboard.press('c')
                keyboard.release('c')
            
        elif 'paste' in voice_data:
            with keyboard.pressed(Key.ctrl):
                keyboard.press('v')
                keyboard.release('v')

        # File Navigation Start
        elif 'list' in voice_data:
            counter = 0
            path = 'C://'
            files = listdir(path)
            for f in files:
                counter+=1
                print(str(counter) + ':  ' + f)
            file_exp_status = True
            
        elif file_exp_status == True:
            counter = 0
            
            if 'open' in voice_data:
                if isfile(join(path,files[int(voice_data.split(' ')[-1])-1])):
                    os.startfile(path + files[int(voice_data.split(' ')[-1])-1])
                    file_exp_status = False
                else:
                    try:
                        files = listdir(path + files[int(voice_data.split(' ')[-1])-1] + '//')
                        path = path + files[int(voice_data.split(' ')[-1])-1] + '//'
                        for f in files:
                            counter+=1
                            print(str(counter) + ':  ' + f)
                    except:
                        print('You donot have permission to open this folder')
                    
                                        
            if 'back' in voice_data:
                if path == 'C://':
                    print('Sorry, this is the root directory')
                else:
                    a = path.split('//')[:-2]
                    path = '//'.join(a)
                    path += '//'
                    files = listdir(path)
                    for f in files:
                        counter+=1
                        print(str(counter) + ':  ' + f)
                                
        #File Navigation End        
                        
        #End of Controls
        else: 
            print('Invalid option')


print("Hey how can I help you ?")
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)

    