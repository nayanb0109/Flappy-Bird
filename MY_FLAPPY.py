import time
import pygame
import sys
import random
import os

def themes(BG_SURF,BIRD_SURFACE,BASE_FLOOR):
    global BIRD_FRAME
    theme = True
    PIPE_SURF = pygame.image.load('gallery/sprites/pipe.png').convert_alpha()

    while theme:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    theme = False


        SCREEN.fill((255, 255, 255))
        SCREEN.blit(BG_SURF, (0, 0))
        SCREEN.blit(BIRD_SURFACE, (100, 200))
        SCREEN.blit(BASE_FLOOR, (0, SCREEN_HEIGHT * 0.8))
        if night_button.draw() == True:
            print("NIGHT SKIN")
            BG_SURF = pygame.image.load('gallery/sprites/background(04).png').convert_alpha()

        if back_button.draw() == True:
            theme = False

        if day_button.draw() == True:
            print("DAY SKIN")
            BG_SURF = pygame.image.load('gallery/sprites/background.png').convert_alpha()

        if next_button.draw() == True:
            BIRD_UP = pygame.image.load('gallery/sprites/white_up.png').convert_alpha()
            BIRD_MID = pygame.image.load('gallery/sprites/white_mid.png').convert_alpha()
            BIRD_DOWN = pygame.image.load('gallery/sprites/white_down.png').convert_alpha()
            BIRD_FRAME = [BIRD_UP, BIRD_MID, BIRD_DOWN]
            BIRD_SURFACE = BIRD_FRAME[BIRD_INDEX]
            BIRD_RECT = BIRD_SURFACE.get_rect(center=(110, 200))
            SCREEN.blit(BIRD_SURFACE,(135,200))
            print('WHITE BIRD')

        if previous_button.draw() == True:
            BIRD_UP = pygame.image.load('gallery/sprites/blue_up.png').convert_alpha()
            BIRD_MID = pygame.image.load('gallery/sprites/blue_mid.png').convert_alpha()
            BIRD_DOWN = pygame.image.load('gallery/sprites/blue_down.png').convert_alpha()
            BIRD_FRAME = [BIRD_UP,BIRD_MID,BIRD_DOWN]
            BIRD_SURFACE = BIRD_FRAME[BIRD_INDEX]
            BIRD_RECT = BIRD_SURFACE.get_rect(center=(110, 200))
            SCREEN.blit(BIRD_SURFACE, (135, 200))
            print('BLUE BIRD')

        if base_next_button.draw() == True:
            BASE_FLOOR=pygame.image.load('gallery/sprites/base-red.png').convert_alpha()
            PIPE_SURF = pygame.image.load('gallery/sprites/pipe-red.png').convert_alpha()


        if base_previous_button.draw() == True:
            BASE_FLOOR=pygame.image.load('gallery/sprites/base.png').convert_alpha()
            PIPE_SURF = pygame.image.load('gallery/sprites/pipe.png').convert_alpha()


        pygame.display.update()
    return BG_SURF,BIRD_SURFACE,BASE_FLOOR,PIPE_SURF,BIRD_FRAME
def pause():
    Pause = True
    pause_surface = button_font.render('PAUSE', True, (0, 0, 0))
    pause_rect = pause_surface.get_rect(center=(140, 450))
    SCREEN.blit(pause_surface, pause_rect)
    #delay_pipe = 100000
    # # UPDATE FRAMES
    # pygame.time.set_timer(SPAWNPIPE, 0)
    pygame.display.update()
    CLOCK.tick(FPS)
    while Pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Pause = False
                    pygame.time.set_timer(SPAWNPIPE,1500)
        print('PAUSE')

def draw_base_floor():
    SCREEN.blit(BASE_FLOOR, (BASE_X_POSTI, BASE_Y_POSTI))
    SCREEN.blit(BASE_FLOOR, (BASE_X_POSTI+325, BASE_Y_POSTI))

