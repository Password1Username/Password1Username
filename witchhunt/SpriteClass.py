import pygame
from pygame.locals import *
import pyganim

pygame.init()


# '''Inputs: https://stackoverflow.com/questions/15652459/pygame-arrow-control'''
#
#
class Input:
    def __init__(self):
        self.inputName = None
        self.timeSinceInput = None


class Inputs:

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


'''Class storing parameters'''


class MyObject():
    ''' The constructor of class '''

    def __init__(self, xpos=0.0, ypos=0.0):
        '''Scaling factors'''
        self.scaleinx = 1.0
        self.scaleiny = 1.0

        # ''' Case: xpos passed in constructor '''
        self.x = xpos
        # '''Case: ypos passed in constructor'''
        self.y = ypos

        self.dx = 0.0
        self.dy = 0.0

        '''Scaled parameters'''
        self.x_scaled = self.x * self.scaleinx
        self.y_scaled = self.y * self.scaleiny

        '''Collision parameters'''
        self.collision_x1 = self.x
        self.collision_y1 = self.y

        self.dx_scaled = self.dx * self.scaleinx
        self.dy_scaled = self.dx * self.scaleiny

        self.collision_x1_scaled = self.x_scaled
        self.collision_y1_scaled = self.y_scaled


# MySprite Class
class MySprite(MyObject):
    # ''' The constructor of class '''

    def __init__(self, imagePath):
        super().__init__()
        # ''' Load image object '''
        self.image_obj_original = pygame.image.load(imagePath)
        self.image_obj = pygame.image.load(imagePath)
        self.image_rect = self.image_obj.get_rect()

        ''' Image parameters '''
        self.width = self.image_rect[2]
        self.height = self.image_rect[3]
        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Set all image values
        # self.getImageValues()
        self.collision_width = self.width
        self.collision_height = self.height

        self.collision_center_x = self.collision_x1 + 0.5 * self.collision_width
        self.collision_center_y = self.collision_y1 + 0.5 * self.collision_height

        # '''Scaled quantities'''
        self.width_scaled = self.width * self.scaleinx
        self.height_scaled = self.height * self.scaleiny

        # print(self.width)
        # exit()

        self.collision_width_scaled = self.width_scaled
        self.collision_height_scaled = self.height_scaled

        self.collision_center_x_scaled = self.collision_x1_scaled + 0.5 * self.collision_width_scaled
        self.collision_center_y_scaled = self.collision_y1_scaled + 0.5 * self.collision_height_scaled

    # Getter functions
    def getObj(self):
        return self.image_obj

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setCollisionX(self, collX1):
        self.collision_x1 = collX1
        self.collision_x1_scaled = collX1 * self.scaleinx

    def setCollisionY(self, collY1):
        self.collision_y1 = collY1
        self.collision_y1_scaled = collY1 * self.scaleiny

    def setCollisionWidth(self, collw):
        self.collision_width = collw
        self.collision_width_scaled = collw * self.scaleinx

    def setCollisionHeight(self, collh):
        self.collision_height = collh
        self.collision_height_scaled = collh * self.scaleiny

    def collision_with(self, sprite):

        collision_rect = pygame.Rect(self.collision_x1, self.collision_y1_,
                                     self.collision_width, self.collision_height)

        if collision_rect.colliderect(sprite.collision_rect):
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
        self.collision_y1_scaled = int(self.scaleiny * self.collision_y1)
        self.collision_width_scaled = int(self.scaleinx * self.collision_width)
        self.collision_height_scaled = int(self.scaleiny * self.collision_height)
        # print(self.collision_x1_scaled, self.collision_y1_scaled,self.collision_width_scaled, self.collision_height_scaled)
        # print( "rect",pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,self.collision_width_scaled, self.collision_height_scaled))
        # exit()
        self.collision_rect_scaled = pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,
                                                 self.collision_width_scaled, self.collision_height_scaled)
        # print(rect ,self.collision_rect_scaled)

    def setX(self, valx):
        self.x = valx
        self.x_scaled = valx * self.scaleinx

    def setY(self, valy):

        self.y = valy
        self.y_scaled = valy * self.scaleiny


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
        self.collision_y1 = self.y

        self.collision_width = self.width
        self.collision_height = self.height

        self.x_offset = self.x - self.collision_x1
        self.y_offset = self.y - self.collision_y1

        self.collision_x1_scaled = self.x_scaled
        self.collision_y1_scaled = self.y_scaled

        self.collision_width_scaled = self.width_scaled
        self.collision_height_scaled = self.height_scaled

        self.collision_center_x_scaled = self.x_scaled + 0.5 * self.width_scaled
        self.collision_center_y_scaled = self.y_scaled + 0.5 * self.height_scaled

    """Setter functions"""
    def setX(self, valx):
        self.x = valx
        self.x_scaled = self.x * self.scaleinx

    def setY(self, valy):

        self.y = valy
        self.y_scaled = self.y * self.scaleiny

    def setdx(self, valdx):
        self.dx = valdx
        self.dx_scaled = self.dx * self.scaleinx

    def setdy(self, valdy):
        self.dy = valdy
        self.dy_scaled = self.dy * self.scaleiny

    def setScale(self, scalew, scaleh):
        self.scaleinx = scalew
        self.scaleiny = scaleh
        # print(self.scaleinx, self.scaleiny)

    def setCollisionX(self, collX1):
        self.collision_x1 = collX1
        self.collision_x1_scaled = collX1 * self.scaleinx

    def setCollisionY(self, collY1):
        self.collision_y1 = collY1
        self.collision_y1_scaled = collY1 * self.scaleiny

    def set_hitbox_X(self, collX1):
        self.x_offset = self.x - collX1
        self.collision_x1 = collX1
        self.collision_x1_scaled = collX1 * self.scaleinx

    def set_hitbox_Y(self, collY1):
        self.y_offset = self.y - collY1
        self.collision_y1 = collY1
        self.collision_y1_scaled = collY1 * self.scaleiny

    def set_dx(self, val_dx):
        self.dx = val_dx

    def set_dy(self, val_dy):
        self.dy = val_dy

    def set_incr_x(self, val_incr_x):
        self.incr_x = val_incr_x
        self.incr_x_scaled = val_incr_x * self.scaleinx

    def set_incr_y(self, val_incr_y):
        self.incr_y = val_incr_y
        self.incr_y_scaled = val_incr_y * self.scaleiny

    def set_collision_width(self, collw):
        self.collision_width = collw
        self.collision_width_scaled = collw * self.scaleinx

    def set_collision_height(self, collh):
        self.collision_height = collh
        self.collision_height_scaled = collh * self.scaleiny

    def setInitAnimation(self, name):
        self.Anim_scaled = self.Animation_scaled[name]

    def setAnimation(self, spritesheet, frames, name):
        # print frames

        self.x = frames[0][2]
        self.x_scaled = frames[0][2] * self.scaleinx

        if self.width == 0:
            self.width = frames[0][2]
            self.collision_x1 = self.x
            self.collision_width = self.width

            self.width_scaled = frames[0][2]
            self.collision_x1_scaled = self.x * self.scaleinx
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

    def intersect_with(self, rect_a, rect_b):
        return rect_a.colliderect(rect_b)

    def collision_with(self, sprite):
        # print("player " + str(self.collision_rect))
        # print("player " + str(self.collision_rect), "sprite " + str(sprite.collision_rect))
        # print(self.collision_rect)
        anim_collision_rect = pygame.Rect(self.collision_x1, self.collision_y1, self.collision_width,
                                          self.collision_height)
        sprite_collision_rect = pygame.Rect(sprite.collision_x1, sprite.collision_y1,
                                            sprite.collision_width, sprite.collision_height)

        value = self.intersect_with(anim_collision_rect, sprite_collision_rect)

        if value == 1:
            if self.incr_x != 0:
                # Moving right; Hit the left side of the tile
                if anim_collision_rect.right + self.incr_x > sprite_collision_rect.left > anim_collision_rect.left:

                    self.setX(sprite_collision_rect.left - self.width + abs(self.x_offset))
                    # print(self.x_offset)
                    self.setCollisionX(self.x - self.x_offset)

                # Moving left; Hit the right side of the tile
                elif self.collision_x1 < sprite_collision_rect.right < anim_collision_rect.right + self.incr_x:

                    self.setX(sprite_collision_rect.right - abs(self.x_offset))
                    self.setCollisionX(self.x - self.x_offset)
            if self.incr_y != 0:
                # Moving down; Hit the top side of the tile
                if anim_collision_rect.bottom + self.incr_y > sprite_collision_rect.top > anim_collision_rect.top:

                    # self.x_offset = self.x - self.collision_x1
                    # self.y_offset = self.y - self.collision_y1

                    self.setY(sprite.collision_y1 - self.height + abs(self.y_offset))
                    self.setCollisionY(self.y - self.y_offset)

                # Moving up; Hit the bottom side of the tile
                elif anim_collision_rect.bottom > sprite_collision_rect.bottom > self.collision_y1 + self.incr_y:

                    self.setY(sprite_collision_rect.bottom - abs(self.y_offset))
                    self.setCollisionY(self.y - self.y_offset)

        return value

    def move(self, surface, event):
        """ This method is used to map keyboard inputs to the animations and their position """
        key_state = super().getKeyState(event)
        # print(inputState)
        pressed_keys = sum(key_state.values())
        # print(pressed_keys)

        # '''Efficient way to implement keys with minimal'''
        self.incr_x = 0
        self.incr_y = 0

        if pressed_keys == 2:
            if key_state['up']:
                if key_state['left']:
                    self.incr_x = -0.71 * self.dx
                    self.incr_y = -0.71 * self.dy
                elif key_state['right']:
                    self.incr_x = 0.71 * self.dx
                    self.incr_y = -0.71 * self.dy

            elif key_state['down']:
                if key_state['left']:
                    self.incr_x = -0.71 * self.dx
                    self.incr_y = 0.71 * self.dy
                elif key_state['right']:
                    self.incr_x = 0.71 * self.dx
                    self.incr_y = 0.71 * self.dy

            self.Anim_scaled.play()

        elif pressed_keys == 1:
            if key_state['up']:
                self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = 0.0
                self.incr_y = -self.dy
            if key_state['down']:
                self.Anim_scaled = self.Animation_scaled['down']
                self.incr_x = 0.0
                self.incr_y = self.dy
            elif key_state['left']:
                self.Anim_scaled = self.Animation_scaled['left']
                self.incr_x = -self.dx
                self.incr_y = 0.0
            elif key_state['right']:
                self.Anim_scaled = self.Animation_scaled['right']
                self.incr_x = self.dx
                self.incr_y = 0.0
            self.Anim_scaled.play()

        elif pressed_keys == 3:
            if not key_state['up']:
                self.Anim_scaled = self.Animation_scaled['down']
                self.incr_x = 0.0
                self.incr_y = self.dy
            elif not key_state['down']:
                self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = 0.0
                self.incr_y = -self.dy
            elif not key_state['left']:
                self.Anim_scaled = self.Animation_scaled['right']
                self.incr_x = self.dx
                self.incr_y = 0.0
            elif not key_state['right']:
                self.Anim_scaled = self.Animation_scaled['left']
                self.incr_x = -self.dx
                self.incr_y = 0.0
            self.Anim_scaled.play()
        else:
            self.incr_y = 0.0
            self.incr_x = 0.0
            self.Anim_scaled.pause()

        self.setX(round(self.x + self.incr_x))
        self.setY(round(self.y + self.incr_y))

        # print(self.collision_width,self.collision_height)
        self.setCollisionX(self.x - self.x_offset)
        self.setCollisionY(self.y - self.y_offset)

        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))
        # pygame.draw.rect(surface, (0, 0, 0), Rect(self.collision_x1, self.collision_y1,
        #                                           self.collision_width, self.collision_height))
        # self.set_incr_x(0)
        # self.set_incr_y(0)

    def playAnim(self, surface, name):
        # self.Animation_scaled[name].play()#.blit(surface, (self.x_scaled, self.y_scaled))
        # if self.Animation_scaled[name]:
        # print ("Animation exists.")
        # if not self.Animation_scaled[name].play():
        self.Anim_scaled = self.Animation_scaled[name]
        self.Anim_scaled.play()
        # print(self.x_scaled, self.y_scaled)
        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))
