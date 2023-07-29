from gi.repository import Gtk
from Page import Page

class CyberToolsPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        tools = {
            "🐧 Linux": "Linux",
            "🌐 Web Applications": "WebApplication",
            "🍎 MacOS": "MacOS",
            "🪟 Windows": "Windows",
            "📱 Mobile Applications": "MobileApplications"
        }

        for i, (tool, toolPage) in enumerate(tools.items()):
            btn = Gtk.Button(label=tool)
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, toolPage)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_class):
        button.get_style_context().add_class('clicked')
        main_window = self.get_root()
        main_window.open_page(button, page_class)
