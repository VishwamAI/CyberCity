import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
from sections import home,training_and_learning, research_and_discovery, cyber_frauds, events_and_entertainments,goback
import sections.cybertools as cybertools
class CyberCity(Gtk.Window):
    
    def __init__(self):
        super().__init__(title="Cyber City")
        self.history_stack = []
        self.set_default_size(900, 700)
        self.current_mode = "light"

        # Main horizontal box for layout
        self.main_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(self.main_hbox)

        # Sidebar (left side)
        self.sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_hbox.pack_start(self.sidebar_box, False, False, 10)

        # Adding items to the sidebar
        self.add_sidebar_items()

        # Content area (center)
        self.content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_hbox.pack_end(self.content_box, True, True, 10)

        # Add home to the content area
        self.on_section_clicked(None, "Home")

        # Add theme switcher button at the bottom-left of the window
        self.add_theme_switcher()
    def set_hand_cursor_on_hover(self, button):
        """Sets the hand cursor on hover for the given button."""
        button.connect("enter-notify-event", self.on_icon_button_hover)
        button.connect("leave-notify-event", self.on_icon_button_leave)
    def add_sidebar_items(self):
        # Define sections with their names and icon paths
        sections = [
            ("Home", "img/Home.png"),
            ("Cyber Tools", "img/Tools.png"),
            ("Training & Learning", "img/book.png"),
            ("Research & Discovery", "img/Research.png"),
            ("Cyber Frauds", "img/Fruds.png"),
            ("Events & Entertainments", "img/Events.png"),
            ("Job Calendars", "img/Jobcalenders.png")
        ]

        ICON_WIDTH = 30
        ICON_HEIGHT = 30
        BUTTON_WIDTH = 40  # This will define the width of the button

        # Create a vertical box for the hamburger button and the sidebar
        self.hamburger_sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        # Create a hamburger toggle button
        self.hamburger_button = Gtk.ToggleButton()
        self.hamburger_button.set_active(False)  # Set initial state as not toggled
        self.hamburger_button.connect("toggled", self.on_hamburger_toggled)
        self.hamburger_button.set_margin_top(10)  # Add 10 pixels of space at the top
                
        # Pack the hamburger button into the hamburger_sidebar_box
        self.hamburger_sidebar_box.pack_start(self.hamburger_button, False, False, 0)

        # Create a VBox to hold the sidebar items
        self.hamburger_sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        # Now that self.hamburger_sidebar is defined, you can call the method
        self._update_hamburger_icon()

        # Add the sidebar to the hamburger_sidebar_box after the button
        self.hamburger_sidebar_box.pack_start(self.hamburger_sidebar, False, False, 0)

        # Make sure the sidebar is initially hidden
        self.hamburger_sidebar.hide()
        # Iterate over sections to add each to the sidebar with its icon
        for section, icon_path in sections:
            icon_button = Gtk.Button()
            # Set the width of the button using CSS
            icon_button.get_style_context().add_class("icon-button")
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(icon_path, ICON_WIDTH, ICON_HEIGHT)
            icon = Gtk.Image.new_from_pixbuf(pixbuf)
            

            icon_button.add(icon)
            icon_button.connect("clicked", self.on_section_clicked, section)
            icon_button.set_tooltip_text(f"{section}")
            icon_button.set_relief(Gtk.ReliefStyle.NONE)  # Remove the default button border
            icon_button.set_focus_on_click(False)  # To prevent focus styling on click

            # Cursor changes
            icon_button.connect("enter-notify-event", self.on_icon_button_hover)
            icon_button.connect("leave-notify-event", self.on_icon_button_leave)
            
            # Setting cursor for the hamburger button
            self.hamburger_button.connect("enter-notify-event", self.on_icon_button_hover)
            self.hamburger_button.connect("leave-notify-event", self.on_icon_button_leave)

            self.hamburger_sidebar.pack_start(icon_button, False, False, 0)
        
        # Add the hamburger_sidebar_box to the main sidebar_box
        self.sidebar_box.pack_start(self.hamburger_sidebar_box, False, False, 0)

        # Hide the sidebar initially
        self.hamburger_sidebar.hide()

        # Update the initial icon of the hamburger button
        self._update_hamburger_icon()

    def _update_hamburger_icon(self):
        """Update the hamburger icon based on the visibility of the sidebar."""
        if self.hamburger_sidebar.get_visible():
            self.hamburger_button.set_label("✖")  # Set to a close icon if sidebar is visible
        else:
            self.hamburger_button.set_label("☰")  # Set to the hamburger icon if sidebar is hidden

    def on_hamburger_toggled(self, button):
        if button.get_active():
            self.hamburger_sidebar.show()
        else:
            self.hamburger_sidebar.hide()
        # Update the icon whenever the toggle state changes
        self._update_hamburger_icon()

    def on_button_hover(self, widget, event):
        # Change the cursor to a hand pointer when hovering over the widget
        display = widget.get_display()
        hand_cursor = Gdk.Cursor.new_for_display(display, Gdk.CursorType.HAND1)
        widget.get_window().set_cursor(hand_cursor)

    def on_button_leave(self, widget, event):
        # Reset the cursor when not hovering over the widget
        widget.get_window().set_cursor(None)

    def on_icon_button_hover(self, button, event):
        # Change cursor to hand pointer when hovering over a button
        display = button.get_display()
        hand_pointer = Gdk.Cursor.new_for_display(display, Gdk.CursorType.HAND2)
        window = button.get_window()
        window.set_cursor(hand_pointer)

    def on_icon_button_leave(self, button, event):
        # Revert to default cursor when mouse leaves the button
        display = button.get_display()
        default_cursor = Gdk.Cursor.new_for_display(display, Gdk.CursorType.ARROW)
        window = button.get_window()
        window.set_cursor(default_cursor)

    def create_button(self, label, callback=None, *callback_args):
        # Create a generic button with optional callback
        button = Gtk.Button(label=label)
        if callback:
            button.connect("clicked", callback, *callback_args)
            button.connect('enter-notify-event', self.on_icon_button_hover)
            button.connect('leave-notify-event', self.on_icon_button_leave)
        return button

    def add_theme_switcher(self):
        # Add a button to the sidebar to switch between light and dark modes
        switch_button = Gtk.Button(label="Switch Mode")
        switch_button.connect("clicked", self.toggle_mode)

        # Add hand cursor on hover to the switch button
        self.set_hand_cursor_on_hover(switch_button)

        self.sidebar_box.pack_end(switch_button, False, False, 5)  # Added to sidebar_box

    def toggle_mode(self, widget):
        # Toggle the theme mode based on current mode
        if self.current_mode == "light":
            self.set_dark_mode()
            self.current_mode = "dark"
        else:
            self.set_light_mode()
            self.current_mode = "light"

    def set_light_mode(self):
        # Adjust the UI to light mode theme
        style_context = self.get_style_context()
        style_context.remove_class('dark-mode')
        style_context.add_class('light-mode')

    def set_dark_mode(self):
        # Adjust the UI to dark mode theme
        style_context = self.get_style_context()
        style_context.remove_class('light-mode')
        style_context.add_class('dark-mode')

    def clear_content_box(self):
        # Clear all widgets from the content box
        for widget in self.content_box.get_children():
            self.content_box.remove(widget)
    
    def on_content_button_clicked(self, button, content_name):
        # Handle the event when a content button is clicked     
        self.clear_content_box()
        label = Gtk.Label(label=f"This is the {content_name} section.")
        self.content_box.pack_start(label, True, True, 0)
        self.content_box.show_all()
    
    def on_section_clicked(self, button, section_name):
        self.clear_content_box()

        # Define content functions
        content_functions = {
            "Home": home.add_home_content,
            "Cyber Tools": cybertools.add_cybertools_content,
            "Training & Learning": training_and_learning.add_training_and_learning_content,
            "Research & Discovery": research_and_discovery.add_research_and_discovery_content,
            "Cyber Frauds": cyber_frauds.add_cyber_frauds_content,
            "Events & Entertainments": events_and_entertainments.add_events_and_entertainments_content
        }
        # If the section_name exists in content_functions, then execute its content
        if section_name in content_functions:
            content_function = content_functions[section_name]
            content_function(self.content_box)  # Call the content function with the content box
            
        else:
            label = Gtk.Label(label=f"This is the {section_name} section.")
            self.content_box.pack_start(label, True, True, 0)

        self.content_box.show_all()
    

if __name__ == "__main__":
    # Load CSS
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    style_context = Gtk.StyleContext()
    style_context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    with open("styles/dark_light.css", "rb") as f:
        css = f.read()
        provider.load_from_data(css)

    window = CyberCity()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()