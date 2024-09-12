import pygame
import sys
import random
import time

# Initialising pygame
pygame.init()

############################# Game Fps #########################
FPS = pygame.time.Clock()

####################### Creating Display and giving title ######################
set_width = 800
set_height = 650
gameWindow = pygame.display.set_mode((set_width, set_height))
pygame.display.set_caption('Car Crash')

####################### Game images and Rectangles #####################
bgImg = pygame.image.load('sprites/background-1.png').convert()
bgImg1 = pygame.transform.scale(bgImg, (750, 650))
bg_rect1 = bgImg1.get_rect(topleft=(25, 0, 0))

bgImg2 = pygame.transform.scale(bgImg, (750, 650))
bg_rect2 = bgImg2.get_rect(topleft=(25, -650))


player_carImg = pygame.image.load('sprites/car.png').convert_alpha()
player_carImg = pygame.transform.smoothscale(
    player_carImg, (55, 95)).convert_alpha()
player_car_rect = player_carImg.get_rect(midbottom=(400, 550))

green_sport_Img = pygame.image.load('sprites/green_sport.png').convert_alpha()
green_sport_Img = pygame.transform.smoothscale(
    green_sport_Img, (50, 90)).convert_alpha()
green_sport_rect = green_sport_Img.get_rect(
    midleft=(random.randint(150, 600), -1900))


white_car_Img = pygame.image.load('sprites/white_car.png').convert_alpha()
white_car_Img = pygame.transform.smoothscale(
    white_car_Img, (100, 100)).convert_alpha()
white_car_rect = white_car_Img.get_rect(
    midright=(random.randint(150, 600), -1000))

blue_car_Img = pygame.image.load('sprites/blue_car.png').convert_alpha()
blue_car_Img = pygame.transform.smoothscale(
    blue_car_Img, (50, 90)).convert_alpha()
blue_car_rect = blue_car_Img.get_rect(midleft=(random.randint(150, 600), -1500))


yellow_car_Img = pygame.image.load('sprites/yellow_car.png').convert_alpha()
yellow_car_Img = pygame.transform.smoothscale(
    yellow_car_Img, (50, 93)).convert_alpha()
yellow_car_rect = yellow_car_Img.get_rect(
    midleft=(random.randint(150, 600), -1200))

truck_Img = pygame.image.load('sprites/truck.png').convert_alpha()
truck_Img = pygame.transform.smoothscale(truck_Img, (120, 120)).convert_alpha()
truck_rect = truck_Img.get_rect(midleft=(random.randint(150, 600), -1100))

grey_car_Img = pygame.image.load('sprites/grey_car.png').convert_alpha()
grey_car_Img = pygame.transform.smoothscale(
    grey_car_Img, (50, 94)).convert_alpha()
grey_car_rect = grey_car_Img.get_rect(
    midleft=((random.randint(150, 600), -1300)))


neon_blue_car_Img = pygame.image.load('sprites/neon_blue_car.png').convert_alpha()
neon_blue_car_Img = pygame.transform.smoothscale(neon_blue_car_Img, (50, 100)).convert_alpha()
neon_blue_rect = neon_blue_car_Img.get_rect(midleft = (random.randint(150, 600), -1300))

######################## Setting up logo ###################
logo = pygame.image.load('sprites/logo.jpg')
pygame.display.set_icon(logo)

####################### colors #######################
grey = (102, 102, 102)


########################## Game specific variables ##############################
acc_car_x = 0
acc_car_y = 0

########################## Game functions ########################


def car_condition():
    ############ Player's car ###########

    # car x condition
    if player_car_rect.x > 602:
        player_car_rect.x = 602
    if player_car_rect.x < 149:
        player_car_rect.x = 149

    # car y condition
    if player_car_rect.y < 10:
        player_car_rect.y = 10
    if player_car_rect.y > 500:
        player_car_rect.y = 500

############# Green sport #############
    if green_sport_rect.y > 650:
        green_sport_rect.x = random.randint(150, 600)
        green_sport_rect.y = random.randint(-3000, -1900)

############# Red car ##############
    if white_car_rect.y > 650:
        white_car_rect.x = random.randint(150, 600)
        white_car_rect.y = random.randint(-2500, -1200)

########### Blue car ##############
    if blue_car_rect.y > 650:
        blue_car_rect.x = random.randint(150, 600)
        blue_car_rect.y = random.randint(-2300, -1400)

########### yellow car ##############
    if yellow_car_rect.y > 650:
        yellow_car_rect.x = random.randint(150, 600)
        yellow_car_rect.y = random.randint(-2200, -2000)

########### Truck ##############
    if truck_rect.y > 650:
        truck_rect.x = random.randint(150, 600)
        truck_rect.y = random.randint(-2000, -1500)

########### yellow car ##############
    if grey_car_rect.y > 650:
        grey_car_rect.x = random.randint(150, 600)
        grey_car_rect.y = random.randint(-3000, -1800)

########### neon blue car ##############
    if neon_blue_rect.y > 650:
        neon_blue_rect.x = random.randint(150, 600)
        neon_blue_rect.y = random.randint(-3000, -1900)


def road_condition():
    global bg_rect1, bg_rect2
    if bg_rect1.y >= set_height:
        bg_rect1.y = -650

    if bg_rect2.y >= set_height:
        bg_rect2.y = -650


def blitting():
    gameWindow.blit(bgImg1, bg_rect1)
    gameWindow.blit(bgImg2, bg_rect2)
    gameWindow.blit(player_carImg, player_car_rect)
    gameWindow.blit(green_sport_Img, green_sport_rect)
    gameWindow.blit(white_car_Img, white_car_rect)
    gameWindow.blit(blue_car_Img, blue_car_rect)
    gameWindow.blit(yellow_car_Img, yellow_car_rect)
    gameWindow.blit(grey_car_Img, grey_car_rect)
    gameWindow.blit(neon_blue_car_Img, neon_blue_rect)
    gameWindow.blit(truck_Img, truck_rect)


def motion():
    player_car_rect.x += acc_car_x
    player_car_rect.y += acc_car_y
    bg_rect1.y += 2
    bg_rect2.y += 2
    green_sport_rect.y += 6
    white_car_rect.y += 4
    blue_car_rect.y += 3
    yellow_car_rect.y += 5
    truck_rect.y += 3
    grey_car_rect.y += 4
    neon_blue_rect.y += 3

def increment_speed():
    green_sport_rect.y += 0.002
    white_car_rect.y += 0.002
    blue_car_rect.y += 0.002
    yellow_car_rect.y += 0.002
    truck_rect.y += 0.002
    grey_car_rect.y += 0.002
    neon_blue_rect.y += 0.002


while True:
    gameWindow.fill(grey)
    blitting()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                acc_car_x = 7
                acc_car_y = 0

            if event.key == pygame.K_LEFT:
                acc_car_x = -7
                acc_car_y = 0

            if event.key == pygame.K_UP:
                acc_car_y = -7
                acc_car_x = 0

            if event.key == pygame.K_DOWN:
                acc_car_y = 7
                acc_car_x = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                acc_car_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                acc_car_y = 0

    motion()
    car_condition()
    road_condition()
    increment_speed()
    FPS.tick(60)
    pygame.display.flip()
