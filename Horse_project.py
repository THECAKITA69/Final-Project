# Your name here
import pygame, pgzrun, numpy

WIDTH = 475
HEIGHT = 399

score = 0
game_over = False



class Horse:

    def __init__(self, image, lives) -> None:
        self.lives = lives

        self.actor = Actor(image)
        self.actor.png = (100, 100)

horse = Horse("horse", lives = 3)

cactus = Actor("cactus")
cactus.png = (100, 100)

apple = Actor("apple")
apple.png = (200, 200)

def draw():
    screen.blit("background", (0, 0))
    screen.draw.text(" " + str(score), color="black", topleft=(30, 12))
    screen.draw.text(" " + str(horse.lives), color="black", topleft=(87, 10))
   
   #Draw the counters
    screen.blit("applescore", (0, 0))
    screen.blit("lives", (55, 8))


    horse.actor.draw()
    apple.draw()
    cactus.draw()
    

    if game_over == True:
        screen.blit("gameoverback")
        screen.draw.text("Score: " + str(score), color="black", center=(WIDTH/2,HEIGHT/2+20))
        screen.draw.text("Game Over!! " + str(), color="black", center=(WIDTH/2,HEIGHT/2))

def place_apple():
    apple.pos = (numpy.random.randint(20, WIDTH - 20),numpy.random.randint(20, HEIGHT - 20))

def place_cactus():
    cactus.pos = (numpy.random.randint(20, WIDTH - 20),numpy.random.randint(20, HEIGHT - 20))


def time_up():
    global game_over
    game_over = True
        

#Allows the actor move when kerborad is click
def update():
    if keyboard.left and horse.actor.x > 0:
        horse.actor.x -= 5
    elif keyboard.right and horse.actor.x < WIDTH:
        horse.actor.x += 5
    elif keyboard.down and horse.actor.y < HEIGHT:
        horse.actor.y += 5
    elif keyboard.up and horse.actor.y > 0:
        horse.actor.y -= 5

    if horse.actor.colliderect(apple):
        add_score()

def subtract_lives():
    global lives

    if horse.actor.colliderect(cactus):     
        lives -= 1

    if lives == 0:
        game_over == True

#Everytime time that the actor touch the apple it will add it to scores
def add_score():
    global score

    score += 1
    place_apple()

place_apple()

place_cactus()
clock.schedule_interval(place_cactus,1.0)

# this will make the game start!
pgzrun.go()


