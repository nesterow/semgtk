import gi
import cairo
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


#= base class for animated widgets
class FrameLoop(Gtk.DrawingArea):

    def __init__(self, interval = 40):
        super().__init__()
        self.interval = interval
        self.connect('draw', self.loop)
        GLib.timeout_add(interval, self.tick)
    
    @property
    def size(self):
        return AreaSize(
            width = self.get_allocated_width(),
            height = self.get_allocated_height()
        )

    def tick(self):
        self.queue_draw()
        return True
    
    def loop(self, wgt, ctx):
        self.draw(ctx, self.size, wgt)
    
    def draw(self, ctx, size, widget):
        print(('Drawing: "draw()" is not implemented'))
        raise NotImplementedError

class AreaSize:
    def __init__(self, width = 300, height = 165):
        self.width = width
        self.height = height
        self.w = width
        self.h = height