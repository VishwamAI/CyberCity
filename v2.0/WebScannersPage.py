from gi.repository import Gtk
import webbrowser
from Page import Page

class WebScannersPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        platforms = {
            "OWASP ZAP": "🕷️ OWASP ZAP",
            "Nikto": "🔍 Nikto",
            "W3af": "🌐 W3af",
            "Arachni": "🕸️ Arachni",
            "VirusTotal": "🦠 VirusTotal",
            "SSL Labs": "🔒 SSL Labs",
            "Sucuri": "🛡️ Sucuri",
            "Observatory": "🔭 Observatory"
        }

        for i, platform in enumerate(platforms):
            btn = Gtk.Button(label=platforms[platform])
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, platform)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        urls = {
            "OWASP ZAP": "https://www.zaproxy.org/",
            "Nikto": "https://cirt.net/Nikto2",
            "W3af": "http://w3af.org/",
            "Arachni": "http://www.arachni-scanner.com/",
            "VirusTotal": "https://www.virustotal.com/",
            "SSL Labs": "https://www.ssllabs.com/ssltest/",
            "Sucuri": "https://sitecheck.sucuri.net/",
            "Observatory": "https://observatory.mozilla.org/"
        }

        if page_name in urls:
            webbrowser.open(urls[page_name])
        else:
            print(f"No URL found for {page_name}")
