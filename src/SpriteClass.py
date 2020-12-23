import pygame

pygame.init()


# '''Class storing parameters'''
class MyObject:
    # ''' The initializer of class '''
    def __init__(self, x_pos=0.0, y_pos=0.0):
        # '''Scaling factors'''
        self.scale_in_x = 1.0
        self.scale_in_y = 1.0

        # ''' Case: x_pos passed in constructor '''
        self.x = x_pos
        # '''Case: y_pos passed in constructor'''
        self.y = y_pos

        self.dx = 0.0
        self.dy = 0.0

        '''Scaled parameters'''
        self.x_scaled = self.x * self.scale_in_x
        self.y_scaled = self.y * self.scale_in_y

        '''Collision parameters'''
        self.collision_x1 = self.x
        self.collision_y1 = self.y

        self.dx_scaled = self.dx * self.scale_in_x
        self.dy_scaled = self.dx * self.scale_in_y

        self.collision_x1_scaled = self.x_scaled
        self.collision_y1_scaled = self.y_scaled


# MySprite Class
class MySprite(MyObject):

    # ''' The initializer of class '''
    def __init__(self, image_path):
        super().__init__()

        # Load image object
        self.image_obj_original = pygame.image.load(image_path)
        self.image_obj = pygame.image.load(image_path)
        self.image_rect = self.image_obj.get_rect()
        # print(self.image_rect)

        ''' Image parameters '''
        self.width = self.image_rect[2]
        self.height = self.image_rect[3]
        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Set all image values
        self.collision_width = self.width
        self.collision_height = self.height

        self.collision_center_x = self.collision_x1 + 0.5 * self.collision_width
        self.collision_center_y = self.collision_y1 + 0.5 * self.collision_height

        # '''Scaled quantities'''
        self.width_scaled = self.width * self.scale_in_x
        self.height_scaled = self.height * self.scale_in_y

        self.collision_width_scaled = self.width_scaled
        self.collision_height_scaled = self.height_scaled

        self.collision_center_x_scaled = self.collision_x1_scaled + 0.5 * self.collision_width_scaled
        self.collision_center_y_scaled = self.collision_y1_scaled + 0.5 * self.collision_height_scaled
        self.collision_rect_scaled = pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,
                                                 self.collision_width_scaled, self.collision_height_scaled)

    # Setter functions
    def set_collision_x(self, collision_x1):
        self.collision_x1 = collision_x1
        self.collision_x1_scaled = collision_x1 * self.scale_in_x

    def set_collision_y(self, collision_y1):
        self.collision_y1 = collision_y1
        self.collision_y1_scaled = collision_y1 * self.scale_in_y

    def set_collision_width(self, collision_width):
        self.collision_width = collision_width
        self.collision_width_scaled = collision_width * self.scale_in_x

    def set_collision_height(self, collision_height):
        self.collision_height = collision_height
        self.collision_height_scaled = collision_height * self.scale_in_y

    def collision_with(self, sprite):

        collision_rect = pygame.Rect(self.collision_x1, self.collision_y1,
                                     self.collision_width, self.collision_height)

        if collision_rect.colliderect(sprite.collision_rect):
            print("Collision detected")
        else:
            print("No collision detected")
        return self.collision_rect.colliderect(sprite.image_rect)

    def scale_values(self, scale_w, scale_h):

        self.scale_in_x = scale_w
        self.scale_in_y = scale_h
        self.x_scaled = int(self.scale_in_x * self.x)
        self.y_scaled = int(self.scale_in_y * self.y)
        self.width_scaled = int(self.scale_in_x * self.width)
        self.height_scaled = int(self.scale_in_y * self.height)
        self.image_rect = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)
        self.image_obj = pygame.transform.scale(self.image_obj_original, (self.width_scaled, self.height_scaled))

        # '''Collision parameters'''
        self.collision_x1_scaled = int(self.scale_in_x * self.collision_x1)
        self.collision_y1_scaled = int(self.scale_in_y * self.collision_y1)
        self.collision_width_scaled = int(self.scale_in_x * self.collision_width)
        self.collision_height_scaled = int(self.scale_in_y * self.collision_height)
        self.collision_rect_scaled = pygame.Rect(self.collision_x1_scaled, self.collision_y1_scaled,
                                                 self.collision_width_scaled, self.collision_height_scaled)

    def set_x(self, val_x):
        self.x = val_x
        self.x_scaled = val_x * self.scale_in_x

    def set_y(self, val_y):

        self.y = val_y
        self.y_scaled = val_y * self.scale_in_y

    # Getter functions
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_obj(self):
        return self.image_obj

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
