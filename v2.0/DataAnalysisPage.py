from gi.repository import Gtk
import webbrowser
from Page import Page

class DataAnalysisPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        tools = {
            "Pandas": "🐼 Pandas",
            "NumPy": "🔢 NumPy",
            "SciPy": "🔬 SciPy",
            "Matplotlib": "📊 Matplotlib",
            "Seaborn": "🌊 Seaborn",
            "Scikit-learn": "🧪 Scikit-learn",
            "TensorFlow": "🧠 TensorFlow"
        }

        for i, tool in enumerate(tools):
            btn = Gtk.Button(label=tools[tool])
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, tool)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        urls = {
            "Pandas": "https://pandas.pydata.org/",
            "NumPy": "https://numpy.org/",
            "SciPy": "https://www.scipy.org/",
            "Matplotlib": "https://matplotlib.org/",
            "Seaborn": "https://seaborn.pydata.org/",
            "Scikit-learn": "https://scikit-learn.org/stable/",
            "TensorFlow": "https://www.tensorflow.org/"
        }

        if page_name in urls:
            webbrowser.open(urls[page_name])
        else:
            print(f"No URL found for {page_name}")
