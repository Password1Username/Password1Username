#!/usr/bin/python

# trex image from Wyverii on http://opengameart.org/content/unsealed-terrex

import sys
import os

import pygame
from pygame.locals import *
import math as m
import SpriteClass
import tilemap

sys.path.append(os.path.abspath('..'))

pygame.init()

'''Tile map dimensions'''
nwidth = 16
nheight = 16

tilewidth = 32
tilewidth_scaled = 32
tileheight = 32
tileheight_scaled = 32

# set up the window
smallwinx = tilewidth * nwidth
winx = smallwinx
smallwiny = tileheight * nheight
winy = smallwiny

scalew = 1.0
scaleh = 1.0

xpos = 0.5 * winx
ypos = 0.5 * winy
xpos_scaled = xpos
ypos_scaled = ypos

ratex = 0.01
ratey = 0.01

dx = winx * ratex
dy = winy * ratey

housex = 50
housey = 50

windowSurface = pygame.display.set_mode((winx, winy), HWSURFACE | DOUBLEBUF | RESIZABLE, 32)
pygame.display.set_caption('Witch Hunt')

# create dummy house object

# First try for using the sprite class

sheetwidth = 6 * 64
sheetheight = 2 * 40
'''Picture offset'''
spritey = 0
spritex = 0
spritewidth = 64
spriteheight = 40

rects_up = [(spritex + 3 * spritewidth, spritey, spritewidth, spriteheight),
            (spritex + 4 * spritewidth, spritey, spritewidth, spriteheight),
            (spritex + 5 * spritewidth, spritey, spritewidth, spriteheight)]

rects_down = [(spritex, spritey, spritewidth, spriteheight),
              (spritex + spritewidth, spritey, spritewidth, spriteheight),
              (spritex + 2 * spritewidth, spritey, spritewidth, spriteheight)]

rects_left = [(spritex, spritey + spriteheight, spritewidth, spriteheight),
              (spritex + spritewidth, spritey + spriteheight, spritewidth, spriteheight),
              (spritex + 2 * spritewidth, spritey + spriteheight, spritewidth, spriteheight)]

rects_right = [(spritex + 3 * spritewidth, spritey + spriteheight, spritewidth, spriteheight),
               (spritex + 4 * spritewidth, spritey + spriteheight, spritewidth, spriteheight),
               (spritex + 5 * spritewidth, spritey + spriteheight, spritewidth, spriteheight)]

# playerAnim_scaled = playerAnim_down

player = SpriteClass.MyPlayer(xpos=0.0, ypos=0.0)
player.setAnimation('./pics/blueboy_64_40.png', rects_down, "down")
player.setAnimation('./pics/blueboy_64_40.png', rects_up, "up")
player.setAnimation('./pics/blueboy_64_40.png', rects_left, "left")
player.setAnimation('./pics/blueboy_64_40.png', rects_right, "right")
player.setInitAnimation("down")

player_initx = 0.0
player_inity = 0.0

hitbox_length = 28

col_initx1 = 18
col_inity1 = 5



player.setX(player_initx)
player.setY(player_inity)

player.set_hitbox_X(col_initx1)
player.set_hitbox_Y(col_inity1)
player.set_collision_width(hitbox_length)
player.set_collision_height(hitbox_length)

# print(player.collision_rect)
# exit()
# print(player.x_scaled, player.y_scaled)
player.setdx(dx)
player.setdy(dy)

danny = SpriteClass.MyPlayer(xpos=0, ypos=0)

rects_down_danny = [(spritex, spritey, spritewidth, spriteheight),
                    (spritex + spritewidth, spritey, spritewidth, spriteheight),
                    (spritex + 2 * spritewidth, spritey, spritewidth, spriteheight),
                    (spritex + 3 * spritewidth, spritey, spritewidth, spriteheight)]

danny.setAnimation('./pics/people/danny_64_40.png', rects_down_danny, "down")
danny.setInitAnimation("down")
danny.setX(0.0)
danny.setY(100.0)
# print(danny.x_scaled, danny.y_scaled)


"""Used to scale objects."""


