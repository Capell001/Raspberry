from tkinter import *

def userClick():
    print("user click")
    pass

def appInterface(window):
    frame = Frame(window, borderwidth=2, relief=GROOVE)
    ledButton = Button(frame, text="ON", padx=10, pady=10, command=userClick).pack(padx=40, pady=40)
    frame.pack(padx=10,pady=10)

if __name__ == '__main__':
    app = Tk()
    app.title("LEDControl")
    app.geometry("500x600")
    appInterface(window=app)
    app.mainloop()