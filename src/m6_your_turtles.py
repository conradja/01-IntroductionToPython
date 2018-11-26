"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Joseph Conrad.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(10)

turtle_blue = rg.SimpleTurtle('turtle')
turtle_green = rg.SimpleTurtle('turtle')
turtle_blue.pen = rg.Pen('blue', 1)
turtle_green.pen = rg.Pen('green', 1)

turtle_green.speed = 15
turtle_blue.speed = 10
angle=90
move_forward = 200
for x in range(100):
    turtle_green.forward(move_forward)
    turtle_blue.forward(move_forward)
    turtle_green.left(angle+5)
    turtle_blue.left(angle)
    angle-=0.5
    move_forward-=1



window.close_on_mouse_click()

