import init
import math
import cairo
import time
from components import Layout, FrameLoop, create_app, easing
from components import Element as E
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Clock(FrameLoop):

    def __init__(self, **kv):
        super().__init__(**kv)
        self.seconds_rotation = 0
        self.minutes_rotation = None
        self.hours_rotation = None

        self._seconds = 0
        self._minutes = 0
        self._hours = 0

    def rotate_seconds(self, seconds, r, size):    
        matrix = cairo.Matrix(xx = 0, yy = - (r - 12), x0 = size.w / 2, y0 = size.h / 2)
        unit = ((math.pi * 2) / 60)
        start = unit * seconds
        if seconds == self._seconds:
            matrix.rotate(start)
            return matrix
        delta = time.time() * 1000 % 1000
        angle = easing.linear(delta , start, unit, 1000)
        matrix.rotate(angle)
        self._seconds = seconds
        return matrix

    def counter(self, ctx, size):
        MINUTE = 60
        HOUR = 60 * 60
        DAY = HOUR * 24
        TICK = time.time()

        seconds = round(TICK % MINUTE)
        minutes = round(TICK % HOUR % HOUR / 60)
        hours = round(TICK % DAY % DAY / 24)

        r = (min(size.w, size.h) / 2.5)
        ctx.set_line_width(min(size.w, size.h) / 400)
        ctx.new_path()
        ctx.move_to(0, 0)
        m = self.rotate_seconds(seconds, r, size)
        ctx.rel_line_to(-m.yx, m.yy)
        ctx.set_source_rgb(0, 0, 0)
        ctx.translate(size.w / 2, size.h / 2)
        ctx.stroke()
        ctx.close_path()


    def draw(self, ctx, size, wgt):
        ctx.set_source_rgb(0.2, 0.5, 1)
        ctx.translate(size.w / 2, size.h / 2)
        ctx.arc(0, 0, min(size.w, size.h) / 2.5 , 0, 2 * math.pi)
        ctx.fill()
        ctx.set_source_rgb(0, 0, 0)
        ctx.arc(0, 0, min(size.w, size.h) / 80 , 0, 2 * math.pi)
        ctx.fill()
        ctx.stroke()
        self.counter(ctx, size)

if __name__ == "__main__":
 
    # layout.set_vertical()
    one = E(Clock)().expand(True, True)

    last = E(Gtk.Button)(label = "Hello").expand(False, False)
    
    layout = Layout().asRows()\
        .add_widgets([one, last]).end()

    create_app(layout, title = "Emulator").run()