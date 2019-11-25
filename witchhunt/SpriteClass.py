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
                         "down":  pygame.K_DOWN,
                         "left":  pygame.K_LEFT,
                         "right":   pygame.K_RIGHT,
                         "lp":  pygame.K_a,
                         "mp":  pygame.K_s,
                         "hp":  pygame.K_d,
                         "lk":  pygame.K_z,
                         "mk":  pygame.K_x,
                         "hk":  pygame.K_c,
                         "pause":   pygame.K_RETURN}

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


'''Sprite Class'''


class MySprite():

    #The constructor of class
    def __init__(self, imagePath, xpos = None, ypos=None):
        #'''image parameters'''
        if xpos:
            self.x = xpos
            self.x_scaled = xpos
        else:
            self.x = None
            self.x_scaled = None
        if ypos:
            self.y = ypos
            self.y_scaled = ypos
        else:
            self.y = None
            self.y_scaled = None

        self.dx = None
        self.dy = None
        self.dx_scaled = None
        self.dy_scaled = None

        self.width = None
        self.height = None

        self.width_scaled = None
        self.height_scaled = None
        self.image_obj = None
        self.image_rect = None

        '''Collision parameters'''
        self.collision_x1=None
        self.collision_x2=None
        self.collision_y1=None
        self.collision_y2=None
        self.collision_width=None
        self.collision_height=None
        self.collision_rect=None

        self.collision_x1_scaled = None
        self.collision_x2_scaled = None
        self.collision_y1_scaled = None
        self.collision_y2_scaled = None
        self.collision_width_scaled = None
        self.collision_height_scaled = None
        # self.collision_rect = None

        # Load image object
        self.image_obj_original = pygame.image.load(imagePath)
        self.image_obj = pygame.image.load(imagePath)
        # Set all image values
        self.getImageValues()

    def setXY(self, valx, valy):
        self.x=valx
        if not self.x_scaled:
            self.x_scaled=valx

        self.y=valy
        if not self.y_scaled:
            self.y_scaled=valy

        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def getObj(self):
        return self.image_obj

    def getWidth(self):
        return self.width

    def getHight(self):
        return self.height

    def getImageValues(self):
        self.image_rect = self.image_obj.get_rect()
        if not self.x:
            self.x=self.image_rect[0]
        if not self.y:
            self.y=self.image_rect[1]
        self.width=self.image_rect[2]
        self.height=self.image_rect[3]

        '''Collision parameters'''
        self.collision_x1 = self.x
        self.collision_x2 = self.x + self.width
        self.collision_y1 = self.y
        self.collision_y2 = self.y + self.height
        self.collision_width = self.width
        self.collision_height = self.height
        self.collision_rect = pygame.Rect(self.collision_x1, self.collision_y1, self.collision_width, self.collision_height)

        # self.setCollisionPos(self.x, self.x+self.width, self.y, self.y+self.height)

    def setCollisionPos(self, collX1, collX2, collY1, collY2):
        self.collision_x1 = collX1
        self.collision_x2 = collX2
        self.collision_y1 = collY1
        self.collision_y2 = collY2
        self.collision_width = self.collision_x2 - self.collision_x1
        self.collsion_height = self.collision_y2 - self.collision_y1
        self.collsion_rect   = pygame.Rect(self.collision_x1,self.collision_y1,self.collision_width,self.collision_height)

    def collision_with(self, sprite):

        if self.collision_rect.colliderect(sprite.collision_rect):
            print(sprite.collision_rect)
            print(self.collision_rect)
            print("Collision detected")
           # print(sprite)

        else:
            print("No collision detected")
        return self.collision_rect.colliderect(sprite.image_rect)

    def scaleValues(self,scalew,scaleh):
        #self.image_rect = scalew*self.image_obj.get_rect()
        self.x_scaled = int(scalew*self.x)
        self.y_scaled = int(scaleh*self.y)
        self.width_scaled = int(scalew*self.width)
        self.height_scaled = int(scaleh*self.height)
        self.image_rect = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)
        self.image_obj= pygame.transform.scale(self.image_obj_original, (self.width_scaled,self.height_scaled))

        '''Collision parameters'''
        self.collision_x1_scaled = int(scalew*self.collision_x1)
        self.collision_x2_scaled = int(scalew* self.collision_x2)
        self.collision_y1_scaled = int(scaleh*self.collision_y1)
        self.collision_y2_scaled = int(scaleh*self.collision_y2)
        self.collision_width_scaled = int(scalew*self.collision_width)
        self.collision_height_scaled = int(scaleh*self.collision_height)
        self.collision_rect = pygame.Rect(self.collision_x1_scaled,self.collision_y1_scaled,self.collision_width_scaled,self.collision_height_scaled)


