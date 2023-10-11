import simplegui

y = 270
xchange = 25
def draw_handler(canvas):
    global y, xchange
    if y >100:
       y-=1
    elif xchange < 100:
        xchange += 1
        
    canvas.draw_circle((300, 300), 100, 5, 'white', "yellow")   
    canvas.draw_circle((300-xchange, y), 20, 10, 'white', "black") 
    canvas.draw_circle((300+xchange, y), 20, 10, ' white', "black")
    canvas.draw_circle((2+xchange, y), 20, 10, ' white', "black")
    canvas.draw_circle((300, 350), 20, 10, ' black', "black")
    canvas.draw_polygon([(330, 350), (270, 350), (300, 300)], 12, 'yellow', 'yellow')
        
frame = simplegui.create_frame('Testing', 600, 600)
frame.set_draw_handler(draw_handler)
frame.start()
