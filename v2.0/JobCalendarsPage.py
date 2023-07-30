# JobCalendarsPage.py
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from Page import Page

class JobCalendarsPage(Page):
    def __init__(self, back_button_text):
        super().__init__(back_button_text)

        label = Gtk.Label()
        label.set_markup("<big><b>Coming Soon!</b></big>")
        self.append(label)  # replace pack_start with append
