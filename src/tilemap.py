import SpriteClass

grass = 0
dirt = 1
water = 3
hedge = 4
stone = 5
block = 6
grass_block = 7

#  '''Initialization of sprite objects'''
grass_obj = SpriteClass.MySprite('./pics/terrain/grass-map-periodic.png')
grass_block_obj = grass_obj
dirt_obj = SpriteClass.MySprite('./pics/terrain/dirt-map.png')
water_obj = SpriteClass.MySprite('./pics/terrain/water-map.png')
stone_obj = SpriteClass.MySprite('./pics/boundaries/stone-map.png')
hedge_obj = SpriteClass.MySprite('./pics/boundaries/hedge-map-green.png')
block_obj = SpriteClass.MySprite('./pics/boundaries/block-map.png')

textures = {
    grass: grass_obj,
    grass_block: grass_block_obj,
    dirt: dirt_obj,
    stone: stone_obj,
    water: water_obj,
    hedge: hedge_obj,
    block: block_obj
}

block_textures = {
    stone: stone_obj,
    # water: water_obj,
    grass_block: grass_block_obj,
    hedge: hedge_obj,
    block: block_obj}

materials = {"grass": 0, "dirt": 1, "water": 3, "hedge": 4, "stone": 5, "block": 6,
             "grass block": 7}


def tile_map_one():
    tile_map = [
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["block"], materials["dirt"], materials["block"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["hedge"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["hedge"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["hedge"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["hedge"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["dirt"], materials["hedge"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"], materials["hedge"], materials["dirt"], materials["grass"], materials["grass"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["stone"], materials["water"], materials["water"], materials["water"], materials["stone"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["stone"], materials["water"], materials["water"], materials["water"], materials["stone"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["hedge"], materials["water"], materials["water"], materials["water"], materials["hedge"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]],
        [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["hedge"], materials["hedge"], materials["hedge"], materials["hedge"], materials["hedge"],
         materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
         materials["grass"]]]
    return tile_map


class TileMap:

    def __init__(self):
        self.n_width = 16
        self.n_height = 16

        self.width = 32
        self.width_scaled = 32
        self.height = 32
        self.height_scaled = 32

        self.current = tile_map_one()
