from tkinter import *
from random import randrange

if __name__ == '__main__':
    x1, y1, x2, y2 = 10, 190, 190, 10
    coul = 'dark green'

    def get_menu_buttons(win):
        return [
            {
                "text": "Quitter",
                "command": lambda: quit_app(win)
            },
            {
                "text": "Déssiner une rosasse",
                "command": lambda: drow_rosasse(win)
            },
            {
                "text": "Déssiner une cible",
                "command": lambda: drow_cible(win)
            }
        ]

    def quit_app(_: Tk):
        ensure = Tk()

        def i_am_sure():
            quit_win(ensure)
            quit_win(_)

        def i_am_not_sure():
            quit_win(ensure)

        ensure.title("Êtes vous sûr ?")
        text = Label(ensure, text="Voulez vous vraiment quitter l'application ?")
        text.pack(side=TOP)
        oui = Button(ensure, text="Oui, je quitte !", command=i_am_sure)
        oui.pack(side=LEFT)
        non = Button(ensure, text="Non, je ne veux pas quitter", command=i_am_not_sure)
        non.pack()
        ensure.mainloop()

    def quit_win(_: Tk):
        _.quit()
        _.destroy()

    def create_main_menu_buttons(_: Tk):
        _return = Button(_, text="Retour", command=lambda: menu(_))
        _return.pack()
        _quit = Button(_, text='Quitter', command=lambda: quit_app(_))
        _quit.pack()

    def menu(subwin: Tk or None = None):
        win = Tk()
        win.title("Menu")

        for button in get_menu_buttons(win):
            _button = Button(win, text=button["text"], command=button["command"])
            _button.pack()

        if subwin is not None:
            quit_win(subwin)

        win.mainloop()

    def drow_rosasse(win):

        def drowline(can1):
            """Tracé d'une ligne dans le canvas can1"""
            global x1, y1, x2, y2, coul
            can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
            y2, y1 = y2 + 10, y1 - 10

        def changecolor():
            """changement aléatoir de couleur du tracé"""
            global coul
            pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
            c = randrange(8)
            coul = pal[c]

        quit_win(win)

        subwin = Tk()
        subwin.title("Rosasse")

        can1 = Canvas(subwin, bg='dark grey', height=200, width=200)
        can1.pack(side=LEFT)
        create_main_menu_buttons(subwin)
        button2 = Button(subwin, text='Tracer une ligne', command=lambda: drowline(can1))
        button2.pack()
        button3 = Button(subwin, text='Autre couleur', command=changecolor)
        button3.pack()

        subwin.mainloop()

    def drow_cible(win):
        quit_win(win)

        subwin = Tk()
        subwin.title("Cible")

        can1 = Canvas(subwin, bg='dark grey', height=200, width=200)

        # create Y axe
        can1.create_line(100, 5, 100, (190 - 10) / 2)
        can1.create_line(100, (190 - 10) / 2 + 20, 100, 195)

        # create X axe
        can1.create_line(5, 100, (190 - 10) / 2, 100)
        can1.create_line((190 - 10) / 2 + 20, 100, 195, 100)

        # create cible circles
        can1.create_oval(10, 10, 190, 190)
        can1.create_oval(30, 30, 170, 170)
        can1.create_oval(50, 50, 150, 150)
        can1.create_oval(70, 70, 130, 130)
        can1.create_oval(90, 90, 110, 110)

        can1.pack(side=LEFT)

        create_main_menu_buttons(subwin)

        subwin.mainloop()

    menu()
