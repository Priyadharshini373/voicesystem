import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unn='priyadharsh237@gmail.com'
pwd='cndu axol kejk ktej'

r=sr.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str="Speak now"
        speak(str)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            return text
        except:
            str="Sorry could not recognize what you said"
            speak(str)

def sendmail(): 
    rec="srilekhs2k3@gmail.com"
    str="Please speak the body of your email"
    speak(str)
    msg=listen()

    str="You have spoken the message"
    speak(str)
    speak(msg)

    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(unn,pwd)
    server.sendmail(unn,rec,msg)
    server.quit()

    str="The mail has been sent"
    speak(str)

def readmail():
    server=e.connect("imap.gmail.com",unn,pwd)
    server.listids()

    str="Please say the Serial number of the email you wanna read starting from latest"
    speak(str)
    print(len(server.listids()))
    a=listen()
    print(a)
    if(a=='Tu'):
        a=2
    elif(a=="one"):
        a=1
    elif(a=="three"):
        a=3
    elif(a=="four"):
        a=4
    elif(a=="five"):
        a=5
    elif(a=="six"):
        a=6
    elif(a=="seven"):
        a=7
    elif(a=="eight"):
        a=8
    elif(a=="nine"):
        a=9
    elif(a=="ten"):
        a=10
    else:
        a=11
    b=int(a)-1

    email=server.mail(server.listids()[b])
    str="The email is from:"
    speak(str)
    speak(email.from_addr)
    str="The subject of the email is:"

    speak(str)

    speak(email.title)
    str="The body of the email is:"
    speak(str)
    speak(email.body)

str='Welcome to voice based Email system for visually impaired persons'
speak(str)

while(1):
    str="What do you want to do?"
    speak(str)
    str="Speak 'SEND' to Send Mail     Speak 'READ' to Read Inbox      Speak 'EXIT' to Exit"
    speak(str)

    ch=listen()

    if(ch=='send'):
        str="You have chosen to send an email"
        speak(str)
        sendmail()
    elif(ch=="read"):
        str="You have chosen to read email"
        speak(str)
        readmail()
    elif(ch=="exit"):
        str="You have chosen to exit, bye bye"
        speak(str)
        break
    else:
        str="Invalid choice, you said:"
        speak(str)
        speak(ch)
