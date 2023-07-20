from gi.repository import Gtk

class Page(Gtk.Box):
    def __init__(self, back_label):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        go_back_button = Gtk.Button()
        icon = Gtk.Image.new_from_icon_name("go-previous-symbolic")
        go_back_button.set_child(icon)
        go_back_button.connect("clicked", self.go_back)

        self.append(go_back_button)

        # Align the button to the start horizontally and set it to the start vertically.
        go_back_button.set_halign(Gtk.Align.START)
        go_back_button.set_valign(Gtk.Align.START)

        # Set margin to create padding around the button.
        go_back_button.set_margin_start(20)
        go_back_button.set_margin_top(20)

    def go_back(self, button):
        main_window = self.get_root()
        # Get the last visited page from the navigation history.
        last_visited_page = main_window.navigation_history.pop() if main_window.navigation_history else "Main Page"
        # Switch to the last visited page without re-adding it to the GtkStack.
        main_window.current_page = last_visited_page
        main_window.stack.set_visible_child_name(last_visited_page)
