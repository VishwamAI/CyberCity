from gi.repository import Gtk
from Page import Page
class ForensicsPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)
        self.grid = Gtk.Grid()

        self.grid.set_row_spacing(20)
        self.grid.set_column_spacing(10)

        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.set_child(self.grid)

        self.append(scroll)
        
        # Here, you have to add appropriate icons (emojis) corresponding to each tool
        tools = {
            "🔬 Autopsy": "Autopsy",
            "🖼️ Binwalk": "Binwalk",
            "💼 Bulk Extractor": "Bulk Extractor",
            "✔️ Chkrootkit": "Chkrootkit",
            "🔝 Foremost": "Foremost",
            "🍪 Galleta": "Galleta",
            "🔑 HashDeep": "HashDeep",
            "🔍 RkHunter": "RkHunter",
            "💾 SSDeep": "SSDeep",
            "🔎 Unhide": "Unhide",
            "📕 Yara": "Yara"
        }
        
        for i, (tool_label, tool_page) in enumerate(tools.items()):
            btn = Gtk.Button(label=tool_label)
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, tool_page)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')
        main_window = self.get_root()
        main_window.open_page(button, page_name)
