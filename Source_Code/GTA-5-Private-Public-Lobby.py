import tkinter as tk
from tkinter import messagebox
import psutil
from time import sleep

win = tk.Tk()
win.title("GTA 5 Private Public Lobby")
win.iconbitmap('icon2.ico')


#Window size/Window Center
win.resizable(False, False)
window_height = 200
window_width = 500

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
#Window size/Window Center

win.configure(background = 'black')
TL = tk.Label(win, text = 'GTA 5 Private Public Lobby', fg = 'green', bg = 'black', font = (None, 30), height = 2)
TL.pack(anchor = 'n')

def GTACommand():
    PROCNAME = "GTA5.exe"
    try:
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                p = psutil.Process(int(proc.pid))
        
#^Get Process ID Number For GTA5^
      
                p.suspend()
                sleep(10)
                p.resume()
                messagebox.showinfo("GTA 5 Private Public Lobby", "You May Now Close The Program You're Now In A Public Lobby With No Other Players, Enjoy!") 
    except NameError:
        messagebox.showinfo("Ooops!", "You Are Not Running GTA 5!")
    
def About():
    messagebox.showinfo("Made By Mirrorable", "Allows You To Have Your Own Public Lobby To Get Away From Greifers/Hackers")
    
    
button1 = tk.Button(win, text="Start", width=25, command=GTACommand)
button2 = tk.Button(win, text="About", width=25, command=About)
button1.pack(anchor='center')
button2.pack(anchor='center')

win.mainloop()




