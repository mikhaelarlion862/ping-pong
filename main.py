from pygame import *


width = 600
height = 500

window = display.set_mode((width, height))
display.set_caption('sebuah permainan kasual yang bernama: ping-pong')

background_color = (38, 163, 214)
window.fill(background_color)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game == False

    window.fill(background_color)
    display.update()



