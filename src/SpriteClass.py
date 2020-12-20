import pygame
import pyganim

pygame.init()


# '''Smooth control inputs: https://stackoverflow.com/questions/15652459/pygame-arrow-control'''
class Input:
    def __init__(self):
        self.input_name = None
        self.time_since_input = 0.0


class InputBuffer:

    def __init__(self):
        self.buffer_max_length = 10
        self.buffer_list = []
        self.t_last_frame = 0
        self.t_current_frame = 0
        self.t_input_delay = 0.5
        self.time_elapsed = 0

    def update_time(self):
        self.t_last_frame = self.t_current_frame
        self.t_current_frame = pygame.time.get_ticks()
        self.time_elapsed = (self.t_current_frame - self.t_last_frame) / 1000.0
        for buffer_item in self.buffer_list:
            buffer_item.time_since_input += self.time_elapsed

    # This method removes old entries in input buffer
    def flush(self):

        if self.buffer_list:
            for idx in range(0, len(self.buffer_list)):
                if self.buffer_list[idx].time_since_input > self.t_input_delay:
                    self.buffer_list.pop(idx)
                if len(self.buffer_list) > self.buffer_max_length:
                    self.buffer_list.pop(idx)
                else:
                    return self.buffer_list
        return self.buffer_list

    def push(self, buffer_input):
        self.buffer_list.append(buffer_input)


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

        self.buffer = InputBuffer()

    def lookup_binding(self, key_entered):
        for binding, key_bound in self.bindings.items():
            if key_entered == key_bound:
                return binding

        return "not found"

    def get_input_state(self, events):

        self.buffer.update_time()
        for current_event in events:
            if current_event.type == pygame.KEYDOWN:
                binding = self.lookup_binding(current_event.key)

                if binding != "not found":
                    new_input = Input()
                    new_input.input_name = binding
                    new_input.time_since_input = 0
                    self.buffer.push(new_input)
                    self.inputState[binding] = True

            if current_event.type == pygame.KEYUP:
                binding = self.lookup_binding(current_event.key)
                if binding != "not found":
                    self.inputState[binding] = False
        self.buffer.flush()
        return self.inputState

    def get_key_state(self, events):

        self.buffer.update_time()
        for current_event in events:
            if current_event.type == pygame.KEYDOWN:
                binding = self.lookup_binding(current_event.key)
                if binding != "not found":
                    new_input = Input()
                    new_input.input_name = binding
                    new_input.time_since_input = 0
                    self.buffer.push(new_input)
                    self.keyState[binding] = True

            if current_event.type == pygame.KEYUP:
                binding = self.lookup_binding(current_event.key)
                if binding != "not found":
                    self.keyState[binding] = False
        self.buffer.flush()
        return self.keyState

    def get_buffer_list(self):
        return self.buffer.buffer_list


# '''Class storing parameters'''
class MyObject:
    # ''' The initializer of class '''
    def __init__(self, xpos=0.0, ypos=0.0):
        # '''Scaling factors'''
        self.scale_in_x = 1.0
        self.scale_in_y = 1.0

        # ''' Case: xpos passed in constructor '''
        self.x = xpos
        # '''Case: ypos passed in constructor'''
        self.y = ypos

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
        # ''' Load image object '''
        self.image_obj_original = pygame.image.load(image_path)
        self.image_obj = pygame.image.load(image_path)
        self.image_rect = self.image_obj.get_rect()

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


def intersect_with(rect_a, rect_b):
    return rect_a.colliderect(rect_b)


class MyPlayer(Inputs):

    def __init__(self, xpos=0.0, ypos=0.0):
        # super(Inputs, self).__init__()
        super().__init__()

        self.motion = False

        self.scale_in_x = 1.0
        self.scale_in_y = 1.0

        self.Animation = {}
        self.Animation_scaled = {}
        self.Anim_scaled = None
        self.Anim = None

        if xpos:
            self.x = xpos
            self.x_prev = xpos
            self.x_scaled = self.x * self.scale_in_x
            self.x_prev_scaled = self.x_prev * self.scale_in_x
            # '''Case: xpos not passed in constructor '''
        else:
            self.x = 0.0
            self.x_prev = 0.0
            self.x_scaled = self.x * self.scale_in_x
            self.x_prev_scaled = self.x_prev * self.scale_in_x

            # '''Case: ypos passed in constructor'''
        if ypos:
            self.y = ypos
            self.y_prev = ypos
            self.y_scaled = self.y * self.scale_in_y
            self.y_prev_scaled = self.y_prev * self.scale_in_y
            # '''Case: ypos not passed in constructor'''
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
        self.dscale = 1.0
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

    """Setter functions"""

    def set_x(self, valx):
        self.x = valx
        self.x_scaled = self.x * self.scale_in_x

    def set_x_prev(self, valx):
        self.x_prev = valx
        self.x_prev_scaled = self.x_prev * self.scale_in_x

    def set_y(self, valy):

        self.y = valy
        self.y_scaled = self.y * self.scale_in_y

    def set_y_prev(self, valy):
        self.y_prev = valy
        self.y_prev_scaled = self.y_prev * self.scale_in_y

    def set_scale(self, scalew, scaleh):
        self.scale_in_x = scalew
        self.scale_in_y = scaleh

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

    def set_init_animation(self, name):
        self.Anim_scaled = self.Animation_scaled[name]

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
        self.Animation[name] = pyganim.PygAnimation(temp)
        self.Animation_scaled[name] = pyganim.PygAnimation(temp)

        if not self.Anim_scaled:
            if self.Animation_scaled["down"]:
                self.Anim = self.Animation_scaled["down"]
            else:
                self.Anim_scaled = self.Animation_scaled[name]

    def collision_with(self, collision_object):
        """
        Collision algorithm pseudo-code discovered in the link below
        https: // jonathanwhiting.com / tutorial / collision /
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
                self.Anim_scaled = self.Animation_scaled[key_buffer_list[-1]]
                self.Anim_scaled.play()

        elif not self.motion:
            self.Anim_scaled.pause()

        self.set_x_prev(self.get_x())
        self.set_collision_x_prev(round(self.get_x() - self.x_offset))
        self.set_x(round(self.get_x() + self.increment_x))

        self.set_y_prev(self.get_y())
        self.set_collision_y_prev(round(self.get_y() - self.y_offset))
        self.set_y(round(self.get_y() + self.increment_y))

        self.set_collision_x(round(self.get_x() - self.x_offset))
        self.set_collision_y(round(self.get_y() - self.y_offset))

        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))

    def play_animation(self, surface, name):

        self.Anim_scaled = self.Animation_scaled[name]
        self.Anim_scaled.play()
        self.Anim_scaled.blit(surface, (self.x_scaled, self.y_scaled))
