import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_content_button(content_name):
    """Creates a button widget with the provided content name."""
    button = Gtk.Button(label=content_name)
    return button

def add_training_and_learning_content(content_box, section_name="Training & Learning"):
    """Populates the provided container with labeled buttons related to training and learning."""
    
    # Create a label with the section name
    label = Gtk.Label()
    label.set_markup(f"<span size='x-large' weight='bold'>Training &amp; Learning</span>")
    
    # Vertical box to hold the label and button rows
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)
    vbox.set_halign(Gtk.Align.CENTER)
    vbox.set_vexpand(False)

    vbox.pack_start(label, False, False, 10)
    
    # First row of buttons: "Training Platforms" and "CTF Platforms"
    hbox1 = Gtk.Box(spacing=10)
    hbox1.pack_start(create_content_button("Training Platforms"), True, True, 0)
    hbox1.pack_start(create_content_button("CTF Platforms"), True, True, 0)
    vbox.pack_start(hbox1, True, True, 10)

    # Second row of buttons: "YouTube Channels" and "Courses"
    hbox2 = Gtk.Box(spacing=10)
    hbox2.pack_start(create_content_button("YouTube Channels"), True, True, 0)
    hbox2.pack_start(create_content_button("Courses"), True, True, 0)
    vbox.pack_start(hbox2, True, True, 10)
    
    # A button for "Student Development Kit"
    vbox.pack_start(create_content_button("Student Development Kit"), True, True, 10)
    
    # Add the vbox to the content box and display all widgets
    content_box.pack_start(vbox, True, True, 0)
    content_box.show_all()
