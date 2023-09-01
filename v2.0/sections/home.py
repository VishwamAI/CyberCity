import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def add_home_content(content_box, section_name="Dashboard"):
        # Clear previous content from the content box
    for widget in content_box.get_children():
        content_box.remove(widget)

    # Create a label with the section name
    label = Gtk.Label()
    label.set_markup(f"<span size='x-large' weight='bold'>{section_name}</span>")
    
    # Vertical box to place the label
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    
    # Set horizontal alignment to center
    vbox.set_halign(Gtk.Align.CENTER)
    
    # Set vertical alignment to start (top)
    vbox.set_valign(Gtk.Align.START)
    vbox.set_vexpand(False)

    # Add some padding to the top of the label to push it down
    label.set_margin_top(30)  # Adjust this value as needed

    vbox.pack_start(label, False, False, 10)
    
    # Add the vbox to the content box and display all widgets
    content_box.pack_start(vbox, True, True, 0)
    content_box.show_all()
