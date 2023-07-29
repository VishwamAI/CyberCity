from gi.repository import Gtk
import webbrowser
from Page import Page

class FeedbackPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        tools = {
            "Email": "✉️",
            "LinkedIn": "🔗",
            "Facebook": "📘",
            "Youtube": "📺"
        }
        for i, tool in enumerate(tools):
            btn = Gtk.Button(label=tools[tool])
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, tool)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')
        
        if page_name == "Email":
            self.contact_email(button)
        elif page_name == "LinkedIn":
            self.open_linkedin(button)
        elif page_name == "Facebook":
            self.open_facebook(button)
        elif page_name == "Youtube":
            self.open_youtube(button)

    def contact_email(self, button):
        webbrowser.open("mailto:exploit0xffff@gmail.com")

    def open_linkedin(self, button):
        webbrowser.open("https://www.linkedin.com/company/exploit0xfffff")

    def open_facebook(self, button):
        webbrowser.open("https://www.facebook.com/Exploit0xffffff")

    def open_youtube(self, button):
        webbrowser.open("https://www.youtube.com/channel/UC4JXxQqQqXK4QHhQgqEeYjQ")
