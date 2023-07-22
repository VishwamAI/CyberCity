import gi
import subprocess
import urllib.request
from io import BytesIO
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GdkPixbuf, Gdk,GLib, Gio
from Page import Page
import webbrowser
class AmassPage(Page):
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
            logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('img/amasslogo.png', 300, 300, True)
        except Exception as e:
            print(f"Failed to load image: {e}")
            theme = Gtk.IconTheme.get_for_display(Gdk.Display.get_default())
            logo_pixbuf = theme.load_icon("image-missing", 300, 0)
        logo = Gtk.Image.new_from_pixbuf(logo_pixbuf)
        grid.attach(logo, 0, 0, 1, 1)

        title = Gtk.Label()
        title.set_markup('<span size="xx-large">Amass</span>')
        grid.attach(title, 1, 0, 1, 1)

        description = Gtk.Label()
        description.set_wrap(True)
        description.set_width_chars(40)
        description.set_markup('Amass is a powerful cybersecurity tool used for network mapping and assets discovery.')
        
        expander = Gtk.Expander(label="Description")
        expander.set_child(description)
        grid.attach(expander, 1, 1, 2, 1)

        license = Gtk.Label()
        license.set_markup('License: GPL-3.0+')
        grid.attach(license, 0, 2, 1, 1)

        link = Gtk.Label()
        link.set_markup('<a href="https://github.com/OWASP/Amass">Project Homepage</a>')
        link.set_use_markup(True)
        grid.attach(link, 1, 2, 1, 1)

        image_upload_button = Gtk.Button(label="Upload Image")
        image_upload_button.connect("clicked", self.on_image_upload_clicked)
        grid.attach(image_upload_button, 0, 3, 1, 1)

        url_entry = Gtk.Entry()
        url_entry.set_placeholder_text("Enter Image URL")
        grid.attach(url_entry, 0, 4, 1, 1)

        url_button = Gtk.Button(label="Load Image from URL")
        url_button.connect("clicked", self.load_image_from_url, url_entry)
        grid.attach(url_button, 1, 4, 1, 1)

        self.install_uninstall_button = Gtk.Button()
        grid.attach(self.install_uninstall_button, 1, 3, 1, 1)

        share_btn = Gtk.Button(label="Share snap")
        share_btn.connect("clicked", self.share_snap)
        grid.attach(share_btn, 0, 5, 3, 1)

        self._install_handler_id = None
        self._uninstall_handler_id = None

        self.check_amass_installed()

    def check_amass_installed(self):
        try:
            output = subprocess.check_output(['which', 'amass'])
            if 'amass' in output.decode():
                self.install_uninstall_button.set_label("Uninstall")
                if self._install_handler_id is not None:
                    self.install_uninstall_button.disconnect(self._install_handler_id)
                self._uninstall_handler_id = self.install_uninstall_button.connect("clicked", self.uninstall_amass)
            else:
                self.install_uninstall_button.set_label("Install")
                if self._uninstall_handler_id is not None:
                    self.install_uninstall_button.disconnect(self._uninstall_handler_id)
                self._install_handler_id = self.install_uninstall_button.connect("clicked", self.install_amass)
        except subprocess.CalledProcessError:
            print("Failed to check if Amass is installed.")
    # rest of your code...

    def on_image_upload_clicked(self, button):
        dialog = Gtk.FileChooserDialog()
        dialog.set_title("Please choose an image")
        dialog.set_transient_for(self.get_root())
        dialog.set_action(Gtk.FileChooserAction.OPEN)
        dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        dialog.add_button("Open", Gtk.ResponseType.OK)

        filter_png = Gtk.FileFilter()
        filter_png.set_name("PNG files")
        filter_png.add_mime_type("image/png")
        dialog.add_filter(filter_png)

        filter_jpeg = Gtk.FileFilter()
        filter_jpeg.set_name("JPEG files")
        filter_jpeg.add_mime_type("image/jpeg")
        dialog.add_filter(filter_jpeg)

        dialog.connect("response", self.on_dialog_response)
        dialog.show()

    def on_dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            file_path = dialog.get_filename()
            try:
                logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(file_path, 300, 300, True)
            except GLib.Error as e:
                print(f"Failed to load image: {e}")
                theme = Gtk.IconTheme.get_for_display(Gdk.Display.get_default())
                logo_pixbuf = theme.load_icon("image-missing", 300, 0)

            logo = Gtk.Image.new_from_pixbuf(logo_pixbuf)
            self.grid.attach(logo, 2, 0, 1, 1)
            self.show_all()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

    def load_image_from_url(self, button, entry):
        url = entry.get_text()
        try:
            response = urllib.request.urlopen(url)
            input_stream = Gio.MemoryInputStream.new_from_data(response.read(), None)
            logo_pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(input_stream, 300, 300, True, None)
        except Exception as e:
            print(f"Failed to load image from URL: {e}")
            theme = Gtk.IconTheme.get_for_display(Gdk.Display.get_default())
            logo_pixbuf = theme.load_icon("image-missing", 300, 0)

        logo = Gtk.Image.new_from_pixbuf(logo_pixbuf)
        self.grid.attach(logo, 2, 0, 1, 1)
        self.show_all()

    def install_amass(self, button):
        try:
            dialog = Gtk.MessageDialog(
                transient_for=self.get_root(),
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text="Installing...",
            )
            dialog.run()
            dialog.destroy()
            subprocess.run(['pkexec', 'snap', 'install', 'amass'], check=True)
            self.install_uninstall_button.set_label("Uninstall")
            self.install_uninstall_button.disconnect_by_func(self.install_amass)
            self.install_uninstall_button.connect("clicked", self.uninstall_amass)
        except subprocess.CalledProcessError:
            print("Failed to install Amass.")

    def uninstall_amass(self, button):
        try:
            dialog = Gtk.MessageDialog(
                transient_for=self.get_root(),
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text="Uninstalling...",
            )
            dialog.run()
            dialog.destroy()
            subprocess.run(['pkexec', 'snap', 'remove', 'amass'], check=True)
            self.install_uninstall_button.set_label("Install")
            self.install_uninstall_button.disconnect_by_func(self.uninstall_amass)
            self.install_uninstall_button.connect("clicked", self.install_amass)
        except subprocess.CalledProcessError:
            print("Failed to uninstall Amass.")

    def on_image_upload_clicked(self, button):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", 
            parent=self.get_toplevel(), 
            action=Gtk.FileChooserAction.OPEN,
            buttons=(
                Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, 
                Gtk.STOCK_OPEN, Gtk.ResponseType.OK
            )
        )

        img_filter = Gtk.FileFilter()
        img_filter.set_name("Images")
        img_filter.add_mime_type("image/*")
        dialog.add_filter(img_filter)

        video_filter = Gtk.FileFilter()
        video_filter.set_name("Videos")
        video_filter.add_mime_type("video/*")
        dialog.add_filter(video_filter)

        link_filter = Gtk.FileFilter()
        link_filter.set_name("Web Links")
        link_filter.add_pattern("*.html")  # You might want to refine this pattern
        dialog.add_filter(link_filter)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print(f"File selected: {dialog.get_filename()}")

        dialog.destroy()

    def share_snap(self, button):
        webbrowser.open("https://snapcraft.io/amass", new=2)