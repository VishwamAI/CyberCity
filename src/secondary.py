import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GdkPixbuf

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='Encryption&Decryption'>
      <menuitem action='CyberChef'/>
      <menuitem action='Rot13'/>
      <menuitem action='decode'/>
      <menuitem action='encode-decode'/>
    </menu>
    <menu action='Web Tools'>
      <menuitem action='UrlScan.io' />
      <menuitem action='vulnHub' />
      <menuitem action='Opswat' />
      <menuitem action='Lobas'/>
    </menu>
    <menu action='Software Tools'>
      <menuitem action='Nmap'/>
      <menuitem action='Metasploit'/>
      <menuitem action='BrupSuite'/>
      <menuitem action='Hydra'/>
    </menu>
    <menu action='Hardware Tools'>
      <menuitem action='Hak5'/>
      <menuitem action='Pine64'/>
    </menu>
    <menu action='Training Platforms'>
      <menuitem action='Try Hack Me'/>
      <menuitem action='Hack The Box'/>
    </menu>
    <menu action='CTF Platforms'>
      <menuitem action='PicoCTF'/>
      <menuitem action='GoogleCTF'/>
    </menu>
  </menubar>
  <popup name='PopupMenu'>
    <menuitem action='EditSomething' />
  </popup>
</ui>  
"""


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Penetration App")
        self.overlay = Gtk.Overlay()
        self.add(self.overlay)
        self.background = Gtk.Image.new_from_file('background.png')
        self.overlay.add(self.background)
        
        # Create action group and add menu actions
        self.action_group = Gtk.ActionGroup(name="my_actions")
        self.add_encryption_decryption_menu_actions(self.action_group)
        self.add_webtools_menu_actions(self.action_group)
        self.add_softwaretools_menu_actions(self.action_group)
        self.add_hardwaretools_menu_actions(self.action_group)
        self.add_trainingplatforms_menu_actions(self.action_group)
        self.add_ctfplatforms_menu_actions(self.action_group)
        
        # Create UI manager and add the action group
        uimanager = self.create_ui_manager()
        uimanager.insert_action_group(self.action_group)

        # Create menu bar and set it as the header bar
        self.menubar = uimanager.get_widget("/MenuBar")
        self.header_bar = Gtk.HeaderBar()
        self.header_bar.set_show_close_button(True)
        self.header_bar.pack_start(self.menubar)
        self.set_titlebar(self.header_bar)

        # Create button box
        self.button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_box.pack_start(Gtk.Button("CyberChef"), True, True, 0)
        self.button_box.pack_start(Gtk.Button("Rot13"), True, True, 0)
        self.button_box.pack_start(Gtk.Button("decode"), True, True, 0)
        self.button_box.pack_start(Gtk.Button("encode-decode"), True, True, 0)
        #create 2nd button box
        self.button_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_box2.pack_start(Gtk.Button("UrlScan.io"), True, True, 0)
        self.button_box2.pack_start(Gtk.Button("VulnHub"), True, True, 0)
        self.button_box2.pack_start(Gtk.Button("Opswat"), True, True, 0)
        self.button_box2.pack_start(Gtk.Button("Lobas"), True, True, 0)
        #create 3rd button box
        self.button_box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_box3.pack_start(Gtk.Button("Nmap"), True, True, 0)
        self.button_box3.pack_start(Gtk.Button("Metasploit"), True, True, 0)
        self.button_box3.pack_start(Gtk.Button("BrupSuite"), True, True, 0)
        self.button_box3.pack_start(Gtk.Button("Hydra"), True, True, 0)
        #create 4th button box
        self.button_box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_box4.pack_start(Gtk.Button("Hak5"), True, True, 0)
        self.button_box4.pack_start(Gtk.Button("Pine64"), True, True, 0)
        #create 5th button box
        self.button_box5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_box5.pack_start(Gtk.Button("Try Hack Me"), True, True, 0)
        self.button_box5.pack_start(Gtk.Button("Hack The Box"), True, True, 0)
        #create 6th button box
        self.button_box6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_box6.pack_start(Gtk.Button("PicoCTF"), True, True, 0)
        self.button_box6.pack_start(Gtk.Button("GoogleCTF"), True, True, 0)
        # Add button box to the main box
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.vbox.pack_start(self.button_box, False, False, 0)
        self.add(self.vbox)

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()
        uimanager.add_ui_from_string(UI_INFO)
        return uimanager

    # Define menu action callbacks
    def add_encryption_decryption_menu_actions(self, action_group):
      menu = Gtk.Menu()
      encryption_decryption_menu = Gtk.MenuItem.new_with_label("Encryption & Decryption")
      encryption_decryption_menu.set_submenu(menu)

      cyberchef = Gtk.MenuItem.new_with_label("CyberChef")
      cyberchef.connect("activate", self.on_cyberchef_activate)
      menu.append(cyberchef)

      rot13 = Gtk.MenuItem.new_with_label("Rot13")
      rot13.connect("activate", self.on_rot13_activate)
      menu.append(rot13)

      decode = Gtk.MenuItem.new_with_label("Decode")
      decode.connect("activate", self.on_decode_activate)
      menu.append(decode)

      encode_decode = Gtk.MenuItem.new_with_label("Encode-Decode")
      encode_decode.connect("activate", self.on_encode_decode_activate)
      menu.append(encode_decode)

      action_group.add_action_with_accel(Gtk.Action.new("Encryption&Decryption", None, None, None))
    def on_cyberchef_activate(self, source):
        print("CyberChef activated!")
    def on_rot13_activate(self, source):
        print("CyberChef activated!")
    def on_decode_activate(self, source):
        print("CyberChef activated!")
    def on_encode_decode_activate(self, source):
        print("CyberChef activated!")
    # here completed encryption and decryption
    # here start web tools
    def on_web_tools_activate(self, action_group):
      menu = Gtk.Menu()
      web_tools_menu = Gtk.MenuItem.new_with_label("Web Tools")
      web_tools_menu.set_submenu(menu)
      
      urlscan = Gtk.MenuItem.new_with_label("UrlScan.io")
      urlscan.connect("activate", self.on_urlscan_activate)
      menu.append(urlscan)
      
      vulnhub = Gtk.MenuItem.new_with_label("VulnHub")
      vulnhub.connect("activate", self.on_vulnhub_activate)
      menu.append(vulnhub)
      
      opswat = Gtk.MenuItem.new_with_label("Opswat")
      opswat.connect("activate", self.on_opswat_activate)
      menu.append(opswat)

      lobas = Gtk.MenuItem.new_with_label("Lobas")
      lobas.connect("activate", self.on_lobas_activate)
      menu.append(lobas)
      
      action_group.add_action_with_accel(Gtk.Action.new("Web Tools", None, None, None))
    def on_urlscan_activate(self, source):
        print("UrlScan.io")
    def on_vulnhub_activate(self, source):
        print("VulnHub")
    def on_opswat_activate(self, source):
        print("Opswat")
    def on_lobas_activate(self, source):
        print("Lobas")
    # here completed web tools
    # here start software tools
    def on_software_tools_activate(self, action_group):
      menu = Gtk.Menu()
      software_tools_menu = Gtk.MenuItem.new_with_label("Software Tools")
      software_tools_menu.set_submenu(menu)
      
      nmap = Gtk.MenuItem.new_with_label("Nmap")
      nmap.connect("activate", self.on_nmap_activate)
      menu.append(nmap)
      
      metasploit = Gtk.MenuItem.new_with_label("Metasploit")
      metasploit.connect("activate", self.on_metasploit_activate)
      menu.append(metasploit)
      
      brupsuite = Gtk.MenuItem.new_with_label("BrupSuite")
      brupsuite.connect("activate", self.on_brupsuite_activate)
      menu.append(brupsuite)

      hydra = Gtk.MenuItem.new_with_label("Hydra")
      hydra.connect("activate", self.on_hydra_activate)
      menu.append(hydra)
      
      action_group.add_action_with_accel(Gtk.Action.new("Software Tools", None, None, None))
    def on_nmap_activate(self, source):
        print("Nmap")
    def on_metasploit_activate(self, source):
        print("Metasploit")
    def on_brupsuite_activate(self, source):
        print("BrupSuite")
    def on_hydra_activate(self, source):
        print("Hydra")
    # here completed software tools
    # here start hardware tools
    
    def on_hardware_tools_activate(self, action_group):
      menu = Gtk.Menu()
      hardware_tools_menu = Gtk.MenuItem.new_with_label("Hardware Tools")
      hardware_tools_menu.set_submenu(menu)
      
      hak5 = Gtk.MenuItem.new_with_label("Hak5")
      hak5.connect("activate", self.on_hak5_activate)
      menu.append(hak5)
      
      pine64 = Gtk.MenuItem.new_with_label("Pine64")
      pine64.connect("activate", self.on_pine64_activate)
      menu.append(pine64)
      
      action_group.add_action_with_accel(Gtk.Action.new("Hardware Tools", None, None, None))
    def on_hak5_activate(self, source):
        print("Hak5")
    def on_pine64_activate(self, source):
        print("Pine64")
    # here completed hardware tools
    # here start training platforms
    
    def on_training_platforms_activate(self, action_group):
      
      menu = Gtk.Menu()
      training_platforms_menu = Gtk.MenuItem.new_with_label("Training Platforms")
      training_platforms_menu.set_submenu(menu)
      
      tryhackme = Gtk.MenuItem.new_with_label("TryHackMe")
      tryhackme.connect("activate", self.on_tryhackme_activate)
      menu.append(tryhackme)
      
      hackthebox = Gtk.MenuItem.new_with_label("HackTheBox")
      hackthebox.connect("activate", self.on_hackthebox_activate)
      menu.append(hackthebox)
      
      action_group.add_action_with_accel(Gtk.Action.new("Training Platforms", None, None, None))
    def on_tryhackme_activate(self, source):
        print("TryHackMe")
    def on_hackthebox_activate(self, source):
        print("HackTheBox")
    
    # here completed training platforms
    # here start CTF platforms
    
    def on_ctf_platforms_activate(self, action_group):
        
        menu = Gtk.Menu()
        ctf_platforms_menu = Gtk.MenuItem.new_with_label("CTF Platforms")
        ctf_platforms_menu.set_submenu(menu)
        
        picocTF = Gtk.MenuItem.new_with_label("PicoCTF")
        picocTF.connect("activate", self.on_picocTF_activate)
        menu.append(picocTF)
        
        googleCTF = Gtk.MenuItem.new_with_label("GoogleCTF")
        googleCTF.connect("activate", self.on_googleCTF_activate)
        menu.append(googleCTF)
        
        action_group.add_action_with_accel(Gtk.Action.new("CTF Platforms", None, None, None))
    def on_picocTF_activate(self, source):
        print("PicoCTF")
    def on_googleCTF_activate(self, source):
        print("GoogleCTF")
    # here completed CTF platforms

window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
