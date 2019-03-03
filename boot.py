#--------------------------Importing Functions----------------------
import os
import pyttsx #Talk function helper
from gtts import gTTS #speech helper
from pygame import mixer #mixing and performing action on audio.
import time# time finction library
import speech_recognition as sr
import getpass #to get current username
import win32api, win32con, win32gui#use in desktop images change variable
import ctypes
import pyautogui as pg # all keabord input and other graphics function
import webbrowser as wb
#--------------------------Global Variables--------------------------
folder_name = "Ray1"
windows_username = getpass.getuser()
username = "sid"
mode = 0
mode_print=['general','web browser','turbo c','python','smart','ultimate','web development']
#--------------------------Defined modes-----------------------------
#           0 = General ( Default )
#           1 = Webbrowser ( easy Internet access)
#           2 = programming mode ( turbo c)
#           3 = python mode ( IDLE )
#           4 = smart mode ( command run )
#           5 = ultimate mode ( Assistant mode )
#           6 = webdevelopment ( brackets editor )
#--------------------------TALKING FUNCTION--------------------------
rey1 = pyttsx.init()
def engine2(text):
    rey1.say(text)
    rey1.runAndWait()

#                               phase 2
mixer.init()
def engine(text):
    tts = gTTS(text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

##                              phase 3
import win32com.client as wincl
def engine1(text) :
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)


#--------------------------Speech Recognizer--------------------------
#engine1("booting recognizer")
def listen( spoken_text ):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        a = r.listen(source)

        try:
                    print ":"
                    spoken_text = r.recognize_google(a)
                    return spoken_text
        except sr.UnknownValueError:
                print('could not understand audio')
                return ""
        except sr.RequestError as e:
                print("Recog Error; (0)".format(e))
                engine1("i am not connect to the internet. i need an internet connection to connect to my server")
                time.sleep(5)
                return ""
#-------------------------application handling---------------------------
engine2("installing drivers")
def open_application(text) :
    location="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\"+text+".lnk"
    location = '"'+location+'"'
    os.system(location)


def close_application(text) :
    command = "taskkill /im "+text+".exe /t /f"
    os.system(command)

def activate():
    change_desktop("black",1)
    time.sleep(1)
    pg.press('win')
    pg.typewrite('rainmeter')
    time.sleep(.5)
    pg.press('enter')
    time.sleep(.5)
    pg.hotkey('win','d')

def deactivate():
    for i in range(20) :
        change_desktop('desktop',1)
        os.system('taskkill /im rainmeter.exe /t')


#--------------------------Wallpaper Change--------------------------------
#engine1("installing system variables")
def change_desktop(path,mode) :
    if mode == 1 :
        location = "C:\\"+folder_name+"\\images\\"+path+".png"
    elif mode == 2 :
        location = "C:\\Users\\"+windows_username+"\\Pictures\\Screenshots\\"+path+".png"
    else:
        location = '"' + path + '"'

    if(os.path.exists(location)):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, location , 0)
    else:
        engine1('sorry! unable to change picture, '+path+' doesnt exists')