def create_pipe():
    PIPE_HEIGHT = PIPE_SURF.get_height()
    OFFSET = SCREEN_HEIGHT/3
    Y2=OFFSET+random.randrange(0,int(SCREEN_HEIGHT-BASE_FLOOR.get_height()-1.2*OFFSET))
    PIPE_X = SCREEN_WIDTH+10
    Y1=PIPE_HEIGHT-Y2+OFFSET
    TOP_PIPE_RECT = PIPE_SURF.get_rect(topleft=(PIPE_X,-Y1 ))
    BOTTOM_PIPE_RECT = PIPE_SURF.get_rect(topleft = (PIPE_X,Y2))
    return BOTTOM_PIPE_RECT,TOP_PIPE_RECT

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if  pipe.bottom>=490:
            SCREEN.blit(PIPE_SURF,pipe)
        else:
            FLIP_PIPE = pygame.transform.flip(PIPE_SURF,False,True)
            SCREEN.blit(FLIP_PIPE, pipe)

    return pipes

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird,-BIRD_MOVMENT*3,1)
    return new_bird

def bird_animation(BIRD_FRAME):
    new_bird = BIRD_FRAME[BIRD_INDEX]
    new_bird_rect = new_bird.get_rect(center = (100,BIRD_RECT.centery))
    return new_bird,new_bird_rect

def check_collision(pipes):
   for pipe in pipes:
       if BIRD_RECT.colliderect(pipe):
           hit_sound.play()
           return False
   if BIRD_RECT.top <=-50:
       hit_sound.play()
       return False
   if BIRD_RECT.bottom>=BASE_Y_POSTI:
       hit_sound.play()
       return False
   return True

def welcome(BG_SURF,BIRD_SURFACE,BASE_FLOOR):
    # bird_up = pygame.image.load('gallery/sprites/blue_up.png').convert_alpha()
    # bird_mid = pygame.image.load('gallery/sprites/blue_mid.png').convert_alpha()
    # bird_down = pygame.image.load('gallery/sprites/blue_down.png').convert_alpha()
    # bird_frame = [bird_up, bird_mid, bird_down]
    # BIRD_SURFACE = bird_frame[BIRD_INDEX]
    # BASE_FLOOR = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    # BG_SURF = pygame.image.load('gallery/sprites/background.png').convert_alpha()
    global BIRD_FRAME, PIPE_SURF
    while True:
        for event in pygame.event.get():
            # QUIT CONTROLS
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #     reverse_gravity = False
            #     return reverse_gravity

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            #     reverse_gravity = True
            #     return reverse_gravity

            else:
                SCREEN.blit(BG_SURF, (0, 0))
                SCREEN.blit(MESSAGE, (50, 50))
                SCREEN.blit(BIRD_SURFACE,(100,200))
                SCREEN.blit(BASE_FLOOR,(0,SCREEN_HEIGHT*0.8))
                if reverse_button.draw() == True:
                    reverse_gravity = True
                    return reverse_gravity,BG_SURF,BIRD_SURFACE,BASE_FLOOR,PIPE_SURF,BIRD_FRAME
                if normal_button.draw()== True:
                    reverse_gravity = False
                    return reverse_gravity,BG_SURF,BIRD_SURFACE,BASE_FLOOR,PIPE_SURF,BIRD_FRAME
                if theme_button.draw() == True:
                    BG_SURF,BIRD_SURFACE,BASE_FLOOR,PIPE_SURF,BIRD_FRAME=themes(BG_SURF,BIRD_SURFACE,BASE_FLOOR)

                # UPDATE FRAMES
                pygame.display.update()
                CLOCK.tick(FPS)
                #return

