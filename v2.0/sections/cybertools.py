import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_content_button(content_name):
    button = Gtk.Button(label=content_name)
    return button

def add_cybertools_content(content_box, section_name="Cyber Tools"):

    label = Gtk.Label()
    label.set_markup("<span size='x-large' weight='bold'>Cyber Tools</span>")

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)
    vbox.set_halign(Gtk.Align.CENTER)
    vbox.set_vexpand(False)

    vbox.pack_start(label, False, False, 10)

    hbox1 = Gtk.Box(spacing=10)
    hbox1.pack_start(create_content_button("Linux"), True, True, 0)
    hbox1.pack_start(create_content_button("WebBrowser"), True, True, 0)

    vbox.pack_start(hbox1, True, True, 10)

    vbox.pack_start(create_content_button("Hardware"), True, True, 10)

    content_box.pack_start(vbox, True, True, 0)
    content_box.show_all()
