'''
Create a screen where we'll have two sections, with 3/4 of the screen occupied by a grid of rows and columns, and the
remaining 1/4 used to display scores. The grid will be 5x5. 

The goal as programmers will be to create a game in which the user clicks on the square that is red.
A total of 20 red squares will appear one after another. When a red square is clicked, another one appears in
a random position. This continues until reaching 20.

The goal as a user will be to click on all 20 squares in the shortest time possible.

Finally, we need to generate a record in a .json file where we will store the user's name and the time taken in seconds.
To do this, at the end of the game, if the user has completed it in less time than the TOP5, a text field should appear
for them to enter their name and a submit button to save it. Otherwise, the message GAME OVER will appear.
'''
# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame
import os
import random

pygame.init()

# ----------------------------------------------------------------------------------------------------------------------
# constants
# window
pygame.display.set_caption('Quick Red')
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (204, 0, 0)

# sizes
SQUARE_SIZE = 80

# coordinates
SQUARE_X1 = SQUARE_Y1 = 10
SQUARE_X2 = SQUARE_Y2 = 110
SQUARE_X3 = SQUARE_Y3 = 210
SQUARE_X4 = SQUARE_Y4 = 310
SQUARE_X5 = SQUARE_Y5 = 410

# assets
PLAY_MENU_IMAGE = pygame.image.load(
    os.path.join('assets', 'play_menu.png'))
PLAY_MENU = pygame.transform.scale(PLAY_MENU_IMAGE, (WIDTH, HEIGHT))

END_MENU_IMAGE = pygame.image.load(
    os.path.join('assets', 'end_menu.png'))
PLAY_MENU = pygame.transform.scale(PLAY_MENU_IMAGE, (WIDTH, HEIGHT))

# text
font_tittle = pygame.font.Font(None, 42)
font_int = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 36)

# others
FPS = 60