def transition():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            SCREEN.blit(BASE_FLOOR, (0, SCREEN_HEIGHT * 0.8))


            if event.type==pygame.KEYDOWN and event.key == pygame.K_1:
               #NIGHT SKIN I.E RED PIPED,NIGHT BG,RED BASE,BROWN BIRD,
               BG = pygame.image.load('gallery/sprites/background(04).png')
               PS =  pygame.image.load('gallery/sprites/pipe-red.png')
               BASE = pygame.image.load('gallery/sprites/base-red.png').convert_alpha()
               bird_up =pygame.image.load('gallery/sprites/white_up.png').convert_alpha()
               bird_mid=pygame.image.load('gallery/sprites/white_mid.png').convert_alpha()
               bird_down=pygame.image.load('gallery/sprites/white_down.png').convert_alpha()
               bird_frame= [bird_up,bird_mid,bird_down]
               BIRD_SURFACE = bird_frame[BIRD_INDEX]
               BIRD_RECT = BIRD_SURFACE.get_rect(center=(110, 200))

               return BG,PS,BASE,bird_frame

            elif event.type==pygame.KEYDOWN and event.key == pygame.K_2:
            #DAY SKIN I.E GREEN PIPE ,DAY BG,GREEN BASE,BLUE BIRD
                BG = pygame.image.load('gallery/sprites/background.png')
                PS = pygame.image.load('gallery/sprites/pipe.png')
                bird_up = pygame.image.load('gallery/sprites/blue_up.png').convert_alpha()
                bird_mid = pygame.image.load('gallery/sprites/blue_mid.png').convert_alpha()
                bird_down = pygame.image.load('gallery/sprites/blue_down.png').convert_alpha()
                BASE = pygame.image.load('gallery/sprites/base.png').convert_alpha()
                bird_frame = [bird_up, bird_mid, bird_down]
                BIRD_SURFACE = bird_frame[BIRD_INDEX]
                BIRD_RECT = BIRD_SURFACE.get_rect(center=(110, 200))

                return BG, PS, BASE, bird_frame

def pipe_score_check():
    global SCORE
    if PIPE_LIST:

        for pipe in PIPE_LIST:

            if 93<pipe.centerx==101:
                SCORE+=1
                score_sound.play()

def score_display(game_state):
    if game_state == 'main_game':
        score_surface=game_font.render(str(int(SCORE)),True,(255,255,255))
        score_rect=score_surface.get_rect(center = (140,75))
        SCREEN.blit(score_surface,score_rect)

    if game_state == 'game_over':
        score_surface = game_font.render(f'SCORE : {(int(SCORE))}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(140, 75))
        SCREEN.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'HIGH SCORE : {int(HIGH_SCORE)}', True, (255, 255, 255))
        high_score_rect =  high_score_surface.get_rect(center=(140, 385))
        SCREEN.blit( high_score_surface,  high_score_rect)

def update_score(SCORE,HIGH_SCORE):
    file = open('High_Score.txt', 'r')
    HIGH_SCORE=int(file.read())
    file.close()
    if SCORE>HIGH_SCORE:
        file = open('High_Score.txt', 'w')
        high_score = str(SCORE)
        file.write(high_score)
        file.close()
        HIGH_SCORE=SCORE
    return HIGH_SCORE

#BASIC THINGS FOR GAMES
pygame.init()
CLOCK = pygame.time.Clock()
FPS = 32
game_font=pygame.font.Font('04B_19.ttf',25)
button_font=pygame.font.Font('cs_regular.ttf',22)
game_over_font=pygame.font.Font('cs_regular.ttf',28)


# SCREEN VARIABLES
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('FLAPPY BIRD')
BG_SURF = pygame.image.load('gallery/sprites/background.png').convert_alpha()
BASE_FLOOR = pygame.image.load('gallery/sprites/base.png').convert_alpha()
MESSAGE = pygame.image.load('gallery/sprites/message.png').convert_alpha()
BASE_X_POSTI = 0
BASE_Y_POSTI = SCREEN_HEIGHT * 0.8
GRAVITY = 0.5
BIRD_MOVMENT = 0
SCORE =0
HIGH_SCORE =0
delay=1
GAME_ACTIVE = True # GAME STATE DECLARATION
reverse_gravity = False



