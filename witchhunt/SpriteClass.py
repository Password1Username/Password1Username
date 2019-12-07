import pygame
from pygame.locals import *
import pyganim


# '''Inputs: https://stackoverflow.com/questions/15652459/pygame-arrow-control'''
#
#
class Input:
    def __init__(self):
        self.inputName = None
        self.timeSinceInput = None


class Inputs():

    def __init__(self):
        self.bindings = {"up": pygame.K_UP,
                         "down": pygame.K_DOWN,
                         "left": pygame.K_LEFT,
                         "right": pygame.K_RIGHT,
                         "lp": pygame.K_a,
                         "mp": pygame.K_s,
                         "hp": pygame.K_d,
                         "lk": pygame.K_z,
                         "mk": pygame.K_x,
                         "hk": pygame.K_c,
                         "pause": pygame.K_RETURN}

        self.inputState = {"up": False,
                           "down": False,
                           "right": False,
                           "left": False,
                           "lp": False,
                           "mp": False,
                           "hp": False,
                           "lk": False,
                           "mk": False,
                           "hk": False,
                           "pause": False}
        self.keyState = {key: self.inputState[key] for key in ("up", "down", "right", "left") if key in self.inputState}

    # self.buffer = InputBuffer()

    def lookupBinding(self, keyEntered):
        for binding, keyBound in self.bindings.items():
            if keyEntered == keyBound:
                return binding

        return "not found"

    # def getInputState(self,event):
    #     if event.type == pygame.KEYDOWN:
    #         binding = self.lookupBinding(event.key)
    #         if binding != "not found":
    #             # newInput = Input()
    #             self.inputState[binding] = True
    #     if event.type == pygame.KEYUP:
    #         binding = self.lookupBinding(event.key)
    #         if binding != "not found":
    #             self.inputState[binding] = False

    def getInputState(self, event):

        if event.type == pygame.KEYDOWN:
            binding = self.lookupBinding(event.key)
            if binding != "not found":
                newInput = Input()
                newInput.inputName = binding
                newInput.timeSinceInput = 0
                # self.buffer.push(newInput)
                self.inputState[binding] = True

        if event.type == pygame.KEYUP:
            binding = self.lookupBinding(event.key)
            if binding != "not found":
                self.inputState[binding] = False

        return self.inputState

    def getKeyState(self, event):

        if event.type == pygame.KEYDOWN:
            binding = self.lookupBinding(event.key)
            if binding != "not found":
                newInput = Input()
                newInput.inputName = binding
                newInput.timeSinceInput = 0
                # self.buffer.push(newInput)
                self.keyState[binding] = True

        if event.type == pygame.KEYUP:
            binding = self.lookupBinding(event.key)
            if binding != "not found":
                self.keyState[binding] = False

        return self.keyState


'''Sprite Class'''


