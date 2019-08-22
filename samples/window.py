import init
from components import Layout, create_app, load_css
from components import Element as E

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from samples.hello import draw

if __name__ == "__main__":
 
    # layout.set_vertical()
    one = E(Gtk.Button)(label="Hello").expand(False, False).cssId('BlackButton')
    one.set_size_request(200, 200)

    last = E(Gtk.Image)().expand(True, True).cssId('image')
    last.set_from_file('samples/background.png')
    last.set_size_request(200, 200)

    layout = Layout().asColumns()\
        .add_widgets([one, last]).end()
    load_css(__file__, 'window.css')
    create_app(layout, title = "Emulator").run()