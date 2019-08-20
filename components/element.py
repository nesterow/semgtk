from .styles import load_css

#@abstract
class SettingsChain:
    
    #= pack arguments for Gtk.Box
    def pack(self, position = [0,0,0]):
        self.args = position
        return self
    
    #= fill available space, 
    #- for horisontal layout: xy = height, yx = with
    #- for vertical layout: xy = width, yx = height 
    def expand(self, xy = True, yx = True):
        self.args [0] = xy
        self.args [1] = yx
        return self

    #= set padding inside row
    def padding(self, padding = 0):
        self.args [2] = padding
        return self
    
    #= set css selector id
    def cssId(self, name):
        self.set_name(name)
        return self

    

def Element(cls):
    class Widget(cls, SettingsChain):
        def __init__(self, *k, **kv):
            try:
                super().__init__(self, *k, **kv)
            except:
                super().__init__()
            self.args = [0,0,0]   
    return Widget
