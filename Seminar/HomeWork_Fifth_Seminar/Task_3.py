# Создайте программу для игры в ""Крестики-нолики"".
from tkinter import *

runing = True
symbol = 'X'
def run():
    def quit():
        window.destroy()

    def exit():
        global runing
        runing = False
        window.destroy()

    def Kres_Nol(event,i):
        global symbol
        if symbol == 'X':
            b[i].configure(text="X", state='disabled')
            symbol ='O'
        else:
            b[i].configure(text="O", state='disabled')
            symbol = 'X'

    window = Tk()
    window.title("Игра Крестики - Нолики")
    window.geometry("90x170+700+300")
    window.resizable(width=True, height=True)

    l = Label(window, text="Крестики-Нолики", font=("Arial Bold", 8))
    restart = Button(window, text="Заного", command=quit)
    b_exit = Button(window, text="Выход", command=exit)
    b={}
    b = \
        {
            '1': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '2': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '3': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '4': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '5': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '6': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '7': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '8': Button(window, width=3, height=1, font=("Arial Bold", 9)),
            '0': Button(window, width=3, height=1, font=("Arial Bold", 9))
        }

    ent = StringVar()

    l.grid(row=0, column=1, columnspan=3, sticky=N)
    b['0'].grid(row=4, column=3, ipadx=0, ipady=0, padx=2, pady=2)
    b['1'].grid(row=2, column=1, ipadx=0, ipady=0, padx=2, pady=2)
    b['2'].grid(row=2, column=2, ipadx=0, ipady=0, padx=2, pady=2)
    b['3'].grid(row=2, column=3, ipadx=0, ipady=0, padx=2, pady=2)
    b['4'].grid(row=3, column=1, ipadx=0, ipady=0, padx=2, pady=2)
    b['5'].grid(row=3, column=2, ipadx=0, ipady=0, padx=2, pady=2)
    b['6'].grid(row=3, column=3, ipadx=0, ipady=0, padx=2, pady=2)
    b['7'].grid(row=4, column=1, ipadx=0, ipady=0, padx=2, pady=2)
    b['8'].grid(row=4, column=2, ipadx=0, ipady=0, padx=2, pady=2)

    restart.grid(row=6, columnspan=5)
    b_exit.grid(row=7, columnspan=5)

    b['0'].bind('<Button-1>', lambda e, f="0": Kres_Nol(e, f))
    b['1'].bind('<Button-1>', lambda e, f="1": Kres_Nol(e, f))
    b['2'].bind('<Button-1>', lambda e, f="2": Kres_Nol(e, f))
    b['3'].bind('<Button-1>', lambda e, f="3": Kres_Nol(e, f))
    b['4'].bind('<Button-1>', lambda e, f="4": Kres_Nol(e, f))
    b['5'].bind('<Button-1>', lambda e, f="5": Kres_Nol(e, f))
    b['6'].bind('<Button-1>', lambda e, f="6": Kres_Nol(e, f))
    b['7'].bind('<Button-1>', lambda e, f="7": Kres_Nol(e, f))
    b['8'].bind('<Button-1>', lambda e, f="8": Kres_Nol(e, f))

    window.mainloop()

while runing:
    run()
