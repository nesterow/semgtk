import gi
import cairo
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


#= base class for animated widgets
class FrameLoop(Gtk.DrawingArea):

    def __init__(self, interval = 40):
        super().__init__()
        self.interval = interval
        self.timers = Timers()
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
        self.timers.count(self.interval)
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


class Timer:
    def __init__(self):
        self.initital = 0
        self.elapsed = 0
        self.timeout = 0

class Timers:
    def __init__(self):
        self.timers = dict()
    
    def timer(self, name, miliseconds):
        t = self.timers.get(name) or Timer()
        if (t.timeout): return
        t.timeout = miliseconds
        t.initital = miliseconds
        self.timers[name] = t
    
    def count(self, interval):
         for t in self.timers.values():
            if t.timeout:
                t.timeout = max(0, t.timeout - interval)
                t.elapsed = t.elapsed + interval
            else:
                t.elapsed = 0

    def done(self, name):
        t = self.timers.get(name) or Timer()
        return not t.timeout
    
    def elapsed(self, name):
        t = self.timers.get(name) or Timer()
        return min(t.elapsed, t.initital)