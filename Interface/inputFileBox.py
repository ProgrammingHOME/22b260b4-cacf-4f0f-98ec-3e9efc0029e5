from kivy.uix.filechooser import FileChooserListView
import os


class FileSelect(FileChooserListView):
    def __init__(self, **kwargs):
        super(FileSelect, self).__init__(**kwargs)
        self.rootpath = os.getcwd() + "/PDF"
        self.filters = ["*.pdf"]
        self.multiselect = False
