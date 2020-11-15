import os
import pygame
import random

pygame.mixer.init()
pygame.init()

# Define Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 176, 68)

screen_width = 800
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg = pygame.image.load("ingame.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Game Over Image
goimg = pygame.image.load("gameover.jpg")
goimg = pygame.transform.scale(goimg, (screen_width, screen_height)).convert_alpha()

# Welcome Image
wcimg = pygame.image.load("startback.jpg")
wcimg = pygame.transform.scale(wcimg, (screen_width, screen_height)).convert_alpha()

# Window Title
pygame.display.set_caption("Snake")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x, y])


def plot_snake(window, color, snk_list, snk_size):
    for x, y in snk_lst:
        pygame.draw.rect(win, green, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False

    while not exit_game:
        win.blit(wcimg, (0, 0))
        text_screen("Welcome To Snake", (255, 153, 51), 240, 170)
        text_screen("Press Space Key To Play",  (255, 153, 51), 220, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    gameLoop()

        pygame.display.update()
        clock.tick(60)


def gameLoop():
    # Game specific variable
    global snake_size
    global snk_lst
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    food_size = 10
    init_velocity = 3
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(200, screen_width-200)
    food_y = random.randint(150, screen_height-150)
    fps = 60
    score = 0

    if not os.path.exists("HighScore.txt"):
        with open("HighScore.txt", "w") as f:
            f.write("0")

    with open("HighScore.txt", "r") as f:
        highscore = f.read()

    snk_lst = []
    snk_length = 1

    # Game Loop
    while not exit_game:
        if game_over:
            with open("HighScore.txt", "w") as j:
                j.write(str(highscore))

            win.fill(white)
            win.blit(goimg, (0, 0))
            text_screen("Press Enter To Continue",  (255, 153, 51), 10, 10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x) < 10 and abs(snake_y-food_y) < 10:
                score += 10
                food_x = random.randint(0, screen_width / 2)
                food_y = random.randint(0, screen_height / 2)
                snk_length += 4

                if score > int(highscore):
                    highscore = score

            win.fill(white)
            win.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), (255, 254, 95), 5, 5)
            pygame.draw.rect(win, red, [food_x, food_y, food_size, food_size])

            head = [snake_x, snake_y]
            snk_lst.append(head)

            if len(snk_lst) > snk_length:
                del snk_lst[0]

            if head in snk_lst[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(win, green, snk_lst, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
