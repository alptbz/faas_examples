import base64
import io
import json
import tkinter
from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk


class ImageDescriptionTestUi:

    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        self.data = []
        self._init_gui()
        self.load_and_update()
        

    def run(self):
        self.root.mainloop()

    def _init_gui(self):
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        self.listbox = tkinter.Listbox(frm, width=100)
        self.listbox.grid(column=0, row=0)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

        self.textbox_description = tkinter.Label(frm)
        self.textbox_description.grid(column=0, row=1)

        self.textbox_tags = tkinter.Label(frm)
        self.textbox_tags.grid(column=0, row=2)

        self.imagecanvas = Canvas(frm, width=300, height=300)
        self.imagecanvas.grid(column=0, row=3)

        reload_button = tkinter.Button(frm, text="Reload", command=self.load_and_update)
        reload_button.grid(column=1, row=0)

    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        entry = [x for x in self.data if x["name"] == value][0]
        self.textbox_description.config(text=entry["description"])
        self.textbox_tags.config(text=entry["tags"])
        im = Image.open(io.BytesIO(base64.b64decode(entry['image'])))
        im_tk = ImageTk.PhotoImage(im)
        self.imagecanvas.create_image(20, 20, anchor=NW, image=im_tk)
        self.imagecanvas.image = im_tk

    def load_and_update(self):
        self.load_data()
        self.update_listbox()

    def load_data(self):
        resp = requests.get(self.endpoint_url)
        self.data = json.loads(resp.content)

    def update_listbox(self):
        self.listbox.delete(0, END)
        i = 0
        for d in self.data:
            self.listbox.insert(i, d["name"])
            i += 1


ui = ImageDescriptionTestUi("http://localhost:7071/api/RetrieveResultsHttpTrigger")
ui.run()

