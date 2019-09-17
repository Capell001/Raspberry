from tkinter import *

def appInterface(window):
    frame = Frame(window,borderwidth=2,width=500,height=600,relief=GROOVE);
    frame.pack(padx=10,pady=10);
    pass

if __name__ == '__main__':
    app = Tk()
    app.title("LEDControl")
    app.geometry("500x600")
    appInterface(window=app);
    app.mainloop()