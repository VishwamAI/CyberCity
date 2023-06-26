#!/usr/bin/env python3
import sys
import os
import gi
import webbrowser
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk,Gio, Gdk, Notify
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
        exploitdb_action = Gio.MenuItem.new("ExploitDB", "win.exploitdb")
        web_tools_menu.append_item(urlscan_action)
        web_tools_menu.append_item(vulnhub_action)
        web_tools_menu.append_item(opswat_action)
        web_tools_menu.append_item(exploitdb_action)
        #End of Web tools submenu
        
        #software submenu
        software_menu = Gio.Menu.new()
        menu.append_submenu("Software Tools", software_menu)
        #software submenus some 
        informationgathering_submenu = Gio.Menu.new()
        vulnerabilityanalysis_submenu = Gio.Menu.new()
        webapplictionanalysis_submenu = Gio.Menu.new()
        passwordattacks_submenu = Gio.Menu.new()
        wirelessattacks_submenu = Gio.Menu.new()
        databaseassessment_submenu = Gio.Menu.new()
        reverseengineering_submenu = Gio.Menu.new()

        software_menu.append_submenu("Information Gathering", informationgathering_submenu)
        software_menu.append_submenu("Vulnerability Analysis", vulnerabilityanalysis_submenu)
        software_menu.append_submenu("Web Application Analysis", webapplictionanalysis_submenu)
        software_menu.append_submenu("Password Attacks", passwordattacks_submenu)
        software_menu.append_submenu("Wireless Attacks", wirelessattacks_submenu)
        software_menu.append_submenu("Data Base Assessment", databaseassessment_submenu)
        software_menu.append_submenu("Reverse Engineering", reverseengineering_submenu)

        # software sub InformationGathering submenus
        amass_action = Gio.MenuItem.new("Amass", "win.Amass")
        dmitry_action = Gio.MenuItem.new("Dmitry", "win.dmitry")
        ikescan_action = Gio.MenuItem.new("Ike-Scan", "win.ikescan")
        legionroot_action = Gio.MenuItem.new("legion(root)", "win.legionroot")
        informationgathering_submenu.append_item(amass_action)
        informationgathering_submenu.append_item(dmitry_action)
        informationgathering_submenu.append_item(ikescan_action)
        informationgathering_submenu.append_item(legionroot_action)

        # Vulnerability Analysis submenu
        nmap_action = Gio.MenuItem.new("Nmap", "win.nmap")
        nikto_action = Gio.MenuItem.new("Nikto", "win.nikto")
        nexpose_action = Gio.MenuItem.new("Nexpose", "win.nexpose") 
        vulnerabilityanalysis_submenu.append_item(nmap_action)
        vulnerabilityanalysis_submenu.append_item(nikto_action)
        vulnerabilityanalysis_submenu.append_item(nexpose_action)

        # Web Application Analysis submenu
        burpsuite_action = Gio.MenuItem.new("Burp Suite", "win.burpsuite")
        wafw00f_action = Gio.MenuItem.new("wafw00f", "win.wafw00f")
        webapplictionanalysis_submenu.append_item(burpsuite_action)
        webapplictionanalysis_submenu.append_item(wafw00f_action)

        # Password Attacks submenu
        hydra_action = Gio.MenuItem.new("Hydra", "win.hydra")
        johntheripper_action = Gio.MenuItem.new("John the Ripper", "win.johntheripper")
        hashcat_action = Gio.MenuItem.new("Hashcat", "win.hashcat")
        passwordattacks_submenu.append_item(hydra_action)
        passwordattacks_submenu.append_item(johntheripper_action)
        passwordattacks_submenu.append_item(hashcat_action)

        # Wireless Attacks submenu
        aircrackng_action = Gio.MenuItem.new("Aircrack-ng", "win.aircracking")
        airmon_ng_action = Gio.MenuItem.new("Airmon-ng", "win.airmon")
        wifite_action = Gio.MenuItem.new("Wifite", "win.wifite")
        wirelessattacks_submenu.append_item(aircrackng_action)
        wirelessattacks_submenu.append_item(airmon_ng_action)
        wirelessattacks_submenu.append_item(wifite_action)

        # Data Base Assessment submenu
        sqlmap_action = Gio.MenuItem.new("sqlmap", "win.sqlmap")
        jsqlinjection_action = Gio.MenuItem.new("jsql Injection", "win.jsqlinjection")
        databaseassessment_submenu.append_item(sqlmap_action)
        databaseassessment_submenu.append_item(jsqlinjection_action)

        # Reverse Engineering submenu
        radare2_action = Gio.MenuItem.new("radare2", "win.radare2")
        binwalk_action = Gio.MenuItem.new("binwalk", "win.binwalk")
        reverseengineering_submenu.append_item(radare2_action)
        reverseengineering_submenu.append_item(binwalk_action)

        #create the submenu actions for Hardware
        hardware_menu = Gio.Menu.new()
        menu.append_submenu("Hardware Tools", hardware_menu)
        
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
        
        self.exploitdb_action = Gio.SimpleAction.new("exploitdb", None)
        self.exploitdb_action.connect("activate", self.exploitdb)
        self.add_action(self.exploitdb_action)
        #End of Web tools submenu
