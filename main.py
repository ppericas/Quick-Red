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
import pygame, os, random, json

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
GREY = (89, 89, 89)

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

# text
FONT_TITTLE = pygame.font.Font(None, 42)
FONT_INT = pygame.font.Font(None, 72)
FONT_SMALL = pygame.font.Font(None, 36)

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

def save_user_data(name, time_taken):
    top_scores = []
    with open('top_scores.json', 'r') as file:
        top_scores = json.load(file)

    top_scores.append({'name': name, 'time_taken': time_taken})
    top_scores.sort(key=lambda x: x['time_taken']) # sort by time_taken

    with open('top_scores.json', 'w') as file:
        json.dump(top_scores[:5], file) # save only the 5 names first from top_scores

def render_text(score, seconds_timer, top_scores, game_over=False):
    x_pos_top5 = 510
    show_name_input = True

    text_score = FONT_TITTLE.render("SCORE", True, BLACK)
    WIN.blit(text_score, (545, 25))

    text_score_int = FONT_INT.render(str(score[0]), True, BLACK)
    WIN.blit(text_score_int, (570, 80))

    text_top = FONT_TITTLE.render("Hall of Fame", True, BLACK)
    WIN.blit(text_top, (x_pos_top5, 250))

    for i in range(5):
        if i < len(top_scores):
            text_top_i = FONT_SMALL.render(f"{i+1}. {top_scores[i]['name']} {top_scores[i]['time_taken']}s", True, BLACK)
            WIN.blit(text_top_i, (x_pos_top5, 330 + i * 30))
        else:
            text_top_i = FONT_SMALL.render(f"{i+1}. ---", True, BLACK)
            WIN.blit(text_top_i, (x_pos_top5, 330 + i * 30))

    if not game_over:
        text_time_seconds = FONT_INT.render(str(int(seconds_timer)) + "s", True, BLACK)
        WIN.blit(text_time_seconds, (550, 200))

    else:
        if show_name_input:
            render_text(score, seconds_timer, top_scores, game_over=True)
        text_game_over = FONT_TITTLE.render("GAME OVER", True, BLACK)
        WIN.blit(text_game_over, (510, 170))

        text_final_score_int = FONT_INT.render(str(score[0]), True, BLACK)
        WIN.blit(text_final_score_int, (590, 260))

        text_record = FONT_TITTLE.render("Congratulations! You made it to the Top 5!", True, BLACK)
        WIN.blit(text_record, (360, 350))
        

def draw_window(score, seconds_timer, top_scores):
    WIN.fill(WHITE)
    WIN.blit(PLAY_MENU, (0, 0))
    render_text(score, seconds_timer, top_scores) # loop to move throught the list and draw red squares
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

def handle_name_input(score, seconds_timer, top_scores):
    name_input = ""
    input_rect = pygame.Rect(495, 280, 10, 32)
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return name_input
                    elif event.key == pygame.K_BACKSPACE:
                        name_input = name_input[:-1]
                    else:
                        name_input += event.unicode
        WIN.fill(WHITE)
        WIN.blit(PLAY_MENU, (0, 0))
        render_text(score, seconds_timer, top_scores, game_over=False)
        txt_surface = FONT_TITTLE.render(name_input, True, GREY)
        width = max(200, txt_surface.get_width() + 10)
        input_rect.w = width
        WIN.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(WIN, GREY, input_rect, 2)
        pygame.display.flip()

def handle_loss(seconds_timer, top_scores):
    if top_scores:
        last_top_score = top_scores[-1]['time_taken']
        if seconds_timer > last_top_score:
            return True
    return False

# ----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    clock = pygame.time.Clock()
    run = True
    seconds = get_random_seconds()
    pygame.time.set_timer(pygame.USEREVENT, seconds)
    start_time = pygame.time.get_ticks()
    score = [0]
    game_over = False

    top_scores = []
    if os.path.exists('top_scores.json'):
        with open('top_scores.json', 'r') as file:
            top_scores = json.load(file)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.USEREVENT:
                if not game_over:
                    generate_random_square()
                else:
                    if score[0] < 5:  # Si el jugador no está en los primeros 5, muestra el formulario de nombre
                        show_name_input = True
                    else:
                        run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                handle_click(score)

        current_time = pygame.time.get_ticks()
        seconds_timer = (current_time - start_time) / 1000
        clock.tick(FPS)
        draw_window(score, seconds_timer, top_scores)

        if score[0] >= 20:
            if handle_loss(seconds_timer, top_scores):
                game_over = True
            name_input = handle_name_input(score, seconds_timer, top_scores)
            save_user_data(name_input, seconds_timer)

    pygame.quit()


if __name__ == '__main__':
    main()