class MySprite():
    ''' The constructor of class '''

    def __init__(self, imagePath, xpos=0.0, ypos=0.0):
        # ''' Load image object '''
        self.image_obj_original = pygame.image.load(imagePath)
        self.image_obj = pygame.image.load(imagePath)
        self.image_rect = self.image_obj.get_rect()
        '''Scaling factors'''
        self.scaleinx = 1.0
        self.scaleiny = 1.0
        ''' Image parameters '''
        ''' Case: xpos passed in constructor '''
        self.x = xpos
        # '''Case: ypos passed in constructor'''
        self.y = ypos
        self.width = self.image_rect[2]
        self.height = self.image_rect[3]
        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # Set all image values
        # self.getImageValues()
        self.dx = 0.0
        self.dy = 0.0
        '''Collision parameters'''
        self.collision_x1 = self.x
        self.collision_y1 = self.y
        self.collision_width = self.width
        self.collision_height = self.height
        self.collision_rect = self.image_rect

        self.collision_x2 = self.collision_x1 + self.collision_width
        self.collision_y2 = self.collision_y1 + self.collision_height

        '''Scaled parameters'''
        self.x_scaled = self.x * self.scaleinx
        self.y_scaled = self.y * self.scaleiny
        self.width_scaled = self.width * self.scaleinx
        self.height_scaled = self.height * self.scaleiny
        self.image_rect_scaled = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)
        self.dx_scaled = 0.0
        self.dy_scaled = 0.0
        # print(self.width)
        # exit()

        self.collision_x1_scaled = self.x_scaled
        self.collision_x2_scaled = self.collision_x1_scaled + self.width_scaled
        self.collision_y1_scaled = self.y_scaled
        self.collision_y2_scaled = self.collision_y1_scaled + self.height_scaled
        self.collision_width_scaled = self.width_scaled
        self.collision_height_scaled = self.height_scaled
        self.collision_rect_scaled = self.image_rect_scaled

    def setXY(self, valx, valy):
        self.x = valx
        self.y = valy
        # print(self.width,self.height)
        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.setCollisionPos(self.x, self.x + self.collision_width, self.y, self.y + self.collision_height)

        self.x_scaled = self.x * self.scaleinx
        self.y_scaled = self.y * self.scaleiny
        self.image_rect_scaled = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)
        # print(self.collision_width,self.collision_height)
        # self.setCollisionPos(self.x, self.x + self.collision_width, self.y, self.y + self.collision_height)

    def getObj(self):
        return self.image_obj

    def getWidth(self):
        return self.width

    def getHight(self):
        return self.height

    def setCollisionPos(self, collX1, collX2, collY1, collY2):
        self.collision_x1 = collX1
        self.collision_x2 = collX2
        self.collision_y1 = collY1
        self.collision_y2 = collY2
        if not self.collision_width:
            self.collision_width = self.collision_x2 - self.collision_x1
            self.collision_height = self.collision_y2 - self.collision_y1
        # print(self.collision_x1, self.collision_y1)
        # print(self.collision_width,self.collision_height)
        self.collision_rect = pygame.Rect(self.collision_x1, self.collision_y1,
                                          self.collision_width, self.collision_height)

        ''' Scaled quantities'''
        self.collision_x1_scaled = self.collision_x1 * self.scaleinx
        self.collision_x2_scaled = self.collision_x2 * self.scaleinx
        self.collision_y1_scaled = self.collision_y1 * self.scaleiny
        self.collision_y2_scaled = self.collision_y2 * self.scaleiny
        self.collision_width_scaled = self.collision_x2_scaled - self.collision_x1_scaled
        self.collision_height_scaled = self.collision_y2_scaled - self.collision_y1_scaled
        self.collision_rect_scaled = pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,
                                                 self.collision_width_scaled, self.collision_height_scaled)

    def collision_with(self, sprite):

        if self.collision_rect.colliderect(sprite.collision_rect):
            # print(sprite.collision_rect)
            # print(self.collision_rect)
            print("Collision detected")
        # print(sprite)

        else:
            print("No collision detected")
        return self.collision_rect.colliderect(sprite.image_rect)

    def scaleValues(self, scalew, scaleh):
        # self.image_rect = scalew*self.image_obj.get_rect()
        self.scaleinx = scalew
        self.scaleiny = scaleh
        self.x_scaled = int(self.scaleinx * self.x)
        self.y_scaled = int(self.scaleiny * self.y)
        self.width_scaled = int(self.scaleinx * self.width)
        self.height_scaled = int(self.scaleiny * self.height)
        self.image_rect = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)
        self.image_obj = pygame.transform.scale(self.image_obj_original, (self.width_scaled, self.height_scaled))

        '''Collision parameters'''
        self.collision_x1_scaled = int(self.scaleinx * self.collision_x1)
        self.collision_x2_scaled = int(self.scaleinx * self.collision_x2)
        self.collision_y1_scaled = int(self.scaleiny * self.collision_y1)
        self.collision_y2_scaled = int(self.scaleiny * self.collision_y2)
        self.collision_width_scaled = int(self.scaleinx * self.collision_width)
        self.collision_height_scaled = int(self.scaleiny * self.collision_height)
        # print(self.collision_x1_scaled, self.collision_y1_scaled,self.collision_width_scaled, self.collision_height_scaled)
        # print( "rect",pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,self.collision_width_scaled, self.collision_height_scaled))
        # exit()
        self.collision_rect_scaled = pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,
                                                 self.collision_width_scaled, self.collision_height_scaled)
        # print(rect ,self.collision_rect_scaled)


