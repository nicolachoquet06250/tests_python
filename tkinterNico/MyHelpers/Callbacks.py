from datetime import date
from random import randrange
from tkinter import StringVar

from dsl import Film
from dsl.FilmManager import FilmManager
from graphTk.GraphTk import GraphTk
from tkinterNico.MyHelpers.MyHelpers import MyHelpers


class Callbacks(object):

	POINT1 = 1
	POINT2 = 2

	OLD_WINDOW_WIDTH: int or None = None
	OLD_WINDOW_HEIGHT: int or None = None

	MY_MOVIE_LIST = FilmManager()
	LAST_MOVIE_ADDED: Film or None = None

	def __init__(self, movies_list_title: str or None = None):
		if movies_list_title is not None:
			Callbacks.MY_MOVIE_LIST.title(movies_list_title)
		self.x1 = self.x2 = self.y1 = self.y2 = self.color = None

	def p(self, num: int = POINT1, x: int or None = None, y: int or None = None):
		if num is 1:
			self.x1 = x
			self.y1 = y
		else:
			self.x2 = x
			self.y2 = y

	def update_movies_list_title(self, title):
		Callbacks.MY_MOVIE_LIST.title(title)

	def update_color(self, color):
		self.color = color

	# callback of menu window
	def menu(self, window: GraphTk):
		window.add_title("Menu")
		window.add_button('Quitter', command=lambda: MyHelpers.quit(MyHelpers.APP, window))
		window.add_button('Déssiner une rosasse', command=lambda: GraphTk(
			GraphTk.ROSASSE, {"before": lambda _: MyHelpers.quit(MyHelpers.WINDOW, window)}))
		window.add_button('Déssiner une cible', command=lambda: GraphTk(
			GraphTk.CIBLE, {"before": lambda _: MyHelpers.quit(MyHelpers.WINDOW, window)}))
		window.add_button('Liste de films', command=lambda: GraphTk(
			GraphTk.MOVIES_LIST, {"before": lambda _: MyHelpers.quit(MyHelpers.WINDOW, window)}))
		window.show()

	# callback of rosasse window
	def rosasse(self, window: GraphTk):
		window.add_title("Rosasse")
		window.add_size(350, 200, True)

		def draw_line(can1):
			"""Tracé d'une ligne dans le canvas can1"""
			# global x1, y1, x2, y2, color
			can1.create_line(self.x1, self.y1, self.x2, self.y2, width=2, fill=self.color)
			self.y2, self.y1 = self.y2 + 10, self.y1 - 10

		def change_color():
			"""changement aléatoir de couleur du tracé"""
			# global color
			pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
			c = randrange(8)
			self.update_color(pal[c])

		canvas = window.add_canvas('dark grey', 200, 200, GraphTk.GraphLeft)

		MyHelpers.create_main_menu_buttons(window)

		window.add_button(text='Tracer une ligne', command=lambda: draw_line(canvas))
		window.add_button(text='Autre couleur', command=change_color)

		window.show()

	# callback of cible window
	def cible(self, window: GraphTk):
		window.add_size(300, 200, True)

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
	def movies_list(self, window: GraphTk):
		window.add_title(Callbacks.MY_MOVIE_LIST.title())
		if Callbacks.OLD_WINDOW_HEIGHT is not None or Callbacks.OLD_WINDOW_WIDTH:
			window.add_size(Callbacks.OLD_WINDOW_WIDTH, Callbacks.OLD_WINDOW_HEIGHT, True)
		else:
			window.__center__(True)

		def reset_movies_list(to_quit: [GraphTk], movie_title: StringVar):
			MyHelpers.quit(MyHelpers.WINDOW, to_quit[0])

			def save_size(old: GraphTk):
				Callbacks.OLD_WINDOW_WIDTH = old.get_width()
				Callbacks.OLD_WINDOW_HEIGHT = old.get_height()
				MyHelpers.quit(MyHelpers.WINDOW, to_quit[1])

			Callbacks.MY_MOVIE_LIST.film()\
				.title(movie_title.get())\
				.release_date(date.today())\
				.realisation_date(date.today())\
				.build()
			Callbacks.LAST_MOVIE_ADDED = Callbacks.MY_MOVIE_LIST.film(movie_title.get())

			print(Callbacks.LAST_MOVIE_ADDED)

			GraphTk(GraphTk.MOVIES_LIST, {
				"before": lambda _: save_size(old=window)
			})

		def add_movie():
			_window = GraphTk(None, None, True)
			_window.add_title("Ajouter un film")
			_window.add_size(200, 100, True)
			movie_title = StringVar(None, '', 'movie_title')
			_window.add_entry(default_variable_text=movie_title, side=GraphTk.GraphTop)
			_window.add_button(text='Valider', command=lambda: reset_movies_list([_window, window], movie_title))
			_window.show()

		window.add_label(text='toto', side=GraphTk.GraphTop)
		window.add_button(text="Ajouter un film", command=add_movie)
		MyHelpers.create_main_menu_buttons(window, GraphTk.GraphLeft, GraphTk.GraphRight)
		window.show()
