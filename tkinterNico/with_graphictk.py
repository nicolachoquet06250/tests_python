from datetime import date
from random import randrange
from tkinter import StringVar, Frame, Label, Button

from dsl.FilmManager import FilmManager
from graphTk.GraphTk import GraphTk


def quit_app(_):
	_ensure = GraphTk(None, None, True)

	def i_am_sure():
		quit_win(_ensure)
		quit_win(_)

	def i_am_not_sure():
		quit_win(_ensure)

	_ensure.add_title("Êtes vous sûr ?")
	_ensure.add_label("Voulez vous vraiment quitter l'application ?", GraphTk.GraphTop)
	_ensure.add_button("Oui, je quitte !", command=i_am_sure, side=GraphTk.GraphLeft)
	_ensure.add_button("Non, je ne veux pas quitter", command=i_am_not_sure)
	_ensure.show()


def quit_win(_):
	if type(_) is GraphTk:
		_.hide()
	else:
		_.quit()
		_.destroy()


def create_main_menu_buttons(_: GraphTk, side_return=None, side_quit=None):
	_.add_button("Retour", command=lambda: GraphTk(
		GraphTk.MENU, {"before": lambda: quit_win(_)}), side=side_return)
	_.add_button("Quitter", command=lambda: quit_app(_), side=side_quit)


def menu(window: GraphTk):
	window.add_title("Menu")
	window.add_button('Quitter', command=lambda: quit_app(window))
	window.add_button('Déssiner une rosasse', command=lambda: GraphTk(
		GraphTk.ROSASSE, {"before": lambda: quit_win(window)}))
	window.add_button('Déssiner une cible', command=lambda: GraphTk(
		GraphTk.CIBLE, {"before": lambda: quit_win(window)}))
	window.add_button('Liste de films', command=lambda: GraphTk(
		GraphTk.MOVIES_LIST, {"before": lambda: quit_win(window)}))
	window.show()


def rosasse(window: GraphTk):

	window.add_title("Rosasse")

	def drowline(can1):
		"""Tracé d'une ligne dans le canvas can1"""
		global x1, y1, x2, y2, color
		can1.create_line(x1, y1, x2, y2, width=2, fill=color)
		y2, y1 = y2 + 10, y1 - 10

	def changecolor():
		"""changement aléatoir de couleur du tracé"""
		global color
		pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
		c = randrange(8)
		color = pal[c]

	canvas = window.add_canvas('dark grey', 200, 200, GraphTk.GraphLeft)

	create_main_menu_buttons(window)

	window.add_button(text='Tracer une ligne', command=lambda: drowline(canvas))
	window.add_button(text='Autre couleur', command=changecolor)

	window.show()


def cible(window: GraphTk):

	def create_canvas(canvas):
		# create Y axe
		canvas.create_line(100, 5, 100, (190 - 10) / 2)
		canvas.create_line(100, (190 - 10) / 2 + 20, 100, 195)

		# create X axe
		canvas.create_line(5, 100, (190 - 10) / 2, 100)
		canvas.create_line((190 - 10) / 2 + 20, 100, 195, 100)

		# create cible circles
		canvas.create_oval(10, 10, 190, 190)
		canvas.create_oval(30, 30, 170, 170)
		canvas.create_oval(50, 50, 150, 150)
		canvas.create_oval(70, 70, 130, 130)
		canvas.create_oval(90, 90, 110, 110)

		return canvas

	window.add_title("Cible")
	window.add_canvas('dark grey', 200, 200, GraphTk.GraphLeft, create_canvas)
	create_main_menu_buttons(window)
	window.show()


def movies_list(window: GraphTk):

	def open_add_film_win(list_win: Frame):
		_ = GraphTk(None, None, True)
		_.add_title("Ajouter un film à la liste" + my_movies_list.title())

		input_content = StringVar(_.root, '')
		_.add_entry(None, input_content, 200, GraphTk.GraphTop)

		def new_film():
			my_movies_list.film().title(input_content.get()) \
				.realisation_date(date.today()) \
				.release_date(date.today()).build()
			list_win.pack()

		_.add_button(text="Valider", command=new_film, side=GraphTk.GraphBottom)
		_.show()

	def build_main_frame(frame: Frame, _: GraphTk):
		my_list = Frame(frame)
		for film in my_movies_list.films:
			title = film.title()
			text = Label(my_list, text=title)
			text.pack(side=GraphTk.GraphTop)

		form = Frame(master=frame, width=200, height=2)
		add_film = Button(master=form, text="Ajouter Un film", command=lambda: open_add_film_win(my_list))
		add_film.pack()
		form.pack(side=GraphTk.GraphBottom)

		my_list.pack()

		return frame

	window.add_title(my_movies_list.title())
	window.add_frame(None, 200, 200, GraphTk.GraphTop, build_main_frame)
	create_main_menu_buttons(window, GraphTk.GraphLeft, GraphTk.GraphRight)
	window.show()


if __name__ == '__main__':
	x1, y1, x2, y2 = 10, 190, 190, 10
	color = 'dark green'

	my_movies_list = FilmManager().title("MCU")

	GraphTk.add_type(GraphTk.MENU, callback=menu)
	GraphTk.add_type(GraphTk.ROSASSE, callback=rosasse)
	GraphTk.add_type(GraphTk.CIBLE, callback=cible)
	GraphTk.add_type(GraphTk.MOVIES_LIST, callback=movies_list)

	GraphTk(GraphTk.MENU)
