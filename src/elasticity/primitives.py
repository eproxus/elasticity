from pyglet.graphics import vertex_list_indexed
from pyglet.graphics import Batch
from pyglet.gl import GL_LINE_LOOP

class Box:
    def __init__(self,
                 position = (0,0),
                 size =     (1,1),
                 anchor =   (0,0),
                 batch = Batch()):
        
        self.position = position
        self.size = size
        self.anchor = anchor
        self.batch = batch
        
        x0 = position[0] - anchor[0] - size[0] / 2
        y0 = position[1] - anchor[1] - size[1] / 2
        x1, y1 = x0 + size[0], y0 + size[1]
        
        self.batch.add_indexed(4, GL_LINE_LOOP, None,
                               [0,1,
                                1,2,
                                2,3,
                                3,0,
                                0,2,  # Cross
                                1,3], # Cross
                                ('v2i', (x0,y0,
                                         x1,y0,
                                         x1,y1,
                                         x0,y1)))
        
    def draw(self):
        self.batch.draw()