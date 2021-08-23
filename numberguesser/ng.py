import tkinter
import random


window = tkinter.Tk()
window.geometry("600x400")
window.config(bg="#3a65ab")
window.resizable(width=False,height=False)
window.title('Number Guessing Game')

n = random.randint(1,99)
title = tkinter.Label(window,text="Guessing Game",font=("Arial",24),fg="White",bg="#3a65ab")
title.place(x=180, y=50)
result = tkinter.Label(window, text="Click to Play button", font=("Arial", 12),fg = "White", bg="#3a65ab")
result.place(x=200, y=200)
user_input = tkinter.Entry()

def close():
    quit()

def play():
    user_input.place(x=210,y=100)
    guessbtn.place(x=350,y=100)
    result.config(text="Guess a number between 1-99")

def guess():
    guessed_number = user_input.get()
    guessed_number_int = int(guessed_number)
    if n > guessed_number_int:
        result.config(text="Its higher than the number, guess other!")
    elif n < guessed_number_int:
        result.config(text="Its lower than the number, guess other!")
    elif n == guessed_number_int:
        result.config(text="Yes it is!")
        guessbtn.pack_forget()



playbtn = tkinter.Button(window,text="Play Game",font=("Arial",14), fg="Black", bg="#37b373", command=play)
playbtn.place(x=170,y=250)
guessbtn = tkinter.Button(window,text="Guess",font=("Arial",14),fg="Black",bg="Red", command=guess)
exitbtn = tkinter.Button(window,text="Exit Game",font=("Arial",14), fg="Black", bg="#fa5a5a", command=close)
exitbtn.place(x=300,y=250)

window.mainloop()