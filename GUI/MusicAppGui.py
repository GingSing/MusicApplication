import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from logic import Downloader
from logic import YTParser
from threading import Thread
from kivy.uix.listview import ListItemButton


# Background layer
class Background(BoxLayout):
    pass


class TopMenu(BoxLayout):
    pass


class Application(BoxLayout):
    pass


# Attached to Application Layout
class Options(BoxLayout):
    pass


class Output(BoxLayout):
    pass


class Manager(ScreenManager):
    pass


# Stuff for Manager
class Downloads(Screen):

    downloader = Downloader.Downloader()
    parser = YTParser.YTParser()

    mp3 = ObjectProperty(True)
    mp4 = ObjectProperty(False)

    result_list = ObjectProperty()

    def download(self, input, ext):

        downloader = self.downloader

        def callback():
            downloader.download(input, ext)

        if input:
            try:
                t = Thread(target=callback)
                t.start()
            except Exception:
                print("Error")

    def submit_search(self, input):

        parser = self.parser

        def callback():
            self.result_list.adapter.data = parser.get_queries(input)
            self.result_list.trigger_reset_populate()

        if input:
            try:
                t = Thread(target=callback)
                t.start()
            except Exception:
                print("Error")


class Songs(Screen):
    pass


class ResultListButton(ListItemButton):
    pass


class PlayList(Screen):
    pass


class Setting(Screen):
    pass


# Menu for the side
class SideMenu(BoxLayout):
    pass


class Space(BoxLayout):
    pass


class LemonWireApp(App):

    def build(self):
        return Background()


lemonWire = LemonWireApp()
lemonWire.run()




# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.core.audio import SoundLoader,Sound
# from kivy.lang import Builder
# Builder.load_string('''
# <MenuPage>:
#     BoxLayout:
#         orientation:'vertical'
#         Button:
#             text:'song'
#             on_press:root.plays()
# ''')
#
# class MenuPage(Screen):
#     M = SoundLoader.load('Defqwop - Heart Afire (feat. Strix) [Lyrics].mp3')
#
#     def plays(self):
#         if MenuPage.M.state == 'stop':
#             MenuPage.M.play()
#         else:
#             MenuPage.M.stop()
#
#
# sm = ScreenManager()
# menu = MenuPage(name='menu')
# sm.add_widget(menu)
#
#
# class TestApp(App):
#     def build(self):
#         return sm
#
#
#
#
# TestApp().run()