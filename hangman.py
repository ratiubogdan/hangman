from tkinter import *
import random
import winsound


class Hangman:
    def __init__(self, window):
        self.window = window
        self.word = ""
        self.guessed = [""]
        self.stage = 0
        self.won = False
        self.lost = False
        self.img = None

        window.geometry("1100x800")
        window.title("Hangman")
        window.resizable(0, 0)
        self.frame = Frame(master=window, bg="white")
        self.frame.pack_propagate(0)  #Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  #Expand the frame to fill the root window

        self.lb = Label(master=self.frame, bg="white", fg="blue", text="Welcome to Ratman's Hangman!", font=("Sans", 25))
        self.lb.grid(row=0, pady=20, columnspan=4)

        self.lb2 = Label(master=self.frame, bg="white", text="Guess one letter", font=("Sans", 20))
        self.lb2.grid(row=1, columnspan=1, sticky=S, pady=10)

        self.et = Entry(master=self.frame, font=("Sans", 20), width=3, bg="lightgray")
        self.et.grid(row=2, sticky=S)
        self.bt = Button(master=self.frame, text="Test", font=("Sans", 16), command=self.test)
        self.bt.grid(row=3, column=0, sticky=N)

        self.guess = Label(master=self.frame, bg="white", font=("Sans", 35))
        self.guess.grid(row=4, columnspan=2)
        self.get_word()
        self.draw_initial()

        self.canvas = Canvas(master=self.frame, width=350, height=410)
        self.canvas.grid(row=1, column=2, rowspan=3, padx=50, pady=50)

        self.bt2 = Button(master=self.frame, text="Exit", font=("Sans", 20), command=sys.exit)
        self.bt2.grid(row=4, column=2, pady=50)

        self.frame.grid_columnconfigure(0, weight=1)

    def get_word(self):
        fp = open("dictionar.txt")
        line = fp.readline()
        num_words = int(line)
        for i in range(random.randint(1, num_words)):
            line = fp.readline().strip()
        self.word = line

    def draw_initial(self):
        self.guess.config(text="_ "*len(self.word))

    def test(self):
        text = self.et.get()
        if text:
            text = text[0]

        if self.won or self.lost:
            return
        if text in self.guessed or text not in self.word:
            self.stage += 1
            #draw the new picture
            img_name = "stage" + str(self.stage) + ".gif"
            self.img = PhotoImage(file=img_name)
            self.canvas.create_image(0, 0, image=self.img, anchor=NW)
            #check if lost
            if self.stage == 9:
                self.lb2.config(text="Ratman Hanged You!", fg="red", font=("Helvetica", 35))
                self.lost = True
                self.guess.config(text=self.word, fg="red")
                # winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
            self.et.delete(0, END)
            return
        won = True
        if text in self.word:
            self.guessed.append(text)
            string = ""
            for c in self.word:
                if c in self.guessed:
                    string += c + " "
                else:
                    string += "_ "
                    won = False
            self.guess.config(text=string)
        if won:
            self.lb2.config(text="You won! Ratman is pleased", fg="red", font=("Helvetica", 30))
            self.won = True
            # winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        self.et.delete(0, END)




window = Tk()
hang = Hangman(window)
window.mainloop()
