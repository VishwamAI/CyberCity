from gi.repository import Gtk
import webbrowser
from Page import Page

class NetworkUtilitiesPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        utilities = {
            "Online Ping Test": "🏓 Online Ping Test",
            "DNS Lookup": "🔍 DNS Lookup",
            "Whois Lookup": "🔍 Whois Lookup",
            "IP Location": "📍 IP Location",
            "Port Check Tool": "🔍 Port Check Tool",
            "URL/Website Scanner": "🕵️‍♂️ URL/Website Scanner",
            "SSL Server Test": "🔒 SSL Server Test",
            "HTTP/HTTPS Header Check": "📋 HTTP/HTTPS Header Check",
            "IP Blacklist Check": "🚫 IP Blacklist Check",
            "Speed Test": "⏱ Speed Test",
            "Online Nmap Scanner": "🔍 Online Nmap Scanner",
            "Online SQLMap": "🔍 Online SQLMap"
        }

        for i, utility in enumerate(utilities):
            btn = Gtk.Button(label=utilities[utility])
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, utility)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        urls = {
            "Online Ping Test": "https://www.ipvoid.com/ping/",
            "DNS Lookup": "https://www.ipvoid.com/dns-lookup/",
            "Whois Lookup": "https://www.ipvoid.com/whois/",
            "IP Location": "https://www.ipvoid.com/ip-locator/",
            "Port Check Tool": "https://www.yougetsignal.com/tools/open-ports/",
            "URL/Website Scanner": "https://www.virustotal.com/gui/home/url",
            "SSL Server Test": "https://www.ssllabs.com/ssltest/",
            "HTTP/HTTPS Header Check": "https://www.rexswain.com/httpview.html",
            "IP Blacklist Check": "https://www.dnsbl.info/",
            "Speed Test": "https://www.speedtest.net/",
            "Online Nmap Scanner": "https://hackertarget.com/nmap-online-port-scanner/",
            "Online SQLMap": "https://pentest-tools.com/sqlmap-online"
        }

        if page_name in urls:
            webbrowser.open(urls[page_name])
        else:
            print(f"No URL found for {page_name}")
