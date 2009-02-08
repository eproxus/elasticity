import pyglet

from pyglet.gl import Config
from pyglet.gl import glu_info

from pyglet.graphics import Batch

from pyglet.window import key

from pyglet.text import Label

from pyglet.clock import ClockDisplay

from elasticity.primitives import Box

class ElasticityWindow(pyglet.window.Window):
    def __init__(self, config = Config()):
        super(ElasticityWindow, self).__init__(config = Config(sample_buffers = 1,
                                                     samples = 4, 
                                                     depth_size = 16,
                                                     double_buffer = True),
                                     caption = "Elasticity")
        
        self.fps_display = ClockDisplay()
        self.fps = False
        self.scene = Batch()
        
    def on_draw(self):
        self.clear()
        
        if self.fps:
            self.fps_display.draw()
            
        self.scene.draw()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == key.F11:
            self.set_fullscreen(not self.fullscreen)
        elif symbol == key.F9:
            self.fps = not self.fps
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

if __name__ == '__main__':
    window = ElasticityWindow()
    
    label = Label('elasticity',
                  font_name = 'default',
                  font_size = 24,
                  x = window.width / 2,
                  y = window.height / 2,
                  anchor_x = 'center',
                  anchor_y = 'center',
                  batch = window.scene)
   
    box = Box(position = (window.width / 2, window.height / 2 - 100),
              size = (100,100),
              batch = window.scene)

    pyglet.app.run()