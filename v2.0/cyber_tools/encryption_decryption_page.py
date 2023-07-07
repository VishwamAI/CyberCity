import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class EncryptionDecryptionPage(Gtk.Box):
    def __init__(self, back_label):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.back_button = Gtk.Button(label=back_label)
        self.back_button.connect("clicked", self.go_back)
        self.append(self.back_button)

    def go_back(self, button):
        main_window = self.get_root()
        main_window.stack.set_visible_child_name("main_page")
