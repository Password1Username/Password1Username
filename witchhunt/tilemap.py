materials = {"grass": 0, "dirt": 1, "water": 3, "hedge": 4, "stone": 5, "block": 6}

class Tilemap():

    def __init__(self):
        self.nwidth = 16
        self.nheight = 16

        self.width = 32
        self.width_scaled = 32
        self.height = 32
        self.height_scaled = 32

        self.current = self.tilemap_one()

    def tilemap_one(self):
        tilemap = [
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["block"], materials["dirt"], materials["block"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["hedge"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["hedge"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["hedge"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["hedge"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["dirt"], materials["hedge"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["hedge"], materials["dirt"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["stone"], materials["water"], materials["water"], materials["water"], materials["stone"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["stone"], materials["water"], materials["water"], materials["water"], materials["stone"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["hedge"], materials["water"], materials["water"], materials["water"], materials["hedge"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]],
            [materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["hedge"], materials["hedge"], materials["hedge"], materials["hedge"], materials["hedge"], materials["grass"], materials["grass"], materials["grass"], materials["grass"], materials["grass"],
             materials["grass"]]]
        return tilemap

