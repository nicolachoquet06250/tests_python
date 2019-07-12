from datetime import date
from random import randrange
from tkinter import StringVar, Frame, Label, Button

from dsl.FilmManager import FilmManager
from graphTk.GraphTk import GraphTk
from tkinterNico.MyHelpers.MyHelpers import MyHelpers


# callback of menu window
def menu(window: GraphTk):
	window.add_title("Menu")
	window.add_button('Quitter', command=lambda: MyHelpers.quit(MyHelpers.APP, window))
	window.add_button('Déssiner une rosasse', command=lambda: GraphTk(
		GraphTk.ROSASSE, {"before": lambda: MyHelpers.quit(MyHelpers.WINDOW, window)}))
	window.add_button('Déssiner une cible', command=lambda: GraphTk(
		GraphTk.CIBLE, {"before": lambda: MyHelpers.quit(MyHelpers.WINDOW, window)}))
	window.add_button('Liste de films', command=lambda: GraphTk(
		GraphTk.MOVIES_LIST, {"before": lambda: MyHelpers.quit(MyHelpers.WINDOW, window)}))
	window.show()


# callback of rosasse window
def rosasse(window: GraphTk):

	window.add_title("Rosasse")

	def draw_line(can1):
		"""Tracé d'une ligne dans le canvas can1"""
		global x1, y1, x2, y2, color
		can1.create_line(x1, y1, x2, y2, width=2, fill=color)
		y2, y1 = y2 + 10, y1 - 10

	def change_color():
		"""changement aléatoir de couleur du tracé"""
		global color
		pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
		c = randrange(8)
		color = pal[c]

	canvas = window.add_canvas('dark grey', 200, 200, GraphTk.GraphLeft)

	MyHelpers.create_main_menu_buttons(window)

	window.add_button(text='Tracer une ligne', command=lambda: draw_line(canvas))
	window.add_button(text='Autre couleur', command=change_color)

	window.show()


# callback of cible window
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
	MyHelpers.create_main_menu_buttons(window)
	window.show()


# callback of movies list window
def movies_list(window: GraphTk):

	def open_add_film_win(_: GraphTk):
		_ = GraphTk(None, None, True)
		_.add_title("Ajouter un film à la liste" + my_movies_list.title())

		input_content = StringVar(_.root, '')
		_.add_entry(None, input_content, 200, GraphTk.GraphTop)

		def new_film():

			def quit():
				MyHelpers.quit(MyHelpers.WINDOW, window)
				MyHelpers.quit(MyHelpers.WINDOW, _)

			my_movies_list.film().title(input_content.get()) \
				.realisation_date(date.today()) \
				.release_date(date.today()).build()
			GraphTk(GraphTk.MOVIES_LIST, {"before": quit})

		_.add_button(text="Valider", command=new_film, side=GraphTk.GraphBottom)
		_.show()

	def build_main_frame(frame: Frame, _: GraphTk):
		my_list = Frame(frame)
		for film in my_movies_list.films:
			title = film.title()
			text = Label(my_list, text=title)
			text.pack(side=GraphTk.GraphTop)

		form = Frame(master=frame, width=200, height=2)
		add_film = Button(master=form, text="Ajouter Un film", command=lambda: open_add_film_win(_))
		add_film.pack()
		form.pack(side=GraphTk.GraphBottom)

		my_list.pack()

		return frame

	window.add_title(my_movies_list.title())
	window.add_frame(None, 200, 200, GraphTk.GraphTop, build_main_frame)
	MyHelpers.create_main_menu_buttons(window, GraphTk.GraphLeft, GraphTk.GraphRight)
	window.show()


if __name__ == '__main__':
	# define global variables
	x1, y1, x2, y2 = 10, 190, 190, 10
	color = 'dark green'
	my_movies_list = FilmManager().title("MCU")

	# define windows types and their callback
	GraphTk.add_type(GraphTk.MENU, callback=menu)
	GraphTk.add_type(GraphTk.ROSASSE, callback=rosasse)
	GraphTk.add_type(GraphTk.CIBLE, callback=cible)
	GraphTk.add_type(GraphTk.MOVIES_LIST, callback=movies_list)

	# start menu window
	GraphTk(GraphTk.MENU)
