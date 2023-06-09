

#Importing Required Libraries

import speech_recognition as sr
import time
import webbrowser as wb
import os
from playsound import playsound
import gtts

#Defining all the required functions in the Project

#Function to Convert text to speech!!
def text_to_speech(audio_text):
    tts = gtts.gTTS(text=audio_text, lang = 'en', slow = False)     #Using Google-Text-to-Speech API
    tts.save("audio_file.mp3")        #Saving the Audio File
    playsound('audio_file.mp3')       #Playing the Audio File
    print(audio_text)                #Printing the text for better understanding
    
    #This is default path in my PC. Change according to yours!
    os.remove("C:/Users/hp/audio_file.mp3")      #Deleteing the file so that it doesn't pile up or throw error


#Function to convert speech to text!!
def speech_listen():
    print("Speak Now!")    #Will ask you to start speaking
    with sr.Microphone() as source:
        speech = r.listen(source)    #Listening
        voice_data = ""
        try:
            voice_data = r.recognize_google(speech)   #Recognizing
        except: 
            print("Sorry, I did not get that")     #Error if couldn't recognize
        return voice_data

#Function to perform various operations in response to our speech command!!
def speech_answer(voice_data):
    if "play music" in voice_data:
        url = "https://www.youtube.com/"              #For Play Music Command
        wb.get().open_new(url)
        text_to_speech("Opening Youtube for you!")
    if "weather" in voice_data:
        url = "https://www.google.com/search?q=weather"     #For Showing Weather Command
        wb.get().open_new(url)
        text_to_speech("Showing you today's weather")
    if "search" in voice_data:
        text_to_speech("What do you want to search?")        #Search for Something Command
        search = speech_listen()
        url = "https://www.google.com/search?q="+ search
        wb.get().open_new(url)
        text_to_speech("I found this for "+ search)
    if "location" in voice_data:
        text_to_speech("Location to where?")                   #Search for locatio Command
        location = speech_listen()
        url = url = "https://www.google.nl/maps/place/"+location
        wb.get().open_new(url)
        text_to_speech("Here is location to" + location)
    if "time" in voice_data:
        text_to_speech(time.ctime())                            #Telling Time Command

#Initialising the Recognizer class
r = sr.Recognizer()

#Main Running Program!

print("Hello, How may I help you? I can do the following tasks") #Bot Starts the Session
task_list = ["Play Music", "Weather Report", "Search Google", "Find you a location", "Tell you Time"]
print(task_list)
print("Give me commands after you hear Speak Now!")    #To consider the waiting time of the execution of commands
while True:
    voice_data = speech_listen()
    print(voice_data)
    speech_answer(voice_data)
    print("Want to Continue? Yes/no")
    Continue = speech_listen()
    if Continue == "no":
        break
print("thank you")  #Bot Ends the Session
