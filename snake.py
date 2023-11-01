import pygame, sys, random, time

SCREEN_WIDTH = 500
SNAKE_WIDTH = 25
SCREEN_BLOCK = SCREEN_WIDTH // SNAKE_WIDTH

#Make a GUI
pygame.init()
pygame.display.set_caption("Snakessss")
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

clock = pygame.time.Clock()


# varibles
snake_x = 0
snake_y = 0
speed = SNAKE_WIDTH
x_speed = 0
y_speed = 0
fruit = None
score = 0
snake_body = [[snake_x, snake_y]]


def draw_snake(snake_head):
    snake_body.insert(0, [snake_head.x, snake_head.y])
    snake_body.pop()
    for body in snake_body:
        block = pygame.Rect(body[0], body[1], SNAKE_WIDTH, SNAKE_WIDTH)
        pygame.draw.rect(window, "Green", block)
 


def check_body_collision(snake_body):
    if len(snake_body) > 1:
        for i in range(1, len(snake_body)):
         if snake_body[0] == snake_body[i]:
            game_over()


# score function
def show_score():
    score_font = pygame.font.SysFont("comicsans", 20)
    score_surface = score_font.render(f'Score: {score}', True, "Red")
    score_rect = score_surface.get_rect()
    window.blit(score_surface, score_rect)




#  Game over
def game_over():
    score_font = pygame.font.SysFont("comicsans", 20)
    score_surface = score_font.render(f'Score: {score}', True, "Red")
    score_rect = score_surface.get_rect()
    score_rect.midtop = (SCREEN_WIDTH // 2, 200)
    window.blit(score_surface, score_rect)
    pygame.display.flip()

    time.sleep(1)
    sys.exit()




#  fruit function
def crate_fruit():
    fruit_x = random.randint( 0, SCREEN_BLOCK - 1) * SNAKE_WIDTH
    fruit_y = random.randint(0, SCREEN_BLOCK - 1) * SNAKE_WIDTH
    fruit_rect = pygame.Rect(fruit_y, fruit_x, SNAKE_WIDTH, SNAKE_WIDTH)
    return fruit_rect

#  chek walls
def chek_walls():
    if snake_head.left > SCREEN_WIDTH:
        game_over()
        
    if snake_head.right < 0:
         game_over()

    if snake_head.top < 0:
        game_over()

    if snake_head.bottom > SCREEN_WIDTH:
         game_over()
 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_speed = speed
                y_speed = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -speed
                y_speed = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed  = -speed
                x_speed = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_speed = speed
                x_speed = 0

    snake_head = pygame.Rect(snake_x, snake_y, SNAKE_WIDTH, SNAKE_WIDTH)
    if not fruit:
        fruit = crate_fruit()

    if snake_head.colliderect(fruit):
        score += 10
        snake_body.append([fruit.x, fruit.y])
        fruit = crate_fruit()

    snake_x += x_speed
    snake_y += y_speed
    chek_walls()
    check_body_collision(snake_body)
    window.fill("Black")
    pygame.draw.rect(window, "Green", snake_head)
    pygame.draw.rect(window, "Red", fruit)
    draw_snake(snake_head)
    show_score()
    pygame.display.flip()
    clock.tick(10) #Controls the FPS