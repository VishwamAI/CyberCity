import gi
import webbrowser

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HardwareToolsPage(Gtk.Box):
    
    def __init__(self):
        super().__init__()
        
        # Add a back button to the top
        go_back_button = self.create_go_back_button()
        self.pack_start(go_back_button, False, False, 0)

        # Create a list of hardware tools and their URLs
        hardware_tools = [
            ("Hak5", "https://hak5.org/"),
            ("Pine64", "https://www.pine64.org/"),
            ("Raspberry Pi", "https://www.raspberrypi.org/"),
            ("Pwnie Express", "https://www.pwnieexpress.com/"),
            ("Think Penguin", "https://www.thinkpenguin.com/"),
            ("SparkFun Electronics", "https://www.sparkfun.com/"),
            ("Arduino", "https://www.arduino.cc/"),
            ("BeagleBoard", "https://beagleboard.org/")
        ]

        # Create a button for each hardware tool
        for label, url in hardware_tools:
            button = Gtk.Button(label=label)
            button.connect("clicked", self.open_website, url)
            self.pack_start(button, False, False, 0)

    def create_go_back_button(self):
        go_back_button = Gtk.Button()
        
        # Create the icon and add it to the button
        icon = Gtk.Image.new_from_icon_name("go-previous-symbolic", Gtk.IconSize.MENU)  # Use MENU size
        go_back_button.add(icon)
        
        # Connect the button's "clicked" signal to the go_back method
        go_back_button.connect("clicked", self.go_back)
        
        # Style the button
        go_back_button.get_style_context().add_class('go-back-button')
        
        # Align the button to the start horizontally and set it to the start vertically.
        go_back_button.set_halign(Gtk.Align.START)
        go_back_button.set_valign(Gtk.Align.START)
        
        # Set margin to create padding around the button.
        go_back_button.set_margin_start(20)
        go_back_button.set_margin_top(20)
        
        return go_back_button

    def go_back(self, button):
        main_window = self.get_root()
        # Assuming the main window has navigation_history and stack as attributes.
        last_visited_page = main_window.navigation_history.pop() if hasattr(main_window, 'navigation_history') and main_window.navigation_history else "Main Page"
        main_window.stack.set_visible_child_name(last_visited_page)

    def open_website(self, button, url):
        webbrowser.open(url)