<<<<<<< HEAD
        
        #Create the inforamtion gathering functions
        self.amass_action = Gio.SimpleAction.new("Amass",None)
        self.amass_action.connect("activate",self.amass)
        self.add_action(self.amass_action)
       
        self.dmitry_action =Gio.SimpleAction.new("dmitry",None)
        self.dmitry_action.connect("activate",self.dmitry)
        self.add_action(self.dmitry_action)

        self.ikescan_action =Gio.SimpleAction.new("ikescan",None)
        self.ikescan_action.connect("activate",self.ikescan)
        self.add_action(self.ikescan_action)
        
        self.legionroot_action =Gio.SimpleAction.new("legionroot",None)
        self.legionroot_action.connect("activate",self.legionroot)
        self.add_action(self.legionroot_action)
        #End of the Information gathering funtions 
        
        #Create the vulnerablity analysis functions
        self.nmap_action =Gio.SimpleAction.new("nmap",None)
        self.nmap_action.connect("activate", self.nmap)
        self.add_action(self.nmap_action)
        
        self.nikto_action =Gio.SimpleAction.new("nikto",None)
        self.nikto_action.connect("activate", self.nikto)
        self.add_action(self.nikto_action)
        
        self.nexpose_action =Gio.SimpleAction.new("nexpose",None)
        self.nexpose_action.connect("activate", self.nexpose)
        self.add_action(self.nexpose_action)
        
        #End of the vulnerablity analysis functions
        
        #create the functions of webapplication analysis
        self.burpsuite_action =Gio.SimpleAction.new("burpsuite",None)
        self.burpsuite_action.connect("activate", self.burpsuite)
        self.add_action(self.burpsuite_action)
        
        self.wafw00f_action =Gio.SimpleAction.new("wafw00f",None)
        self.wafw00f_action.connect("activate", self.wafw00f)
        self.add_action(self.wafw00f_action)
        #End of the webapplication analysis functions
        
=======
>>>>>>> origin/main
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
        # Get the current directory of the script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute file path
        css_file_path = os.path.join(current_dir, 'style.css')

        # Load CSS file
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(css_file_path)

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
        # Initialize the notification system
        Notify.init("Penetration App")
   # Define the functions for encryption submenu action
    def cyberchef(self, action, param):
        webbrowser.open_new_tab("https://cyberchef.org/")

    def Rot13(self, action, param):
        webbrowser.open_new_tab("https://rot13.com/")

    def decode(self, action, param):
        webbrowser.open_new_tab("https://www.dcode.fr/")

    def encode(self, action, param):
        webbrowser.open_new_tab("https://www.base64encode.org/")
    # End of encryption submenu action
    
    # Define the functions for web tools submenu action
    def urlscan(self, action, param):
        webbrowser.open_new_tab("https://urlscan.io/")
    def vulnhub(self, action, param):
        webbrowser.open_new_tab("https://www.vulnhub.com/")
    def opswat(self, action, param):
        webbrowser.open_new_tab("https://www.opswat.com/")
    def exploitdb(self, action, param):
        webbrowser.open_new_tab("https://www.exploit-db.com/")
    # End of web tools submenu action
    
    # Define the functions for software inforamation gathering sub-submenu action
    def amass(self,action,param):
        print('amass')
    
    def dmitry(self,action,param):
        print('dmitry')
    
    def ikescan(self,action,parm):
        print('ikescan')
    
    def legionroot(self,action,parm):
        print('legion(root)')
        
    # Define the functions for software inforamation gathering sub-submenu action
    # Create the vulnerability analysis functions
    def nmap(self, action, parameter):
        print('nmap')

    def nikto(self, action, parameter):
        print('nikto')

    def nexpose(self, action, parameter):
        print('nexpose')
    
    # End of the vulnerablity analysis functions
    def burpsuite(self,param,parameter):
        print('brupsutie')

    def wafw00f(self,param,Parameter):
        print('wafw00f')
        
    # Define the functions for hardware submenu action
    def Hak5(self, action, param):
        webbrowser.open_new_tab("https://hak5.org/")
    def pine64(self, action, param):
        webbrowser.open_new_tab("https://pine64.com/")
    # End of hardware submenu action
    # Define the functions for training platforms submenu action
    def tryhackme(self, action, param):
        webbrowser.open_new_tab("https://tryhackme.com/")
    def hackthebox(self, action, param):
        webbrowser.open_new_tab("https://www.hackthebox.com/")
    # End of training platforms submenu action
    # Define the functions for CTF platforms submenu action
    def picoctf(self, action, param):
        webbrowser.open_new_tab("https://picoctf.org/")
    def ctfwithgoogle(self, action, param):
        webbrowser.open_new_tab("https://capturetheflag.withgoogle.com/")
    # End of CTF platforms submenu action
class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)
        
    def on_activate(self, app):
        self.win = MainWindow(application=app,title="Penetration App")
        self.win.present()

       
if __name__ == "__main__":
    app = MyApp(application_id='org.PenetrationApp.GtkApplication')
    app.run(sys.argv)
