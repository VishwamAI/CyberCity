import gi
import subprocess
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GdkPixbuf, Gdk, GLib, Gio
from Page import Page
import webbrowser

class MaltegoPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)
        grid = Gtk.Grid()
        grid.set_row_spacing(10)
        grid.set_column_spacing(10)
        grid.set_halign(Gtk.Align.CENTER)
        self.append(grid)
        css_provider = Gtk.CssProvider()

        try:
            css_provider.load_from_path('style.css')
            Gtk.StyleContext.add_provider_for_display(
                Gdk.Display.get_default(),
                css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )
        except GLib.Error as e:
            print(f"Failed to load CSS: {e}")

        try:
            logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('img/maltego.png', 300, 300, True)
        except Exception as e:
            print(f"Failed to load image: {e}")
            theme = Gtk.IconTheme.get_for_display(Gdk.Display.get_default())
            logo_pixbuf = theme.load_icon("image-missing", 300, 0)
        logo = Gtk.Image.new_from_pixbuf(logo_pixbuf)
        grid.attach(logo, 0, 0, 1, 1)

        title = Gtk.Label()
        title.set_markup('<span size="xx-large">Maltego</span>')
        grid.attach(title, 1, 0, 1, 1)

        description = Gtk.Label()
        description.set_wrap(True)
        description.set_width_chars(40)
        description.set_markup('Maltego is a visual link analysis tool that comes with a standard set of data connectors.')
        
        expander = Gtk.Expander(label="Description")
        expander.set_child(description)
        grid.attach(expander, 1, 1, 2, 1)

        license = Gtk.Label()
        license.set_markup('License: Commercial and CE version')
        grid.attach(license, 0, 2, 1, 1)

        link = Gtk.Label()
        link.set_markup('<a href="https://www.paterva.com/">Project Homepage</a>')
        link.set_use_markup(True)
        grid.attach(link, 1, 2, 1, 1)

        # Button for installation or uninstallation of Maltego
        self.install_uninstall_button = Gtk.Button()
        self.install_uninstall_button.set_child(Gtk.Image.new_from_file('path/to/install/icon.png'))
        grid.attach(self.install_uninstall_button, 0, 3, 3, 1)

        # Add a new grid to segregate functionalities in a more organized way
        button_grid = Gtk.Grid()
        button_grid.set_row_spacing(10)
        button_grid.set_column_spacing(10)
        button_grid.set_halign(Gtk.Align.CENTER)
        grid.attach(button_grid, 0, 4, 3, 1)

        # Button for user manual
        user_manual_button = Gtk.Button()
        user_manual_button.set_child(Gtk.Image.new_from_file('img/github.png'))
        user_manual_button.connect("clicked", self.user_manual)
        button_grid.attach(user_manual_button, 0, 0, 1, 1)

        # Button for sharing the snap
        share_icon = Gtk.Image.new_from_file('img/kalilogo.png')
        share_btn = Gtk.Button()
        share_btn.set_child(share_icon)
        share_btn.connect("clicked", self.share_snap)
        button_grid.attach(share_btn, 1, 0, 1, 1)

        # Button for about Maltego, now at the bottom
        about_button = Gtk.Button()
        about_button.set_child(Gtk.Image.new_from_file('img/maltego.jpg'))
        about_button.connect("clicked", self.about)
        button_grid.attach(about_button, 2, 0, 1, 1)

        self._install_handler_id = None
        self._uninstall_handler_id = None

        self.check_maltego_installed()

    def check_maltego_installed(self):
        try:
            output = subprocess.check_output(['which', 'maltego'], stderr=subprocess.STDOUT)
            if 'maltego' in output.decode():
                self.install_uninstall_button.set_label("Uninstall")
                if self._install_handler_id is not None:
                    self.install_uninstall_button.disconnect(self._install_handler_id)
                self._uninstall_handler_id = self.install_uninstall_button.connect("clicked", self.uninstall_maltego)
            else:
                self.install_uninstall_button.set_label("Install")
                if self._uninstall_handler_id is not None:
                    self.install_uninstall_button.disconnect(self._uninstall_handler_id)
                self._install_handler_id = self.install_uninstall_button.connect("clicked", self.install_maltego)
        except subprocess.CalledProcessError:
            self.install_uninstall_button.set_label("Install")
            if self._uninstall_handler_id is not None:
                self.install_uninstall_button.disconnect(self._uninstall_handler_id)
            self._install_handler_id = self.install_uninstall_button.connect("clicked", self.install_maltego)

    def install_maltego(self, button):
        subprocess.run(['sudo', 'apt', 'install', '-y', 'maltego'])

    def uninstall_maltego(self, button):
        subprocess.run(['sudo', 'apt', 'remove', '-y', 'maltego'])

    def share_snap(self, button):
        webbrowser.open('https://www.paterva.com/web7/downloads.php')

    def user_manual(self, button):
        webbrowser.open('https://www.paterva.com/web7/community/community.php')

    def about(self, button):
        webbrowser.open('https://www.paterva.com/web7/meet-maltego/maltego.php')
