from tkinter import Tk, Label


class GraphTk(object):
	types: dict = {}

	MENU = 'menu'
	ROSASSE = 'rosasse'
	CIBLE = 'cible'

	@staticmethod
	def add_type(type_window: str, callback: callable):
		GraphTk.types[type_window] = callback

	def __init__(self, type_window: str or None = None, create_window: bool = False):
		self.window_type: str or None = None
		self.root: Tk or None = Tk() if create_window else None
		self.title: str or None = None
		if type_window is not None:
			self.__type__(type_window)
			self.init()

	def init(self):
		self.process_init()

	def process_init(self):
		current_local_window = GraphTk(None, True)
		current_local_window.__type__(self.window_type)
		GraphTk.types[self.window_type](current_local_window)

	def __type__(self, type_window):
		self.window_type = type_window

	def __is__(self, type_window: str or None = None) -> bool or str:
		if type_window is None:
			return self.window_type
		return self.window_type is type_window

	def add_label(self, text, side: str or None = None):
		label = Label(master=self.root, text=text)
		label.pack() if side is None else label.pack(side=side)

	def add_title(self, title: str):
		self.title = title
		return self.root.title(title)

	def get_title(self):
		return self.title

	def show(self):
		self.root.mainloop()

	def hide(self):
		self.root.quit()
		self.root.destroy()
