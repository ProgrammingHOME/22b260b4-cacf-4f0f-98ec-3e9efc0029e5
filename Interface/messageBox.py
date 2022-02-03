from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MesageBox (Popup):
    def __init__(self, **kwargs):
        super(MesageBox, self).__init__(**kwargs)
        self.title = "Information"
        self.size_hint = (None, None)
        self.size = (300, 300)

    def show(self, message: str) -> None:
        self.message_text = message
        self.content = self.get_content()
        self.open()

    def get_content(self) -> BoxLayout:
        grup_box = BoxLayout(orientation="vertical")
        message = Label(text=self.message_text)
        close_btn = Button(text="close", size_hint=(1, 0.2))
        close_btn.bind(on_press=self.close_message_box)
        grup_box.add_widget(message)
        grup_box.add_widget(close_btn)
        return grup_box

    def close_message_box(self, instance):
        self.dismiss()
