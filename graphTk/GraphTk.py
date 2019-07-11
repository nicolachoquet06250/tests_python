from tkinter import Tk, Label, Button, TOP, LEFT, RIGHT, BOTTOM, Canvas, Frame, StringVar, Entry


class GraphTk(object):
	types: dict = {}

	MENU = 'menu'
	ROSASSE = 'rosasse'
	CIBLE = 'cible'
	MOVIES_LIST = 'my_movies_list'

	GraphTop = TOP
	GraphLeft = LEFT
	GraphRight = RIGHT
	GraphBottom = BOTTOM

	@staticmethod
	def add_type(type_window: str, callback: callable):
		GraphTk.types[type_window] = callback

	def __init__(self, type_window: str or None = None, process: dict or None = None, create_window: bool = False):
		self.window_type: str or None = None
		self.root: Tk or None = Tk() if create_window else None
		self.title: str or None = None
		if type_window is not None:
			self.__type__(type_window)
			if process is not None:
				before_process = None
				after_process = None
				if "before" in process:
					before_process = process["before"]
				if "after" in process:
					after_process = process["after"]
				self.init(before_process, after_process)
			else:
				self.init()

	def init(self, before_process: callable or None = None, after_process: callable or None = None):
		self.process_init(before_process, after_process)

	def process_init(self, before_process: callable or None = None, after_process: callable or None = None):
		current_local_window = GraphTk(None, None, True)
		current_local_window.__type__(self.window_type)
		current_local_window.add_title(current_local_window.__is__())
		if before_process is not None:
			before_process()
		GraphTk.types[self.window_type](current_local_window)
		if after_process is not None:
			after_process()

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

	def add_button(self, text, command, side: str or None = None):
		button = Button(self.root, text=text, command=command)
		button.pack() if side is None else button.pack(side=side)

	def add_canvas(self, bg, height=200, width=200, side: str or None = None, callback: callable or None = None):
		canvas = Canvas(self.root, bg=bg, height=height, width=width)
		if callback is not None:
			canvas = callback(canvas)
		canvas.pack() if side is None else canvas.pack(side=side)
		return canvas

	def add_frame(self, master=None, width=200, height=200, side: str or None = None, callback: callable or None = None):
		frame = Frame(master=self.root if master is None else master, width=width, height=height)
		if callback is not None:
			frame = callback(frame, self)
		frame.pack() if side is None else frame.pack(side=side)
		return frame

	def add_entry(self, default_text: str or None = None, default_variable_text: StringVar or None = None, width=200, side: str or None = None):
		entry = Entry(self.root, text=default_text, textvariable=default_variable_text, width=width)
		entry.pack() if side is None else entry.pack(side=side)

	def get_title(self):
		return self.title

	def show(self):
		self.root.mainloop()

	def hide(self):
		self.root.quit()
		self.root.destroy()
