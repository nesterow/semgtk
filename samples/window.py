import init
from components import HorizontalSplit, create_app, load_css
from components import Element as E

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from samples.hello import draw

if __name__ == "__main__":
    

    # layout.set_vertical()
    one = E(Gtk.Button, lambda w: (
        w.set_label('hello'),
        w.expand(True, True),
        w.cssId('BlackButton'),
        w.set_size_request(200, 200)
    ))


    last = E(Gtk.Image, lambda w: (
        w.expand(False, False),
        w.cssId('image'),
        w.set_from_file('samples/background.png'),
        w.set_size_request(200, 200)
    ))
 
    layout = HorizontalSplit([one, last])
    load_css(__file__, 'window.css')
    create_app(layout, title = "Emulator", fullscreen = True).run()