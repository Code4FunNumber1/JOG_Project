import pygame, random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")

FPS = 20
clock = pygame.time.Clock()

SNAKE_SIZE = 20
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100
snake_dx = 0
snake_dy = 0
score = 0

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
DARKGREEN = (10, 50, 10)
DARKRED = (150, 0, 0)

font = pygame.font.SysFont('gabriola', 48)


# Set text

def create_text_and_rect(text, color, background_color, **locations):
    text = font.render(text, True, color, background_color)
    rect = text.get_rect()
    for location in locations.keys():
        if location == "center":
            rect.center = locations[location]
        if location == "topleft":
            rect.topleft = locations[location]
    return text, rect


(title_text, title_rect) = create_text_and_rect("~~Snake~~", GREEN, DARKRED,
                                             center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

(score_text, score_rect) = create_text_and_rect("Score: " + str(score), GREEN, DARKRED,
                                                topleft=(10, 10))

(game_over_text, game_over_rect) = create_text_and_rect("GAMEOVER", RED, DARKGREEN,
                                                        center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

(continue_text, continue_rect) = create_text_and_rect("Press any key to play again", RED, DARKGREEN,
                                                      center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64))

pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

apple_pos = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_pos)
head_pos = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_pos)
body_pos = []


# The main game loop
running = True
is_paused = False


def move_snake(event):
    global snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        key = event.key
        if key == pygame.K_LEFT or pygame.K_a:
            snake_dx = -1 * SNAKE_SIZE
            snake_dy = 0
        if key == pygame.K_RIGHT or pygame.K_d:
            snake_dx = SNAKE_SIZE
            snake_dy = 0
        if key == pygame.K_UP or pygame.K_w:
            snake_dx = 0
            snake_dy = -1 * SNAKE_SIZE
        if key == pygame.K_DOWN or pygame.K_s:
            snake_dx = 0
            snake_dy = SNAKE_SIZE


def check_quit(event):
    global running
    if event == pygame.QUIT:
        running = False


def check_events():
    global running
    for event in pygame.event.get():
        check_quit(event)
        move_snake(event)

def handle_snake():
    global body_pos
    global head_x
    global head_y
    global head_pos
    global snake_dx, snake_dy
    body_pos.insert(0, head_pos)
    body_pos.pop()
    head_x += snake_dx
    snake_dy += head_y
    head_pos = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

def reset_game_after_game_over(event):
    global is_paused, score, head_x, head_y, head_pos, body_pos, snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        score = 0
        head_x = WINDOW_WIDTH // 2
        head_y = WINDOW_HEIGHT // 2 + 100
        head_pos = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
        body_pos = []
        snake_dx = 0
        snake_dy = 0
        is_paused = False

def check_end_game_after_game_over(event):
    global is_paused
    global running
    if event.type == pygame.QUIT:
        is_paused = False
        running = False


def check_game_over():
    global head_rect
    global head_pos
    global body_pos
    global running
    global is_paused
    if head_rect.left < 0  or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_pos in body_pos:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                reset_game_after_game_over(event)
                check_end_game_after_game_over(event)

def check_collisions():
    global score, apple_x, apple_y, apple_pos, body_pos
    # TODO: if head_rect.colliderect(apple_rect)
        # TODO: add 1 to the score
        # TODO: call pick_up_sound.play()
        # TODO: set apple_x to random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        # TODO: set apple_y to random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        # TODO: set apple_coord to (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: call body_coords.append(head_coord)
        pass # TODO: remove this pass when done.

def blit_hud():
    # TODO: call display_surface.blit(title_text, title_rect)
    # TODO: call display_surface.blit(score_text, score_rect)
    pass  # TODO: remove this pass when done.

def blit_assets():
    # TODO: for body in body_coords:
        # TODO: call pygame.draw.rect(display_surface, DARKGREEN, body)
    # TODO: set head_rect to pygame.draw.rect(display_surface, GREEN, head_coord)
    # TODO: set apple_rect to pygame.draw.rect(display_surface, RED, apple_coord)
    pass  # TODO: remove this pass when done.

def update_display_and_tick_clock():
    # TODO: call pygame.display.update()
    # TODO: call clock.tick(FPS)
    pass  # TODO: remove this pass when done.

while running:
    # Check pygame events
    check_events()

    # handle growing and manipulating the snake
    handle_snake()

    # Check for game over
    check_game_over()

    # Check for collisions
    check_collisions()

    # Update HUD
    # TODO: set score_text to font.render("Score: " + str(score), True, GREEN, DARKRED)

    # Fill the surface
    # TODO: call display_surface.fill(WHITE)

    # Blit HUD
    blit_hud()

    # Blit assets
    blit_assets()

    # Update display and tick clock
    update_display_and_tick_clock()

# End the game
pygame.quit()
