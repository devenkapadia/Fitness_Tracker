from tkinter import *
from Exercises import counter

def run():
    root=Tk()
    root.title("Fitness Tracker")
    # WxH
    root.geometry('1080x720')
    f2 = Frame(root, bg="#292F3F", pady=10)
    lbl1 = Label(f2, text="Instructions :", bg="light blue", font="Helvetica 20 bold", pady=5)
    lbl1.pack()
    str2 = "1. You can choose the mode to play 3,4 or 5 letter wordle\n2. When the letter is available in the word and the position is also correct than the letter will be coloured green\n3. When the letter is available in the word and but the position is not correct than the letter will be coloured yellow\n4. When the letter is not available in the word, than it will be coloured black\n5. You will get 6 trials"
    rules = Label(f2, text=str2, bg="#8CD4C9", font="TimesNewRoman 15", justify="left")
    rules.pack(pady=8, padx=14)
    btn = Button(f2, text="Yoga", font="Vardana 12 bold", width=8, height=1, bg="#8CD4C9",
                 command=lambda:exit())
    btn2 = Button(f2, text="Exercise-Bicep Curls", font="Vardana 12 bold", width=15, height=1, bg="#8CD4C9",
                 command=lambda: counter())
    btn.pack()
    btn2.pack()
    f2.pack()
    root.mainloop()

def email():
    id,pw = "20dce125@charusat.edu.in", "PRUTHA3011"
    return id,pw

def data():
    exn = "Bicep Curls"
    reps = 12
    cal = '34kcal'
    return exn,reps,cal

if __name__ == '__main__':
    run()