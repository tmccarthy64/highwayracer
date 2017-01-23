####### Highway Racer
####### Tim McCarthy

import pygame
import time
import random

pygame.init()

# game dimensions
display_width = 800
display_height = 600
car_width = 70

# colors
black = (0,0,0)
white = (255,255,255)
carblue = (43,51,162)
red = (255,0,0)
startgamecolor = (0,119,113)
startgamelightercolor = (0,149,141)
introquitcolor = (22,97,54)
introquitlightcolor = (32,142,79)
street_yellow = (255,242,0)
pause = True

# lists
scores = [0]


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Highway Racer")
clock = pygame.time.Clock()

# Image files
iconImg = pygame.image.load('icon.png')
carImg = pygame.image.load('car.png')
streetImg = pygame.image.load('street.png')
introImg = pygame.image.load('intro.png')
crashImg = pygame.image.load('crash.png')
level_one_icon = pygame.image.load('level_one_icon.png')
level_one_thing = pygame.image.load('level_one_thing.png')
racing_flag = pygame.image.load('racingflag.png')
level_two_backdrop = pygame.image.load('level_two_backdrop.png')
level_two_trees = pygame.image.load('level_two_trees.png')
level_two_crab = pygame.image.load('level_two_crab.png')
level_two_icon = pygame.image.load('level_two_icon.png')

pygame.display.set_icon(iconImg)


# audio files
#crashSound = pygame.mixer.Sound("crash.mp3")
pygame.mixer.music.load("gamemusic.mp3")

# score count
def things_dodged(count):
    font = pygame.font.Font('racingfont.ttf', 15)
    text = font.render('Score: '+str(count), True, black)
    gameDisplay.blit(text, (5,95))

# high score
def high_score(count):
    font = pygame.font.Font('racingfont.ttf', 15)
    text = font.render('High Score: '+str(count), True, black)
    gameDisplay.blit(text, (5,125))

# image related items
def things(img,thingx, thingy, thingw, thingh):
    gameDisplay.blit(img,[thingx,thingy,thingw,thingh])

# items drawn to the screen
def scene_things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

# main car for the game
def car(img,x,y):
    gameDisplay.blit(img,(x,y))

# default text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('racingfont.ttf',90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    level_one_loop()

# crash sequence
def crash():

    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crashSound)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(crashImg,(0,0))
        largeText = pygame.font.Font('racingfont.ttf',60)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play Again",225,300,150,50,startgamelightercolor,startgamecolor, level_select_loop)
        button("Quit Game",450,300,150,50,introquitlightcolor,introquitcolor, quitgame)

        pygame.display.update()

        clock.tick(15)

