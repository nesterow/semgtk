import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


LAYOUT_OPTS = dict (
    fullscreen = False, 
    width = 0, 
    height = 0
)

PROPS = dict (
    spacing = 0,
    halign = 0,
    valign = 0
)

COLUMNS = 1
ROWS = 0

class Layout:

    def __init__(self, split = COLUMNS):
        self._args = None
        self._widgets = []
        if split == ROWS:  
            self.set_horizontal()
            self.is_vertical = False
        else:
            self.set_vertical()

    def asColumns(self):
        self.set_horizontal()
        return self
    
    def asRows(self):
        self.set_vertical()
        return self

    def add_widgets(self, widgets):
        self._widgets = widgets 
        for widget in widgets:
            self.layout.pack_start(widget, *widget.args)
        return self
    
    def _redraw(self):
        self.add_widgets(self._widgets)

    def set_horizontal(self):
        self.layout = Gtk.Box(**(self._args or PROPS))
        self._redraw()
        return self

    def clean(self):
        if self.is_vertical:
            self.set_vertical()
        else:
            self.set_horizontal()
        return self

    def set_vertical(self):
        self.is_vertical = True 
        self.layout = Gtk.Box(
            orientation = Gtk.Orientation.VERTICAL,
            **(self._args or PROPS)
        )
        self._redraw()
        return self

    def get(self):
        return self.layout