class MyPlayer(Inputs):


    def __init__(self, xpos=None, ypos=None):
        # super().__init__(self,xpos=None, ypos=None)
        super().__init__()
        self.Animation = {}
        self.Animation_scaled = {}
        self.Anim_scaled = None

        self.x = xpos
        self.x_scaled = xpos
        # print "x_scaled: "+ str(self.x_scaled)

        self.y = ypos
        self.y_scaled = ypos


        self.dx = 0
        self.dx_scaled=0
        self.incr_x=0.0
        self.incr_y=0.0
        self.dscale = 1.0
        self.dy=0
        self.dy_scaled=0


        self.height = None
        self.width = None
        self.width_scaled = None
        self.height_scaled = None

        '''Collision parameters'''
        self.collision_x1 = None
        self.collision_x2 = None
        self.collision_y1 = None
        self.collision_y2 = None
        self.collision_width = None
        self.collision_height = None
        self.collision_rect = None

        self.collision_x1_scaled = None
        self.collision_x2_scaled = None
        self.collision_y1_scaled = None
        self.collision_y2_scaled = None
        self.collision_width_scaled = None
        self.collision_height_scaled = None
        # self.collision_rect = None

        self.scalew=1.0
        self.scaleh=1.0





    def setAnimation(self, spritesheet, frames, name):
        # print frames
        if not self.x:
            self.x=frames[0][2]
            self.x_scaled=frames[0][2]

        if not self.width:
            self.width=frames[0][2]
            self.width_scaled=frames[0][2]
            self.collision_x1 = self.x
            self.collision_x2 = self.x+self.width
            self.collision_width = self.width

        if not self.y:
            self.y=frames[0][3]
            self.y_scaled=frames[0][3]

        if not self.height:
            self.height=frames[0][3]
            self.height_scaled=frames[0][3]
            self.collision_y1 = self.y
            self.collision_y2 = self.y+self.height
            self.collision_height = self.height

            #print(frames[0][0],frames[0][1])
        temp=pyganim.getImagesFromSpriteSheet(spritesheet, rects=frames)
        temp = list(zip(temp, [100] * len(temp)))
        self.Animation[name]= pyganim.PygAnimation(temp)
        self.Animation_scaled[name] = pyganim.PygAnimation(temp)

        if not self.Anim_scaled:
            if self.Animation_scaled["down"]:
                self.Anim=self.Animation_scaled["down"]
            else:
                self.Anim_scaled=self.Animation_scaled[name]

    def setInitAnimation(self, name):
        self.Anim_scaled=self.Animation_scaled[name]

    def setCollisionPos(self, collX1, collX2, collY1, collY2):
        self.collision_x1 = collX1
        self.collision_x2 = collX2
        self.collision_y1 = collY1
        self.collision_y2 = collY2
        self.collision_width = self.collision_x2 - self.collision_x1
        self.collsion_height = self.collision_y2 - self.collision_y1
        self.collsion_rect   = pygame.Rect(self.collision_x1,self.collision_y1,self.collision_width,self.collision_height)

    def getCollision(self, sprite):

        if self.collision_rect.colliderect(sprite.collision_rect):
            #print(sprite.collision_rect)
            #print(self.collision_rect)
            print("Collision detected")
           # print(sprite)

        else:
            print("No collision detected")
        return self.collision_rect.colliderect(sprite.image_rect)

    def setXY(self, valx, valy):
        self.x=valx
        if not self.x_scaled:
            self.x_scaled=self.x

        self.y=valy
        if not self.y_scaled:
            self.y_scaled=self.y

    def setdxdy(self, valdx, valdy):
        self.dx=valdx
        if not self.dx_scaled:
            self.dx_scaled=valdx
        self.dy=valdy
        if not self.dy_scaled:
            self.dy_scaled=valdy

    def setScale(self, scalew, scaleh):
        self.scalew=scalew
        self.scaleh=scaleh

    def scaleValues(self):
        #self.image_rect = scalew*self.image_obj.get_rect()
        #print scalew,scaleh
        self.x_scaled = int(round(self.scalew*self.x))
        self.y_scaled = int(round(self.scaleh*self.y))
        #self.dx_scaled = int(round(self.scalew * self.dx))
        #self.dy_scaled = int(round(self.scaleh * self.dy))
        self.width_scaled = int(round(self.scalew*self.width))
        self.height_scaled = int(round(self.scaleh*self.height))
        #self.Animation_scaled={key: value for key, value in d.items()}
        #self.inv_scalew=1.0/scalew
        #self.inv_scaleh=1.0/scaleh
        #print self.x_scaled , self.y_scaled
        for key in self.Animation_scaled.keys():
            '''Warning, getCopy is necessary to avoid issues with memory address storage of transformations'''
            '''https://github.com/asweigart/pyganim/blob/master/examples/simulation_time_demo.py'''
            self.Animation_scaled[key]=self.Animation[key].getCopy()
            self.Animation_scaled[key].smoothscale((self.width_scaled, self.height_scaled))
            self.Animation_scaled[key].makeTransformsPermanent()
            #.smoothscale((self.width_scaled, self.height_scaled))

            self.Anim_scaled=self.Anim.getCopy()
            self.Anim_scaled.smoothscale((self.width_scaled, self.height_scaled))
            self.Anim_scaled.makeTransformsPermanent()


            #del self.Animation_scaled[key]
            #print value
            #self.Animation_scaled[key]=value
            #print self.Animation_scaled[key]


        #self.image_rect = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)
        #self.image_obj= pygame.transform.scale(self.image_obj_original, (self.width_scaled,self.height_scaled))

        '''Collision parameters'''
        self.collision_x1_scaled = int(round(self.scalew*self.collision_x1))
        self.collision_x2_scaled = int(round(self.scalew* self.collision_x2))
        self.collision_y1_scaled = int(round(self.scaleh*self.collision_y1))
        self.collision_y2_scaled = int(round(self.scaleh*self.collision_y2))
        #print(scalew)
        self.collision_width_scaled = int(round(self.scalew*self.collision_width))
        self.collision_height_scaled = int(round(self.scaleh*self.collision_height))
        self.collision_rect = pygame.Rect(self.collision_x1_scaled,self.collision_y1_scaled,self.collision_width_scaled,self.collision_height_scaled)
        #print str(self.x_scaled) + "!" +str(self.y_scaled)
    # def move(self,event,surface):

    #     pass
    def move(self, event, surface):
        #dx = 0.0
        #dy = 0.0
        #dx = 0.0
        #dy = 0.0
        #dscale = 1.0

        inputState = super().getInputState(event)
        # print(inputState)

        if inputState['up']:

            if inputState['down']:
                if self.Anim_scaled != self.Animation_scaled['down']:
                    self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = 0.0
                self.incr_y = 0.0

            elif inputState['right']:
                if self.Anim_scaled != self.Animation_scaled['right']:
                    self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = 0.71*self.dx
                self.incr_y = -0.71*self.dy

            elif inputState['left']:
                if self.Anim_scaled != self.Animation_scaled['left']:
                    self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = -0.71 * self.dx
                self.incr_y = -0.71 * self.dy

            else:
                self.Anim_scaled = self.Animation_scaled['up']
                self.incr_x = 0.0
                self.incr_y = -self.dy
            self.Anim_scaled.play()

        elif inputState['down']:


            # if inputState['up']:
            #     self.incr_x = 0.0
            #     self.incr_y = 0.0

            if inputState['right']:
                self.incr_x = 0.71 * self.dx
                self.incr_y = 0.71 * self.dy

            elif inputState['left']:
                self.incr_x = -0.71 * self.dx
                self.incr_y = 0.71 * self.dy

            else:
                self.Anim_scaled = self.Animation_scaled['down']
                self.incr_x = 0.0
                self.incr_y = self.dy
            self.Anim_scaled.play()

        elif inputState['right']:
            if inputState['left']:
                # print(inputState)
                if self.Anim_scaled != self.Animation_scaled['left']:
                    self.Anim_scaled = self.Animation_scaled['right']
                self.incr_x = 0.0
                self.incr_y = 0.0
            else:
                self.Anim_scaled = self.Animation_scaled['right']
                self.incr_x = self.dx
                self.incr_y = 0.0
            self.Anim_scaled.play()

        elif inputState['left']:
            # if inputState['right']:
            #     if not self.Animation_scaled['right']:
            #         self.Anim_scaled = self.Animation_scaled['left']
            #     self.incr_x = 0.0

            self.Anim_scaled = self.Animation_scaled['left']
            self.incr_x = -self.dx
            self.incr_y = 0.0
            self.Anim_scaled.play()
        else:
            self.incr_x = 0.0
            self.incr_y = 0.0
            self.Anim_scaled.pause()

        self.x = round(self.x + self.dscale * self.incr_x)
        self.y = round(self.y + self.dscale * self.incr_y )
        self.x_scaled = self.x*self.scalew
        self.y_scaled = self.y*self.scaleh
        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))

    def playAnim(self,surface,name):
        #self.Animation_scaled[name].play()#.blit(surface, (self.x_scaled, self.y_scaled))
        #if self.Animation_scaled[name]:
        #    print ("Animation exists.")
        #if not self.Animation_scaled[name].play():
        self.Anim_scaled = self.Animation_scaled[name]
        self.Anim_scaled.play()
        #print(self.x_scaled, self.y_scaled)
        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))