class MyPlayer(Inputs):

    def __init__(self, xpos=0.0, ypos=0.0):
        # super().__init__(self,xpos=None, ypos=None)
        super().__init__()

        self.scaleinx = 1.0
        self.scaleiny = 1.0

        self.Animation = {}
        self.Animation_scaled = {}
        self.Anim_scaled = None
        self.Anim = None

        if xpos:
            self.x = xpos
            self.x_scaled = self.x * self.scaleinx
            # '''Case: xpos not passed in constructor '''
        else:
            self.x = 0.0
            self.x_scaled = self.x * self.scaleinx
            # '''Case: ypos passed in constructor'''
        if ypos:
            self.y = ypos
            self.y_scaled = self.y * self.scaleiny
            # '''Case: ypos not passed in constructor'''
        else:
            self.y = 0.0
            self.y_scaled = self.y * self.scaleiny

        self.dx = 0.0
        self.dx_scaled = 0.0
        self.incr_x = 0.0
        self.incr_y = 0.0
        self.dscale = 1.0
        self.dy = 0
        self.dy_scaled = 0

        self.width = 0.0
        self.height = 0.0

        self.width_scaled = self.width * self.scaleinx
        self.height_scaled = self.height * self.scaleiny

        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image_rect_scaled = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)

        '''Collision parameters'''
        self.collision_x1 = self.x
        self.collision_x2 = self.collision_x1 + self.width
        self.collision_y1 = self.y
        self.collision_y2 = self.collision_y1 + self.height
        self.collision_width = self.width
        self.collision_height = self.height
        self.collision_rect = self.image_rect

        self.collision_x1_scaled = self.x_scaled
        self.collision_x2_scaled = self.collision_x1_scaled + self.width_scaled
        self.collision_y1_scaled = self.y_scaled
        self.collision_y2_scaled = self.collision_y1_scaled + self.height_scaled
        self.collision_width_scaled = self.width_scaled
        self.collision_height_scaled = self.height_scaled
        self.collision_rect_scaled = self.image_rect_scaled

    def setAnimation(self, spritesheet, frames, name):
        # print frames

        self.x = frames[0][2]
        self.x_scaled = frames[0][2] * self.scaleinx

        if self.width == 0:
            self.width = frames[0][2]
            self.collision_x1 = self.x
            self.collision_x2 = self.x + self.width
            self.collision_width = self.width

            self.width_scaled = frames[0][2]
            self.collision_x1_scaled = self.x * self.scaleinx
            self.collision_x2_scaled = self.x_scaled + self.width_scaled
            self.collision_width_scaled = self.width * self.scaleinx

        if not self.y:
            self.y = frames[0][3]
            self.collision_y1 = self.y

            self.width_scaled = frames[0][2] * self.scaleiny
            self.y_scaled = self.y * self.scaleiny
            self.collision_y1_scaled = self.y_scaled

        if not self.height:
            self.height = frames[0][3]
            self.collision_height = self.height
            self.collision_y2 = self.collision_y1 + self.collision_height

            self.height_scaled = self.height * self.scaleiny
            self.collision_y2_scaled = self.collision_y1_scaled + self.collision_height_scaled

            # print(frames[0][0],frames[0][1])
        temp = pyganim.getImagesFromSpriteSheet(spritesheet, rects=frames)
        temp = list(zip(temp, [100] * len(temp)))
        self.Animation[name] = pyganim.PygAnimation(temp)
        self.Animation_scaled[name] = pyganim.PygAnimation(temp)

        if not self.Anim_scaled:
            if self.Animation_scaled["down"]:
                self.Anim = self.Animation_scaled["down"]
            else:
                self.Anim_scaled = self.Animation_scaled[name]

    def setInitAnimation(self, name):
        self.Anim_scaled = self.Animation_scaled[name]

    def setCollisionPos(self, collx1, collx2, colly1, colly2):

        self.collision_x1 = collx1
        self.collision_x2 = collx2
        self.collision_y1 = colly1
        self.collision_y2 = colly2
        self.collision_width = self.collision_x2 - self.collision_x1
        self.collision_height = self.collision_y2 - self.collision_y1
        self.collision_rect = pygame.Rect(self.collision_x1, self.collision_y1, self.collision_width,
                                          self.collision_height)

        self.collision_x1_scaled = self.collision_x1 * self.scaleinx
        self.collision_x2_scaled = self.collision_x2 * self.scaleinx
        self.collision_y1_scaled = self.collision_y1 * self.scaleiny
        self.collision_y2_scaled = self.collision_y2 * self.scaleiny
        self.collision_width_scaled = self.collision_x2_scaled - self.collision_x1_scaled
        self.collision_height_scaled = self.collision_y2_scaled - self.collision_y1_scaled
        self.collision_rect_scaled = pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,
                                                 self.collision_width_scaled, self.collision_height_scaled)

    def collision_with(self, sprite):
        # print("player " + str(self.collision_rect), "sprite " + str(sprite.collision_rect))
        # print(self.collision_rect)
        value=self.collision_rect.colliderect(sprite.collision_rect)
        if value==1:
            if self.dx>0:
                if self.incr_x > 0:  # Moving right; Hit the left side of the wall
                    self.setX(sprite.collision_x1-sprite.collision_width)
                if self.incr_x < 0: # Moving left; Hit the right side of the wall
                    self.setX(sprite.collision_x2)
                if self.incr_y > 0:  # Moving down; Hit the top side of the wall
                    self.setY(sprite.collision_y1-sprite.collision_height)
                if self.incr_y < 0:  # Moving up; Hit the bottom side of the wall
                    self.setY(sprite.collision_y2)
        return value

    def setX(self,valx):
        self.x = valx
        self.x_scaled = self.x * self.scaleinx

    def setY(self,valy):

        self.y = valy
        self.y_scaled = self.y * self.scaleiny


    def setXY(self, valx, valy):

        self.x = valx
        self.x_scaled = self.x * self.scaleinx

        self.y = valy
        self.y_scaled = self.y * self.scaleiny

    def setdxdy(self, valdx, valdy):
        self.dx = valdx
        self.dx_scaled = self.dx * self.scaleinx
        self.dy = valdy
        self.dy_scaled = self.dy * self.scaleiny

    def setScale(self, scalew, scaleh):
        self.scaleinx = scalew
        self.scaleiny = scaleh
        # print(self.scaleinx, self.scaleiny)
        self.scaleValues()

    def scaleValues(self):
        # self.image_rect = scalew*self.image_obj.get_rect()
        # print (self.scaleinx, self.scaleiny)
        self.x_scaled = int(round(self.scaleinx * self.x))
        self.y_scaled = int(round(self.scaleiny * self.y))
        # self.dx_scaled = int(round(self.scalew * self.dx))
        # self.dy_scaled = int(round(self.scaleh * self.dy))
        self.width_scaled = int(round(self.scaleinx * self.width))
        self.height_scaled = int(round(self.scaleiny * self.height))
        # self.Animation_scaled={key: value for key, value in d.items()}
        # self.inv_scalew=1.0/scalew
        # self.inv_scaleh=1.0/scaleh
        # print self.x_scaled , self.y_scaled
        for key in self.Animation_scaled.keys():
            '''Warning, getCopy is necessary to avoid issues with memory address storage of transformations'''
            '''https://github.com/asweigart/pyganim/blob/master/examples/simulation_time_demo.py'''
            self.Animation_scaled[key] = self.Animation[key].getCopy()
            self.Animation_scaled[key].smoothscale((self.width_scaled, self.height_scaled))
            self.Animation_scaled[key].makeTransformsPermanent()
            # .smoothscale((self.width_scaled, self.height_scaled))

            self.Anim_scaled = self.Anim.getCopy()
            self.Anim_scaled.smoothscale((self.width_scaled, self.height_scaled))
            self.Anim_scaled.makeTransformsPermanent()

        '''Collision parameters'''
        self.collision_x1_scaled = int(round(self.scaleinx * self.collision_x1))
        self.collision_x2_scaled = int(round(self.scaleinx * self.collision_x2))
        self.collision_y1_scaled = int(round(self.scaleiny * self.collision_y1))
        self.collision_y2_scaled = int(round(self.scaleiny * self.collision_y2))

        self.collision_width_scaled = int(round(self.scaleinx * self.collision_width))
        self.collision_height_scaled = int(round(self.scaleiny * self.collision_height))
        self.collision_rect = pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,
                                          self.collision_width_scaled, self.collision_height_scaled)

    def move(self, event, surface):
        # dx = 0.0
        # dy = 0.0
        # dx = 0.0
        # dy = 0.0
        # dscale = 1.0

        keyState = super().getKeyState(event)
        # print(inputState)
        pressedKeys = sum(keyState.values())
        # print(pressedKeys)

        '''Efficient way to implement keys with minimal'''

        if pressedKeys == 2:
            if keyState['up']:
                if keyState['left']:
                    self.incr_x = -0.71 * self.dx
                    self.incr_y = -0.71 * self.dy
                elif keyState['right']:
                    self.incr_x = 0.71 * self.dx
                    self.incr_y = -0.71 * self.dy
                else:
                    self.incr_x = 0.0
                    self.incr_y = 0.0

            elif keyState['down']:
                if keyState['left']:
                    self.incr_x = -0.71 * self.dx
                    self.incr_y = 0.71 * self.dy
                elif keyState['right']:
                    self.incr_x = 0.71 * self.dx
                    self.incr_y = 0.71 * self.dy
                else:
                    self.incr_x = 0.0
                    self.incr_y = 0.0
            else:
                self.incr_x = 0.0
                self.incr_y = 0.0

            self.Anim_scaled.play()

        elif pressedKeys == 1:
            if keyState['up']:
                self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = 0.0
                self.incr_y = -self.dy
            if keyState['down']:
                self.Anim_scaled = self.Animation_scaled['down']
                self.incr_x = 0.0
                self.incr_y = self.dy
            elif keyState['left']:
                self.Anim_scaled = self.Animation_scaled['left']
                self.incr_x = -self.dx
                self.incr_y = 0.0
            elif keyState['right']:
                self.Anim_scaled = self.Animation_scaled['right']
                self.incr_x = self.dx
                self.incr_y = 0.0
            self.Anim_scaled.play()

        elif pressedKeys == 3:
            if not keyState['up']:
                self.Anim_scaled = self.Animation_scaled['down']
                self.incr_x = 0.0
                self.incr_y = self.dy
            elif not keyState['down']:
                self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = 0.0
                self.incr_y = -self.dy
            elif not keyState['left']:
                self.Anim_scaled = self.Animation_scaled['right']
                self.incr_x = self.dx
                self.incr_y = 0.0
            elif not keyState['right']:
                self.Anim_scaled = self.Animation_scaled['left']
                self.incr_x = -self.dx
                self.incr_y = 0.0
            self.Anim_scaled.play()
        else:
            self.incr_y = 0.0
            self.incr_x = 0.0
            self.Anim_scaled.pause()

        self.x = round(self.x + self.dscale * self.incr_x)
        self.y = round(self.y + self.dscale * self.incr_y)
        self.x_scaled = self.x * self.scaleinx
        self.y_scaled = self.y * self.scaleiny
        # print(self.collision_width,self.collision_height)
        self.setCollisionPos(self.x, self.x + self.collision_width, self.y, self.y + self.collision_height)
        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))

    def playAnim(self, surface, name):
        # self.Animation_scaled[name].play()#.blit(surface, (self.x_scaled, self.y_scaled))
        # if self.Animation_scaled[name]:
        # print ("Animation exists.")
        # if not self.Animation_scaled[name].play():
        self.Anim_scaled = self.Animation_scaled[name]
        self.Anim_scaled.play()
        # print(self.x_scaled, self.y_scaled)
        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))
