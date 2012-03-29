import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label


class AppScreen(FloatLayout):
    app = ObjectProperty(None)


class EditorScreen(AppScreen):
    instrument_list_wid = ObjectProperty(None)
    
    def draw_instrument_list(self):
        label1 = Label(text='Open High Hat')
        self.instrument_list_wid.add_widget(label1)

    def init_editor(self):
        self.draw_instrument_list()

class TeachMeScreen(AppScreen):
    pass

class MainMenu(AppScreen):
    pass

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
        if screen_name == 'editor':
            EditorScreen().init_editor()
            
  
if __name__ == '__main__':
    DrumPoserApp().run()
