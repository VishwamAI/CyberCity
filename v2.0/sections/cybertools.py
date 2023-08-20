import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
stack = Gtk.Stack()
navigation_history = []

def create_content_button(content_name, callback=None):
    button = Gtk.Button(label=content_name)
    if callback:
        button.connect("clicked", callback)
    return button

def create_top_bar():
    hbox = Gtk.Box(spacing=10)
    hbox.pack_start(create_go_back_button(), False, False, 10)
    # Placeholder for a hamburger menu, replace this with actual functionality if needed
    return hbox

def create_go_back_button():
    go_back_button = Gtk.Button()
    icon = Gtk.Image.new_from_icon_name("go-previous-symbolic", Gtk.IconSize.MENU)
    go_back_button.add(icon)
    go_back_button.connect("clicked", go_back)
    return go_back_button

def go_back(button):
    last_visited_page = navigation_history.pop() if navigation_history else "cybertools_main"
    stack.set_visible_child_name(last_visited_page)

def navigate_to_page(button, page_name):
    navigation_history.append(stack.get_visible_child_name())
    stack.set_visible_child_name(page_name)

def add_page_to_stack(page_name, title):
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.pack_start(create_top_bar(), False, False, 10)  # Add the top bar with go back button and hamburger menu
    label = Gtk.Label(label=f"Welcome to {title} Page")
    vbox.pack_start(label, True, True, 10)
    stack.add_titled(vbox, page_name, title)


def add_cybertools_content(content_box, section_name="Cyber Tools"):
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)
    vbox.set_halign(Gtk.Align.CENTER)
    
    label = Gtk.Label()
    label.set_markup(f"<span size='x-large' weight='bold'>{section_name}</span>")
    vbox.pack_start(label, False, False, 10)

    hbox_top = Gtk.Box(spacing=10)
    hbox_top.pack_start(create_content_button("Linux", lambda button: navigate_to_page(button, "linux")), True, True, 0)
    hbox_top.pack_start(create_content_button("WebBrowser", lambda button: navigate_to_page(button, "webbrowser")), True, True, 0)
    vbox.pack_start(hbox_top, True, True, 10)

    hardware_button = create_content_button("Hardware Tools", lambda button: navigate_to_page(button, "hardwaretools"))
    vbox.pack_start(hardware_button, True, True, 10)

    stack.add_titled(vbox, "cybertools_main", "Cyber Tools")
    content_box.pack_start(stack, True, True, 0)

    # Add pages for Linux, WebBrowser, and Hardware Tools
    add_page_to_stack("linux", "Linux")
    add_page_to_stack("webbrowser", "Web Browser")
    add_page_to_stack("hardwaretools", "Hardware Tools")
    
    content_box.show_all()
    stack.set_visible_child_name("cybertools_main")

def main():
    window = Gtk.Window(title="CyberCity")
    content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    window.add(content_box)

    add_cybertools_content(content_box)
    
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
