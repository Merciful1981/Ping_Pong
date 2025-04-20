class GameSprite(sprite.Sprite): #Основной класс спрайта
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

speed_x = 3
speed_y = 3

while game:
    if finish != True
    ball.rect.x += speed_x
    ball.rect.y += speed_y

if ball.rect.y > win_height-50
    or ball.rect.y < 0:
        speed_y *= -1



font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0))

while game:
    if ball.rect.x < 0:
        finish = True
        window.blit(losel, (200, 200))
