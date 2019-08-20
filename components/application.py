import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

OPTS = dict (
    fullscreen = False, 
    width = 0, 
    height = 0
)


class Application(Gtk.ApplicationWindow):
    def __init__(self, *k, **kv):
        super().__init__(*k, **kv)
        self.connect('destroy', lambda w: Gtk.main_quit())
    
    def run(self):
        self.show_all()
        Gtk.main()

def create_app(layout, *args, fullscreen = 0, width = 0, height = 0, **opts):
    app = Application(type = Gtk.WindowType.TOPLEVEL, **opts)
    if fullscreen: app.fullscreen()
    app.set_default_size(
        (width or 800),
        (height or 600),
    )
    app.add(layout)
    return app
