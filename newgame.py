import pygame
import random

# Initialise the pygame
pygame.init()

# Window settings
screen_width = 600
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Again")

# For FPS
clock = pygame.time.Clock()

# For text
font = pygame.font.SysFont(None, 40, True)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


# To write text on window screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x, y])


# Main Game loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    fps = 30
    snake_size = 20
    snake_x = 150
    snake_y = 150
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    food_radius = 8
    food_x = random.randint(100, screen_width)
    food_y = random.randint(100, screen_height)
    score = 0
    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            win.fill(white)
            text_screen("Game Over! Your Score Was " + str(score), black, 80, 200)
            text_screen("Press Enter to Play Again", red, 95, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

            pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    elif event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) <= 20:
                score += 10
                food_x = random.randint(100, screen_width)
                food_y = random.randint(100, screen_height)
                snk_length += 5

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            win.fill(white)
            text_screen("Score: " + str(score), black, 5, 5)

            head = [snake_x, snake_y]
            snk_list.append(head)

            for x, y in snk_list:
                pygame.draw.rect(win, black, [x, y, snake_size, snake_size])

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            pygame.draw.circle(win, red, [food_x, food_y], food_radius)
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()


gameloop()
