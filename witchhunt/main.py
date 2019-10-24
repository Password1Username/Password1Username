#!/usr/bin/python

# trex image from Wyverii on http://opengameart.org/content/unsealed-terrex

import sys
import os
sys.path.append(os.path.abspath('..'))
import pygame
from pygame.locals import *
import pyganim
import math as m
from SpriteClass import MySprite, MyPlayer


pygame.init()


'''Tile map dimensions'''
nwidth=16
nheight=16

tilewidth=32
tilewidth_scaled=32
tileheight=32
tileheight_scaled=32



# set up the window
smallwinx=tilewidth*nwidth
winx=smallwinx
smallwiny=tileheight*nheight
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

#create dummy house object
#house = pygame.image.load('./pics/buildings/haus1.png')

#First try for using the sprite class
house_obj = MySprite('./pics/buildings/haus1.png', housex, housey)
#house_obj
#house_obj.

sheetwidth=6*64
sheetheight=2*40
'''Picture offset'''
spritey=0
spritex=0
spritewidth=64
spriteheight=40

rects_up   = [(  spritex+   3*spritewidth , spritey , spritewidth,spriteheight),
              (  spritex+   4*spritewidth , spritey , spritewidth,spriteheight),
              (  spritex+   5*spritewidth , spritey , spritewidth,spriteheight)]   

rects_down = [(  spritex                  , spritey , spritewidth,spriteheight),
              (  spritex+     spritewidth , spritey , spritewidth,spriteheight),
              (  spritex+   2*spritewidth , spritey , spritewidth,spriteheight)]   

rects_left = [(  spritex                  , spritey+spriteheight , spritewidth,spriteheight),
              (  spritex+     spritewidth , spritey+spriteheight , spritewidth,spriteheight),
              (  spritex+   2*spritewidth , spritey+spriteheight , spritewidth,spriteheight)]   

rects_right= [(  spritex+   3*spritewidth , spritey+spriteheight , spritewidth,spriteheight),
              (  spritex+   4*spritewidth , spritey+spriteheight , spritewidth,spriteheight),
              (  spritex+   5*spritewidth , spritey+spriteheight , spritewidth,spriteheight)]   







# playerAnim_scaled = playerAnim_down

player = MyPlayer(xpos=0.0,ypos=0.0)
player.feedAnimation('./pics/blueboy_64_40.png' , rects_down , "down")
player.feedAnimation('./pics/blueboy_64_40.png' , rects_up , "up")
player.feedAnimation('./pics/blueboy_64_40.png' , rects_left ,"left")
player.feedAnimation('./pics/blueboy_64_40.png', rects_right ,"right")
player.initAnimation("down")
player.readxy(0.0,0.0)
player.readdxdy(dx,dy)


danny = MyPlayer(xpos=0,ypos=0)

rects_down_danny = [(  spritex , spritey , spritewidth,spriteheight),
              (  spritex+     spritewidth , spritey , spritewidth,spriteheight),
              (  spritex+   2*spritewidth , spritey , spritewidth,spriteheight),
            (  spritex+   3*spritewidth , spritey , spritewidth,spriteheight)]

danny.feedAnimation('./pics/people/danny_64_40.png', rects_down_danny, "down")
danny.initAnimation("down")
danny.readxy(0.0,0.0)
#player.readdxdy(dx,dy)


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
pygame.mixer.music.load('./music/intro.wav')
pygame.mixer.music.play(0)

FPS=30

#pygame.key.set_repeat(100,1000)
house_scaled=house_obj


red = (100, 50, 50)
grassgreen=(170,244,66)
earthbrown=(230, 115, 0)


grass=0
dirt=1
water=3
hedge=4
stone=5
block=6

'''Initialization of sprite objects'''
grass_obj = MySprite('./pics/terrain/grass-map-periodic.png')
dirt_obj  = MySprite('./pics/terrain/dirt-map.png')
water_obj = MySprite('./pics/terrain/water-map.png')
stone_obj = MySprite('./pics/boundaries/stone-map.png')
hedge_obj = MySprite('./pics/boundaries/hedge-map-green.png')
block_obj = MySprite('./pics/boundaries/block-map.png')

                                     
textures={
        grass: grass_obj,
        dirt: dirt_obj,
        stone: stone_obj,
        water: water_obj,
        hedge: hedge_obj,
        block: block_obj
        }

