import os.path
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

from components import Layout, create_app, load_css
from components import Element as E

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


if __name__ == "__main__":
 
    # layout.set_vertical()
    one = E(Gtk.Button)(label="Hello").expand(False, False).cssId('BlackButton')
    one.set_size_request(200, 200)
    print(one.get_css_name())

    two = E(Gtk.Button)(label="Glob").expand(True, True)
    two.set_size_request(100, 100)

    last = E(Gtk.Button)(label="Olleh").expand(True, True)
    last.set_size_request(100, 100)
    layout = Layout().asColumns()\
        .add_widgets([one, two, last]).end()
    load_css(__file__, 'window.css')
    create_app(layout).run()