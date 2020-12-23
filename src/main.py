#!/usr/bin/python

# T-rex image from "Wyverii" on http://opengameart.org/content/unsealed-terrex

import sys
import os

import pygame
from pygame.locals import *
import math as m
import AnimationClass
import tilemap

sys.path.append(os.path.abspath('..'))
os.environ['SDL_VIDEODRIVER'] = 'windlib'
# pygame.display.list_modes()

# Set up: https://docs.w3cub.com/pygame/ref/mixer/
# https://xszz.org/faq-1/question-2018090534515.html
pygame.mixer.init(44100, -16, 2, 2048)
pygame.init()

# '''Music'''
# pygame.mixer.music.load('./music/intro.wav')

pygame.mixer.music.load('./music/witch-hunt.wav')
pygame.mixer.music.play(0)


'''Tile map dimensions'''
n_width = 16
n_height = 16

tile_width = 32
tile_width_scaled = 32
tile_height = 32
tile_height_scaled = 32

# set up the window
small_win_x = tile_width * n_width
win_x = small_win_x
small_win_y = tile_height * n_height
winy = small_win_y

scale_w = 1.0
scale_h = 1.0

xpos = 0.5 * win_x
ypos = 0.5 * winy
xpos_scaled = xpos
ypos_scaled = ypos

ratex = 0.01
ratey = 0.01

dx = win_x * ratex
dy = winy * ratey

housex = 50
housey = 50

windowSurface = pygame.display.set_mode((win_x, winy), HWSURFACE | DOUBLEBUF | RESIZABLE, 32)
pygame.display.set_caption('Witch Hunt')

# create dummy house object

# First try for using the sprite class

sheet_width = 6 * 64
sheet_height = 2 * 40
'''Picture offset'''
sprite_y = 0
sprite_x = 0
sprite_width = 64
sprite_height = 40

rects_up = [(sprite_x + 3 * sprite_width, sprite_y, sprite_width, sprite_height),
            (sprite_x + 4 * sprite_width, sprite_y, sprite_width, sprite_height),
            (sprite_x + 5 * sprite_width, sprite_y, sprite_width, sprite_height)]

rects_down = [(sprite_x, sprite_y, sprite_width, sprite_height),
              (sprite_x + sprite_width, sprite_y, sprite_width, sprite_height),
              (sprite_x + 2 * sprite_width, sprite_y, sprite_width, sprite_height)]

rects_left = [(sprite_x, sprite_y + sprite_height, sprite_width, sprite_height),
              (sprite_x + sprite_width, sprite_y + sprite_height, sprite_width, sprite_height),
              (sprite_x + 2 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height)]

rects_right = [(sprite_x + 3 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height),
               (sprite_x + 4 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height),
               (sprite_x + 5 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height)]


player = AnimationClass.MyPlayer(x_pos=0.0, y_pos=0.0)
player.set_animation('./pics/blueboy_64_40.png', rects_down, "down")
player.set_animation('./pics/blueboy_64_40.png', rects_up, "up")
player.set_animation('./pics/blueboy_64_40.png', rects_left, "left")
player.set_animation('./pics/blueboy_64_40.png', rects_right, "right")
player.set_init_animation("down")

player_init_x = 0.0
player_init_y = 0.0

hit_box_length = 28

col_init_x1 = 18
col_init_y1 = 5

player.set_x(player_init_x)
player.set_y(player_init_y)

player.set_hit_box_x(col_init_x1)
player.set_hit_box_y(col_init_y1)
player.set_collision_width(hit_box_length)
player.set_collision_height(hit_box_length)

player.set_dx(dx)
player.set_dy(dy)

danny = AnimationClass.MyPlayer(x_pos=0, y_pos=0)

rects_down_danny = [(sprite_x, sprite_y, sprite_width, sprite_height),
                    (sprite_x + sprite_width, sprite_y, sprite_width, sprite_height),
                    (sprite_x + 2 * sprite_width, sprite_y, sprite_width, sprite_height),
                    (sprite_x + 3 * sprite_width, sprite_y, sprite_width, sprite_height)]

danny.set_animation('./pics/people/danny_64_40.png', rects_down_danny, "down")
danny.set_init_animation("down")
danny.set_x(tile_width_scaled)
danny.set_y(3*tile_height_scaled)


# """Used to scale objects."""
def scaled_variable(variable, scale):
    return scale * variable


def scaled_anim_object(ref_object, image_w, image_h, scale_w, scale_h):
    scaled_object = ref_object
    scaled_object.smoothscale((round(scale_w * image_w), round(scale_h * image_h)))
    return scaled_object


#
mainClock = pygame.time.Clock()

FPS = 30

# pygame.key.set_repeat(100,1000)


red = (100, 50, 50)
grassgreen = (170, 244, 66)
earthbrown = (230, 115, 0)


current_game_map = tilemap.tile_map_one()
current_game_map_textures = tilemap.textures


for row in range(0, n_height):
    for column in range(0, n_width):
        current_game_map_textures[current_game_map[row][column]].set_x(round(column * tile_width))
        current_game_map_textures[current_game_map[row][column]].set_y(round(row * tile_height))

while True:
    windowSurface.fill(grassgreen)
    # scale_h=1.0
    # scale_w=1.0
    pygame.event.pump()

    current_events = pygame.event.get()

    for event in current_events:
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        # Video resize code via Stack Exchange
        # https://stackoverflow.com/questions/11603222/allowing-resizing-window-pygame

        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.

            tempSurface = pygame.display.set_mode((event.w, event.h), HWSURFACE | DOUBLEBUF | RESIZABLE)
            windowSurface.blit(tempSurface, (0, 0))
            windowSurface = tempSurface
            win_x = windowSurface.get_width()
            winy = windowSurface.get_height()
            del tempSurface
            scale_w = float(win_x) / small_win_x
            scale_h = float(winy) / small_win_y
            tile_width_scaled = round(scaled_variable(tile_width, scale_w))
            tile_height_scaled = round(scaled_variable(tile_height, scale_h))

            for row in range(0, n_height):
                for column in range(0, n_width):
                    current_game_map_textures[current_game_map[row][column]].set_x(column * tile_width_scaled)
                    current_game_map_textures[current_game_map[row][column]].set_y(row * tile_height_scaled)
                    current_game_map_textures[current_game_map[row][column]].scale_values(scale_w, scale_h)

            player.set_scales(scale_w, scale_h)
            danny.set_scales(scale_w, scale_h)

    # '''Tile map collision detection'''
    for row in range(0, n_height):
        for column in range(0, n_width):

            current_tile = current_game_map[row][column]
            current_game_map_textures[current_tile].set_x(round(column * tile_width_scaled))
            current_game_map_textures[current_tile].set_y(round(row * tile_height_scaled))
            current_game_map_textures[current_game_map[row][column]].image_rect = (
                round(column * tile_width_scaled), round(row * tile_height_scaled), m.ceil(tile_width_scaled),
                m.ceil(tile_height_scaled))
            windowSurface.blit(current_game_map_textures[current_tile].image_obj, current_game_map_textures[current_tile].image_rect)

            if current_tile in tilemap.block_textures:
                current_game_map_textures[current_tile].set_collision_x(round(column * tile_width_scaled))
                current_game_map_textures[current_tile].set_collision_y(round(row * tile_height_scaled))
                player.collision_with(current_game_map_textures[current_tile])

    danny.play_animation(windowSurface, "down")
    player.arrow_key_animation_motion(windowSurface, current_events)
    pygame.display.update()

    mainClock.tick(FPS)
