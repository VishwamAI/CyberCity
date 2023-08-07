from gi.repository import Gtk
import webbrowser
from Page import Page

class YoutubeChannelsPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        channels = {
            "David Bombal": "https://www.youtube.com/@davidbombal",
            "Jhon Hammond": "https://www.youtube.com/@_JohnHammond",
            "InsiderPhD": "https://www.youtube.com/@InsiderPhD",
            " Cybersecurity Meg": "https://www.youtube.com/@CybersecurityMeg",
        }
        for i, channel in enumerate(channels):
            btn = Gtk.Button(label=channel)
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_channel, channels[channel])
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_channel(self, button, channel_url):
        button.get_style_context().add_class('clicked')
        webbrowser.open(channel_url)
