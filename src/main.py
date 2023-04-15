import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio
        
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        action = Gio.SimpleAction.new("something", None)
        action.connect("activate", self.print_something)
        menu = Gio.Menu.new()
        # Encryption and decryption submenu
        encryption_submenu = Gio.Menu.new()
        encryption_submenu.append("CyberChef", "app.cyberchef")
        encryption_submenu.append("Rot13", "app.Rot13")
        encryption_submenu.append("Decode", "app.Decode")
        encryption_submenu.append("Encode-Decode", "app.Encode-Decode")
        menu.append_submenu("Encryption&decryption", encryption_submenu)

        # Webtools submenu
        webtools_submenu = Gio.Menu.new()
        webtools_submenu.append("Urlscan.io", "app.urlscan.io")
        webtools_submenu.append("VulnHub", "app.VulnHub")
        webtools_submenu.append("Opswat", "app.Opswat")
        webtools_submenu.append("Lobas", "Lobas")
        menu.append_submenu("Webtools", webtools_submenu)

        # Software tools submenu
        software_submenu = Gio.Menu.new()
        software_submenu.append("Nmap", "app.Nmap")
        software_submenu.append("Metasploit", "app.Metasploit")
        software_submenu.append("BrupSuite", "app.Brupsuite")
        software_submenu.append("Hydra", "app.Hydra")
        menu.append_submenu("Software tools", software_submenu)

        # Hardware tools submenu
        hardware_submenu = Gio.Menu.new()
        hardware_submenu.append("Hak5", "app.Hak5")
        hardware_submenu.append("Pine64", "app.Pine64")
        menu.append_submenu("Hardware tools", hardware_submenu)

        # Training platforms submenu
        training_submenu = Gio.Menu.new()
        training_submenu.append("TryHackMe", "app.TryHackMe")
        training_submenu.append("HackTheBox", "app.HackTheBox")
        menu.append_submenu("Training platforms", training_submenu)

        # CTF platforms submenu
        CTF_platforms_submenu = Gio.Menu.new()
        CTF_platforms_submenu.append("PicoCTF", "app.picoCTF")
        CTF_platforms_submenu.append("CTFWithGoogle", "app.GoogleCTF")
        menu.append_submenu("CTF Platforms", CTF_platforms_submenu)

        
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)
        self.header = Gtk.HeaderBar()  # Move this line up
        self.set_titlebar(self.header)
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")
        self.header.pack_start(self.hamburger)  # Move this line down
        self.add_action(action)

    def print_something(self, action, param):
        print("something!")
class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)
        
    def on_activate(self, app):
        self.win = MainWindow(application=app,title="Penetration App")
        self.win.present()
       
if __name__ == "__main__":
    app = MyApp(application_id='org.example.GtkApplication')
    app.run(sys.argv)