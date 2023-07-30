from gi.repository import Gtk
import webbrowser
from Page import Page

class CyberSecurityPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        resources = {
            "OWASP": "🌐 OWASP",
            "Krebs on Security": "🔐 Krebs on Security",
            "Schneier on Security": "🔒 Schneier on Security",
            "National Vulnerability Database": "📖 National Vulnerability Database",
            "CVE Details": "📑 CVE Details",
            "MITRE": "🛡️ MITRE",
            "NIST Cybersecurity Framework": "🔨 NIST Cybersecurity Framework",
            "Cybrary": "📚 Cybrary",
            "Infosec Institute": "🎓 Infosec Institute"
        }

        for i, resource in enumerate(resources):
            btn = Gtk.Button(label=resources[resource])
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, resource)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        urls = {
            "OWASP": "https://www.owasp.org/",
            "Krebs on Security": "https://krebsonsecurity.com/",
            "Schneier on Security": "https://www.schneier.com/",
            "National Vulnerability Database": "https://nvd.nist.gov/",
            "CVE Details": "https://www.cvedetails.com/",
            "MITRE": "https://www.mitre.org/",
            "NIST Cybersecurity Framework": "https://www.nist.gov/cyberframework",
            "Cybrary": "https://www.cybrary.it/",
            "Infosec Institute": "https://www.infosecinstitute.com/"
        }

        if page_name in urls:
            webbrowser.open(urls[page_name])
        else:
            print(f"No URL found for {page_name}")
