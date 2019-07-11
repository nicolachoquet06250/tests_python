from dsl.FilmManager import FilmManager
from graphTk.GraphTk import GraphTk


def menu(window: GraphTk):
	window.add_title(window.__is__())
	print(window.get_title())
	window.show()


def rosasse(window: GraphTk):
	window.root.title(window.__is__())
	window.show()


def cible(window: GraphTk):
	window.root.title(window.__is__())
	window.show()


if __name__ == '__main__':
	x1, y1, x2, y2 = 10, 190, 190, 10
	coul = 'dark green'

	liste = FilmManager().title("MCU")

	GraphTk.add_type(GraphTk.MENU, callback=menu)
	GraphTk.add_type(GraphTk.ROSASSE, callback=rosasse)
	GraphTk.add_type(GraphTk.CIBLE, callback=cible)

	GraphTk(GraphTk.MENU)
