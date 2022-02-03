from kivy.app import App
from Interface.mainScreen import MainScreen
from kivy.core.window import Window


class WatermarkApp(App):
    def build(self):
        self.title = "WaterMARK - www.ednc.gov.md (remover)"
        Window.size = (600, 400)
        return MainScreen()


if __name__ == "__main__":
    WatermarkApp().run()