def scaled_variable(variable, scale):
    return scale * variable


def scaled_anim_object(ref_object, image_w, image_h, scale_w, scale_h):
    scaled_object = ref_object
    scaled_object.smoothscale((round(scale_w * image_w), round(scale_h * image_h)))
    return scaled_object


#
mainClock = pygame.time.Clock()
'''Music'''
pygame.mixer.music.load('./music/witch-hunt.wav')
# pygame.mixer.music.load('./music/intro.wav')
pygame.mixer.music.play(0)

FPS = 30

# pygame.key.set_repeat(100,1000)


red = (100, 50, 50)
grassgreen = (170, 244, 66)
earthbrown = (230, 115, 0)


current_game_map = tilemap.Tilemap().tilemap_one()
current_game_map_textures = tilemap.textures


for row in range(0, nheight):
    for column in range(0, nwidth):
        current_game_map_textures[current_game_map[row][column]].setX(round(column * tilewidth))
        current_game_map_textures[current_game_map[row][column]].setY(round(row * tileheight))

while True:
    windowSurface.fill(grassgreen)
    # scaleh=1.0
    # scalew=1.0
    for event in pygame.event.get():
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
            winx = windowSurface.get_width()
            winy = windowSurface.get_height()
            del tempSurface
            scalew = float(winx) / smallwinx
            scaleh = float(winy) / smallwiny
            tilewidth_scaled = round(scaled_variable(tilewidth, scalew))
            tileheight_scaled = round(scaled_variable(tileheight, scaleh))

            for row in range(0, nheight):
                for column in range(0, nwidth):
                    current_game_map_textures[current_game_map[row][column]].setX(column * tilewidth_scaled)
                    current_game_map_textures[current_game_map[row][column]].setY(row * tileheight_scaled)
                    current_game_map_textures[current_game_map[row][column]].scaleValues(scalew, scaleh)
                    # i+=1
                    # print(i)
                    # print(textures[tilemap[row][column]].image_rect)

            # print(scalew,scaleh)
            player.setScale(scalew, scaleh)
            danny.setScale(scalew, scaleh)
            # danny.scaleValues()
            # danny.playAnim"down"]
            # danny.move(event, windowSurface)

    # '''Inter'''
    for row in range(0, nheight):
        for column in range(0, nwidth):
            # print str(row)+","+str(column)
            # print(tilemap[row][column])
            # print(block_obj.getCollision(house_obj))
            current_tile = current_game_map[row][column]
            current_game_map_textures[current_tile].setX(round(column * tilewidth_scaled))
            current_game_map_textures[current_tile].setY(round(row * tileheight_scaled))
            # print(round(column * tilewidth_scaled),round(row * tileheight_scaled))
            current_game_map_textures[current_game_map[row][column]].image_rect = (
                round(column * tilewidth_scaled), round(row * tileheight_scaled), m.ceil(tilewidth_scaled),
                m.ceil(tileheight_scaled))
            # print(textures[tilemap[row][column]].image_rect)
            windowSurface.blit(current_game_map_textures[current_tile].image_obj, current_game_map_textures[current_tile].image_rect)

            if current_tile in tilemap.block_textures:
                current_game_map_textures[current_tile].setCollisionX(round(column * tilewidth_scaled))
                current_game_map_textures[current_tile].setCollisionY(round(row * tileheight_scaled))
                # pygame.draw.rect(windowSurface, (0, 0, 0), Rect(textures[current_tile].collision_x1,
                # textures[current_tile].collision_y1, textures[current_tile].collision_width,
                #                                           textures[current_tile].collision_height))
                player.collision_with(current_game_map_textures[current_tile])

    # pygame.draw.rect(windowSurface, (0,0,0), Rect(player.col, col_inity1,2*hitbox_2,2*hitbox_2))
    # print(Rect(col_initx1, col_inity1, 2 * hitbox_2, 2 * hitbox_2))
    danny.playAnim(windowSurface, "down")

    player.move(windowSurface, event)
    # print(player.x_scaled, player.y_scaled)
    # print("player " + str(player.collision_rect))

    pygame.display.update()
    mainClock.tick(FPS)
