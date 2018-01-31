import pygame,sys,time,random

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
effect = pygame.mixer.Sound('/home/shivam/PycharmProjects/snakes/beep-02.wav')
play_surface = pygame.display.set_mode((720, 460))

red = pygame.Color(255,0,0)
purple = pygame.Color(94,60,153)
green =  pygame.Color(26,244,15)
blue = pygame.Color(0,0,100)
white = pygame.Color(255,255,255)

fps_controller = pygame.time.Clock()

snake_start = [90,50]
snake_body = [[90,50],[80,50],[70,50]]


food_pos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
food_spawn = True


direction = 'RIGHT'
change = direction



def showscore(score):
    font = pygame.font.SysFont('comicsans', 72)
    surface = font.render("Score : {0}".format(score), True, blue)
    rectangle = surface.get_rect()
    rectangle.midtop = (540, 0)
    play_surface.blit(surface, rectangle)
    pygame.display.update(rectangle)


score = 0

def gameover():
    font = pygame.font.SysFont('comicsans',72)
    surface = font.render('Oh! Game Over!',True,purple)
    rectangle = surface.get_rect()
    rectangle.midtop = (360,15)
    surface2 = font.render('Final Score : {}'.format(score), True, red)
    rectangle2 = surface2.get_rect()
    rectangle2.midtop = (360, 100)
    play_surface.blit(surface,rectangle)
    play_surface.blit(surface2, rectangle2)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    sys.exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change = 'RIGHT'
            if event.key == pygame.K_DOWN:
                change = 'DOWN'
            if event.key == pygame.K_UP:
                change = 'UP'
            if event.key == pygame.K_LEFT:
                change = 'LEFT'

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    if change == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    if change == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'

    if change == 'UP' and not direction == 'DOWN':
        direction = 'UP'

    if change == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snake_start[0]+=10

    if direction == 'LEFT':
        snake_start[0]-=10

    if direction == 'UP':
        snake_start[1]-=10

    if direction == 'DOWN':
        snake_start[1]+=10

    snake_body.insert(0,list(snake_start))
    if snake_start == food_pos:
        food_spawn = False
        effect.play()
        score+=1

    else:
        snake_body.pop()

    if food_spawn == False:
        food_pos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        food_spawn = True

    play_surface.fill(white)

    for bodypart in snake_body:
        pygame.draw.rect(play_surface,green,pygame.Rect(bodypart[0],bodypart[1],10,10))

    pygame.draw.rect(play_surface, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_start[0]>710 or snake_start[0]<10 or snake_start[1]>450 or snake_start[1]<10:
        gameover()

    for bodypart in snake_body[1:]:
        if bodypart ==snake_start:
            gameover()

    showscore(score)
    pygame.display.flip()
    fps_controller.tick(25)