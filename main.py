import pygame
import random
import sys
import os

from pygame.constants import SCALED

sys.setrecursionlimit(10000)
# initialising pygame
pygame.init()
clock = pygame.time.Clock()


# game sounds
pygame.mixer.init()


# Creating Display and giving title
set_width = 1000
set_height = 900
gameWindow = pygame.display.set_mode((set_width, set_height))
pygame.display.set_caption('Car Crash')

# setting up logo
logo = pygame.image.load('sprites/logo.jpg')
pygame.display.set_icon(logo)

# Images
bgImg = pygame.image.load('sprites/background-1.png').convert_alpha()
carImg = pygame.image.load('sprites/car.png').convert_alpha()
green_sport_Img = pygame.image.load('sprites/green_sport.png').convert_alpha()
red_car_Img = pygame.image.load('sprites/red_car.png').convert_alpha()
blue_car_Img = pygame.image.load('sprites/blue_car.png').convert_alpha()
yellow_car_Img = pygame.image.load('sprites/yellow_car.png').convert_alpha()
green_car_Img = pygame.image.load('sprites/green_car.png').convert_alpha()
white_car_Img = pygame.image.load('sprites/white_car.png').convert_alpha()
neon_blue_car_Img = pygame.image.load('sprites/neon_blue_car.png').convert_alpha()


# colors
grey = (102, 102, 102)

# game specific variables

# main car variables
car_x = 470
car_y = 750
vel_car_x = 0
vel_car_y = 0


# green_sport_car1 variables
green_sport_x1 = random.randint(222, 727)
green_sport_y1 = random.randint(-3000, -1300)
vel_green_sport = 6

# green_sport_car2 variables
green_sport_x2 = random.randint(222, 727)
green_sport_y2 = random.randint(-3400, -1500)
vel_green_sport = 6

# red_car_variables
red_car_x = random.randint(222, 727)
red_car_y = random.randint(-2500, -1000)
vel_red = 3

# blue car variables
blue_car_x = random.randint(222, 727)
blue_car_y = random.randint(-2300, -1400)
vel_blue = 4

# yellow car variables
yellow_car_x = random.randint(222, 727)
yellow_car_y = random.randint(-2200, -1100)
vel_yellow = 4

# green car variables
green_car_x = random.randint(222, 727)
green_car_y = random.randint(-2100, -1000)
vel_green = 4

# white car variables
white_car_x = random.randint(224, 727)
white_car_y = random.randint(-3000, -1100)
vel_white = 5

# neon blue car variables
neon_blue_car_x = random.randint(224, 727)
neon_blue_car_y = random.randint(-2000, -1000)
vel_neon_blue = 3


# road variables
road_position_x = 80
road_position_y1 = 0
road_position_y2 = -900
vel_road = 3

score = 0
score_vel = 2
score_x1 = 135
score_x2 = 830
score_y1 = 250
score_y2 = -650
fps = 65


def backGround(gameWindow, bgImg):
    global road_position_y1, road_position_y2
    bgimg = pygame.transform.smoothscale(bgImg, (840, 910))
    gameWindow.blit(bgimg, (road_position_x, road_position_y1))
    gameWindow.blit(bgimg, (road_position_x, road_position_y2))
    road_position_y1 += vel_road
    road_position_y2 += vel_road


def car(gameWindow, carImg):
    carimg = pygame.transform.smoothscale(carImg, (55, 95)).convert_alpha()
    gameWindow.blit(carimg, (car_x, car_y))


def enemy_green_sport1(gameWindow, green_sport_Img):
    global green_sport_y1
    green_sport_img = pygame.transform.smoothscale(
        green_sport_Img, (50, 90)).convert_alpha()
    gameWindow.blit(green_sport_img, (green_sport_x1, green_sport_y1))
    green_sport_y1 += vel_green_sport


def enemy_green_sport2(gameWindow, green_sport_Img):
    global green_sport_y2
    green_sport_img = pygame.transform.smoothscale(
        green_sport_Img, (50, 90)).convert_alpha()
    gameWindow.blit(green_sport_img, (green_sport_x2, green_sport_y2))
    green_sport_y2 += vel_green_sport


def enemy_red_car(gameWindow, red_car_Img):
    global red_car_y
    red_car_img = pygame.transform.scale(red_car_Img, (50, 90))
    gameWindow.blit(red_car_img, (red_car_x, red_car_y))
    red_car_y += vel_red


