import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_content_button(content_name):
    """Creates a button widget with the provided content name."""
    button = Gtk.Button(label=content_name)
    return button

def add_research_and_discovery_content(content_box):
    label = Gtk.Label()
    label.set_markup("<span size='x-large' weight='bold'>Research &amp; Discovery</span>")

    # Box to hold the label and buttons, align it to the center
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)  # Align towards the top
    vbox.set_halign(Gtk.Align.CENTER)  # Center horizontally
    vbox.set_vexpand(False)  # Don't expand vertically

    vbox.pack_start(label, False, False, 10)

    # Box to hold the first row of buttons
    hbox1 = Gtk.Box(spacing=10)
    hbox1.pack_start(create_content_button("Academic Journals"), True, True, 0)
    hbox1.pack_start(create_content_button("Whitepapers"), True, True, 0)
    vbox.pack_start(hbox1, True, True, 10)

    # Box to hold the second row of buttons
    hbox2 = Gtk.Box(spacing=10)
    hbox2.pack_start(create_content_button("Industry Reports"), True, True, 0)
    hbox2.pack_start(create_content_button("Collaborative Projects"), True, True, 0)
    vbox.pack_start(hbox2, True, True, 10)

    # Box to hold the third row of buttons
    hbox3 = Gtk.Box(spacing=10)
    hbox3.pack_start(create_content_button("Open Source Repositories"), True, True, 0)
    hbox3.pack_start(create_content_button("Latest Innovations"), True, True, 0)
    vbox.pack_start(hbox3, True, True, 10)

    # Box to hold the fourth row of buttons
    hbox4 = Gtk.Box(spacing=10)
    hbox4.pack_start(create_content_button("Thought Leadership"), True, True, 0)
    hbox4.pack_start(create_content_button("Organizations"), True, True, 0)
    vbox.pack_start(hbox4, True, True, 10)

    content_box.pack_start(vbox, True, True, 0)
    content_box.show_all()
