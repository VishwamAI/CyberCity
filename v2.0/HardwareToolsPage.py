from gi.repository import Gtk
import webbrowser
from Page import Page

class HardwareToolsPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        tools = {
            "Hak5": "https://hak5.org/",
            "Pine64": "https://www.pine64.org/",
            "Raspberry Pi": "https://www.raspberrypi.org/",
            "Pwnie Express": "https://www.pwnieexpress.com/",
            "Think Penguin": "https://www.thinkpenguin.com/",
            "SparkFun Electronics": "https://www.sparkfun.com/"
        }

        for i, tool in enumerate(tools):
            btn = Gtk.Button(label=tool)
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_tool, tools[tool])
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_tool(self, button, tool_url):
        button.get_style_context().add_class('clicked')
        webbrowser.open(tool_url)