def enemy_blue_car(gameWindow, blue_car_Img):
    global blue_car_y
    blue_car_img = pygame.transform.smoothscale(
        blue_car_Img, (50, 90)).convert_alpha()
    gameWindow.blit(blue_car_img, (blue_car_x, blue_car_y))
    blue_car_y += vel_blue


def enemy_yellow_car(gameWindow, yellow_car_Img):
    global yellow_car_y
    yellow_car_img = pygame.transform.smoothscale(
        yellow_car_Img, (50, 93)).convert_alpha()
    gameWindow.blit(yellow_car_img, (yellow_car_x, yellow_car_y))
    yellow_car_y += vel_yellow


def enemy_green_car(gameWindow, green_car_Img):
    global green_car_y
    green_car_img = pygame.transform.smoothscale(
        green_car_Img, (50, 90)).convert_alpha()
    gameWindow.blit(green_car_img, (green_car_x, green_car_y))
    green_car_y += vel_green


def enemy_white_car(gameWindow, white_car_Img):
    global white_car_y
    white_car_img = pygame.transform.smoothscale(
        white_car_Img, (50, 100)).convert_alpha()
    gameWindow.blit(white_car_img, (white_car_x, white_car_y))
    white_car_y += vel_white


def enemy_neon_blue_car(gameWindow, neon_blue_car_Img):
    global neon_blue_car_y
    neon_blue_car_img = pygame.transform.smoothscale(
        neon_blue_car_Img, (50, 100)).convert_alpha()
    gameWindow.blit(neon_blue_car_img, (neon_blue_car_x, neon_blue_car_y))
    neon_blue_car_y += vel_neon_blue


def blitting_enemy_cars():
    enemy_green_sport1(gameWindow, green_sport_Img)
    enemy_green_sport2(gameWindow, green_sport_Img)
    enemy_red_car(gameWindow, red_car_Img)
    enemy_blue_car(gameWindow, blue_car_Img)
    enemy_yellow_car(gameWindow, yellow_car_Img)
    enemy_green_car(gameWindow, green_car_Img)
    enemy_white_car(gameWindow, white_car_Img)
    enemy_neon_blue_car(gameWindow, neon_blue_car_Img)


def collision():
    # collision condition
    if abs(green_sport_x1 - car_x) < 46 and abs(green_sport_y1 - car_y) < 98:

        display_game_over()
        game_over()

    elif abs(green_sport_x2 - car_x) < 46 and abs(green_sport_y2 - car_y) < 98:

        display_game_over()
        game_over()

    elif abs(red_car_x - car_x) < 46 and abs(red_car_y - car_y) < 98:
        display_game_over()
        game_over()

    elif abs(blue_car_x - car_x) < 46 and abs(blue_car_y - car_y) < 98:
        display_game_over()
        game_over()

    elif abs(yellow_car_x - car_x) < 46 and abs(yellow_car_y - car_y) < 98:
        display_game_over()
        game_over()

    elif abs(green_car_x - car_x) < 46 and abs(green_car_y - car_y) < 98:
        display_game_over()
        game_over()

    elif abs(white_car_x - car_x) < 46 and abs(white_car_y - car_y) < 98:
        display_game_over()
        game_over()

    elif abs(neon_blue_car_x - car_x) < 46 and abs(neon_blue_car_y - car_y) < 98:
        display_game_over()
        game_over()


def respawn():
    # Respawn condition

    global red_car_x, red_car_y, green_sport_x1, green_sport_y1, green_sport_x2, green_sport_y2, blue_car_x, blue_car_y, yellow_car_x, yellow_car_y, green_car_x, green_car_y, white_car_x, white_car_y, neon_blue_car_x, neon_blue_car_y, score
    if red_car_y >= 900:
        score += 1
        red_car_x = random.randint(224, 727)
        red_car_y = random.randint(-2500, -1000)

    if green_sport_y1 >= 900:
        score += 1
        green_sport_x1 = random.randint(224, 727)
        green_sport_y1 = random.randint(-3000, -1300)

    if green_sport_y2 >= 900:
        score += 1
        green_sport_x2 = random.randint(224, 727)
        green_sport_y2 = random.randint(-3000, -1300)

    if blue_car_y >= 900:
        score += 1
        blue_car_x = random.randint(224, 727)
        blue_car_y = random.randint(-2300, -1400)

    if yellow_car_y >= 900:
        score += 1
        yellow_car_x = random.randint(224, 727)
        yellow_car_y = random.randint(-2200, -1100)

    if green_car_y >= 900:
        score += 1
        green_car_x = random.randint(224, 727)
        green_car_y = random.randint(-2100, -1000)

    if white_car_y >= 900:
        score += 1
        white_car_x = random.randint(224, 727)
        white_car_y = random.randint(-3000, -1100)

    if neon_blue_car_y >= 900:
        score += 1
        neon_blue_car_x = random.randint(224, 727)
        neon_blue_car_y = random.randint(-2000, -1000)


