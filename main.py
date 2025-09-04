from pygame import *


width = 600
height = 500

window = display.set_mode((width, height))
display.set_caption('sebuah permainan kasual yang bernama: ping-pong')

background_color = (38, 163, 214)
window.fill(background_color)

class GameSprite(sprite.Sprite):
 #class constructor
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #call for the class (Sprite) constructor:
       sprite.Sprite.__init__(self)


       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #every sprite must have the rect property that represents the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #method drawing the character on the window
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   #method to control the sprite with arrow keys
   def move_p1(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < height - 80:
           self.rect.y += self.speed

   def move_p2(self):
       keys = key.get_pressed()
       if keys[K_a] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_d] and self.rect.y < height - 80:
           self.rect.y += self.speed

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 FAILED!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 FAILED!', True, (180, 0, 0))

p1 = Player('racket.png',30, 200, 30, 100, 5)
p2 = Player('racket.png',520, 200, 30, 100, 5)
ball = GameSprite('tenis_ball.png', 250, 300, 50, 50, 5)

clock = time.Clock()

speed_x = 3
speed_y = 3

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game == False

    if finish != True:
        window.fill(background_color)

        p1.reset()
        p2.reset()
        ball.reset()

        p1.move_p1()
        p2.move_p2()

    #bola bergerk di awl
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (200, 200))

    display.update()
    clock.tick(60)









