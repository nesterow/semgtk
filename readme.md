SemanticGTK [WIP]
-----------------

Python utilities for [GTK+](https://www.gtk.org/) and [gobject-introspection](https://gi.readthedocs.io/en/latest/).

### Getting stated
Install Python3, GTK3, and gobject-introspection libraries for your operation system. 
This work is currently tested with MacOS, Arch Linux and Alpine Linux ARM.

Then clone this repository:
```
~# git clone https://github.com/nesterow/semgtk
```

To verify that GTK3 works correctly in your system, run:
```
~# python3 samples/clock.py
```

### Features
This package provides several wrappers for GTK Widgets and Layouts.

#### Element configurator
Simple API for setting up GTK widgets. It provides additional convenience methods.

##### Usage:
```python
from components import HorizontalSplit, create_app, load_css
from components import Element as e

if __name__ == "__main__":
    button = e(Gtk.Button, lambda w: (
        w.set_label('hello'),
        w.expand(True, True),
        w.cssId('BlackButton'),
        w.set_size_request(200, 200)
    ))
    image = e(Gtk.Image, lambda w: (
        w.expand(False, False),
        w.cssId('image'),
        w.set_from_file('samples/background.png'),
        w.set_size_request(200, 200)
    ))
    layout = HorizontalSplit([button, image])
    load_css(__file__, 'window.css')
    create_app(layout, title = "Emulator", fullscreen = True).run()
```

##### Configurator methods:

All GTK.Widget options are available. And additionally:

- w.expand(xy: Bool, yx: Bool) - element packing options inside `Gtk.Box`. For horisontal layout: `xy = height, yx = with` - for vertical vice versa
- w.padding(padding: Number) - element padding for allocated space inside `Gtk.Box` layouts
- w.cssId(id: String) - set CSS id selector to the element


## Layouts

- HorizontalSplit(widgets: List) - the space will be split horizontally (as rows). The amount of space should be controlled by `w.expand`
- VerticalSplit(widgets: List) - the space will be split vertivally (as columns). `w.expand` options will be inverted


## FrameLoop component [WIP]
FrameLoop is basic class that inherits from `Gtk.DrawingArea`. It provides simple methods to create animated widgets.
See [clock example](samples/clock.py) for the reference.

#### FrameLoop::timers
Convenince methods for setting animation timers.
- ::timers.timer(name: String, timeout: int[ms]) - sets a timer
- ::timers.elapsed(name: String): int - returns time elapsed for a timer
- ::timers.done(name: String): Bool - check whether the timer is stoped

```python
# samples/clock.py
    def rotate_minutes(self, minutes, r):
        #.....
        self.timers.timer('minutes', 300)        
        start = rotation - unit
        angle = easing.inOutSine(self.timers.elapsed('minutes'), start, unit, 300)
        matrix.rotate(angle)
        return matrix
```

## Easing
Tweener's easing functions (Penner's Easing Equations)

```
For all easing functions:
  t = elapsed time
  b = begin
  c = change == ending - beginning
  d = duration (total time)
```

- easing.linear(t, b, c, d)
- easing.inQuad(t, b, c, d)
- easing.outQuad(t, b, c, d)
- easing.inOutQuad(t, b, c, d)
- easing.inCubic(t, b, c, d)
- easing.outCubic(t, b, c, d)
- easing.inOutCubic(t, b, c, d)
- easing.defoutInCubic(t, b, c, d)
- easing.inQuart(t, b, c, d)
- easing.outQuart(t, b, c, d)
- easing.inOutQuart(t, b, c, d)
- easing.outInQuart(t, b, c, d)
- esinsg.inQuint(t, b, c, d)
- easing.outQuint(t, b, c, d)
- easing.inOutQuint(t, b, c, d)
- easing.outInQuint(t, b, c, d)
- easing.in[Out]Sine(t, b, c, d)
- easing.in[Out]Expo(t, b, c, d)
- easing.in[Out]Circ(t, b, c, d)
- easing.in[Out]Elastic(t, b, c, d)
- easing.in[Out]Bounce(t, b, c, d)


## Graphics

- RGB(R: Int8 ,G: Int8 ,B: Int8, [A: Float]): Tuple - returns RGB or RGBA in float values. To be used with Cairo
- load_css(path: __file__, filename: String): load styles from file
