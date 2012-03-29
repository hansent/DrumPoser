import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, StringProperty
from kivy.uix.label import Label
from kivy.factory import Factory as F


class AppScreen(FloatLayout):
    app = ObjectProperty(None)


class MainMenu(AppScreen):
    pass


class TeachMeScreen(AppScreen):
    pass


class EditorScreen(AppScreen):
    instrument_list = ObjectProperty(None)
    settings = ObjectProperty(None)
    controlls = ObjectProperty(None)


    def init_editor(self):
        self.instrument_list.clear_widgets()
        for instr_name in open("instruments.txt", "r").readlines():
            instr = InstrumentEditor(name=instr_name)
            self.instrument_list.add_widget(instr)


    def play(self):
        print "PLAY"

    def pause(self):
        print "PLAY"

    def previous(self):
        print "PREVIOUS"

    def next(self):
        print "NEXT"


class EditorSettings(BoxLayout):
    time_signature = NumericProperty(4.0)
    tempo = NumericProperty(4.0)



class EditorControlls(BoxLayout):
    pass


class InstrumentEditor(BoxLayout):
    name = StringProperty("Instrument")




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
            self.screens["editor"].init_editor()



F.register("EditorSettings", EditorSettings)
F.register("EditorControlls", EditorControlls)
F.register("InstrumentEditor", InstrumentEditor)

if __name__ == '__main__':
    DrumPoserApp().run()
