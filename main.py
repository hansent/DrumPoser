import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class AppScreen(FloatLayout):
    app = ObjectProperty(None)


class EditorScreen(AppScreen):
    beat = ObjectProperty(None)


class TeachMeScreen(AppScreen):
    pass

class MainMenu(AppScreen):
    def new_beat(self):
        new_beat = {"name": "New Beat"}
        self.app.screens["editor"].beat = new_beat
        self.app.goto_screen("editor")


class DrumPoserApp(App):
    def build(self):
        self.screens = {}
        self.screens["editor"] = EditorScreen(app=self)
        self.screens["teachme"] = TeachMeScreen(app=self)
        self.screens["menu"] = MainMenu(app=self)
        self.root = FloatLayout()
        self.goto_screen("menu")
        return self.root

    def goto_screen(self, screen_name):
        self.root.clear_widgets()
        self.root.add_widget(self.screens[screen_name])

  
if __name__ == '__main__':
    DrumPoserApp().run()
