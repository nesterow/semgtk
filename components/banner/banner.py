from .. import *

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib



class Banner(Gtk.DrawingArea):
    def __init__(self, **kv):
        super().__init__(self, **kv)