# ----------------------------------------------------------------------------------------------------------------------
# variables
'''
empty array to add the squares that are not available for filling with red. This was not specified in the statement, 
but its only to add complexity to the game and to make it a little bit more challenging to code
TODO unaviable_squares = []
'''
'''
coordinate system for all the squares
dictionary to acces all the squares by their coordinates and be able to change if i want it to be red or not displayed:
'''
squares_storage = {
    'SQUARE_X1_Y1': {
        'square': pygame.Rect(SQUARE_X1, SQUARE_Y1, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X2_Y1': {
        'square': pygame.Rect(SQUARE_X2, SQUARE_Y1, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X3_Y1': {
        'square': pygame.Rect(SQUARE_X3, SQUARE_Y1, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X4_Y1': {
        'square': pygame.Rect(SQUARE_X4, SQUARE_Y1, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X5_Y1': {
        'square': pygame.Rect(SQUARE_X5, SQUARE_Y1, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X1_Y2': {
        'square': pygame.Rect(SQUARE_X1, SQUARE_Y2, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X2_Y2': {
        'square': pygame.Rect(SQUARE_X2, SQUARE_Y2, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X3_Y2': {
        'square': pygame.Rect(SQUARE_X3, SQUARE_Y2, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X4_Y2': {
        'square': pygame.Rect(SQUARE_X4, SQUARE_Y2, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X5_Y2': {
        'square': pygame.Rect(SQUARE_X5, SQUARE_Y2, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X1_Y3': {
        'square': pygame.Rect(SQUARE_X1, SQUARE_Y3, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X2_Y3': {
        'square': pygame.Rect(SQUARE_X2, SQUARE_Y3, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X3_Y3': {
        'square': pygame.Rect(SQUARE_X3, SQUARE_Y3, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X4_Y3': {
        'square': pygame.Rect(SQUARE_X4, SQUARE_Y3, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X5_Y3': {
        'square': pygame.Rect(SQUARE_X5, SQUARE_Y3, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X1_Y4': {
        'square': pygame.Rect(SQUARE_X1, SQUARE_Y4, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X2_Y4': {
        'square': pygame.Rect(SQUARE_X2, SQUARE_Y4, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X3_Y4': {
        'square': pygame.Rect(SQUARE_X3, SQUARE_Y4, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X4_Y4': {
        'square': pygame.Rect(SQUARE_X4, SQUARE_Y4, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X5_Y4': {
        'square': pygame.Rect(SQUARE_X5, SQUARE_Y4, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X1_Y5': {
        'square': pygame.Rect(SQUARE_X1, SQUARE_Y5, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X2_Y5': {
        'square': pygame.Rect(SQUARE_X2, SQUARE_Y5, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X3_Y5': {
        'square': pygame.Rect(SQUARE_X3, SQUARE_Y5, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X4_Y5': {
        'square': pygame.Rect(SQUARE_X4, SQUARE_Y5, SQUARE_SIZE, SQUARE_SIZE),
        'color': None},
    'SQUARE_X5_Y5': {
        'square': pygame.Rect(SQUARE_X5, SQUARE_Y5, SQUARE_SIZE, SQUARE_SIZE),
        'color': None}
}

# ----------------------------------------------------------------------------------------------------------------------
# class & functions
def get_random_seconds():
    return random.randint(400, 800)

'''
TODO make dificulty harder by increasing the number of squares and time between
'''

def render_text():
    text_score = font_tittle.render("SCORE", True, BLACK)
    text_score_width = text_score.get_width()
    WIN.blit(text_score, (500 + text_score_width / 2, 15))

    text_score_int = font_int.render("1", True, BLACK)
    text_score_int_width = text_score_int.get_width()
    WIN.blit(text_score_int, (500 + text_score_int_width / 2, 0))

    text_time = font_tittle.render("Tiempo restante", True, BLACK)
    text_time_width = text_time.get_width()
    WIN.blit(text_time, (500 + text_time_width / 2, 0))

    text_time_seconds = font_int.render("1" + "s", True, BLACK)
    text_time_seconds_width = text_time_seconds.get_width()
    WIN.blit(text_time_seconds, (500 + text_time_seconds_width / 2, 0))

    text_top = font_tittle.render("Hall of Fame", True, BLACK)
    text_top_width = text_top.get_width()
    WIN.blit(text_top, (500 + text_top_width / 2, 0))

    text_top_1 = font_small.render("1. " + "A" + "1", True, BLACK)
    text_top_1_width = text_top_1.get_width()
    WIN.blit(text_top_1, (500 + text_top_1_width / 2, 0))

    text_top_2 = font_small.render("2. " + "A" + "1", True, BLACK)
    text_top_2_width = text_top_2.get_width()
    WIN.blit(text_top_2, (500 + text_top_2_width / 2, 0))

    text_top_3 = font_small.render("3. " + "A" + "1", True, BLACK)
    text_top_3_width = text_top_3.get_width()
    WIN.blit(text_top_3, (500 + text_top_3_width / 2, 0))

    text_top_4 = font_small.render("4. " + "A" + "1", True, BLACK)
    text_top_4_width = text_top_4.get_width()
    WIN.blit(text_top_4, (500 + text_top_4_width / 2, 0))

    text_top_5 = font_small.render("5. " + "A" + "1", True, BLACK)
    text_top_5_width = text_top_5.get_width()
    WIN.blit(text_top_5, (500 + text_top_5_width / 2, 0))

def draw_window(menu):
    WIN.fill(WHITE)
    WIN.blit(menu, (0, 0))
    render_text()
    # loop to move throught the list and draw red squares
    for square in squares_storage.values():
        if square['color'] is RED:
            pygame.draw.rect(WIN, RED, square['square'])
    pygame.display.update()

def handle_click(score):
    for square in squares_storage.keys():
        if squares_storage[square]['square'].collidepoint(pygame.mouse.get_pos()): # check if you click in the red square
            if squares_storage[square]['color'] is RED:
                score[0] += 1
                squares_storage[square]['color'] = None
                break
            else:
                score[0] -= 1

def generate_random_square():
    random_square_x = random.randint(1, 5)
    random_square_y = random.randint(1, 5)
    square = 'SQUARE_X' + str(random_square_x) + '_Y' + str(random_square_y)
    squares_storage[square]['color'] = RED

# ----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    menu = PLAY_MENU
    clock = pygame.time.Clock()
    run = True
    seconds = get_random_seconds()
    pygame.time.set_timer(pygame.USEREVENT, seconds)
    score = [0]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.USEREVENT:
                generate_random_square()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_click(score)
        # Update timer
        timer = 0
        timer += clock.get_rawtime()  # Get the time since the last tick
        clock.tick(FPS)
        draw_window(menu)
    pygame.quit()

if __name__ == '__main__':
    main()