#BIRD VARIABLES
BIRD_UP = pygame.image.load('gallery/sprites/blue_up.png').convert_alpha()
BIRD_MID = pygame.image.load('gallery/sprites/blue_mid.png').convert_alpha()
BIRD_DOWN = pygame.image.load('gallery/sprites/blue_down.png').convert_alpha()
W_BIRD_UP = pygame.image.load('gallery/sprites/white_up.png').convert_alpha()
W_BIRD_MID = pygame.image.load('gallery/sprites/white_mid.png').convert_alpha()
W_BIRD_DOWN = pygame.image.load('gallery/sprites/white_down.png').convert_alpha()

BIRD_INDEX = 0
BIRD_FRAME = [BIRD_UP,BIRD_MID,BIRD_DOWN]
BIRD_SURFACE = BIRD_FRAME[BIRD_INDEX]

W_BIRD_FRAME = [W_BIRD_UP,W_BIRD_MID,W_BIRD_DOWN]
W_BIRD_SURFACE = W_BIRD_FRAME[BIRD_INDEX]

BIRD_RECT = BIRD_SURFACE.get_rect(center = (110,200))


BIRD_FLAP = pygame.USEREVENT+1
pygame.time.set_timer(BIRD_FLAP,100)

#PIES VARIABLES
PIPE_SURF = pygame.image.load('gallery/sprites/pipe.png').convert_alpha()
PIPE_LIST = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1500)


#SOUND FILES
death_sound = pygame.mixer.Sound('gallery/audio/die.wav')
hit_sound = pygame.mixer.Sound('gallery/audio/hit.wav')
score_sound= pygame.mixer.Sound('gallery/audio/point.wav')
swoosh_sound = pygame.mixer.Sound('gallery/audio/swoosh.wav')
flap_sound = pygame.mixer.Sound('gallery/audio/wing.wav')


class Button:
    def __init__(self,text,width,height,pos):
        #Core Attributes
        self.pressed = False
        self.action = False

        #top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#D74B4B'

        #text
        self.text_surf = button_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)


    def draw(self):
        self.action = False
        pygame.draw.rect(SCREEN,self.top_color,self.top_rect,border_radius=7)
        SCREEN.blit(self.text_surf,self.text_rect)
        self.check_click()
        return self.action

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.top_color = '#00e672'
                self.pressed = True

            elif self.pressed == True:
                 self.action = True
                 self.pressed = False
        else:
            self.top_color = '#D74B4B'
        return self.action

main_menu = Button('MAIN MENU',135,40,(75,190))
theme_button = Button('- THEME',135,40,(75,360))
restart_button = Button('RESTART',135,40,(75,240))
reverse_button=Button('REVERSE',135,40,(75,250))
normal_button=Button('NORMAL',135,40,(75,310))
day_button=Button('DAY',135,40,(75,360))
night_button=Button('NIGHT',135,40,(75,310))
next_button = Button('>',25,25,(265,210))
previous_button = Button('<',25,25,(0,210))
base_next_button = Button('>',25,25,(215,440))
base_previous_button = Button('<',25,25,(50,440))
back_button=Button('- BACK',90,30,(190,15))


