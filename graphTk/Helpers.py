from tkinter import Tk
from graphTk.GraphTk import GraphTk


class Helpers(object):
	APP = 'app',
	WINDOW = 'win'

	@staticmethod
	def quit(type_quit=WINDOW, _: Tk or GraphTk or None = None):
		def switch():
			def quit_app():
				_ensure = GraphTk(None, None, True)
				_ensure.add_size(350, 50, True)

				def i_am_sure():
					quit_win(_ensure)
					quit_win(_)

				def i_am_not_sure():
					quit_win(_ensure)

				_ensure.add_title("Êtes vous sûr ?")
				_ensure.add_label("Voulez vous vraiment quitter l'application ?", GraphTk.GraphTop)
				_ensure.add_button("Oui, je quitte !", command=i_am_sure, side=GraphTk.GraphLeft)
				_ensure.add_button("Non, je ne veux pas quitter", command=i_am_not_sure, side=GraphTk.GraphRight)
				_ensure.show()

			def quit_win(__):
				if type(__) is GraphTk:
					__.hide()
				else:
					__.quit()
					__.destroy()

			switcher = {
				Helpers.APP: quit_app,
				Helpers.WINDOW: lambda: quit_win(_)
			}
			switcher.get(type_quit)()
		switch()

