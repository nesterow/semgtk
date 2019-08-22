import init
import math
import cairo
import time
from components import VerticalSplit, FrameLoop, create_app, easing, RGB
from components import Element as E
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

RADIAN = math.pi * 2

class Clock(FrameLoop):

    def __init__(self, **kv):
        super().__init__(**kv)
        self._seconds = 0
        self._minutes = 0
        self._hours = 0
    
    def draw_hours(self, ctx, size, r):
        text = [ str(i) for i in range(1,13) ]
        ctx.select_font_face("Courier", cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_BOLD)
        font_size = r / 20
        ctx.set_font_size(font_size)
        unit = RADIAN / 12
        for i in text:
            ctx.set_source_rgba(*RGB(0,0,0, .9))
            ctx.rotate(unit)
            ctx.move_to( - (font_size / 4),-(r - font_size * 4))
            ctx.show_text(i)

    def draw_minutes(self, ctx, size, r):
        text = [ str(i) for i in range(1,61) ]
        ctx.select_font_face("Courier", cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_BOLD)
        font_size = r / 30
        ctx.set_font_size(font_size)
        unit = RADIAN / 60
        for i in text:
            ctx.set_source_rgba(*RGB(0,0,0, .9))
            ctx.rotate(unit)
            ctx.move_to( - (font_size / 4),-(r - font_size * 2.5))
            ctx.show_text(i)


    def rotate_seconds(self, seconds, r):
        unit = RADIAN / 60
        rotation = unit * seconds
        matrix = cairo.Matrix(xx = 0, yy = - (r), x0 = 0, y0 = 0)
        if seconds == self._seconds and self.timers.done('seconds'):
            matrix.rotate(rotation)
            return matrix
        self.timers.timer('seconds',300)
        start = rotation - unit
        angle = easing.outElastic(self.timers.elapsed('seconds'),
            rotation - unit, 
            unit, 
            300
        )
        matrix.rotate(angle)
        self._seconds = seconds
        return matrix
    
    def rotate_minutes(self, minutes, r):
        unit = RADIAN / 60
        rotation = unit * minutes
        matrix = cairo.Matrix(xx = 0, yy = - (r), x0 = 0, y0 = 0)
        if minutes == self._minutes and self.timers.done('minutes'):
            matrix.rotate(rotation)
            return matrix
        self.timers.timer('minutes',300)        
        start = rotation - unit
        angle = easing.inOutSine(self.timers.elapsed('minutes'), start, unit, 300)
        matrix.rotate(angle)
        self._minutes = minutes
        return matrix
    
    def rotate_hours(self, hours, r):
        unit = RADIAN / 12
        matrix = cairo.Matrix(xx = 0, yy = - (r), x0 = 0, y0 = 0)
        if hours == self._hours and self.timers.done('hours'):
            matrix.rotate(unit * hours)
            return matrix
        self.timers.timer('hours',300)
        start = unit * hours - unit
        angle = easing.inOutSine(self.timers.elapsed('hours') , start, unit, 300)
        matrix.rotate(angle)
        self._hours = hours
        return matrix

    def draw(self, ctx, size, wgt):
        ctx.rectangle(0,0, size.w, size.h)
        ctx.set_source_rgba(*RGB(60,60,60, 1))
        ctx.fill()
        
        ctx.translate(size.w / 2, size.h / 2)

        ctx.arc(0, 0, min(size.w, size.h) / 2.5 , 0, 2 * math.pi)
        ctx.set_source_rgb(*RGB(100,100,100))
        ctx.fill()

        ctx.arc(0, 0, min(size.w, size.h) / 2.6 , 0, 2 * math.pi)
        ctx.set_source_rgba(*RGB(255,255,255, .9))
        ctx.fill()

        ctx.arc(0, 0, min(size.w, size.h) / 2.8 , 0, 2 * math.pi)
        ctx.set_source_rgba(*RGB(255,255,255, .7))
        ctx.fill()
        
        seconds = int(time.strftime('%S', time.gmtime()))
        minutes = int(time.strftime('%M', time.gmtime()))
        hours = int(time.strftime('%I', time.gmtime()))
        r = (min(size.w, size.h) / 2.5)
        
        def draw_line(width_factor, color, rotation):
            ctx.new_path()
            ctx.set_line_width(min(size.w, size.h) / width_factor)
            ctx.move_to(0, 0)
            matrix = rotation()
            ctx.rel_line_to(-matrix.yx, matrix.yy)
            ctx.set_source_rgb(*color)
            ctx.stroke()
            ctx.close_path()

        draw_line(70, RGB(200, 200, 200), lambda: self.rotate_hours(hours, r / 1.3))
        draw_line(200, RGB(200, 200, 200), lambda: self.rotate_minutes(minutes, r / 1.1 ))
        draw_line(400, RGB(200, 200, 200), lambda: self.rotate_seconds(seconds, r / 1.05))
        
        ctx.set_source_rgb(*RGB(200, 200, 200))
        ctx.arc(0, 0, min(size.w, size.h) / 80 , 0, 2 * math.pi)
        ctx.fill()

        self.draw_hours(ctx, size, r)
        self.draw_minutes(ctx, size, r)

if __name__ == "__main__":
 
    # layout.set_vertical()
    one = E(Clock, lambda w: (
        w.expand(True, True)
    ))

    last = E(Gtk.Button, lambda w: (
        w.expand(False, False),
        w.set_label('button')
    ))
    
    layout = VerticalSplit([one, last])

    create_app(layout, title = "Emulator", fullscreen= True).run()