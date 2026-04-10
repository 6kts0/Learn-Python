import glfw
from OpenGL.GL import *

if not glfw.init():
    raise Exception('GLFW could not be initialized')

# Create window
window = glfw.create_window(800, 600, "OpenGL Window", None, None)
if not window:
    glfw.terminate()
    raise Exception('GLFW window could not be opened')

# Make the OpenGL window context current 
glfw.make_context_current(window)

# Set screen color and clear screen loop
while not glfw.window_should_close(window):
    glClearColor(0.2, 0.3, 0.5, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glfw.swap_buffers(window) # Swap front and back buffers
    glfw.poll_events() # Check for keyboard and mouse events

# Kill prog
glfw.terminate()