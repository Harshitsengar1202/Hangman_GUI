import pygame
import math
import random

#############WINDOW#########################

pygame.init()
WIDTH,HEIGHT = 850, 500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!!")

################IMAGES##################

images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

##############GAME VARIABLES################

hangman_status = 0
words = [
'THEGODFATHER', 'FORRESTGUMP', 'THEDARKNIGHT', 'VERTIGO',
'SOMELIKEITSHOT',
'AHARDDAYSNIGHT', 'INCEPTION', 'INTERSTELLAR', 'THEMATRIX', 'PULPFICTION',
'FIGHTCLUB', 'THEDEPARTED', 'THEPRESTIGE',
'THEREVENANT', 'DUNKIRK', 'JOKER',
'THEBIGLEBOWSKI', 'SNATCH', 'GLADIATOR', 'WHIPLASH',
'MEMENTO', 'CHILDRENOFMEN',
'SKYFALL', 'ARRIVAL', 'BABYDRIVER'
]
#words="DEVELOPER"
word=random.choice(words)
guessed=[]

#############BUTTONS###################

RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A+i), True])

#################COLORS###################

WHITE = (255,255,255)
BLACK = (0,0,0)

########################FONTS#####################

LETTER_FONT = pygame.font.SysFont('comicsans', 32)
WORD_FONT = pygame.font.SysFont('comicsans', 45)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

#################FPS######################

FPS = 90
clock = pygame.time.Clock()
run = True

###################MESSAGEFUNCTION###########

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message,1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2, HEIGHT/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    
#############DRAWFUNCTION################

def draw():
    win.fill(WHITE)

    #################TITLE################

    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 5))

    #############DRWAWORD##################

    display_word=""
    for letter in word:
        if letter in guessed:
            display_word+= letter + " "
        else:
            display_word+="_ "
    text = WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(300,200))

    ###############DRAWBUTTONS#################
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text,(x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (90,100))
    pygame.display.update()

###############MAINLOOP##################

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis<RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
    draw()
    won=True
    for letter in word:
        if letter not in guessed:
            won=False
            break
    
    if won:
        display_message("YOU WON!!!")
        break

    if hangman_status == 6:
        display_message("YOU LOST!!")
        break

pygame.quit()