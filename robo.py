import gtts, os, time, requests, uuid, json
from playsound import playsound
import speech_recognition as sr

r = sr.Recognizer()
uidexist = os.path.exists("custom.uid")
inuse = False

if not (uidexist):
    with open("custom.uid", "r") as file:
        data = file.read().rstrip()
        uid = data
        file.close()
        print("UID IMPORTED:", uid)
else:
    with open("custom.uid", "w") as file:
        uidget = uuid.uuid4()
        file.write(str(uidget))
        file.close()
        uid = str(uidget)
        print("UID DID NOT EXIST. NEW UID CREATED IN 'custom.uid':", uid)
    
def talktoai(cmd):
    with open('robo.aikey', 'r') as file:
        data = file.read().rstrip()
        cmdedit = cmd.replace(" ", "%20")
        url = "http://api.brainshop.ai/get?bid=172046&key=" + data + "&uid=" + uid + "&msg=" + cmdedit
        print(url)
        response = requests.get(url)
        file.close()
        y = json.loads(response.text)
        print(response.text)
        print(y["cnt"])
        return(y["cnt"])

def speak(string):
    tts = gtts.gTTS(string)
    tts.save("temp.mp3")
    time.sleep(3)
    playsound("temp.mp3")
    time.sleep(10)
    os.remove("temp.mp3")

print("Setup Finished")
def command():
    inuse = True
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Listened to Speech")
    try:
        response = r.recognize_google(audio)
        print("Recognised Speech:", response)
        if "hey robo" in response:
            command = response.replace('hey robo', '')
            print("Got Command ready")
            ai = talktoai(command)
            print("Sent to acobot.robo")
            speak(ai)
            print("Words Spoken from AI Response:" + ai)
            inuse = False
        if "hey Robbo" in response:
            command = response.replace('hey Robbo', '')
            print("Got Command ready")
            ai = talktoai(command)
            print("Sent to acobot.robo")
            speak(ai)
            print("Words Spoken from AI Response:" + ai)
            inuse = False
    except sr.RequestError:
        response = "requesterror"
        print("I'm sorry, I could not connect to my servers.")
        inuse = False
    except sr.UnknownValueError:
        # speech was unintelligible
        response = "unknownspeech"
        inuse = False
while True:
    if (inuse == False):
        command()