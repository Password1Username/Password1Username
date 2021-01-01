import pygame
import pyganim
import InputClass


def intersect_with(rect_a, rect_b):
    return rect_a.colliderect(rect_b)


class MyPlayer(InputClass.Inputs):

    def __init__(self, x_pos=0.0, y_pos=0.0):
        super().__init__()

        self.motion = False

        self.scale_in_x = 1.0
        self.scale_in_y = 1.0

        self.animations = {}
        self.animations_scaled = {}
        self.current_animation = None
        self.current_animation_scaled = None

        # Case: x_pos passed into constructor
        if x_pos:
            self.x = x_pos
            self.x_prev = x_pos
            self.x_scaled = self.x * self.scale_in_x
            self.x_prev_scaled = self.x_prev * self.scale_in_x
        # Case: x_pos not passed into constructor
        else:
            self.x = 0.0
            self.x_prev = 0.0

        self.x_scaled = self.x * self.scale_in_x
        self.x_prev_scaled = self.x_prev * self.scale_in_x

        # Case: y_pos passed into constructor
        if y_pos:
            self.y = y_pos
            self.y_prev = y_pos

        # Case: y_pos not passed into constructor
        else:
            self.y = 0.0
            self.y_prev = 0.0
        self.y_scaled = self.y * self.scale_in_y
        self.y_prev_scaled = self.y_prev * self.scale_in_y

        self.dx = 0.0
        self.dx_scaled = 0.0

        self.increment_x = 0.0
        self.increment_x_scaled = self.increment_x * self.scale_in_x

        self.increment_y = 0.0
        self.increment_y_scaled = self.increment_y * self.scale_in_y
        self.d_scale = 1.0
        self.dy = 0
        self.dy_scaled = 0

        self.width = 0.0
        self.height = 0.0

        self.width_scaled = self.width * self.scale_in_x
        self.height_scaled = self.height * self.scale_in_y

        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image_rect_scaled = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)

        '''Collision parameters'''
        self.collision_x1 = self.x
        self.collision_x1_prev = self.collision_x1

        self.collision_y1 = self.y
        self.collision_y1_prev = self.collision_y1

        self.collision_width = self.width
        self.collision_height = self.height

        self.x_offset = self.x - self.collision_x1
        self.y_offset = self.y - self.collision_y1

        self.collision_x1_scaled = self.x_scaled
        self.collision_x1_prev_scaled = self.collision_x1_scaled

        self.collision_y1_scaled = self.y_scaled
        self.collision_y1_prev_scaled = self.collision_x1_scaled

        self.collision_width_scaled = self.width_scaled
        self.collision_height_scaled = self.height_scaled

        self.collision_center_x_scaled = self.x_scaled + 0.5 * self.width_scaled
        self.collision_center_y_scaled = self.y_scaled + 0.5 * self.height_scaled

    """Getter functions"""
    def get_buffer(self):
        return self.buffer

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_x_prev(self):
        return self.x_prev

    def get_y_prev(self):
        return self.y_prev

    def get_scale_in_x(self):
        return self.scale_in_x

    def get_scale_in_y(self):
        return self.scale_in_y

    def get_width_scaled(self):
        return self.width_scaled

    def get_height_scaled(self):
        return self.height_scaled

    """Setter functions"""
    def set_x(self, val_x):
        self.x = val_x
        self.x_scaled = int(round(self.x * self.scale_in_x))

    def set_x_scaled(self, scale_w):
        self.x_scaled = int(round(scale_w * self.x))

    def set_x_prev(self, val_x):
        self.x_prev = val_x
        self.x_prev_scaled = self.x_prev * self.scale_in_x

    def set_y(self, val_y):
        self.y = val_y
        self.y_scaled = int(round(self.y * self.scale_in_y))

    def set_y_scaled(self, scale_h):
        self.y_scaled = int(round(scale_h * self.y))

    def set_y_prev(self, val_y):
        self.y_prev = val_y
        self.y_prev_scaled = self.y_prev * self.scale_in_y

    def set_scale_in_x(self, scale_w):
        self.scale_in_x = scale_w

    def set_scale_in_y(self, scale_h):
        self.scale_in_y = scale_h

    def set_scaled_width(self, scale_w):
        self.width_scaled = int(round(scale_w * self.width))

    def set_scaled_height(self, scale_h):
        self.height_scaled = int(round(scale_h * self.height))

    def set_collision_x(self, collision_x1):
        self.collision_x1 = collision_x1
        self.collision_x1_scaled = collision_x1 * self.scale_in_x

    def set_collision_x_prev(self, collision_x1):
        self.collision_x1_prev = collision_x1
        self.collision_x1_prev_scaled = collision_x1 * self.scale_in_x

    def set_collision_y(self, collision_y1):
        self.collision_y1 = collision_y1
        self.collision_y1_scaled = collision_y1 * self.scale_in_y

    def set_collision_y_prev(self, collision_y1):
        self.collision_y1_prev = collision_y1
        self.collision_y1_prev_scaled = collision_y1 * self.scale_in_y

    def set_hit_box_x(self, collision_x1):
        self.x_offset = self.x - collision_x1
        self.collision_x1 = collision_x1
        self.collision_x1_scaled = collision_x1 * self.scale_in_x

    def set_hit_box_y(self, collision_y1):
        self.y_offset = self.y - collision_y1
        self.collision_y1 = collision_y1
        self.collision_y1_scaled = collision_y1 * self.scale_in_y

    def set_dx(self, val_dx):
        self.dx = val_dx

    def set_dy(self, val_dy):
        self.dy = val_dy

    def set_increment_x(self, val_increment_x):
        self.increment_x = val_increment_x
        self.increment_x_scaled = val_increment_x * self.scale_in_x

    def set_increment_y(self, val_increment_y):
        self.increment_y = val_increment_y
        self.increment_y_scaled = val_increment_y * self.scale_in_y

    def set_collision_width(self, collision_width):
        self.collision_width = collision_width
        self.collision_width_scaled = collision_width * self.scale_in_x

    def set_collision_height(self, collision_height):
        self.collision_height = collision_height
        self.collision_height_scaled = collision_height * self.scale_in_y

    def scale_attributes(self, scale_w, scale_h):

        self.set_scale_in_x(scale_w)
        self.set_scale_in_y(scale_h)

        self.set_scaled_width(scale_w)
        self.set_scaled_height(scale_h)

        self.set_x(self.x)
        self.set_collision_x_prev(self.collision_x1_prev)

        self.set_y_scaled(self.y)
        self.set_collision_y_prev(self.collision_y1_prev)

        self.image_rect_scaled = pygame.Rect(self.x_scaled, self.y_scaled, self.width_scaled, self.height_scaled)

        # '''Collision parameters'''
        self.set_collision_x(self.collision_x1)
        self.set_collision_y(self.collision_y1)
        self.set_collision_width(self.collision_width)
        self.set_collision_height(self.collision_height)

        self.set_increment_x(self.increment_x)
        self.set_increment_y(self.increment_y)

    def set_init_animation(self, name):
        self.current_animation = self.animations[name]
        self.current_animation_scaled = self.animations_scaled[name]

    def set_animation(self, sprite_sheet, frames, name):

        self.x = frames[0][2]
        self.x_scaled = frames[0][2] * self.scale_in_x

        if self.width == 0:
            self.width = frames[0][2]
            self.collision_x1 = self.x
            self.collision_width = self.width

            self.width_scaled = frames[0][2]
            self.collision_x1_scaled = self.x * self.scale_in_x
            self.collision_width_scaled = self.width * self.scale_in_x

        if not self.y:
            self.y = frames[0][3]
            self.collision_y1 = self.y

            self.width_scaled = frames[0][2] * self.scale_in_y
            self.y_scaled = self.y * self.scale_in_y
            self.collision_y1_scaled = self.y_scaled

        if not self.height:
            self.height = frames[0][3]
            self.collision_height = self.height
            self.height_scaled = self.height * self.scale_in_y

        temp = pyganim.getImagesFromSpriteSheet(sprite_sheet, rects=frames)
        temp = list(zip(temp, [100] * len(temp)))
        self.animations[name] = pyganim.PygAnimation(temp)
        self.animations_scaled[name] = pyganim.PygAnimation(temp)

        if self.animations["down"]:
            self.current_animation = self.animations["down"]
            self.current_animation_scaled = self.animations_scaled["down"]
        else:
            self.current_animation = self.animations[name]
            self.current_animation_scaled = self.animations_scaled[name]

    def set_animation_scale(self, scale_w, scale_h):

        if self.width_scaled != 1.0 or self.height_scaled != 1.0:

            self.scale_attributes(scale_w, scale_h)

            for name in self.animations:
                # See http: // pygame.org / docs / ref / transform.html  # pygame.transform.scale
                self.animations_scaled[name].clearTransforms()
                self.animations_scaled[name].scale((self.width_scaled, self.height_scaled))

        else:

            self.scale_attributes(scale_w, scale_h)

            for name in self.animations:
                # See http: // pygame.org / docs / ref / transform.html  # pygame.transform.scale
                self.animations_scaled[name].scale((self.width_scaled, self.height_scaled))

    def collision_with(self, collision_object):
        """
        Collision algorithm pseudo-code discovered in the link below
        https://jonathanwhiting.com/tutorial/collision/
        """

        sprite_collision_rect = pygame.Rect(collision_object.collision_x1, collision_object.collision_y1,
                                            collision_object.collision_width, collision_object.collision_height)

        anim_collision_rect = pygame.Rect(self.collision_x1, self.collision_y1_prev, self.collision_width,
                                          self.collision_height)

        if intersect_with(anim_collision_rect, sprite_collision_rect) == 1:
            self.set_x(self.get_x_prev())
            self.set_collision_x(self.collision_x1_prev)

        anim_collision_rect = pygame.Rect(self.collision_x1, self.collision_y1, self.collision_width,
                                          self.collision_height)

        if intersect_with(anim_collision_rect, sprite_collision_rect) == 1:
            self.set_y(self.get_y_prev())
            self.set_collision_y(self.collision_y1_prev)

    def arrow_key_animation_motion(self, surface, events):
        # """ This method is used to map keyboard arrow inputs to the animations and their position """

        key_state = super().get_key_state(events)
        key_buffer_list = [buffer_element.input_name for buffer_element in super().get_buffer_list()]

        self.motion = False
        self.increment_x = 0
        self.increment_y = 0

        if key_state['right']:
            self.motion = True
            self.increment_x += self.dx
        if key_state['left']:
            self.motion = True
            self.increment_x -= self.dx
        if key_state['up']:
            self.motion = True
            self.increment_y -= self.dy
        if key_state['down']:
            self.motion = True
            self.increment_y += self.dy

        if self.motion:
            if self.increment_x != 0 and self.increment_y != 0:
                self.increment_x *= 0.7071
                self.increment_y *= 0.7071

            if key_buffer_list:
                self.current_animation_scaled = self.animations_scaled[key_buffer_list[-1]]
                self.current_animation_scaled.play()

        elif not self.motion:
            self.current_animation_scaled.pause()

        self.set_x_prev(self.get_x())
        self.set_collision_x_prev(round(self.get_x() - self.x_offset))
        self.set_x(round(self.get_x() + self.increment_x))

        self.set_y_prev(self.get_y())
        self.set_collision_y_prev(round(self.get_y() - self.y_offset))
        self.set_y(round(self.get_y() + self.increment_y))

        self.set_collision_x(round(self.get_x() - self.x_offset))
        self.set_collision_y(round(self.get_y() - self.y_offset))

        self.current_animation_scaled.blit(surface, (self.x_scaled, self.y_scaled))

    def play_animation(self, surface, name):

        self.current_animation_scaled = self.animations_scaled[name]

        self.current_animation_scaled.play()
        self.current_animation_scaled.blit(surface, (self.x_scaled, self.y_scaled))
