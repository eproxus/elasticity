import pyglet
from pyglet import window
from pyglet.window import key

class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__()
        self.fps_display = pyglet.clock.ClockDisplay()
        self.fps = False
        
    def on_draw(self):
        self.clear()
        if self.fps:
            self.fps_display.draw()
        self.label.draw()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == key.F11:
            self.set_fullscreen(not self.fullscreen)
        elif symbol == key.F9:
            self.fps = not self.fps
        elif symbol == key.ESCAPE:
            self.close()

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
