import AnimationClass
from surface_configuration import win_x
from surface_configuration import win_y
from surface_configuration import sprite_x
from surface_configuration import sprite_y
from surface_configuration import sprite_width
from surface_configuration import sprite_height
from surface_configuration import dx
from surface_configuration import dy


x_pos = 0.5 * win_x
y_pos = 0.5 * win_y
x_pos_scaled = x_pos
y_pos_scaled = y_pos

rects_up = [(sprite_x + 3 * sprite_width, sprite_y, sprite_width, sprite_height),
            (sprite_x + 4 * sprite_width, sprite_y, sprite_width, sprite_height),
            (sprite_x + 5 * sprite_width, sprite_y, sprite_width, sprite_height)]

rects_down = [(sprite_x, sprite_y, sprite_width, sprite_height),
              (sprite_x + sprite_width, sprite_y, sprite_width, sprite_height),
              (sprite_x + 2 * sprite_width, sprite_y, sprite_width, sprite_height)]

rects_left = [(sprite_x, sprite_y + sprite_height, sprite_width, sprite_height),
              (sprite_x + sprite_width, sprite_y + sprite_height, sprite_width, sprite_height),
              (sprite_x + 2 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height)]

rects_right = [(sprite_x + 3 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height),
               (sprite_x + 4 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height),
               (sprite_x + 5 * sprite_width, sprite_y + sprite_height, sprite_width, sprite_height)]


player = AnimationClass.MyPlayer(x_pos=0.0, y_pos=0.0)
player.set_animation('./pics/blueboy_64_40.png', rects_down, "down")
player.set_animation('./pics/blueboy_64_40.png', rects_up, "up")
player.set_animation('./pics/blueboy_64_40.png', rects_left, "left")
player.set_animation('./pics/blueboy_64_40.png', rects_right, "right")
player.set_init_animation("down")

player_init_x = 0.0
player_init_y = 0.0

hit_box_length = 28

col_init_x1 = 18
col_init_y1 = 5

player.set_x(player_init_x)
player.set_y(player_init_y)

player.set_hit_box_x(col_init_x1)
player.set_hit_box_y(col_init_y1)
player.set_collision_width(hit_box_length)
player.set_collision_height(hit_box_length)

player.set_dx(dx)
player.set_dy(dy)
