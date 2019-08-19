
#@abstract
class Extension:
    
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

    

def Element(cls):
    class Widget(cls, Extension):
        def __init__(self, *k, **kv):
            super().__init__(self, *k, **kv)
            self.args = [0,0,0]   
    return Widget
