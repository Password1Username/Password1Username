#!/usr/bin/python

# trex image from Wyverii on http://opengameart.org/content/unsealed-terrex

import sys
import os
sys.path.append(os.path.abspath('..'))
import pygame
from pygame.locals import *
from SpriteClass import MySprite, MyPlayer
from tilemap import materials, Tilemap

pygame.init()

tilemap = Tilemap()

# set up the window
smallwinx=tilemap.width*tilemap.nwidth
winx=smallwinx
smallwiny=tilemap.height*tilemap.nheight
winy=smallwiny

scalew=1.0
scaleh=1.0

xpos=0.5*winx
ypos=0.5*winy
xpos_scaled=xpos
ypos_scaled=ypos

ratex=0.01
ratey=0.01

dx=winx*ratex
dy=winy*ratey

housex=50
housey=50

windowSurface = pygame.display.set_mode((winx,winy), HWSURFACE|DOUBLEBUF|RESIZABLE, 32)
pygame.display.set_caption('Witch Hunt')

#First try for using the sprite class
house_obj = MySprite('./pics/buildings/haus1.png', housex, housey)

sheetwidth=6*64
sheetheight=2*40
'''Picture offset'''
spritey=0
spritex=0
spritewidth = 64
spriteheight = 40

# rects_up   = [(  spritex+   3*spritewidth , spritey , spritewidth,spriteheight),
#               (  spritex+   4*spritewidth , spritey , spritewidth,spriteheight),
#               (  spritex+   5*spritewidth , spritey , spritewidth,spriteheight)]
#
# rects_down = [(  spritex                  , spritey , spritewidth,spriteheight),
#               (  spritex+     spritewidth , spritey , spritewidth,spriteheight),
#               (  spritex+   2*spritewidth , spritey , spritewidth,spriteheight)]
#
# rects_left = [(  spritex                  , spritey+spriteheight , spritewidth,spriteheight),
#               (  spritex+     spritewidth , spritey+spriteheight , spritewidth,spriteheight),
#               (  spritex+   2*spritewidth , spritey+spriteheight , spritewidth,spriteheight)]
#
# rects_right= [(  spritex+   3*spritewidth , spritey+spriteheight , spritewidth,spriteheight),
#               (  spritex+   4*spritewidth , spritey+spriteheight , spritewidth,spriteheight),
#               (  spritex+   5*spritewidth , spritey+spriteheight , spritewidth,spriteheight)]


# playerAnim_scaled = playerAnim_down

player =  MyPlayer(xpos=0.0,ypos=0.0)
player.setAnimation('./pics/blueboy_64_40.png', "down")
player.setAnimation('./pics/blueboy_64_40.png', "up")
player.setAnimation('./pics/blueboy_64_40.png', "left")
player.setAnimation('./pics/blueboy_64_40.png', "right")
player.setInitAnimation("down")
player.setXY(0.0, 0.0)
player.setdxdy(dx, dy)


danny = MyPlayer(xpos=0,ypos=0)

rects_down_danny = [(  spritex , spritey , spritewidth,spriteheight),
              (  spritex+     spritewidth , spritey , spritewidth,spriteheight),
              (  spritex+   2*spritewidth , spritey , spritewidth,spriteheight),
            (  spritex+   3*spritewidth , spritey , spritewidth,spriteheight)]

danny.setAnimation('./pics/people/danny_64_40.png', rects_down_danny, "down")
danny.setInitAnimation("down")
danny.setXY(0.0, 0.0)

"""Used to scale objects."""
def scaled_variable(variable,scale):
    return scale*variable

def scaled_anim_object(ref_object,image_w,image_h,scale_w,scale_h):
    scaled_object=ref_object 
    scaled_object.smoothscale((round(scale_w*image_w),round(scale_h*image_h)))
    return scaled_object


mainClock = pygame.time.Clock()
'''Music'''
#pygame.mixer.music.load('./music/witch-hunt.wav')
#pygame.mixer.music.load('./music/intro.wav')
#pygame.mixer.music.play(-1)

FPS=30

#pygame.key.set_repeat(100,1000)
house_scaled=house_obj

red = (100, 50, 50)
grassgreen=(170,244,66)
earthbrown=(230, 115, 0)

'''Initialization of sprite objects'''
grass_obj = MySprite('./pics/terrain/grass-map-periodic.png')
dirt_obj  = MySprite('./pics/terrain/dirt-map.png')
water_obj = MySprite('./pics/terrain/water-map.png')
stone_obj = MySprite('./pics/boundaries/stone-map.png')
hedge_obj = MySprite('./pics/boundaries/hedge-map-green.png')
block_obj = MySprite('./pics/boundaries/block-map.png')

textures={
        materials["grass"]: grass_obj,
        materials["dirt"]: dirt_obj,
        materials["stone"]: stone_obj,
        materials["water"]: water_obj,
        materials["hedge"]: hedge_obj,
        materials["block"]: block_obj
        }

for row in range(0, tilemap.nheight):
    for column in range(0, tilemap.nwidth):
        textures[tilemap.current[row][column]].setXY(round(column * tilemap.width_scaled), round(row * tilemap.height_scaled))

while True:
    windowSurface.fill(grassgreen)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        '''
        Video resize code via Stack Exchange
        https://stackoverflow.com/questions/11603222/allowing-resizing-window-pygame
        '''
        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            tempSurface = pygame.display.set_mode((event.w, event.h),HWSURFACE|DOUBLEBUF|RESIZABLE)
            windowSurface.blit(tempSurface, (0,0))
            windowSurface = tempSurface
            winx=windowSurface.get_width()
            winy=windowSurface.get_height()
            del tempSurface
            scalew=float(winx)/smallwinx
            scaleh=float(winy)/smallwiny
            tilewidth_scaled=round(scaled_variable(tilemap.width,scalew))
            tileheight_scaled=round(scaled_variable(tilemap.height,scaleh))
            for row in range(0, tilemap.nheight):
                for column in range(0, tilemap.nwidth):
                    textures[tilemap.current[row][column]].setXY(column * tilewidth_scaled, row * tileheight_scaled)
                    textures[tilemap.current[row][column]].scaleValues(scalew,scaleh)
            house_scaled=house_obj
            house_scaled.scaleValues(scalew,scaleh)

            player.setScale(scalew, scaleh)
            player.scaleValues()

            danny.setScale(scalew, scaleh)
            danny.scaleValues()

    '''Inter'''
    for row in range(0, tilemap.nheight):
        for column in range(0,tilemap.nwidth):
            textures[tilemap.current[row][column]].setXY(round(column * tilemap.width_scaled), round(row * tilemap.height_scaled))
            windowSurface.blit(textures[tilemap.current[row][column]].image_obj,textures[tilemap.current[row][column]].image_rect)

    danny.playAnim(windowSurface, "down")
    player.move(event, windowSurface)

    pygame.display.update()
    mainClock.tick(FPS) 
