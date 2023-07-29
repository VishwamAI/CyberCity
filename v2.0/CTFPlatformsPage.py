from gi.repository import Gtk
import webbrowser
from Page import Page

class CTFPlatformsPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        platforms = {
            "PicoCTF": "🚩 PicoCTF",
            "GoogleCTF": "🌍 GoogleCTF",
            "CTFtime": "⏰ CTFtime",
            "Hack The Box": "📦 Hack The Box",
            "CTFlearn": "🎓 CTFlearn",
            "OverTheWire": "🌉 OverTheWire",
        }

        for i, platform in enumerate(platforms):
            btn = Gtk.Button(label=platforms[platform])
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, platform)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        urls = {
            "PicoCTF": "https://picoctf.org/",
            "GoogleCTF": "https://g.co/ctf",
            "CTFtime": "https://ctftime.org/",
            "Hack The Box": "https://www.hackthebox.eu/",
            "CTFlearn": "https://ctflearn.com/",
            "OverTheWire": "https://overthewire.org/wargames/",
        }

        if page_name in urls:
            webbrowser.open(urls[page_name])
        else:
            print(f"No URL found for {page_name}")
