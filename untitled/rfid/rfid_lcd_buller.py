from tkinter import *
class App:
    def __init__(self,window):
        #buzzer button
        buzzerFrame = Frame(window)
        Button(buzzerFrame,text="Buzzer_Control",padx=5,pady=5,command=self.userClickBuzzer).pack(padx=10,pady=10)
        buzzerFrame.pack()

        #button init

    def userClickBuzzer(self):
        print("user click")
        pass
if __name__ == "__main__":
    root = Tk()
    root.title("RFID_LCD_BUZZER")
    root.option_add("*font", ("verdana", 18, "bold"))
    root.option_add("*background", "gold")
    root.option_add("*forground", "#888888")


    app = App(root)
    root.mainloop()