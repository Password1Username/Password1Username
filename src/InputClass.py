import pygame


# Smooth control inputs: https://stackoverflow.com/questions/15652459/pygame-arrow-control1
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
