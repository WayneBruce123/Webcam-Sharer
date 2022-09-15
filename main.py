import time
import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from filesharer import Fileshare
from kivy.core.clipboard import Clipboard

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.start.text = 'Stop camera'
        self.ids.camera.texture = self.ids.camera.texture  # self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.start.text = 'Start camera'
        self.ids.camera.texture = None

    def capture(self):
        capture_time = time.strftime('%y%m%d - %H%M%S')
        self.file_path = f'files/{capture_time}.png'
        self.ids.camera.export_to_png(self.file_path)
        self.manager.current = 'photo_screen'
        self.manager.current_screen.ids.img.source = self.file_path


class PhotoScreen(Screen):

    def create_shareable_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.file_path
        file_share = Fileshare(file_path)
        self.url = file_share.share()
        self.ids.label.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.label.text = 'Create a link first'

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.label.text = 'Create a link first'

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