#MAIN GAME LOOP
if __name__ == "__main__":
    reverse_gravity,BG_SURF,BIRD_SURFACE,BASE_FLOOR,PIPE_SURF,BIRD_FRAME = welcome(BG_SURF,BIRD_SURFACE,BASE_FLOOR)
    #BG_SURF,PIPE_SURF,BASE_FLOOR,BIRD_FRAME=transition()

   #Game Loop
    while True:
        for event in pygame.event.get():
            # QUIT CONTROLS
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            #MOVMENT CONTROLS
            # if (event.type == pygame.KEYDOWN and event.key == pygame.K_m) and GAME_ACTIVE == False:
            #     reverse_gravity = welcome()
            #     BG_SURF, PIPE_SURF, BASE_FLOOR, BIRD_FRAME = transition()
            # Pause Game Option

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pause()

            if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if reverse_gravity:
                    BIRD_MOVMENT = 0
                    BIRD_MOVMENT = +8
                    flap_sound.play()
                else:
                    BIRD_MOVMENT = 0
                    BIRD_MOVMENT = -8
                    flap_sound.play()

                if event.key==pygame.K_SPACE and GAME_ACTIVE == False:
                    GAME_ACTIVE = True
                    PIPE_LIST.clear()
                    BIRD_MOVMENT = 0
                    BIRD_RECT.center = (50,200)
                    SCORE=0
                    delay=1
                    #welcome()



            #PIPE CREATION
            if event.type==SPAWNPIPE:
                PIPE_LIST.extend(create_pipe())

            #BRID ANIMATION
            if event.type==BIRD_FLAP:
                if BIRD_INDEX <2:
                    BIRD_INDEX+=1
                else:
                    BIRD_INDEX=0
                BIRD_SURFACE,BIRD_RECT = bird_animation(BIRD_FRAME)

        SCREEN.blit(BG_SURF, (0, 0))
        if GAME_ACTIVE==False:
            game_over_surface = game_over_font.render('GAME OVER', True, (250, 250, 250))
            game_over_rect = game_over_surface.get_rect(center=(140, 150))
            SCREEN.blit(game_over_surface,game_over_rect)
            if restart_button.draw() ==True:
                GAME_ACTIVE = True
                PIPE_LIST.clear()
                BIRD_MOVMENT = 0
                BIRD_RECT.center = (50, 200)
                SCORE = 0
                delay = 1
            if main_menu.draw() == True:
                reverse_gravity,BG_SURF,BIRD_SURFACE,BASE_FLOOR,PIPE_SURF,BIRD_FRAME = welcome(BG_SURF,BIRD_SURFACE,BASE_FLOOR)
                #BG_SURF, PIPE_SURF, BASE_FLOOR, BIRD_FRAME = transition()
                GAME_ACTIVE = True
                PIPE_LIST.clear()
                BIRD_MOVMENT = 0
                BIRD_RECT.center = (50, 200)
                SCORE = 0
                delay = 1

            #SCREEN.blit(MESSAGE, (50, 50))

        if GAME_ACTIVE:
            # PIPES ANIMATION
            PIPE_LIST = move_pipe(PIPE_LIST)
            draw_pipes(PIPE_LIST)
            pipe_score_check()
            score_display('main_game')

            if reverse_gravity:
                BIRD_MOVMENT -= GRAVITY  # GRAVITY ADDEND TO THE Y-CORDINATE OF RECTANGLE OF BIRD
                BIRD_RECT.centery += BIRD_MOVMENT
                ROTATED_BIRD = rotate_bird(BIRD_SURFACE)  # THIS FUNCTION ROTATED THE BIRD
                SCREEN.blit(ROTATED_BIRD, BIRD_RECT)
                GAME_ACTIVE = check_collision(PIPE_LIST)
            else:
                # BIRD GRAVITY AND ROTATION EFFECT
                BIRD_MOVMENT += GRAVITY  # GRAVITY ADDEND TO THE Y-CORDINATE OF RECTANGLE OF BIRD
                BIRD_RECT.centery += BIRD_MOVMENT
                ROTATED_BIRD = rotate_bird(BIRD_SURFACE)  # THIS FUNCTION ROTATED THE BIRD
                SCREEN.blit(ROTATED_BIRD, BIRD_RECT)
                GAME_ACTIVE = check_collision(PIPE_LIST)
        else:
            if(delay==1):
                time.sleep(1)
                delay=delay-1
            HIGH_SCORE=update_score(SCORE,HIGH_SCORE)
            score_display('game_over')


        #BASE ANIMATION
        BASE_X_POSTI-=2
        draw_base_floor()
        if BASE_X_POSTI < -300:
            BASE_X_POSTI = 0

        #UPDATE FRAMES
        pygame.display.update()
        CLOCK.tick(FPS)