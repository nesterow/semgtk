import os.path
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

from components.layout import Layout
from components.element import Element as E

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


if __name__ == "__main__":
    layout = Layout().asColumns()
    # layout.set_vertical()
    one = E(Gtk.Button)(label="Hello").expand(False, False)
    one.set_size_request(200, 200)

    two = E(Gtk.Button)(label="Glob").expand(True, True)
    two.set_size_request(100, 100)

    last = E(Gtk.Button)(label="Hello").expand(True, True)
    last.set_size_request(100, 100)

    layout.add_widgets([one, two, last])

    element = layout.get()

    
    window = Gtk.Window()
    window.set_default_size(800, 600)
    
    window.add(element)
    window.show_all()

    window.connect('destroy', lambda w: Gtk.main_quit())
    Gtk.main()