import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

display_surfase=pygame.display.set_mode((WIDTH,HEIGHT))#create a screen
pygame.display.set_caption("Birthday")#this creates a title
img=pygame.image.load("lesson 4/image/backgroundone.jpg")
image=pygame.transform.scale(img, (WIDTH,HEIGHT))#this sets the image

while True:
    font=pygame.font.SysFont("Times New Roman",78)
    text=font.render("Happy",True,(255,0,0))
    text2=font.render("Birthday",True,(0,255,255))

    display_surfase.fill((255,255,255))#this adds white color
    display_surfase.blit(image,(0,0))#this adds image

    display_surfase.blit(text,(210,180))#this will add happy
    display_surfase.blit(text2,(180,264))#this will add birthday

    pygame.display.update()
    time.sleep(2)#this will pause screen for 2 seconds
    image2=pygame.image.load("lesson 4/image/backgroudtwo.jpg")
    font=pygame.font.SysFont("Georgia",38)

    text3=font.render("I am not happy that you are born!",True,(255,255,0))
    display_surfase.fill((255,255,255))
    display_surfase.blit(image2,(0,0))
    display_surfase.blit(text3,(30,30))

    pygame.display.update()
    time.sleep(2)
    image3=pygame.image.load("lesson 4/image/backgroundthree.jpg")
    font=pygame.font.SysFont("Arial Nova Bold",50)

    text4=font.render("You WILL EAT THIS CAKE!",True,(0,0,0))
    display_surfase.fill((255,255,255))
    display_surfase.blit(image3,(0,0))
    display_surfase.blit(text4,(30,30))

    pygame.display.update()
    time.sleep(2)



