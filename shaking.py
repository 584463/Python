import simplegui, random
x = 300
y = 300


eye_y = 300 - 25

x_speed = 1
y_speed = 5
eye_speed = 1

color = "Yellow"
count = 0


def draw_handler(canvas):
    global x, y, y_speed, x_speed, color, count, eye_y, eye_speed
    canvas.draw_circle((x, y), 100, 3, color, color)
    canvas.draw_circle((x + 40, y - 25), 20, 3, 'Black', 'White')
    canvas.draw_circle((x + 40, y), 10, 3, 'Black', 'White')
    canvas.draw_circle((x - 40, y -25), 20, 3, 'Black', 'White')
    canvas.draw_circle((x - 40, y), 10, 3, 'Black', 'White')
    canvas.draw_circle((x, y + 50), 15, 3, 'Black', 'Black')

    
    
    x += 1
    y += y_speed

    if y > 350 or y < 250:
        y_speed *= -1
        
    if eye_y > 350 or eye_y < y - 25 - 20:
       eye_speed *= -1  
    
    
    if random.random() < .01:
        x_speed *= -1
        
        
    if count == 100:
        color = "Red"
        x_speed *= 10
        y_speed *= 10

frame = simplegui.create_frame('lol', 600, 600)
frame.set_draw_handler(draw_handler)
frame.start()
