import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import webbrowser

stack = Gtk.Stack()
navigation_history = []

def create_content_button(content_name, callback=None):
    button = Gtk.Button(label=content_name)
    button.set_relief(Gtk.ReliefStyle.NONE)
    button.connect("enter-notify-event", lambda widget, event: widget.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2)))
    button.connect("leave-notify-event", lambda widget, event: widget.get_window().set_cursor(None))
    if callback:
        button.connect("clicked", callback)
    return button

def go_back(button):
    last_visited_page = navigation_history.pop() if navigation_history else "cybertools_main"
    stack.set_visible_child_name(last_visited_page)
    button.connect("enter-notify-event", lambda widget, event: widget.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2)))
    button.connect("leave-notify-event", lambda widget, event: widget.get_window().set_cursor(None))

def navigate_to_page(button, page_name):
    current_page = stack.get_visible_child_name()
    if current_page != page_name:
        navigation_history.append(current_page)
        stack.set_visible_child_name(page_name)

def create_top_bar():
    hbox = Gtk.Box(spacing=10)
    go_back_button = Gtk.Button()
    icon = Gtk.Image.new_from_icon_name("go-previous-symbolic", Gtk.IconSize.MENU)
    go_back_button.add(icon)
    go_back_button.connect("clicked", go_back)
    hbox.pack_start(go_back_button, False, False, 10)
    return hbox

def add_page_to_stack(page_name, title):
    if not stack.get_child_by_name(page_name):
        if page_name == "webbrowser":
            add_webbrowsers_page()
        elif page_name == "hardwaretools":
            add_hardwaretools_page()
        else:
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
            vbox.pack_start(create_top_bar(), False, False, 10)
            label = Gtk.Label(label=f"Welcome to {title} Page")
            vbox.pack_start(label, True, True, 10)
            stack.add_titled(vbox, page_name, title)

def initialize_stack():
    add_page_to_stack("cybertools_main", "Cyber Tools")
    add_page_to_stack("webbrowsers", "Web Browser")
    add_page_to_stack("linux", "Linux Tools")
    add_page_to_stack("hardwaretools", "Hardware Tools")
    initialize_tool_pages()  # Initialize individual tool pages
    # Initialize more pages here

def initialize_tool_pages():
    for tool_name, page_name in webbrowsers.items():
        vbox = add_tool_content(tool_name)
        stack.add_titled(vbox, page_name, tool_name)

def add_cybertools_content(content_box):
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)
    vbox.set_halign(Gtk.Align.CENTER)

    label = Gtk.Label()
    label.set_markup("<span size='x-large' weight='bold'>Cyber Tools</span>")
    vbox.pack_start(label, False, False, 10)

    hbox_top = Gtk.Box(spacing=10)
    hbox_top.pack_start(create_content_button("Linux", lambda button: navigate_to_page(button, "linux")), True, True, 0)
    hbox_top.pack_start(create_content_button("WebBrowser", lambda button: navigate_to_page(button, "webbrowsers")), True, True, 0)
    vbox.pack_start(hbox_top, True, True, 10)

    hardware_button = create_content_button("Hardware Tools", lambda button: navigate_to_page(button, "hardwaretools"))
    vbox.pack_start(hardware_button, True, True, 10)

    stack.add_titled(vbox, "cybertools_main", "Cyber Tools")
    content_box.pack_start(stack, True, True, 0)

    initialize_stack()

    content_box.show_all()
    stack.set_visible_child_name("cybertools_main")
# webbrowser Page
webbrowsers = {
    "🔀 E&D": "EncodeDecode",
    "💣 Exploits": "Exploits",
    "🕸️ Web Scanners": "WebScanners",
    "📊 Data Analysis": "DataAnalysis",
    "🌐 Network Utilities": "NetworkUtilities",
}

def navigate_to_tool_page(button, tool_name):
    navigate_to_page(button, webbrowsers[tool_name])

def add_tool_content(tool_name):
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    label = Gtk.Label(label=f"{tool_name} Tools")
    vbox.pack_start(label, False, False, 10)

    # This is just an example, you can add specific content for each tool.
    for i in range(1, 4):
        button = create_content_button(f"{tool_name} Option {i}")
        vbox.pack_start(button, True, True, 10)
    return vbox

def add_webbrowsers_page():
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)
    vbox.pack_start(create_top_bar(), False, False, 10)

    label = Gtk.Label()
    label.set_markup("<span size='x-large' weight='bold'>Web Browser Tools</span>")
    vbox.pack_start(label, False, False, 10)

    hbox_top = Gtk.Box(spacing=10)
    hbox_top.set_homogeneous(True)
    hbox_top.set_halign(Gtk.Align.CENTER)

    for tool_name, page_name in list(webbrowsers.items())[:2]:
        def button_callback(button, page_name=page_name):
            navigate_to_page(button, page_name)
        button = create_content_button(tool_name, button_callback)
        button.set_size_request(100, 100)
        hbox_top.pack_start(button, True, True, 0)

    vbox.pack_start(hbox_top, False, False, 10)

    hbox_bottom = Gtk.Box(spacing=10)
    hbox_bottom.set_homogeneous(True)
    hbox_bottom.set_halign(Gtk.Align.CENTER)

    for tool_name, page_name in list(webbrowsers.items())[2:]:
        def button_callback(button, page_name=page_name):
            navigate_to_page(button, page_name)
        button = create_content_button(tool_name, button_callback)
        button.set_size_request(100, 100)
        hbox_bottom.pack_start(button, True, True, 0)

    vbox.pack_start(hbox_bottom, False, False, 10)
    stack.add_titled(vbox, "webbrowsers", "Web Browser")

# Hardware Tools page
hardware_tools = {
    "Hak5": "https://hak5.org/",
    "Pine64": "https://www.pine64.org/",
    "Raspberry Pi": "https://www.raspberrypi.org/",
    "Pwnie Express": "https://www.pwnieexpress.com/",
    "Think Penguin": "https://www.thinkpenguin.com/",
    "SparkFun Electronics": "https://www.sparkfun.com/",
    "Arduino": "https://www.arduino.cc/",
    "BeagleBoard": "https://beagleboard.org/",
}

def open_website(button, website_url):
    webbrowser.open(website_url)

def add_hardwaretools_page():
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_valign(Gtk.Align.START)
    vbox.pack_start(create_top_bar(), False, False, 10)

    label = Gtk.Label()
    label.set_markup("<span size='x-large' weight='bold'>Hardware Tools</span>")
    vbox.pack_start(label, False, False, 10)

    hardware_tools_list = list(hardware_tools.items())
    tools_per_row = 3  # Adjust the number of tools per row as needed

    for i in range(0, len(hardware_tools_list), tools_per_row):
        hbox = Gtk.Box(spacing=10)
        for tool_name, url in hardware_tools_list[i:i + tools_per_row]:
            button = create_content_button(tool_name, lambda button, url=url: open_website(button, url))
            
            # Set the size based on the tool name
            if tool_name == 'Hak5':
                button.set_size_request(150, 50)
            elif tool_name == 'Raspberry Pi':
                button.set_size_request(200, 70)
            else:
                button.set_size_request(100, 100)
            
            hbox.pack_start(button, True, True, 0)
        vbox.pack_start(hbox, False, False, 10)

    stack.add_titled(vbox, "hardwaretools", "Hardware Tools")
