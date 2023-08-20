import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
class CyberCity(Gtk.Window):
    
    def __init__(self):
        super().__init__(title="Cyber City")
        self.history_stack = []
        self.set_default_size(800, 600)
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

        ICON_WIDTH = 124
        ICON_HEIGHT = 45

        # Create a vertical box for the hamburger button and the sidebar
        self.hamburger_sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        # Create a hamburger toggle button
        self.hamburger_button = Gtk.ToggleButton()
        self.hamburger_button.set_active(False)  # Set initial state as not toggled
        self.hamburger_button.connect("toggled", self.on_hamburger_toggled)
        
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

        if section_name == "Home":
            dashboard_label = Gtk.Label()
            dashboard_label.set_markup("<span size='x-large' weight='bold'>Dashboard</span>")
            self.content_box.pack_start(dashboard_label, False, False, 10)

        elif section_name == "Cyber Tools":
            self.add_cyber_tools_content()                
        elif section_name == "Training & Learning":
            label = Gtk.Label()
            label.set_markup("<span size='x-large' weight='bold'>Training &amp; Learning</span>")
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
            vbox.set_valign(Gtk.Align.START)
            vbox.set_halign(Gtk.Align.CENTER)
            vbox.set_vexpand(False)

            vbox.pack_start(label, False, False, 10)
            hbox1 = Gtk.Box(spacing=10)
            hbox1.pack_start(self.create_content_button("Training Platforms"), True, True, 0)
            hbox1.pack_start(self.create_content_button("CTF Platforms"), True, True, 0)
            
            vbox.pack_start(hbox1, True, True, 10)
            hbox2 = Gtk.Box(spacing=10)
            hbox2.pack_start(self.create_content_button("YouTube Channels"), True, True, 0)
            hbox2.pack_start(self.create_content_button("Courses"), True, True, 0)

            vbox.pack_start(hbox2, True, True, 10)
            vbox.pack_start(self.create_content_button("Student Development Kit"), True, True, 10)
            
            self.content_box.pack_start(vbox, True, True, 0)
            self.content_box.show_all()
            
        elif section_name == "Research & Discovery":
            self.add_research_and_discovery_content()
            
        elif section_name == "Cyber Frauds":
            self.add_cyber_frauds_content()
            
        elif section_name == "Events & Entertainments":
            self.add_events_and_entertainments_content()    
            
        else:
            label = Gtk.Label(label=f"This is the {section_name} section.")
            self.content_box.pack_start(label, True, True, 0)

        self.content_box.show_all()
    #Cyber Tools content
    def add_cyber_tools_content(self):
        label = Gtk.Label()
        label.set_markup("<span size='x-large' weight='bold'>CyberTools</span>")

        # Box to hold the label and buttons, align it to the center
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_valign(Gtk.Align.START)  # Align towards the top
        vbox.set_halign(Gtk.Align.CENTER)  # Center horizontally
        vbox.set_vexpand(False)  # Don't expand vertically

        vbox.pack_start(label, False, False, 10)

        # Box to hold the first row of buttons
        hbox1 = Gtk.Box(spacing=10)
        hbox1.pack_start(self.create_content_button("Linux"), True, True, 0)
        hbox1.pack_start(self.create_content_button("WebBrowser"), True, True, 0)

        vbox.pack_start(hbox1, True, True, 10)

        # The last button for "Hardware"
        vbox.pack_start(self.create_content_button("Hardware"), True, True, 10)

        self.content_box.pack_start(vbox, True, True, 0)
        self.content_box.show_all()
    # Research section
    def add_research_and_discovery_content(self):
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
        hbox1.pack_start(self.create_content_button("Academic Journals"), True, True, 0)
        hbox1.pack_start(self.create_content_button("Whitepapers"), True, True, 0)

        vbox.pack_start(hbox1, True, True, 10)

        # Box to hold the second row of buttons
        hbox2 = Gtk.Box(spacing=10)
        hbox2.pack_start(self.create_content_button("Industry Reports"), True, True, 0)
        hbox2.pack_start(self.create_content_button("Collaborative Projects"), True, True, 0)

        vbox.pack_start(hbox2, True, True, 10)

        # Box to hold the third row of buttons
        hbox3 = Gtk.Box(spacing=10)
        hbox3.pack_start(self.create_content_button("Open Source Repositories"), True, True, 0)
        hbox3.pack_start(self.create_content_button("Latest Innovations"), True, True, 0)

        vbox.pack_start(hbox3, True, True, 10)

        # Box to hold the fourth row of buttons
        hbox4 = Gtk.Box(spacing=10)
        hbox4.pack_start(self.create_content_button("Thought Leadership"), True, True, 0)
        hbox4.pack_start(self.create_content_button("Organizations"), True, True, 0)

        vbox.pack_start(hbox4, True, True, 10)

        self.content_box.pack_start(vbox, True, True, 0)
        self.content_box.show_all()
    # Frauds section
    def add_cyber_frauds_content(self):
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
        hbox1.pack_start(self.create_content_button("Case Studies"), True, True, 0)
        hbox1.pack_start(self.create_content_button("Recent Attacks"), True, True, 0)
        hbox1.pack_start(self.create_content_button("Mitigation Techniques"), True, True, 0)
        
        vbox.pack_start(hbox1, True, True, 10)

        # Box to hold the second row of buttons
        hbox2 = Gtk.Box(spacing=10)
        hbox2.pack_start(self.create_content_button("Threat Intelligence"), True, True, 0)
        hbox2.pack_start(self.create_content_button("Digital Forensics"), True, True, 0)

        vbox.pack_start(hbox2, True, True, 10)

        self.content_box.pack_start(vbox, True, True, 0)
        self.content_box.show_all()
    #Events& entratainements section
    def add_events_and_entertainments_content(self):
        label = Gtk.Label()
        label.set_markup("<span size='x-large' weight='bold'>Events &amp; Entertainments</span>")

        # Box to hold the label and buttons, align it to the center
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_valign(Gtk.Align.START)  # Align towards the top
        vbox.set_halign(Gtk.Align.CENTER)  # Center horizontally
        vbox.set_vexpand(False)  # Don't expand vertically

        vbox.pack_start(label, False, False, 10)

        # Box to hold the first row of buttons
        hbox1 = Gtk.Box(spacing=10)
        hbox1.pack_start(self.create_content_button("Podcasts"), True, True, 0)
        hbox1.pack_start(self.create_content_button("Blogs"), True, True, 0)
        
        vbox.pack_start(hbox1, True, True, 10)

        # Box to hold the second row of buttons
        hbox2 = Gtk.Box(spacing=10)
        hbox2.pack_start(self.create_content_button("Global Events"), True, True, 0)
        hbox2.pack_start(self.create_content_button("Workshops"), True, True, 0)

        vbox.pack_start(hbox2, True, True, 10)

        # Box to hold the third row of buttons
        hbox3 = Gtk.Box(spacing=10)
        hbox3.pack_start(self.create_content_button("Webinars"), True, True, 0)
        hbox3.pack_start(self.create_content_button("Competitions"), True, True, 0)

        vbox.pack_start(hbox3, True, True, 10)

        self.content_box.pack_start(vbox, True, True, 0)
        self.content_box.show_all()

    def create_content_button(self, content_name):
        # hand cursor on content button
        button = Gtk.Button(label=content_name)
        button.connect("clicked", self.on_content_button_clicked, content_name)
        button.connect('enter-notify-event', self.on_icon_button_hover)
        button.connect('leave-notify-event', self.on_icon_button_leave)

        # Set a uniform button size
        button_width = 150
        button_height = 70
        button.set_size_request(button_width, button_height)

        # Optionally, limit the label length (if the content_name is too long)
        if len(content_name) > 20:
            button.set_label(content_name[:17] + "...")

        return button

if __name__ == "__main__":
    # Creating a style provider
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    style_context = Gtk.StyleContext()
    style_context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    # Adding CSS for the dark and light modes
    css = b"""
    .dark-mode {
        background-color: #2E2E2E;
        color: #FFF;
    }
    
    .light-mode {
        background-color: #FFF;
        color: #2E2E2E;
    }

    button {
        border: 1px solid #2E2E2E;
        border-radius: 4px;
        padding: 5px 10px;
    }

    .dark-mode button {
        background-color: #555;
        color: #FFF;
    }

    .light-mode button {
        background-color: #FFF;
        color: #2E2E2E;
    }
    """
    
    provider.load_from_data(css)

    window = CyberCity()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
