class game_object(image):
    image_obj=pygame.image.load(image)
    image_rect=image_obj.get_rect()
    #init_list=[image,width,height,offx,offy]
    def __init__(self,image):
        self.image=image
        self.x=image_rect[0]
        self.y=image_rect[1]
        self.width=image_rect[2]
        self.height=image_rect[3]
        self.offx=0
        self.offy=0
        self.collision_x1=image_rect[0]
        self.collision_x2=image_rect[0]+self.width
        self.collision_y1=image_rect[1]
        self.collision_y2=image_rect[1]+self.height

    def read_image(self,image):
        image_obj=pygame.image.load(image)
        self.width=image_rect=image_rect[2]
        self.height=image_rect=image_rect[3]
        self.offx=0
        self.offy=0
        self.collision_x1=image_rect[0]
        self.collision_x2=image_rect[0]+self.width
        self.collision_y1=image_rect[1]
        self.collision_y2=image_rect[1]+self.height


