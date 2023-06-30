#!/usr/bin/env python3
import sys
import os
import gi
import webbrowser
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk,Gio, Gdk, Notify
import subprocess
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
        databaseassessment_submenu = Gio.Menu.new()
        passwordattacks_submenu = Gio.Menu.new()
        wirelessattacks_submenu = Gio.Menu.new()
        reverseengineering_submenu = Gio.Menu.new()
        exploitationtools_submenu = Gio.Menu.new()
        sniffingtools_submenu = Gio.Menu.new()
        postexploitation_submenu = Gio.Menu.new()
        forensics_submenu = Gio.Menu.new()
        reportingtools_submenu = Gio.Menu.new()
        socialengneeringtoolkit_submenu = Gio.Menu.new()
        systemservicestoolkit_submenu = Gio.Menu.new()
        

        software_menu.append_submenu("Information Gathering", informationgathering_submenu)
        software_menu.append_submenu("Vulnerability Analysis", vulnerabilityanalysis_submenu)
        software_menu.append_submenu("Web Application Analysis", webapplictionanalysis_submenu)
        software_menu.append_submenu("Data Base Assessment", databaseassessment_submenu)
        software_menu.append_submenu("Password Attacks", passwordattacks_submenu)
        software_menu.append_submenu("Wireless Attacks", wirelessattacks_submenu)
        software_menu.append_submenu("Reverse Engineering", reverseengineering_submenu)
        software_menu.append_submenu("Exploitation Tools", exploitationtools_submenu)
        software_menu.append_submenu("Sniffing Tools",sniffingtools_submenu)
        software_menu.append_submenu("Post Exploitation",postexploitation_submenu)
        software_menu.append_submenu("Forensics",forensics_submenu)
        software_menu.append_submenu("Reporting Tools",reportingtools_submenu)
        software_menu.append_submenu("Social Engeneering Toolkit",socialengneeringtoolkit_submenu)
        software_menu.append_submenu("System Services Toolkit",systemservicestoolkit_submenu)
        
        # software sub InformationGathering submenus
        
        # Information Gathering submenu
        amass_action = Gio.MenuItem.new("Amass", "win.Amass")
        dmitry_action = Gio.MenuItem.new("Dmitry", "win.Dmitry")
        ikescan_action = Gio.MenuItem.new("Ike-Scan", "win.Ikescan")
        legionroot_action = Gio.MenuItem.new("legion(root)", "win.Legionroot")
        matelgo_action = Gio.MenuItem.new("Matelgo", "win.Matelgo")
        netdiscover_action = Gio.MenuItem.new("Netdiscover", "win.Netdiscover")
        nmap_action = Gio.MenuItem.new("Nmap", "win.Nmap")
        reconng_action = Gio.MenuItem.new("Recon-ng", "win.Reconng")
        spiderfoot_action = Gio.MenuItem.new("Spider Foot", "win.Spiderfoot")

        informationgathering_submenu.append_item(amass_action)
        informationgathering_submenu.append_item(dmitry_action)
        informationgathering_submenu.append_item(ikescan_action)
        informationgathering_submenu.append_item(legionroot_action)
        informationgathering_submenu.append_item(matelgo_action)
        informationgathering_submenu.append_item(netdiscover_action)
        informationgathering_submenu.append_item(nmap_action)
        informationgathering_submenu.append_item(reconng_action)
        informationgathering_submenu.append_item(spiderfoot_action)

        # Vulnerability Analysis submenu
        gvmintalsetup_action = Gio.MenuItem.new("GVM Intal Setup", "win.Gvmintalsetup")
        gvmstart_action = Gio.MenuItem.new("GVM Start", "win.Gvmstart")
        legionroot_action = Gio.MenuItem.new("legion(root)", "win.Legionroot")
        lynis_action = Gio.MenuItem.new("Lynis", "win.Lynis")
        nikito_action = Gio.MenuItem.new("Nikito", "win.Nikito")
        nmap_action = Gio.MenuItem.new("Nmap", "win.Nmap")
        peass_action = Gio.MenuItem.new("Peass", "win.Peass")
        unixprvesccheck_action = Gio.MenuItem.new("unix-privesc-check", "win.Unixprvesccheck")

        vulnerabilityanalysis_submenu.append_item(gvmintalsetup_action)
        vulnerabilityanalysis_submenu.append_item(gvmstart_action)
        vulnerabilityanalysis_submenu.append_item(legionroot_action)
        vulnerabilityanalysis_submenu.append_item(lynis_action)
        vulnerabilityanalysis_submenu.append_item(nikito_action)
        vulnerabilityanalysis_submenu.append_item(nmap_action)
        vulnerabilityanalysis_submenu.append_item(peass_action)
        vulnerabilityanalysis_submenu.append_item(unixprvesccheck_action)

        # Web Application Analysis submenu
        burpsuite_action = Gio.MenuItem.new("Burp Suite", "win.burpsuite")
        commix_action = Gio.MenuItem.new("Commix", "win.commix")
        httrack_action = Gio.MenuItem.new("HT-Track", "win.httrack")
        pros_action = Gio.MenuItem.new("Prox", "win.prox")
        skipfish_action = Gio.MenuItem.new("Skipfish", "win.skipfish")
        sqlmap_action = Gio.MenuItem.new("SQLmap", "win.sqlmap")
        webscrab_action = Gio.MenuItem.new("Web Scrab", "win.webscrab")
        webshells_action = Gio.MenuItem.new("Web Shells", "win.webshells")
        wpscan_action = Gio.MenuItem.new("WPScan", "win.wpscan")
        zap_action = Gio.MenuItem.new("ZAP", "win.zap")
        
        webapplictionanalysis_submenu.append_item(burpsuite_action)
        webapplictionanalysis_submenu.append_item(commix_action)
        webapplictionanalysis_submenu.append_item(httrack_action)
        webapplictionanalysis_submenu.append_item(pros_action)
        webapplictionanalysis_submenu.append_item(skipfish_action)
        webapplictionanalysis_submenu.append_item(sqlmap_action)
        webapplictionanalysis_submenu.append_item(webscrab_action)
        webapplictionanalysis_submenu.append_item(webshells_action)
        webapplictionanalysis_submenu.append_item(wpscan_action)
        webapplictionanalysis_submenu.append_item(zap_action)
        
        #Database Attacks submenu
        jsqlinjection_action = Gio.MenuItem.new("JSQL Injection", "win.jsqlinjection")
        mdbsql_action = Gio.MenuItem.new("MDB-SQL", "win.mdb-sql")
        oscanner_action = Gio.MenuItem.new("Oscanner", "win.oscanner")
        sidegueuser_action = Gio.MenuItem.new("Sidegueuser", "win.sidegueuser")
        sqldict_action = Gio.MenuItem.new("SQLdict", "win.sqldict")
        sqllitedbbrowser_action = Gio.MenuItem.new("SQLlite DB Browser", "win.sqllitedbbrowser")
        sqlmap_action = Gio.MenuItem.new("SQLmap", "win.sqlmap")
        sqlninja_action = Gio.MenuItem.new("SQLninja", "win.sqlninja")
        sqlsus_action = Gio.MenuItem.new("SQLsus", "win.sqlsus")
        transcmdlog_action = Gio.MenuItem.new("Transcmdlog", "win.transcmdlog")
        
        databaseassessment_submenu.append_item(jsqlinjection_action)
        databaseassessment_submenu.append_item(mdbsql_action)
        databaseassessment_submenu.append_item(oscanner_action)
        databaseassessment_submenu.append_item(sidegueuser_action)
        databaseassessment_submenu.append_item(sqldict_action)
        databaseassessment_submenu.append_item(sqllitedbbrowser_action)
        databaseassessment_submenu.append_item(sqlmap_action)
        databaseassessment_submenu.append_item(sqlninja_action)
        databaseassessment_submenu.append_item(sqlsus_action)
        databaseassessment_submenu.append_item(transcmdlog_action)
        
        # Password Attacks submenu
        cewl_action = Gio.MenuItem.new("Cewl", "win.cewl")
        crunch_action = Gio.MenuItem.new("Crunch", "win.crunch")
        hashcat_action = Gio.MenuItem.new("Hashcat", "win.hashcat")
        hydra_action = Gio.MenuItem.new("Hydra", "win.hydra")
        john_action = Gio.MenuItem.new("John", "win.john")
        johnny_action = Gio.MenuItem.new("Johnny", "win.johnny")
        medusa_action = Gio.MenuItem.new("Medusa", "win.medusa")
        nrcrack_action = Gio.MenuItem.new("Ncrack", "win.ncrack")
        ophcrack_action = Gio.MenuItem.new("Ophcrack", "win.ophcrack")
        ranbowcrack_action = Gio.MenuItem.new("Rainbow Crack", "win.rainbowcrack")
        rcrackimt_action = Gio.MenuItem.new("Rcracki Mt", "win.rcrackimt")
        wordlists_action = Gio.MenuItem.new("Wordlists", "win.wordlists")
        
        passwordattacks_submenu.append_item(cewl_action)
        passwordattacks_submenu.append_item(crunch_action)
        passwordattacks_submenu.append_item(hashcat_action)
        passwordattacks_submenu.append_item(hydra_action)
        passwordattacks_submenu.append_item(john_action)
        passwordattacks_submenu.append_item(johnny_action)
        passwordattacks_submenu.append_item(medusa_action)
        passwordattacks_submenu.append_item(nrcrack_action)
        passwordattacks_submenu.append_item(ophcrack_action)
        passwordattacks_submenu.append_item(ranbowcrack_action)
        passwordattacks_submenu.append_item(rcrackimt_action)
        passwordattacks_submenu.append_item(wordlists_action)
        
        # Wireless Attacks submenu
        aircrackng_action = Gio.MenuItem.new("Aircrack-ng", "win.aircracking")
        airmon_ng_action = Gio.MenuItem.new("Airmon-ng", "win.airmon")
        wifite_action = Gio.MenuItem.new("Wifite", "win.wifite")
        wirelessattacks_submenu.append_item(aircrackng_action)
        wirelessattacks_submenu.append_item(airmon_ng_action)
        wirelessattacks_submenu.append_item(wifite_action)

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
    def amass(self,subprocess):
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
        self.win = MainWindow(application=app,title="PenetrationApp")
        self.win.present()

       
if __name__ == "__main__":
    app = MyApp(application_id='org.PenetrationApp.GtkApplication')
    app.run(sys.argv)
