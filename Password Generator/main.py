import tkinter as tk
import random

#input = int(input("How many characters? "))

#generate a new password
def new_rand():
    myentry.delete 

    password_length = int(myentry.get())

    my_password = ''

    for i in range(password_length):
        my_password += chr(random.randint(33,126))

    myentry2.insert(0, my_password)
#copy to clipboard
def clipper():
    window.clipboard_clear()
    window.clipboard_append(myentry2.get())

#password generator GUI
window = tk.Tk()

window.geometry("500x500")
window.title("Password Generator")

label = tk.LabelFrame(window, text="How many Characters?")
label.pack(pady=20)

myentry = tk.Entry(label, font=("Helvetica", 24))
myentry.pack(padx=20, pady=20)

myentry2 = tk.Entry(window , text="", font = ('Helvetica', 24), bd = 0, bg = "systembuttonface")
myentry2.pack(pady = 20)

frame = tk.Frame(window)
frame.pack(pady=20)

button1 = tk.Button(frame, text="Generate a Password", command=new_rand)
button1.grid(row = 0, column=0, padx=10 )

button2 = tk.Button(frame, text="Copy To Clipboard", command=clipper)
button2.grid(row = 0, column=1, padx=10 )

window.mainloop()
#def randnumgenerator(input):
