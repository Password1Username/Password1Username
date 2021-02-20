import AnimationClass
from surface_configuration import tile_width_scaled
from surface_configuration import tile_height_scaled
from surface_configuration import sprite_x
from surface_configuration import sprite_y
from surface_configuration import sprite_width
from surface_configuration import sprite_height


rects_down_danny = [(sprite_x, sprite_y, sprite_width, sprite_height),
                    (sprite_x + sprite_width, sprite_y, sprite_width, sprite_height),
                    (sprite_x + 2 * sprite_width, sprite_y, sprite_width, sprite_height),
                    (sprite_x + 3 * sprite_width, sprite_y, sprite_width, sprite_height)]

x_pos = tile_width_scaled
y_pos = 3 * tile_height_scaled
x_pos_scaled = x_pos
y_pos_scaled = y_pos

danny = AnimationClass.MyPlayer(x_pos=x_pos, y_pos=y_pos)

danny.set_animation('./pics/people/danny_64_40.png', rects_down_danny, "down")
danny.set_init_animation("down")
danny.set_x(tile_width_scaled)
danny.set_y(3 * tile_height_scaled)

danny_init_x = tile_width_scaled
danny_init_y = 3 * tile_height_scaled

hit_box_length = 28

col_init_x1 = x_pos + 18
col_init_y1 = y_pos + 5

danny.set_x(danny_init_x)
danny.set_y(danny_init_y)

danny.set_hit_box_x(col_init_x1)
danny.set_hit_box_y(col_init_y1)
danny.set_collision_width(hit_box_length)
danny.set_collision_height(hit_box_length)
