import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk


stack = Gtk.Stack()
navigation_history = []

def create_content_button(content_name, callback=None):
    button = Gtk.Button(label=content_name)
    button.set_relief(Gtk.ReliefStyle.NONE)
    button.connect("enter-notify-event", lambda widget, event: widget.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2)))
    button.connect("leave-notify-event", lambda widget, event: widget.get_window().set_cursor(None))
    if callback:
        button.connect("clicked", callback)
    return button

def go_back(button):
    last_visited_page = navigation_history.pop() if navigation_history else "cybertools_main"
    stack.set_visible_child_name(last_visited_page)
    button.connect("enter-notify-event", lambda widget, event: widget.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2)))
    button.connect("leave-notify-event", lambda widget, event: widget.get_window().set_cursor(None))

def navigate_to_page(button, page_name):
    current_page = stack.get_visible_child_name()
    if current_page != page_name:
        navigation_history.append(current_page)
        stack.set_visible_child_name(page_name)

def create_top_bar():
    hbox = Gtk.Box(spacing=10)
    go_back_button = Gtk.Button()
    icon = Gtk.Image.new_from_icon_name("go-previous-symbolic", Gtk.IconSize.MENU)
    go_back_button.add(icon)
    go_back_button.connect("clicked", go_back)
    hbox.pack_start(go_back_button, False, False, 10)
    return hbox

def add_page_to_stack(page_name, title):
    if not stack.get_child_by_name(page_name): 
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
            vbox.pack_start(create_top_bar(), False, False, 10)
            label = Gtk.Label(label=f"Welcome to {title} Page")
            vbox.pack_start(label, True, True, 10)
            stack.add_titled(vbox, page_name, title)

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
