#imports
import pygame
import sys
import os
import time

#Creates window
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Breakout")

#Variables
px = 300
x = 300
y = 250
mody = -1
modx = -.5
boxes = 20
score = "0"
game_score_font = pygame.font.SysFont("Verdana",30)
font_color = (255,255,255)
lives = 5
speed =10
boxes =[]
cp=50
for col in range(5):
    rp = 5
    for row in range(15):
        box = pygame.draw.rect(screen, (255,255,255), [(rp,cp),(30,15)])
        boxes.append(box)
        rp+=40
    cp+=25

#While Running
running  = True
while running:

    #Creates the base map
    screen.fill((100,100,100))

    #Draws the score
    formated_score = game_score_font.render(score, True, font_color)
    screen.blit(formated_score, (500, 0))

    #Draws the lives
    pos = 10
    for live in range(lives):
        pygame.draw.circle(screen, (0,0,0), (pos, 15), 7)
        pos += 20

    #Draws the paddle
    paddle = pygame.draw.rect(screen, (255,255,255), [(px,375),(70,13)])

    #Draws the ball
    ball = pygame.draw.circle(screen, (0,0,0), (x,y), 7)

    #Draws the boxes
    for box in boxes:
        pygame.draw.rect(screen, (255,255,255), [(box.topleft), (30,15)])

        #Manages collision with ball
        if ball.colliderect(box):
            boxes.remove(box)
            mody *=-1
            score = str(int(score) + 50)
            if boxes == []:
                cp=50
                for col in range(5):
                    rp = 5
                    for row in range(15):
                        box = pygame.draw.rect(screen, (255,255,255), [(rp,cp),(30,15)])
                        boxes.append(box)
                        rp+=40
                    cp+=25
                lives +=1
                speed +=1
                
    #Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Checks for key presses
    key_presses = pygame.key.get_pressed()
    if key_presses[pygame.K_LEFT]:
        if px > 0:
            px -= 2
    if key_presses[pygame.K_RIGHT]:
        if px < 530:
            px += 2

    #Updates ball position
    if ball.colliderect(paddle):
        mody *=-1
        if x <= px+35:
            modx = 2
        if x > px +35 and x < px+70:
            modx = -2

    #Reacts to ball and frame position
    if y > 400:
        x = 300
        y = 200
        modx = 0
        lives -=1
    if y < 0:
        mody *=-1
    if x > 600 or x < 0:
        modx *=-1
    x -= modx
    y -= mody

    #Ends game if the lives reach 0
    if lives <=0:
        running = False

    pygame.display.flip()

pygame.quit()
