# main.py
import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Notify','0.7')
from gi.repository import Gtk, Gdk,Gtk

# First page
from CyberToolsPage import CyberToolsPage
from TrainingPlatformsPage import TrainingPlatformsPage
from CTFPlatformsPage import CTFPlatformsPage
from JobCalendarsPage import JobCalendarsPage
from ResearchDiscoveryPage import ResearchDiscoveryPage
from CyberFraudsPage import CyberFraudsPage
from StudentDevelopmentPage import StudentDevelopmentPage
from EventsEntertainmentsPage import EventsEntertainmentsPage
from FeedbackPage import FeedbackPage


#second Page
from LinuxPage import LinuxPage
from WebApplicationsPage import WebApplicationsPage
from MacOSPage import MacOSPage
from WindowsPage import WindowsPage
from MobileApplicationsPage import MobileApplicationsPage

# Linux page
from InformationGatheringPage import InformationGatheringPage
from VulnerabilityAnalysisPage import VulnerabilityAnalysisPage
from WebApplicationPage import WebApplicationPage
from DataBaseAssessmentPage import DataBaseAssessmentPage
from PasswordAttacksPage import PasswordAttacksPage
from WirelessAttacksPage import WirelessAttacksPage
from ReverseEngineeringPage import ReverseEngineeringPage
from ExplorationToolsPage import ExplorationToolsPage
from SniffingToolsPage import SniffingToolsPage
from PostExploitationPage import PostExploitationPage
from ForensicsPage import ForensicsPage
from ReportingToolsPage import ReportingToolsPage
from SocialEngineeringToolkitPage import SocialEngineeringToolkitPage
from SystemServicesPage import SystemServicesPage

# WebTools page
from EncodeDecodePage import EncodeDecodePage
from ExploitsPage import ExploitsPage
from WebScannersPage import WebScannersPage
from DataAnalysisPage import DataAnalysisPage
from NetworkUtilitiesPage import NetworkUtilitiesPage
from CyberSecurityPage import CyberSecurityPage
#InformationGatheringPage Download pages
from AmassPage import AmassPage
from DmitryPage import DmitryPage
from ikescanpage import IkeScanPage
from LegionPage import LegionPage
from Maltegopage import MaltegoPage
from NetDiscoverPage import NetDiscoverPage
from NmapPage import NmapPage
from ReconNgPage import ReconNgPage

#VulnerabilityAnalysisPage Download Pages
from GVMPage import GVMPage
from LynisPage import LynisPage
from NiktoPage import NiktoPage
from Page import Page

#InformationGatheringPage Download pages
from AmassPage import AmassPage
from DmitryPage import DmitryPage
from ikescanpage import IkeScanPage
from LegionPage import LegionPage
from Maltegopage import MaltegoPage
from NetDiscoverPage import NetDiscoverPage
from NmapPage import NmapPage
from ReconNgPage import ReconNgPage

#VulnerabilityAnalysisPage Download Pages
from GVMPage import GVMPage
from LynisPage import LynisPage
from NiktoPage import NiktoPage
from Page import Page

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_decorated(True)
        self.set_resizable(True)
        self.maximize()
        self.stack = Gtk.Stack()
        self.set_child(self.stack)

        self.grid = Gtk.Grid()
        self.stack.add_named(self.grid, "Main Page")
        self.current_page = "Main Page"

        self.navigation_history = []
        self.added_pages = set()

        buttons = {
            "Cyber Tools": "🏢",
            "Training Platforms": "🏫",
            "CTF Platforms": "🏟️",
            "Job Calendars": "📅",
            "Research\n & Discovery": "🧪",
            "Cyber Frauds": "👮",
            "Student\nDevelopment Kit": "🏞️",
            "Events\n & Entertainments": "🎡",
            "Feedback": "📩"
        }


        for i, (tool, emoji) in enumerate(buttons.items()):
        # Change label from "{emoji}\n{text}" to "{emoji} {text}"
            btn = Gtk.Button(label=f"{emoji} {tool}")
            btn.get_style_context().add_class("kite")
            btn.connect("clicked", self.open_page, tool)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)
            



    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        if page_name not in self.added_pages:
            page_classes = {
                "Cyber Tools": CyberToolsPage,
                "Linux": LinuxPage,
                "Feedback": FeedbackPage,
                "Information Gathering": InformationGatheringPage,
                "Vulnerability Analysis": VulnerabilityAnalysisPage,
                "WebApplication": WebApplicationPage,
                "DataBase-Assessment": DataBaseAssessmentPage,
                "Password Attacks": PasswordAttacksPage,
                "Wireless Attacks": WirelessAttacksPage,
                "Reverse Engineering": ReverseEngineeringPage,
                "Exploration Tools": ExplorationToolsPage,
                "Sniffing Tools": SniffingToolsPage,
                "Post Exploitation": PostExploitationPage,
                "Forensics": ForensicsPage,
                "Reporting Tools": ReportingToolsPage,
                "Social Engineering Toolkit": SocialEngineeringToolkitPage,
                "System Services": SystemServicesPage,
                "Amass": AmassPage,
                "Dmitry":DmitryPage,
                "Ike-Scan": IkeScanPage,
                "Legion": LegionPage,
                "Maltego": MaltegoPage,
                "NetDiscover": NetDiscoverPage,
                "Nmap": NmapPage,
                "Recon-Ng": ReconNgPage,
                "GVM": GVMPage,
                "Lynis": LynisPage,
                "Nikto": NiktoPage,
                "Training Platforms": TrainingPlatformsPage, 
                "CTF Platforms":CTFPlatformsPage,
                "Job Calendars": JobCalendarsPage,
                "Research\n & Discovery":ResearchDiscoveryPage,
                "Cyber Frauds": CyberFraudsPage,
                "Student\nDevelopment Kit": StudentDevelopmentPage,
                "Events\n & Entertainments": EventsEntertainmentsPage,
                "MacOS":MacOSPage,
                "Windows":WindowsPage,
                "MobileApplications":MobileApplicationsPage,
                "WebApplications":WebApplicationsPage,
                "EncodeDecode":EncodeDecodePage,
                "Exploits":ExploitsPage,
                "WebScanners":WebScannersPage,
                "DataAnalysis":DataAnalysisPage,
                "NetworkUtilities":NetworkUtilitiesPage,
                "CyberSecurity":CyberSecurityPage,
            }
            if page_name in page_classes:
                page = page_classes[page_name]("Go back from " + self.current_page)
                self.stack.add_named(page, page_name)
                self.added_pages.add(page_name)
            else:
                page = Page("Go back from " + self.current_page)

        if self.current_page != page_name:
            self.navigation_history.append(self.current_page)

        self.current_page = page_name
        self.stack.set_visible_child_name(page_name)

class  CyberCity(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app, title="Cyber City")
        self.win.present()

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('style.css')
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

if __name__ == "__main__":
    app = CyberCity(application_id='org.PenetrationApp.GtkApplication')
    app.run(sys.argv)
