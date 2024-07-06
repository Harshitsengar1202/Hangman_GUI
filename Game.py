import pygame
import os

##########WINDOW#########################
pygame.init()
WIDTH,HEIGHT=800,500
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!!")



################IMAGES##############
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)



##############GAME VARIABLES###########
hangman_status=0



############COLORS###########
WHITE=(255,255,255)




#################FPS################
FPS =90
clock=pygame.time.Clock()
run=True

###############MAINLOOP############

while run:
    clock.tick(FPS)
    win.fill(WHITE)
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            print(pos)

pygame.quit()