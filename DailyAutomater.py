import os
import pyttsx3
import pywhatkit
import datetime
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
np = ["Times of India", "The Hindu", "Hindustan Times", "Indian Express", "The Pioneer", "Deccan Herald"]

def talk(text):
    engine.say(text)
    engine.runAndWait()
    print("")

def newsStarter(news):
    if news == '1':
        print("Sure! Showing latest news on " + np[0])
        talk("Sure. Showing latest news on times of india")
        webbrowser.open('https://timesofindia.indiatimes.com/')
    elif news == '2':
        print("Sure! Showing latest news on " + np[1])
        talk("Sure. Showing latest news on the hindu")
        webbrowser.open('https://www.thehindu.com/')
    elif news == '3':
        print("Sure! Showing latest news on " + np[2])
        talk("Sure. Showing latest news on hindustan times")
        webbrowser.open('https://www.hindustantimes.com/')
    elif news == '4':
        print("Sure! Showing latest news on " + np[3])
        talk("Sure. Showing latest news on indian express")
        webbrowser.open('https://indianexpress.com/')
    elif news == '5':
        print("Sure! Showing latest news on " + np[4])
        talk("Sure. Showing latest news on the pioneer")
        webbrowser.open('https://www.dailypioneer.com/')
    elif news == '6':
        print("Sure! Showing latest news on " + np[5])
        talk("Sure. Showing latest news on deccan herald")
        webbrowser.open('https://www.deccanherald.com/')
    else:
        print("Error! Choice doesn't exist.")
        talk("Error. Choice doesn't exist")

def ytSearch(arg):
    arg = arg.lower()
    if arg == "":
        print("You didn't type anything!")
        talk("You didn't type anything")
    else:
        talk('playing ' + arg)
        pywhatkit.playonyt(arg)

def main():
    choice = input("News/YT/Both: ")
    choice = choice.lower()
    if choice == 'news':
        print("Which provider would you like to choose?\n1."+np[0]+"\n2."+np[1]+"\n3."+np[2]+"\n4."+np[3]+"\n5."+np[4]+"\n6."+np[5])
        talk("Which provider would you like to choose")
        news = input("Type number of choice: ")
        newsStarter(news)
    elif choice == "yt":
        print("What would you like to listen to/watch?")
        talk("What would you like to listen to or watch?")
        yt = input()
        ytSearch(yt)
    elif choice == "both":
        print("Which provider would you like to choose?\n1."+np[0]+"\n2."+np[1]+"\n3."+np[2]+"\n4."+np[3]+"\n5."+np[4]+"\n6."+np[5])
        news = input("Type number of choice: ")
        print("What would you like to listen to/watch?")
        talk("What would you like to listen to or watch?")
        yt = input()
        ytSearch(yt)
        newsStarter(news)
    else:
        print("Error! Invalid argument passed!")
        talk("Error. Invalid argument passed")

print("Hello there. I'm your News and Youtube handler. Sadly, for you, hehe, only I'll do the talking here.")
talk("Hello there. I'm your News and Youtube handler. Sadly, for you, hehe, only I'll do the talking here.")
print("What's your pick for today's start? Might wanna start off with some news and chill with songs, y'know.")
talk("What's your pick for today's start? Might wanna start off with some news and chill with songs y'know")

main()