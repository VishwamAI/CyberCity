import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QMenuBar, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set the window size and title
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Encryption and Decryption")
        
        # Set the background image as a QPixmap
        pixmap = QPixmap("background.png")
        
        # Create a QLabel to hold the pixmap
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 800, 600)
        
        # Create the menus
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("background-color: #1e2f41;")
        encryption_decryption_menu = menu_bar.addMenu("Encryption & Decryption")
        web_tools_menu = menu_bar.addMenu("Web Tools")
        softwaretools_menu = menu_bar.addMenu("Software Tools")
        Hardwaretools_menu = menu_bar.addMenu("Hardware Tools")
        Trainingplatforms_menu = menu_bar.addMenu("Training Platforms")
        CTFPlatforms_menu= menu_bar.addMenu("CTF Platforms")
        #create the submenu actions for Encryption & Decryption
        cyberchef_action = QAction("Cyber Chef",self)
        Rot13_action = QAction("Rot13",self)
        decode_action = QAction("Decode",self)
        encode_action = QAction("Encode-Decode",self)
        
        # Add the submenu actions to the Encryption & Decryption menu
        encryption_decryption_menu.addAction(cyberchef_action)
        encryption_decryption_menu.addAction(Rot13_action)
        encryption_decryption_menu.addAction(decode_action)
        encryption_decryption_menu.addAction(encode_action)
        
        # Connect the actions to their respective functions
        cyberchef_action.triggered.connect(self.cyberchef)
        Rot13_action.triggered.connect(self.Rot13)
        decode_action.triggered.connect(self.decode)
        encode_action.triggered.connect(self.encode)
     
        # Create the submenu actions for Web Tools menu
        urlscan_io_action = QAction("urlscan.io", self)
        vulnhub_action = QAction("vulnhub", self)
        opswat_action = QAction("opswat", self)
        lobas_action = QAction("lobas", self)
        
        # Add the submenu actions to the Web Tools menu
        web_tools_menu.addAction(urlscan_io_action)
        web_tools_menu.addAction(vulnhub_action)
        web_tools_menu.addAction(opswat_action)
        web_tools_menu.addAction(lobas_action)
        
        # Connect the actions to their respective functions
        urlscan_io_action.triggered.connect(self.urlscan_io)
        vulnhub_action.triggered.connect(self.vulnhub)
        opswat_action.triggered.connect(self.opswat)
        lobas_action.triggered.connect(self.lobas)
        
        #create the submenu actions for Software tools
        Nmap_action = QAction("NMAP",self)
        Metasploit_action = QAction("Metasploit",self)
        Brupsuite_action = QAction("Brupsuite",self)
        Hydra_action = QAction("Hydra",self)
        
        # Add the submenu actions to the Encryption & Decryption menu
        softwaretools_menu.addAction(Nmap_action)
        softwaretools_menu.addAction(Metasploit_action)
        softwaretools_menu.addAction(Brupsuite_action)
        softwaretools_menu.addAction(Hydra_action)
        
        # Connect the actions to their respective functions
        Nmap_action.triggered.connect(self.Nmap)
        Metasploit_action.triggered.connect(self.Metasploit)
        Brupsuite_action.triggered.connect(self.Brupsuite)
        Hydra_action.triggered.connect(self.Hydra)

        
        #create the submenu actions for Hardware tools
        Hak5_action = QAction("Hak5",self)
        Pine64_action = QAction("Pine64",self)
        
        
        # Add the submenu actions to the Encryption & Decryption menu
        Hardwaretools_menu.addAction(Hak5_action)
        Hardwaretools_menu.addAction(Pine64_action)
        
        # Connect the actions to their respective functions
        Hak5_action.triggered.connect(self.Hak5)
        Pine64_action.triggered.connect(self.Pine64)
        
        
        #create the submenu actions for Training platforms
        Tryhackme_action = QAction("Tryhackme",self)
        hackthebox_action = QAction("Hackthebox",self)
        # Add the submenu actions to the Training  platforms
        Trainingplatforms_menu.addAction(Tryhackme_action)
        Trainingplatforms_menu.addAction(hackthebox_action)
        # Connect the actions to their respective functions
        Tryhackme_action.triggered.connect(self.Tryhackme)
        hackthebox_action.triggered.connect(self.Hackthebox)
        
        #create the submenu actions for CTF platforms
        PicoCTF_action = QAction("PicoCTF",self)
        GoogleCTF_action = QAction("GoogleCTF",self)
        # Add the submenu actions to the CTF  platforms
        CTFPlatforms_menu.addAction(PicoCTF_action)
        CTFPlatforms_menu.addAction(GoogleCTF_action)
        # Connect the actions to their CTF functions
        PicoCTF_action.triggered.connect(self.PicoCTF)
        GoogleCTF_action.triggered.connect(self.GoogleCTF)
        
    #Define the functions for encryption submenu action
    def cyberchef(self):
        print("cyberchef selected")
    def Rot13(self):
        print("Rot13 selected")
    def decode(self):
        print("decode selected")
    def encode(self):
        print("encode selected")
    # Define the functions for webtools submenu action
    def urlscan_io(self):
        print("urlscan.io selected.")
    
    def vulnhub(self):
        print("vulnhub selected.")
    
    def opswat(self):
        print("opswat selected.")
    
    def lobas(self):
        print("lobas selected.")
    
    #Define the functions for software tools
    def Nmap(self):
        print("Nmap selected")
    def Metasploit(self):
        print("Metasploit selected")
    def Brupsuite(self):
        print("Brupsuite selected")
    def Hydra(self):
        print("Hydra selected")
    #Define the functions for Hardware tools
    def Hak5(self):
        print("Hak5 selected")
    def Pine64(self):
        print("Pine64 selected")
    #Define the funtions of Training Platforms
    def Tryhackme(self):
        print("Tryhackme selected")
    def Hackthebox(self):
        print("Hack the box selected ")
    #Define the funtions of CTF Platforms
    def PicoCTF(self):
        print("PicoCTF selected")
    def GoogleCTF(self):
        print("GoogleCTF selected")
if __name__ == "__main__":
    # Create the application and main window
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
        
    # Start the event loop
    sys.exit(app.exec_())
