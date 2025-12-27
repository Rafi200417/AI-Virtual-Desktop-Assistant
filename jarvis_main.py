import datetime
import os
import random
import webbrowser
import bs4
import notification
import pyautogui
import pyttsx3
import requests
import speech_recognition
import speedtest
from pygame import mixer
from sqlalchemy.testing.plugin.plugin_base import config

from internet_speed import check_speed
from calculatenumbers import Calc
from config import wolframalpha

for i in range(3):
    a = input("Enter password to open Jarvis :-")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (a!=pw):
        print("Try Again")



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")                                             
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en-in')
        print("You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetME import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("OK sir , You can call anytime")
                    break

                # JARVIS: The  Trilogy 2.0 ###############################

                elif "change password" in query:
                    speak("What the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks = [] # empty list
                    speak("Do you want to clear old tasks (plz speak YES or NO")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the task :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no .of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}.{tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()

                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )


                elif "open" in query: #Easy method
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")


                elif  "check internet speed" in query:
                     check_speed()



                elif "ipl score" in query:
                    from plyer import notification  # pip install plyer
                    import requests  # pip install requests
                    from bs4 import BeautifulSoup  # pip install beautifulsoup4

                    try:
                        url = "https://www.cricbuzz.com/"
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                        }

                        page = requests.get(url, headers=headers)
                        soup = BeautifulSoup(page.text, "html.parser")

                        # Find the first live match block
                        live_match = soup.find("div", class_="cb-col cb-col-100 cb-ltst-wgt-hdr")

                        if live_match:
                            team_names = live_match.find_all("span", class_="cb-ovr-flo cb-hmscg-tm-nm")
                            team_scores = live_match.find_all("span", class_="cb-ovr-flo")

                            if len(team_names) >= 2 and len(team_scores) >= 2:
                                team1 = team_names[0].get_text()
                                team2 = team_names[1].get_text()
                                team1_score = team_scores[1].get_text()  # Index 1 usually holds score
                                team2_score = team_scores[3].get_text()  # Index 3 usually holds score

                                print(f"{team1} : {team1_score}")
                                print(f"{team2} : {team2_score}")

                                notification.notify(
                                    title="IPL SCORE :-",
                                    message=f"{team1} : {team1_score}\n{team2} : {team2_score}",
                                    timeout=15
                                )
                            else:
                                print("Team names or scores not found.")
                        else:
                            print("Live match section not found.")

                    except Exception as e:
                        print("Error occurred while fetching IPL scores:", e)


                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                    import pyautogui  # pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if a == 1:
                        speak("Entering the focus mode....")
                        os.startfile(r"C:\Users\srile\OneDrive\Desktop\JARVIS")
                        exit()
                    elif a ==2:
                        speak("Focus mode cancelled.")
                    else:
                        speak("please enter valid option: 1 for Yes or 2 for No.")
                        exceptValueError
                        speak ("Invalid input. please enter a number: 1 for Yes or 2 for No.")
                        pass

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "translate" in query:
                     from Translator import translategl
                     query = query.replace("jarvis", "")
                     query = query.replace("translate", "")
                     translategl(query)

                    ##############################################
                
                elif "hi" in query:
                    speak("Hello sir , how are ypu ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("You are welcome , sir")
                    
                elif "tired" in query:
                    speak("playing your favourite songs, Sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=rgGDTO8g2Pg&list=PPSV")
                    
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                    
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,Sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down,Sir")
                    volumedown()
                    
                elif "Open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                    
                elif "calculate" in query:
                    from calculatenumbers import WolfRamAlpha
                    from calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                    
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()




                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    }
                    r = requests.get(url, headers=headers)
                    data = bs4.BeautifulSoup(r.text, "html.parser")

                    temp = data.select_one("span#wob_tm")  # Google uses this ID for temperature now
                    if temp:
                        speak(f"Current {search} is {temp.text}°C")
                    else:
                        speak("Sorry, I couldn't fetch the temperature.")


                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = bs4.BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeaWE")
                    speak(f"current{search} is {temp}")
                    
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a= input("please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep, sir")
                    exit()
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("you told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                    
                    
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no):").lower()

                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                     speak("shutdown cancelled.")







                    
                    
                        
                    
    
    
        
            
        

    
            