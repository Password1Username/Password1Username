# Tile map dimensions
n_width = 16
n_height = 16

tile_width = 32
tile_width_scaled = 32
tile_height = 32
tile_height_scaled = 32

# Set up the window
small_win_x = tile_width * n_width
win_x = small_win_x
small_win_y = tile_height * n_height
win_y = small_win_y

scale_w = 1.0
scale_h = 1.0

sprite_x = 0
sprite_y = 0
sprite_width = 64
sprite_height = 40

sheet_width = 6 * 64
sheet_height = 2 * 40

ratex = 0.01
ratey = 0.01

dx = win_x * ratex
dy = win_y * ratey