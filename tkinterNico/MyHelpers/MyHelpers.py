from graphTk.GraphTk import GraphTk
from graphTk.Helpers import Helpers


class MyHelpers(Helpers):

	@staticmethod
	def create_main_menu_buttons(_: GraphTk, side_return=None, side_quit=None):
		_.add_button("Retour", command=lambda: GraphTk(
			GraphTk.MENU, {"before": lambda: Helpers.quit(Helpers.WINDOW, _)}), side=side_return)
		_.add_button("Quitter", command=lambda: Helpers.quit(Helpers.APP, _), side=side_quit)