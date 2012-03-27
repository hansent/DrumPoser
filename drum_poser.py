import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from bar_editor import BarEditorScreen

parent = Widget()

class MainMenu(Widget):
	def new_beat(self):
		self.canvas.clear()
		bar_editor = BarEditorScreen()
		parent.clear_widgets()
		parent.add_widget(bar_editor)


class DrumPoserApp(App):
	def build(self):
		mainmenu = MainMenu()
		
		parent.add_widget(mainmenu)

		return parent
#		return MainMenu()

if __name__ == '__main__':
    DrumPoserApp().run()

