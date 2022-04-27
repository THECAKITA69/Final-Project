# Your name here
import pygame, pgzrun, numpy

WIDTH = 400
HEIGHT = 400

score = 0
game_over = False

horse = Actor("horse")
horse.png = (100, 100)

#cactus = Actor("captus")
#cactus.png = (100, 100)

apple = Actor("apple")
apple.png = (200, 200)

def draw():
    screen.fill("green")
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
   
    horse.draw()
    apple.draw()
    #cactus.draw()
    

    if game_over == True:
        screen.fill("blue")
        screen.draw.text("Score: " + str(score), color="black", center=(WIDTH/2,HEIGHT/2+20))
        screen.draw.text("Game Over!! " + str(), color="black", center=(WIDTH/2,HEIGHT/2))

def place_apple():
    apple.pos = (numpy.random.randint(20, WIDTH - 20),numpy.random.randint(20, HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    if keyboard.left and horse.x > 0:
        horse.x -= 5
    elif keyboard.right and horse.x < WIDTH:
        horse.x += 5
    elif keyboard.down and horse.y < HEIGHT:
        horse.y += 5
    elif keyboard.up and horse.y > 0:
        horse.y -= 5

    if horse.colliderect(apple):
        add_score()

def add_score():
    global score
    score += 1
    place_apple()

place_apple()
clock.schedule(time_up,10.0)

# this will make the game start!
pgzrun.go()


