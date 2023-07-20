# main.py
import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk
from CyberToolsPage import CyberToolsPage
from LinuxPage import LinuxPage
from FeedbackPage import FeedbackPage
from InformationGatheringPage import InformationGatheringPage
from Page import Page

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_decorated(True)
        self.set_resizable(True)
        self.maximize()
        self.stack = Gtk.Stack()
        self.set_child(self.stack)

        self.grid = Gtk.Grid()
        self.stack.add_named(self.grid, "Main Page")  # Changed from "main_page" to "Main Page"
        self.current_page = "Main Page"  # Initialize current page to "Main Page"

        # Initialize a list to store the navigation history.
        self.navigation_history = []

        # Keep track of added pages.
        self.added_pages = set()

        buttons = ["Cyber Tools", "Training Platforms", "CTF Platforms", "Job Calendars", "Research & Discovery","Cyber Frauds","Student Development Kit","Events & Entertainments","Feedback"]        
        pages = {
            "Cyber Tools": CyberToolsPage,
            "Linux": LinuxPage,
            "Feedback": FeedbackPage,
            "InformationGathering": InformationGatheringPage,
        }

        for i, button in enumerate(buttons):
            btn = Gtk.Button(label=button)
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, button)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

            if button in pages and button not in self.added_pages:
                page = pages[button]("Go back from " + self.current_page)
                self.stack.add_named(page, button)
                self.added_pages.add(button)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        # Only create and add a new page to the GtkStack if it does not exist yet.
        if page_name not in self.added_pages:
            if page_name == "Linux":
                page = LinuxPage("Go back from " + self.current_page)
            elif page_name == "InformationGathering":
                page = InformationGatheringPage("Go back from " + self.current_page)
            else:
                page = Page("Go back from " + self.current_page)

            self.stack.add_named(page, page_name)
            self.added_pages.add(page_name)

        # Store the current page in the navigation history before switching to the new page.
        if self.current_page != page_name:
            self.navigation_history.append(self.current_page)

        self.current_page = page_name
        self.stack.set_visible_child_name(page_name)


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app, title="Cyber City")
        self.win.present()

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('style.css')
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

if __name__ == "__main__":
    app = MyApp(application_id='org.PenetrationApp.GtkApplication')
    app.run(sys.argv)