# layout for buttons
def button(msg,x,y,w,h,i,a,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, i, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, a, (x,y,w,h))
    smallText = pygame.font.Font("racingfont.ttf", 15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)),(y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

# layout for image buttons
def imgbutton(img,x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        gameDisplay.blit(img,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        gameDisplay.blit(img,(x,y,w,h))
    #smallText = pygame.font.Font("racingfont.ttf", 15)
    #textSurf, textRect = text_objects(msg, smallText)
    #textRect.center = ( (x+(w/2)),(y+(h/2)) )
    #gameDisplay.blit(textSurf, textRect)

# quit
def quitgame():
    pygame.quit()
    quit()

# unpause game
def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()

# pause screen
def pause():
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font('racingfont.ttf',75)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",250,300,100,50,startgamelightercolor,startgamecolor, unpause)
        button("Quit Game",450,300,100,50,introquitlightcolor,introquitcolor, quitgame)

        pygame.display.update()

        clock.tick(15)


# level complete screen
def level_complete():

    while level_complete:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font('racingfont.ttf',60)
        TextSurf, TextRect = text_objects("Level Completed", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("Levels",150,300,100,50,startgamelightercolor,startgamecolor, level_select_loop)
        button("Start Menu",350,300,100,50,startgamelightercolor,startgamecolor, game_intro)
        button("Quit Game",550,300,100,50,introquitlightcolor,introquitcolor, quitgame)

        pygame.display.update()

        clock.tick(15)

# game start menu/ intro screen
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(introImg,(0,0))
        largeText = pygame.font.Font('racingfont.ttf',60)
        TextSurf, TextRect = text_objects("Highway Racer", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start Game",200,300,150,50,startgamelightercolor,startgamecolor, level_select_loop)
        button("Quit Game",450,300,150,50,introquitlightcolor,introquitcolor, quitgame)

        pygame.display.update()

        clock.tick(15)

# level select page
def level_select_loop():

    level_select = True

    while level_select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
        gameDisplay.fill(white)
        #gameDisplay.blit(introImg,(0,0))
        largeText = pygame.font.Font('racingfont.ttf',60)
        TextSurf, TextRect = text_objects("PICK A LEVEL", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)

        imgbutton(level_one_icon,100,200,100,100,level_one_loop)
        imgbutton(level_two_icon,300,200,100,100,level_two_loop)


        pygame.display.update()

        clock.tick(15)

# first level loop
def level_one_loop():

    #pygame.mixer.music.play(-1)

    global scores


    x = (display_width * 0.3)
    y = (display_height * 0.75)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(200, display_width - 200)
    thing_starty = -600
    thing_speed = 2
    thing_width = 50
    thing_height = 50
    flag_speed = 0
    flag_width = 350
    flag_height = 50
    flagy = -10 - flag_height
    flagx = 225
    scene_thing_speed = 2
    scene_thingx = 375
    scene_thing_width = 50
    scene_thing_height = 120
    scene_thing_oney = display_height - scene_thing_height
    scene_thing_twoy = (scene_thing_oney - scene_thing_height) - scene_thing_height
    scene_thing_threey = (scene_thing_twoy - scene_thing_height) - scene_thing_height
    scene_thing_foury = (scene_thing_threey - scene_thing_height) - scene_thing_height

    dodged = 0

    game_Exit = False

    while not game_Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change += -5
                elif event.key == pygame.K_DOWN:
                    y_change += 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.blit(streetImg, (0,0))
        scene_things(scene_thingx, scene_thing_oney, scene_thing_width, scene_thing_height, street_yellow)
        scene_things(scene_thingx, scene_thing_twoy, scene_thing_width, scene_thing_height, street_yellow)
        scene_things(scene_thingx, scene_thing_threey, scene_thing_width, scene_thing_height, street_yellow)
        scene_things(scene_thingx, scene_thing_foury, scene_thing_width, scene_thing_height, street_yellow)
        scene_thing_oney += scene_thing_speed
        scene_thing_twoy += scene_thing_speed
        scene_thing_threey += scene_thing_speed
        scene_thing_foury += scene_thing_speed
        things(racing_flag,flagx, flagy, flag_width, flag_height)
        flagy += flag_speed
        things(level_one_thing, thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed
        car(carImg,x,y)
        things_dodged(dodged)
        high_score(max(scores))
        button("Start Menu",5,5,150,30,startgamelightercolor,startgamecolor, game_intro)
        button("Pause Game",5,45,150,30,startgamelightercolor,startgamecolor, pause)

        if x > (display_width - 200) -  car_width or x < 200:
            crash()

        if y > display_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(200, (display_width - 200) - thing_width)
            dodged += 1
            thing_speed += 1
            scores.append(dodged)

        if scene_thing_oney > display_height:
            scene_thing_oney = (scene_thing_foury - scene_thing_height) - scene_thing_height
            scene_thing_speed += 0.05
        if scene_thing_twoy > display_height:
            scene_thing_twoy = (scene_thing_oney - scene_thing_height) - scene_thing_height
            scene_thing_speed += 0.05
        if scene_thing_threey > display_height:
            scene_thing_threey = (scene_thing_twoy - scene_thing_height) - scene_thing_height
            scene_thing_speed += 0.05
        if scene_thing_foury > display_height:
            scene_thing_foury = (scene_thing_threey - scene_thing_height) - scene_thing_height
            scene_thing_speed += 0.05
        if y < thing_starty + thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:

                crash()

        if max(scores) == 18:
            flag_speed = 5

        if y < flagy + flag_height:
            level_complete()




        pygame.display.update()
        clock.tick(60)

def level_two_loop():

    #pygame.mixer.music.play(-1)

    global scores


    x = (display_width / 2 )
    y = (display_height * 0.75)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(270, display_width - 150)
    thing_starty = -600
    thing_speed = 2
    thing_width = 50
    thing_height = 50
    flag_speed = 0
    flag_width = 350
    flag_height = 50
    flagy = -10 - flag_height
    flagx = 280
    scene_thing_speed = 2
    scene_thing_width = 224
    scene_thing_height = 599
    scene_thingx = display_width - scene_thing_width
    scene_thing_oney = 0
    scene_thing_twoy = scene_thing_oney - scene_thing_height

    dodged = 0

    game_Exit = False

    while not game_Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change += -5
                elif event.key == pygame.K_DOWN:
                    y_change += 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.blit(level_two_backdrop, (0,0))
        things(level_two_trees, scene_thingx, scene_thing_oney, scene_thing_width, scene_thing_height)
        things(level_two_trees, scene_thingx, scene_thing_twoy, scene_thing_width, scene_thing_height)
        scene_thing_oney += scene_thing_speed
        scene_thing_twoy += scene_thing_speed
        things(racing_flag,flagx, flagy, flag_width, flag_height)
        flagy += flag_speed
        things(level_two_crab, thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed
        car(carImg,x,y)
        things_dodged(dodged)
        high_score(max(scores))
        button("Start Menu",5,5,150,30,startgamelightercolor,startgamecolor, game_intro)
        button("Pause Game",5,45,150,30,startgamelightercolor,startgamecolor, pause)

        if x > (display_width - 150) -  car_width or x < 250:
            crash()

        if y > display_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(270, (display_width - 150) - thing_width)
            dodged += 1
            thing_speed += 1
            scores.append(dodged)

        if scene_thing_oney > display_height:
            scene_thing_oney = scene_thing_twoy - scene_thing_height
            scene_thing_speed += 0.05
        if scene_thing_twoy > display_height:
            scene_thing_twoy = scene_thing_oney - scene_thing_height
            scene_thing_speed += 0.05

        if y < thing_starty + thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:

                crash()

        if max(scores) == 18:
            flag_speed = 5

        if y < flagy + flag_height:
            level_complete()

        pygame.display.update()
        clock.tick(60)

game_intro()
level_one_loop()
level_two_loop
pygame.quit()
quit()