'''
if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction()
'''
##------------------------booted perfectly-------------
#engine1("hey sid!! I am ready for work.. how may i help  you?")
while True:
    spoken_text = ""
    word = ['q','q','q','q']
    print ":"
    spoken_text = listen ( spoken_text)
    print spoken_text
    #time.sleep(5)
    #   spoken_text = "start first two services of xampp"
    spoken_text += ' q'
    analyzed_text = spoken_text.split()

    for i in range(0,len(analyzed_text)-1):
        #print analyzed_text[i]
        #print i
        if ((analyzed_text[i].lower() ==  "hey") or (analyzed_text[i].lower() == "hi" )or (analyzed_text[i].lower() =="hello") ):
            word[0] = analyzed_text[i] + ' ' + username
        elif (analyzed_text[i].lower() == "good") and ( analyzed_text[i+1].lower() == "morning" or analyzed_text[i+1].lower() == "evening" or analyzed_text[i+1].lower() == "afternoon"):
            word[1] = 'good '+ analyzed_text[i+1] + ' ' + username
        elif (analyzed_text[i].lower() == "how") and analyzed_text[i+1].lower() == "are" and analyzed_text[i+2].lower() == "you":
            word[2] = 'i am good '+username+', how are you.'
        elif (analyzed_text[i].lower() == "i") and analyzed_text[i+1].lower() == "am" and analyzed_text[i+2].lower() == "fine":
            word[3] = 'i am glad to here that.'
        elif (((analyzed_text[i].lower() == "goto" or analyzed_text[i].lower() == "open") and analyzed_text[i+1].lower() == "desktop" ) or (analyzed_text[i].lower() == "minimize" and (analyzed_text[i+1].lower() == "all" or analyzed_text[i+1].lower() == "everything"))):
            mode = 0
            pg.hotkey('win','d')
        elif (analyzed_text[i].lower() == "customise" and analyzed_text[i+1].lower() == "yourself"):
               engine1("Activating Ultimate mode")
               activate()
        elif (analyzed_text[i].lower() == "get" and analyzed_text[i+1].lower() == "back" and analyzed_text[i+4].lower() == "normal"):
                engine1("deactivating ultimatemode")
                deactivate()
        elif (analyzed_text[i].lower() == "want" and analyzed_text[i+2].lower() == "play" and analyzed_text[i+3].lower() == "tic"):
                wb.open_new_tab('https://playtictactoe.org/')
        elif (analyzed_text[i].lower() == "i" and analyzed_text[i+2].lower() == "not"):
                engine1("who are you what is your name")
        elif (analyzed_text[i].lower() == "my" and analyzed_text[i+1].lower() == "name"):
                username = analyzed_text[i+3]
                engine1("oh.. hello "+username +" how are you?")
        elif (analyzed_text[i].lower() == "start" and analyzed_text[i+1].lower() == "first" and analyzed_text[i+2].lower() == "two"  and analyzed_text[i+5].lower() == "xampp"):
                pg.press('tab')
                pg.press('tab')
                pg.press('enter')
                time.sleep(3)
                pg.press('tab')
                pg.press('tab')
                pg.press('enter')
        elif ((analyzed_text[i].lower() == "shut" and analyzed_text[i+1].lower() == "down") or analyzed_text[i].lower() == "shutdown"):
                pg.hotkey('win','d')
                time.sleep(.5)
                pg.hotkey('alt','f4')
                time.sleep(.5)
                pg.press('enter')
            


        elif analyzed_text[i].lower() == "restart":
                pg.hotkey('win','d')
                time.sleep(.5)
                pg.hotkey('alt','f4')
                pg.press('r')
                time.sleep(.5)
                pg.press('enter')

        elif analyzed_text[i].lower() == "sleep" and analyzed_text[i+1].lower() == "mode":
                pg.hotkey('win','d')
                time.sleep(.5)
                pg.hotkey('alt','f4')
                pg.press('s')
                pg.press('s')
                pg.press('s')
                time.sleep(.5)
                pg.press('enter')
        
        
        elif analyzed_text[i].lower() == "what" and analyzed_text[i+1].lower() == "is" and analyzed_text[i+3].lower() == "current" and analyzed_text[i+4].lower() == "mode":
                print mode_print[mode]
                engine1("i am on current "+mode_print[mode]+" mode")
        if mode == 1 :


            if (analyzed_text[i].lower() == "minimise" or analyzed_text[i].lower() == "minimize"):

                pg.hotkey("alt","space")
                time.sleep(.5)
                pg.press("n")
                
            elif (analyzed_text[i].lower() == "maximise" or analyzed_text[i].lower() == "maximize"):

                pg.hotkey("alt","space")
                time.sleep(.5)
                pg.press("x")
            elif (analyzed_text[i].lower() == "small" and analyzed_text[i+1].lower() == "window"):
                pg.hotkey("alt","space")
                time.sleep(.5)
                pg.press("R")
                
            elif (analyzed_text[i].lower() == "close" and analyzed_text[i+2].lower() == "window") :
                    pg.hotkey('alt','f4')
            elif (analyzed_text[i].lower() == "close" and analyzed_text[i+1].lower() == "all") and ( analyzed_text[i+2].lower() == "windows" or analyzed_text[i+3].lower() == "windows"):
                    close_application('chrome')
            elif (analyzed_text[i].lower() == "refresh") :
                        pg.hotkey('ctrl','r')
            elif (analyzed_text[i].lower() == "restore" and analyzed_text[i+1].lower() == "previous") :
                    pg.hotkey('alt','shift','t')
            elif analyzed_text[i].lower() == "search":
                string = ""
                if ( analyzed_text[i+1].lower() != "for" or analyzed_text[i+1] != "about" ):
                    for j in range(i+1,len(analyzed_text)-3) :
                      string += analyzed_text[j]+ " "
                    if (analyzed_text[j+2].lower() != "tab") and (analyzed_text[j+2].lower() != "window"):
                       string += analyzed_text[j+1] + analyzed_text[j+2]
                    elif (analyzed_text[j+2].lower() == "tab" and analyzed_text[j+1].lower() == "new") :
                       pg.hotkey('ctrl','t')
                    elif (analyzed_text[j+2].lower() == "window" and analyzed_text[j+1].lower() == "new" ) :
                       pg.hotkey('ctrl','n')
                    pg.typewrite(string)
                    pg.press("enter")
            elif analyzed_text[i].lower() == "open" :
                    if (analyzed_text[i+2].lower() == "tab" and analyzed_text[i+1].lower() == "new") :
                       pg.hotkey('ctrl','t')
                       engine1("opening new tab")
                    elif (analyzed_text[i+2].lower() == "window" and analyzed_text[i+1].lower() == "new" ) :
                       pg.hotkey('ctrl','n')
                       engine1("opening new window")
                    string = ""
                    if ( analyzed_text[i+1].lower() == "facebook" or (analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "facebook")):
                            wb.open_new_tab("www.facebook.com")

                    elif ( analyzed_text[i+1].lower() == "gmail" or analyzed_text[i+1].lower() == "mails" or (analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "mails")):
                            wb.open_new_tab("www.gmail.com")

                    elif ( analyzed_text[i+1].lower() == "instagram" or analyzed_text[i+1].lower() == "instagrame" or (analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "instagram")):
                            wb.open_new_tab("www.instagram.com")

                    elif ( analyzed_text[i+1].lower() == "github" or(analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "github")):
                            wb.open_new_tab("www.github.com")

                    else:
                            pg.press("win")
                            pg.typewrite(analyzed_text[i+1])
                            time.sleep(.5)
                            pg.press("enter")
                            engine1("openning "+analyzed_text[i+1])

                            if analyzed_text[i+1].lower() == "chrome" or analyzed_text[i+1].lower() == "google" :
                                mode = 1  #chrome mode

                            elif analyzed_text[i+1].lower() == "turbo":
                                mode = 2
                            elif analyzed_text[i+1].lower() == "idle":
                                mode = 3
                            elif analyzed_text[i+1].lower() == "brackets":
                                mode = 6
        else:
                    if (analyzed_text[i].lower() ==  "open"):
                        if ( analyzed_text[i+1].lower() == "facebook" or (analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "facebook")):
                            wb.open_new_tab("www.facebook.com")
                            mode = 1
                        elif ( analyzed_text[i+1].lower() == "gmail" or analyzed_text[i+1].lower() == "mails" or (analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "mails")):
                            wb.open_new_tab("www.gmail.com")
                            mode = 1
                        elif ( analyzed_text[i+1].lower() == "instagram" or analyzed_text[i+1].lower() == "instagrame" or (analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "instagram")):
                            wb.open_new_tab("www.instagram.com")
                            mode = 1
                        elif ( analyzed_text[i+1].lower() == "github" or(analyzed_text[i+1].lower() == "my" and analyzed_text[i+2].lower() == "github")):
                            wb.open_new_tab("www.github.com")
                            mode = 1
                        else:
                            pg.press("win")
                            pg.typewrite(analyzed_text[i+1])
                            time.sleep(.5)
                            pg.press("enter")
                            engine1("openning "+analyzed_text[i+1])

                            if analyzed_text[i+1].lower() == "chrome" or analyzed_text[i+1].lower() == "google" :
                                mode = 1  #chrome mode

                            elif analyzed_text[i+1].lower() == "turbo":
                                mode = 2
                            elif analyzed_text[i+1].lower() == "idle":
                                mode = 3
                            elif analyzed_text[i+1].lower() == "brackets":
                                mode = 6

                    if (analyzed_text[i].lower() == "search" ):
                        string = ""
                        if ( analyzed_text[i+1].lower() != "for" or analyzed_text[i+1] != "about" ):
                            for j in range(i+2,len(analyzed_text)-3) :
                                string += analyzed_text[j]+"+"
                            if (analyzed_text[j+2].lower() != "internet" ) :
                                string += analyzed_text[j+1]+"+" + analyzed_text[j+2]
                            string = "www.google.com/search?q=" + string
                            mode = 1
                            engine1("I got this search result from the google")
                            wb.open_new_tab(string)


    print word

    i=0
    while i<= 3 :
        if ( word[i] != 'q' ):
            engine1(word[i])

        i=i+1

    time.sleep(1)
