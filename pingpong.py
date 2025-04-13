class GameSprite(sprite.Sprite): #Основной класс спрайта
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y