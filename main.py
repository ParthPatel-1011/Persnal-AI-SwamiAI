import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import os
import cohere
import random


chatStr =""
def chat(query):
    global chatStr
    api_key = '' #todo:Set the your Cohere API key
    co = cohere.Client(api_key)
    chatStr += f"Swami : {query}\n: "
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=chatStr,
        max_tokens=200
    )
    print(response.generations[0].text)
    say(response.generations[0].text)
    chatStr += f"{response.generations[0].text}"
    return response.generations[0].text

def ai(prompt):
    # Set the Cohere API key
    api_key = ''
    co = cohere.Client(api_key)
    text=f"cohere response for prompt : {prompt}\n ************************\n"
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=200
    )
    try:
        print(response.generations[0].text)
        text += response.generations[0].text
    except Exception as e:
        print("Sorry from Swami . Not Choice Availabel")
    if not os.path.exists("cohere Files"):
        os.mkdir("cohere Files")

    with open(f"cohere Files/{''.join(prompt.split('ai')[1:]).strip()}.txt","w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def tackCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1 #todo:wait for Listning
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Swami"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am swami AI")
    while True:
        print("Listening...")
        query = tackCommand()

        #add more website when you open
        sites = [["YouTube","https://www.youtube.com"],["Google","https://www.google.com"],["Chat GPT","https://chatgpt.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} ...")
                webbrowser.open(site[1])

        if "open music".lower() in query.lower():
            musicpath= "C:/Users/Patel Parth/Downloads/Unstoppable - Dino James  Ft Avengers  Dipan Patel.mp3"
            os.startfile(musicpath)    #replce: os.system(f"open {musicpath}")

        elif "the time".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            minut = datetime.datetime.now().strftime("%M")
            say(f"Sir the Time is {hour} hours and {minut} minutes")

        elif "using AI".lower() in  query.lower():
            ai(prompt=query)

        if "let's talk".lower() in query.lower():
            say("Sure, Why Not?")
            while True:
                print("Listening...")
                query = tackCommand()
                if "bye".lower() in query.lower():
                    say("Bye! It was nice chatting with you.")
                    exit(0)
                chat(query)

        #Add application when you open
        application = [["VS code","C:/Users/Patel Parth/Desktop/Visual Studio Code.lnk"],["file explorer","C:/Users/Patel Parth/Desktop/File Explorer.lnk"]]
        for app in application:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]} sir...")
                os.startfile(app[1])
        if "Swami shutdown".lower() in query.lower():
            say("Ok. By by , see you soon...")
            exit(0)
