import pygame
import random
import math

pygame.init()

row = 600
game_over = False

display = pygame.display.set_mode((row, row))
pygame.display.set_caption("Snake Game")

game_state = True

# snake related items
snake_x = 20
snake_y = 20
snake_s = 20
velocity_x = 0
velocity_y = 20
length = 1

# food related items
x = random.randint(0, 590)
while x % 20 != 0:
    x = random.randint(0, 590)

food_x = food_y = x
food_s = 20


# collision checker
def collision_status(snackX, snakeY, foodX, FoodY):
    distance = math.sqrt((math.pow(snackX - foodX, 2)) + (math.pow(snakeY - FoodY, 2)))
    if distance < 20:
        return True
    else:
        return False


# score update
score = 0
font = pygame.font.Font('Font/Roboto-Black.ttf', 30)


def score_update(x, y):
    final_display_score = font.render("Score : " + str(score), True, (0, 0, 0))
    display.blit(final_display_score, (x, y))


snake_list = []
fps = 10
clock = pygame.time.Clock()


def draw_rect(display):
    dis = 600 // 30

    x = 0
    y = 0
    for i in range(row):
        x += dis
        y += dis
        pygame.draw.line(display, [0, 0, 0], (x, 0), (x, 600))
        pygame.draw.line(display, [0, 0, 0], (0, y), (600, y))
        # pygame.display.update()


def our_snake(snakeS, snakeList):
    for le in snakeList:
        pygame.draw.rect(display, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],
                         [le[0], le[1], snakeS, snakeS])


while game_state:
    if game_over is not True:
        display.fill((255, 255, 255))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_state = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    velocity_x = snake_s
                    velocity_y = 0

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    velocity_x = -snake_s
                    velocity_y = 0

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    velocity_y = -snake_s
                    velocity_x = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    velocity_y = snake_s
                    velocity_x = 0

        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        for i in snake_list[:-1]:
            if i == snake_head:
                game_over = True

        if len(snake_list) > length:
            del snake_list[0]

        if snake_x < 0:
            snake_x = 600
        elif snake_x > 600:
            snake_x = 0
        elif snake_y < 0:
            snake_y = 600
        elif snake_y > 600:
            snake_y = 0
        else:
            pass

        collision = collision_status(snake_x, snake_y, food_x, food_y)

        if collision:
            x = random.randint(0, 590)
            while x % 20 != 0:
                x = random.randint(0, 590)

            food_x = food_y = x
            length += 1
            score += 10
        else:
            pass

        draw_rect(display)
        pygame.draw.rect(display, [123, 12, 23], [food_x, food_y, food_s, food_s])
        our_snake(snake_s, snake_list)
        score_update(10, 10)
        pygame.display.update()
        clock.tick(fps)
    else:
        snake_list = 0
        snake_head = 0
        score = 0
        length = 0
        Game_Over_ms = pygame.font.Font('Font/Roboto-Black.ttf', 50)
        final_display_ms = Game_Over_ms.render("Game Over", True, (0, 0, 0))
        display.blit(final_display_ms, (300, 300))
        pygame.display.update()

pygame.quit()
quit()