def car_condition():
    # car x condition
    global car_x, car_y
    if car_x > 730:
        car_x = 730
    if car_x < 219:
        car_x = 219

    # car y condition
    if car_y > 800:
        car_y = 800

    if car_y < 10:
        car_y = 10


def road_condition():
    # road condition
    global road_position_y1, road_position_y2
    if road_position_y1 >= set_height:
        road_position_y1 = -900

    if road_position_y2 >= set_height:
        road_position_y2 = -900


def velocity_increment():
    global vel_green_sport, vel_red, vel_blue, vel_yellow, vel_green, vel_white, vel_neon_blue, vel_road
    vel_green_sport += 0.002
    vel_red += 0.002
    vel_blue += 0.002
    vel_yellow += 0.002
    vel_green += 0.002
    vel_white += 0.002
    vel_neon_blue += 0.002
    vel_road += 0.0001


def score_condition():
    global score_x, score_y1, score_y2
    if score_y1 >= set_height:
        score_y1 = -900

    if score_y2 >= set_height:
        score_y2 = -900


def score_blitting():
    # left side score bliltting
    display_score(f'Score = {score}', (0, 0, 0), score_x1, score_y1)
    display_score(f'Score = {score}', (0, 0, 0), score_x1, score_y2)

    # right side score blitting
    display_score(f'Score = {score}', (0, 0, 0), score_x2, score_y1)
    display_score(f'Score = {score}', (0, 0, 0), score_x2, score_y2)


score_font = pygame.font.Font('fonts/ARCADE.ttf', 64)


def display_score(text, color, x, y):
    screen_text = score_font.render(text, True, color)
    screen_text = pygame.transform.rotate(screen_text, 90)
    gameWindow.blit(screen_text, [x, y])


game_over_font = pygame.font.Font('fonts/font.otf', 96)


def display_game_over():
    screen_text = game_over_font.render("Game Over", True, (255, 0, 0))
    gameWindow.blit(screen_text, [390, 300])


def game_over():
    global vel_car_x, vel_car_y, vel_green_sport, vel_red, vel_blue, vel_yellow, vel_green, vel_white, vel_neon_blue, vel_road, hiscore
    vel_car_x = 0
    vel_car_y = 0
    vel_green_sport = 0
    vel_red = 0
    vel_blue = 0
    vel_yellow = 0
    vel_green = 0
    vel_white = 0
    vel_neon_blue = 0
    vel_road = 0
    if(not os.path.exists("Hiscore.txt")):
        with open('Hiscore.txt', 'w') as f:
            f.write(str(0))

    with open('Hiscore.txt', 'r') as f:
        hiscore = f.read()
    if score > int(hiscore):
        with open('Hiscore.txt', 'w') as f:
            f.write(str(score))


# main game loop
def game_loop():
    global exit_game, car_x, car_y, score_y1, score_y2, vel_car_x, vel_car_y, event
    exit_game = False
    while not exit_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vel_car_x = 10
                    vel_car_y = 0
                    if collision():
                        vel_car_x = 0
                        vel_car_y = 0

                if event.key == pygame.K_LEFT:
                    vel_car_x = - 10
                    vel_car_y = 0
                    if collision():
                        vel_car_x = 0
                        vel_car_y = 0

                if event.key == pygame.K_UP:
                    vel_car_y = -10
                    vel_car_x = 0
                    if collision():
                        vel_car_x = 0
                        vel_car_y = 0

                if event.key == pygame.K_DOWN:
                    vel_car_y = +10
                    vel_car_x = 0
                    if collision():
                        vel_car_x = 0
                        vel_car_y = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vel_car_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                vel_car_y = 0

        car_x += vel_car_x
        car_y += vel_car_y
        score_y1 += vel_road
        score_y2 += vel_road
        gameWindow.fill(grey)
        backGround(gameWindow, bgImg)

        car_condition()
        road_condition()
        score_condition()

        collision()

        respawn()
        score_blitting()

        car(gameWindow, carImg)
        blitting_enemy_cars()
        velocity_increment()
        # updating screen
        pygame.display.flip()
        clock.tick(fps)


game_loop()
pygame.quit()
quit()
