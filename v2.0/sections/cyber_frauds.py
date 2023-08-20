import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_content_button(content_name):
    """Creates a button widget with the provided content name."""
    button = Gtk.Button(label=content_name)
    return button

def add_cyber_frauds_content(content_box):
    label = Gtk.Label()
    label.set_markup("<span size='x-large' weight='bold'>Cyber Frauds &amp; Emerging Threats</span>")

    # Box to hold the label and buttons, align it to the center
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)  # Align towards the top
    vbox.set_halign(Gtk.Align.CENTER)  # Center horizontally
    vbox.set_vexpand(False)  # Don't expand vertically

    vbox.pack_start(label, False, False, 10)

    # Box to hold the first row of buttons
    hbox1 = Gtk.Box(spacing=10)
    hbox1.pack_start(create_content_button("Case Studies"), True, True, 0)
    hbox1.pack_start(create_content_button("Recent Attacks"), True, True, 0)
    hbox1.pack_start(create_content_button("Mitigation Techniques"), True, True, 0)
    vbox.pack_start(hbox1, True, True, 10)

    # Box to hold the second row of buttons
    hbox2 = Gtk.Box(spacing=10)
    hbox2.pack_start(create_content_button("Threat Intelligence"), True, True, 0)
    hbox2.pack_start(create_content_button("Digital Forensics"), True, True, 0)
    vbox.pack_start(hbox2, True, True, 10)

    content_box.pack_start(vbox, True, True, 0)
    content_box.show_all()
