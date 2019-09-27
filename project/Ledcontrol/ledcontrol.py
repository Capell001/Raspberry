from tkinter import *
import RPi.GPIO as GPIO

from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('/home/pi/Documents/iotcapel-firebase-adminsdk-ps4ca-4caaa40275.json')

firebase_admin.initialize_app(cred, {
    'databaseURL':'https://iotcapel.firebaseio.com/',
    'databaseAuthVariableOverride': {'uid':'UrkkzLIJNdTGzLLaM0GyorLEYlp2'}
})

ledControlRef = db.reference(path='iot0624/lcdControl')

def appInterface(window):
    try:
        lcdState = ledControlRef.get()
    except FirebaseError as err:
        print("error connect to Firebase: {}".format(err))
    except ValueError as err:
        print("valueError: {}".format(err))
    except:
        print("Error")

    if lcdState:
        buttonText.set("OFF")
    else:
        buttonText.set("ON")

    frame = Frame(window, borderwidth=2, relief=GROOVE)
    ledButton = Button(frame, textvariable=buttonText, padx=30, pady=10, command=userClick, width=10).pack(padx=40,pady=40)
    frame.pack(padx=10, pady=10)


def userClick():
    lcdState = ledControlRef.get()
    if lcdState:
        buttonText.set('ON')
        GPIO.output(17, GPIO.LOW)
    else:
        buttonText.set('OFF')
        GPIO.output(17, GPIO.HIGH)

    ledControlRef.set(not lcdState)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)

    app = Tk()
    buttonText = StringVar()
    app.title("LEDControl")
    # app.geometry("500x600");
    appInterface(window=app)
    app.mainloop()