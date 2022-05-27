
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.config import Config
from kivy.app import runTouchApp

# You can create your kv code in the Python file

# Create a class for all screens in which you can include
# helpful methods specific to that screen

class MainWindow(Screen):
    space_texture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.space_texture = Image(source = "img/space_earth.jpg").texture
        self.space_texture.wrap = 'repeat'
        self.space_texture.uvsize = (Window.width/self.space_texture.width, -1)

    def scroll_textures(self, time_passed):
        #Update the uvpos
        self.space_texture.uvpos = ((self.space_texture.uvpos[0] + time_passed/200) % Window.width, (self.space_texture.uvpos[1] - time_passed/200) % Window.width)
        #Redraw textures
        texture = self.property('space_texture')
        texture.dispatch(self)

class Window1(Screen):
    text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def read_text(self):
        with open("data/bigbang.txt") as f:
            return f.read()

class Window2(Screen):
    s1_texture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s1_texture = Image(source = "img/blackhole.png").texture
        self.s1_texture.wrap = 'repeat'
        self.s1_texture.uvsize = (Window.width/self.s1_texture.width, -1)

    def scroll_textures(self, time_passed):
        #Update the uvpos
        self.s1_texture.uvpos = ((self.s1_texture.uvpos[0] + time_passed/60) % Window.width, (self.s1_texture.uvpos[1] - time_passed/20) % Window.width)
        #Redraw textures
        texture = self.property('s1_texture')
        texture.dispatch(self)

class Window3(Screen):
    text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def read_text(self):
        with open("data/blackhole.txt") as f:
            return f.read()

class Window4(Screen):
    text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def read_text(self):
        with open("data/wormhole.txt") as f:
            return f.read()

class Window5(Screen):
    text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def read_text(self):
        with open("data/hyperspace.txt") as f:
            return f.read()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

#Config.write()
class MyApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.mainwindow.scroll_textures, 1/60.)
        Clock.schedule_interval(self.root.ids.window2.scroll_textures, 1/60.)
        pass
    def build(self):
        return kv


MyApp().run()
