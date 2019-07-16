from dsl.FilmManager import FilmManager
from graphTk.GraphTk import GraphTk
from tkinterNico.MyHelpers.Callbacks import Callbacks


if __name__ == '__main__':
	# define global variables
	# x1, y1, x2, y2 = 10, 190, 190, 10
	# color = 'dark green'

	callbacks = Callbacks()

	callbacks.update_movies_list_title("MCU")
	callbacks.update_color('dark green')
	callbacks.p(Callbacks.POINT1, 10, 190)
	callbacks.p(Callbacks.POINT2, 190, 10)

	# define windows types and their callback
	GraphTk.add_type(GraphTk.MENU, callback=callbacks.menu)
	GraphTk.add_type(GraphTk.ROSASSE, callback=callbacks.rosasse)
	GraphTk.add_type(GraphTk.CIBLE, callback=callbacks.cible)
	GraphTk.add_type(GraphTk.MOVIES_LIST, callback=callbacks.movies_list)

	# start menu window
	GraphTk(GraphTk.MENU)
