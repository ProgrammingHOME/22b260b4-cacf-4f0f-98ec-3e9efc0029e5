from kivy.uix.boxlayout import BoxLayout
from Interface.submitButton import SubmitButton


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50]
        self.spacing = [20, 30]
        my_button = SubmitButton()
        self.add_widget(my_button.fileInput)
        self.add_widget(my_button)
