#!/usr/bin/python

# T-rex image from "Wyverii" on http://opengameart.org/content/unsealed-terrex

import sys
import os

import pygame
import surface_configuration
import tilemap
import initialize_player
import initialize_danny

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

housex = 50
housey = 50

windowSurface = pygame.display.set_mode((surface_configuration.win_x, surface_configuration.win_y),
                                        pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE, 32)
pygame.display.set_caption('Witch Hunt')

player = initialize_player.player
danny = initialize_danny.danny


def scaled_variable(variable, scale):
    """Used to scale objects."""
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
grass_green = (170, 244, 66)
earth_brown = (230, 115, 0)

current_game_map = tilemap.tile_map_one()
current_game_map_textures = tilemap.textures

for row in range(0, surface_configuration.n_height):
    for column in range(0, surface_configuration.n_width):
        current_game_map_textures[current_game_map[row][column]].set_x(round(column * surface_configuration.tile_width))
        current_game_map_textures[current_game_map[row][column]].set_y(round(row * surface_configuration.tile_height))

while True:
    windowSurface.fill(grass_green)
    # scale_h=1.0
    # scale_w=1.0
    pygame.event.pump()

    current_events = pygame.event.get()

    for event in current_events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        # Video resize code via Stack Exchange
        # https://stackoverflow.com/questions/11603222/allowing-resizing-window-pygame

        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.

            tempSurface = pygame.display.set_mode((event.w, event.h),
                                                  pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            windowSurface.blit(tempSurface, (0, 0))
            windowSurface = tempSurface
            surface_configuration.win_x = windowSurface.get_width()
            surface_configuration.win_y = windowSurface.get_height()
            del tempSurface
            surface_configuration.scale_w = float(surface_configuration.win_x) / surface_configuration.small_win_x
            surface_configuration.scale_h = float(surface_configuration.win_y) / surface_configuration.small_win_y

            for row in range(0, surface_configuration.n_height):
                for column in range(0, surface_configuration.n_width):
                    current_game_map_textures[current_game_map[row][column]]. \
                        scale_attributes(surface_configuration.scale_w,
                                         surface_configuration.scale_h)

            player.set_animation_scale(surface_configuration.scale_w, surface_configuration.scale_h)
            danny.set_animation_scale(surface_configuration.scale_w, surface_configuration.scale_h)

    # Tile map collision detection
    for row in range(0, surface_configuration.n_height):
        for column in range(0, surface_configuration.n_width):

            current_tile = current_game_map[row][column]
            current_game_map_textures[current_tile].set_image_rect(
                column * surface_configuration.tile_width_scaled,
                row * surface_configuration.tile_height_scaled, surface_configuration.tile_width_scaled,
                surface_configuration.tile_height_scaled)
            windowSurface.blit(current_game_map_textures[current_tile].image_obj,
                               current_game_map_textures[current_tile].image_rect)

            if current_tile in tilemap.block_textures:
                current_game_map_textures[current_tile].set_collision_rect(
                    column * surface_configuration.tile_width,
                    row * surface_configuration.tile_height, surface_configuration.tile_width,
                    surface_configuration.tile_height)

                player.collision_with(current_game_map_textures[current_tile])

    player.collision_with(danny)

    danny.play_animation(windowSurface, "down")
    player.arrow_key_animation_motion(windowSurface, current_events)
    pygame.display.update()

    mainClock.tick(FPS)
