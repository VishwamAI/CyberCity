import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, Gdk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menu = Gio.Menu.new()
        # Encryption and decryption submenu
        encryption_decryption_menu = Gio.Menu.new()
        menu.append_submenu("Encryption & Decryption", encryption_decryption_menu)

        # Create the submenu actions for Encryption & Decryption
        cyberchef_action = Gio.MenuItem.new("Cyber Chef", "win.cyberchef")
        rot13_action = Gio.MenuItem.new("Rot13", "win.rot13")
        decode_action = Gio.MenuItem.new("Decode", "win.decode")
        encode_action = Gio.MenuItem.new("Encode-Decode", "win.encode")
        encryption_decryption_menu.append_item(cyberchef_action)
        encryption_decryption_menu.append_item(rot13_action)
        encryption_decryption_menu.append_item(decode_action)
        encryption_decryption_menu.append_item(encode_action)
        
        #End of Encryption and decryption submenu
        #Web tools submenu
        web_tools_menu = Gio.Menu.new()
        menu.append_submenu("Web Tools", web_tools_menu)
        
        #Create the submenu actions for Web Tools
        urlscan_action = Gio.MenuItem.new("Urlscan.io", "win.urlscan")
        vulnhub_action = Gio.MenuItem.new("Vulnhub", "win.vulnhub")
        opswat_action = Gio.MenuItem.new("OPSWAT", "win.opswat")
        Lobas_action = Gio.MenuItem.new("Lobas", "win.lobas")
        web_tools_menu.append_item(urlscan_action)
        web_tools_menu.append_item(vulnhub_action)
        web_tools_menu.append_item(opswat_action)
        web_tools_menu.append_item(Lobas_action)
        #End of Web tools submenu
        
        #software submenu
        software_menu = Gio.Menu.new()
        menu.append_submenu("Software", software_menu)
        
        #Create the submenu actions for Software
        benmap_action = Gio.MenuItem.new("Benmap", "win.benmap")
        Hellosploit_action = Gio.MenuItem.new("Hellosploit", "win.Hellosploit")
        cydra_action = Gio.MenuItem.new("Cydra", "win.cydra")
        Brupsuite_action = Gio.MenuItem.new("Brupsuite", "win.Brupsuite")
        software_menu.append_item(benmap_action)
        software_menu.append_item(Hellosploit_action)
        software_menu.append_item(cydra_action)
        software_menu.append_item(Brupsuite_action)
        #End of software submenu
        
        #create the submenu actions for Hardware
        hardware_menu = Gio.Menu.new()
        menu.append_submenu("Hardware", hardware_menu)
        
        #Create the submenu actions for Hardware
        Hak5_action = Gio.MenuItem.new("Hak5", "win.Hak5")
        pine64_action = Gio.MenuItem.new("Pine64", "win.pine64")
        hardware_menu.append_item(Hak5_action)
        hardware_menu.append_item(pine64_action)
        #End of Hardware submenu
        
        #create the submenu actions for Training platoforms
        training_menu = Gio.Menu.new()
        menu.append_submenu("Training Platforms", training_menu)
        
        #Create the submenu actions for Training Platforms
        tryhackme_action = Gio.MenuItem.new("Tryhackme", "win.tryhackme")
        hackthebox_action = Gio.MenuItem.new("Hackthebox", "win.hackthebox")
        training_menu.append_item(tryhackme_action)
        training_menu.append_item(hackthebox_action)
        #End of Training Platforms submenu
        
        #create the submenu actions for CTF platforms
        ctf_menu = Gio.Menu.new()
        menu.append_submenu("CTF Platforms", ctf_menu)
        
        #Create the submenu actions for CTF Platforms
        picoctf_action = Gio.MenuItem.new("PicoCTF", "win.picoctf")
        ctfwithgoogle_action = Gio.MenuItem.new("CTF with Google", "win.ctfwithgoogle")
        ctf_menu.append_item(picoctf_action)
        ctf_menu.append_item(ctfwithgoogle_action)
        #End of CTF Platforms submenu
        
        
        # Create the SimpleAction objects and connect them to the functions
        self.cyberchef_action = Gio.SimpleAction.new("cyberchef", None)
        self.cyberchef_action.connect("activate", self.cyberchef)
        self.add_action(self.cyberchef_action)

        self.rot13_action = Gio.SimpleAction.new("rot13", None)
        self.rot13_action.connect("activate", self.Rot13)
        self.add_action(self.rot13_action)

        self.decode_action = Gio.SimpleAction.new("decode", None)
        self.decode_action.connect("activate", self.decode)
        self.add_action(self.decode_action)

        self.encode_action = Gio.SimpleAction.new("encode", None)
        self.encode_action.connect("activate", self.encode)
        self.add_action(self.encode_action)
        
        #Create the SimpleAction objects and connect them to the functions
        self.urlscan_action = Gio.SimpleAction.new("urlscan", None)
        self.urlscan_action.connect("activate", self.urlscan)
        self.add_action(self.urlscan_action)
        
        self.vulnhub_action = Gio.SimpleAction.new("vulnhub", None)
        self.vulnhub_action.connect("activate", self.vulnhub)
        self.add_action(self.vulnhub_action)
        
        self.opswat_action = Gio.SimpleAction.new("opswat", None)
        self.opswat_action.connect("activate", self.opswat)
        self.add_action(self.opswat_action)
        
        self.Lobas_action = Gio.SimpleAction.new("lobas", None)
        self.Lobas_action.connect("activate", self.lobas)
        self.add_action(self.Lobas_action)
        #End of Web tools submenu
        #Create the SimpleAction objects and connect them to the functions
        self.benmap_action = Gio.SimpleAction.new("benmap", None)
        self.benmap_action.connect("activate", self.benmap)
        self.add_action(self.benmap_action)
        
        self.Hellosploit_action = Gio.SimpleAction.new("Hellosploit", None)
        self.Hellosploit_action.connect("activate", self.Hellosploit)
        self.add_action(self.Hellosploit_action)
        
        self.cydra_action = Gio.SimpleAction.new("cydra", None)
        self.cydra_action.connect("activate", self.cydra)
        self.add_action(self.cydra_action)
        
        self.Brupsuite_action = Gio.SimpleAction.new("Brupsuite", None)
        self.Brupsuite_action.connect("activate", self.Brupsuite)
        self.add_action(self.Brupsuite_action)
        #End of software submenu
        #Create the SimpleAction objects and connect them to the functions
        self.Hak5_action = Gio.SimpleAction.new("Hak5", None)
        self.Hak5_action.connect("activate", self.Hak5)
        self.add_action(self.Hak5_action)
        
        self.pine64_action = Gio.SimpleAction.new("pine64", None)
        self.pine64_action.connect("activate", self.pine64)
        self.add_action(self.pine64_action)
        #End of Hardware submenu
        #Create the SimpleAction objects and connect them to the functions
        self.tryhackme_action = Gio.SimpleAction.new("tryhackme", None)
        self.tryhackme_action.connect("activate", self.tryhackme)
        self.add_action(self.tryhackme_action)
        
        self.hackthebox_action = Gio.SimpleAction.new("hackthebox", None)
        self.hackthebox_action.connect("activate", self.hackthebox)
        self.add_action(self.hackthebox_action)
        #End of Training Platforms submenu
        #Create the SimpleAction objects and connect them to the functions
        self.picoctf_action = Gio.SimpleAction.new("picoctf", None)
        self.picoctf_action.connect("activate", self.picoctf)
        self.add_action(self.picoctf_action)
        
        self.ctfwithgoogle_action = Gio.SimpleAction.new("ctfwithgoogle", None)
        self.ctfwithgoogle_action.connect("activate", self.ctfwithgoogle)
        self.add_action(self.ctfwithgoogle_action)
        #End of CTF Platforms submenu

        # Load CSS file
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('style.css')

        # Apply CSS to window
        display = Gdk.Display.get_default()
        self.add_css_class("background")
        Gtk.StyleContext.add_provider_for_display(display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)
        self.header = Gtk.HeaderBar()  # Move this line up
        self.set_titlebar(self.header)
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")
        self.header.pack_start(self.hamburger)  # Move this line down
        
   # Define the functions for encryption submenu action
    def cyberchef(self, action, param):
        print("cyberchef selected")

    def Rot13(self, action, param):
        print("Rot13 selected")

    def decode(self, action, param):
        print("decode selected")

    def encode(self, action, param):
        print("encode selected")
    # End of encryption submenu action
    
    # Define the functions for web tools submenu action
    def urlscan(self, action, param):
        print("urlscan selected")
    def vulnhub(self, action, param):
        print("vulnhub selected")
    def opswat(self, action, param):
        print("opswat selected")
    def lobas(self, action, param):
        print("lobas selected")
    # End of web tools submenu action
    # Define the functions for software submenu action
    def benmap(self, action, param):
        print("benmap selected")
    def Hellosploit(self, action, param):
        print("Hellosploit selected")
    def cydra(self, action, param):
        print("cydra selected")
    def Brupsuite(self, action, param):
        print("Brupsuite selected")
    # End of software submenu action
    # Define the functions for hardware submenu action
    def Hak5(self, action, param):
        print("Hak5 selected")
    def pine64(self, action, param):
        print("pine64 selected")
    # End of hardware submenu action
    # Define the functions for training platforms submenu action
    def tryhackme(self, action, param):
        print("tryhackme selected")
    def hackthebox(self, action, param):
        print("hackthebox selected")
    # End of training platforms submenu action
    # Define the functions for CTF platforms submenu action
    def picoctf(self, action, param):
        print("picoctf selected")
    def ctfwithgoogle(self, action, param):
        print("ctfwithgoogle selected")
    # End of CTF platforms submenu action
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