from kivy.uix.button import Button
from Interface.inputFileBox import FileSelect
from Interface.messageBox import MesageBox
import fitz
import os


class SubmitButton (Button):
    def __init__(self, **kwargs):
        super(SubmitButton, self).__init__(**kwargs)
        self.text = "delete"
        self.size_hint_max = [30, 50]
        self.watermark_id = [2, 1, 81, 82]  # Id Watermark to remove
        self.bind(on_press=self.on_click)
        self.fileInput = FileSelect()
        self.mesageBox = MesageBox()

    def on_click(self, instance):
        pdf_file = fitz.open(self.fileInput.selection[0])
        # iterate all PDF pages
        for page_index in range(len(pdf_file)):
            # get the page itself
            page = pdf_file[page_index]
            image_list = page.get_images()
            # printing number of images found in this page
            if image_list:
                rdoc = self.remove_watermark_on_pdf(pdf_file, page_index)
                self.mesageBox.show(f"Watermark was deleted from file \n \
                     {os.path.basename(self.fileInput.selection[0])}")
                rdoc.save("./Export/cleared_" +
                          os.path.basename(self.fileInput.selection[0]))

    def remove_watermark_on_pdf(self, idoc, page):
        # image list
        img_list = idoc.get_page_images(page)
        con_list = idoc[page].get_contents()
        for i in con_list:
            c = idoc.xref_stream(i)  # read the stream source
            # print(c) - verify
            if c is not None:
                for v in img_list:
                    if v[0] in self.watermark_id:
                        # print(v[0])
                        arr = bytes(v[7], 'utf-8')
                        r = c.find(arr)  # try find the image
                        if r != -1:
                            cnew = c.replace(arr, b"")
                            idoc.update_stream(i, cnew)
                            c = idoc.xref_stream(i)
        return idoc