tilemap=[[grass,grass,grass,grass,grass,grass,block,dirt ,block,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,grass,dirt ,grass,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,grass,dirt ,hedge,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,hedge,dirt ,grass,grass,grass,grass,grass,grass,grass,grass], 
         [grass,grass,grass,grass,grass,grass,grass,dirt ,grass,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,grass,dirt ,grass,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,grass,dirt ,hedge,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,hedge,dirt ,grass,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,grass,dirt ,grass,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,grass,dirt ,grass,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,grass,dirt ,hedge,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,grass,hedge,dirt ,grass,grass,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,stone,water,water,water,stone,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,stone,water,water,water,stone,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,hedge,water,water,water,hedge,grass,grass,grass,grass,grass,grass],
         [grass,grass,grass,grass,grass,hedge,hedge,hedge,hedge,hedge,grass,grass,grass,grass,grass,grass]]

for row in range(0, nheight):
    for column in range(0, nwidth):
        # print str(row)+","+str(column)
        # print(tilemap[row][column])
        # print(block_obj.collision_with(house_obj))

        textures[tilemap[row][column]].readxy(round(column * tilewidth_scaled), round(row * tileheight_scaled))





while True:
    windowSurface.fill(grassgreen)
    #scaleh=1.0
    #scalew=1.0
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
            tilewidth_scaled=round(scaled_variable(tilewidth,scalew))
            tileheight_scaled=round(scaled_variable(tileheight,scaleh))
            #textures[tilemap[row][column]].image_rect
            #textures={key: pygame.transform.scale(textures[key] , (int(tilewidth_scaled),int(tileheight_scaled))) for (key,textures[key]) in textures.items()}
            for row in range(0, nheight):
                for column in range(0, nwidth):
                    textures[tilemap[row][column]].readxy(column * tilewidth_scaled,row * tileheight_scaled)
                    textures[tilemap[row][column]].scaleValues(scalew,scaleh)
                    #print(textures[tilemap[row][column]].image_rect)
            #xpos_scaled=scaled_variable(xpos,scalew)
            #ypos_scaled=scaled_variable(ypos,scaleh)

            house_scaled=house_obj
            house_scaled.scaleValues(scalew,scaleh)

            #print player.Animation_scaled
            player.readScale(scalew,scaleh)
            player.scaleValues()
            player.move(event, windowSurface)

            danny.readScale(scalew, scaleh)
            danny.scaleValues()
            #danny.playAnim"down"]
            #danny.move(event, windowSurface)

    '''Inter'''
    for row in range(0,nheight):
        for column in range(0,nwidth):
            #print str(row)+","+str(column)
            #print(tilemap[row][column])
            #print(block_obj.collision_with(house_obj))
            textures[tilemap[row][column]].readxy(round(column * tilewidth_scaled), round(row * tileheight_scaled))
            #textures[tilemap[row][column]].image_rect=(round(column * tilewidth_scaled), round(row * tileheight_scaled), m.ceil(tilewidth_scaled),m.ceil(tileheight_scaled))
            #print(textures[tilemap[row][column]].image_rect)
            windowSurface.blit(textures[tilemap[row][column]].image_obj,textures[tilemap[row][column]].image_rect)


    # print(event)
    #print player.x_scaled, player.y_scaled
    #windowSurface.blit(house_scaled.image_obj, (house_scaled.x_scaled,house_scaled.y_scaled)) #display house on
    #player.Anim_scaled.blit(windowSurface, (player.x_scaled,player.y_scaled))
    danny.playAnim(windowSurface, "down")
    #print(danny.x_scaled,danny.y_scaled)
    player.move(event, windowSurface)
    #print(player.x_scaled, player.y_scaled)

    #print(danny.x_scaled)
    #danny.move(event,windowSurface)
    #player.Anim_scaled.blit(windowSurface, (player.x_scaled, player.y_scaled))
    pygame.display.update()
    mainClock.tick(FPS) 



