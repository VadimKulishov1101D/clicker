import pygame
pygame.init()

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Clicker game')

mob_image = pygame.image.load('mob.png')
mob_image = pygame.transform.scale(mob_image, (200,200))

white = (255,255,255)
black = (0,0,0)

class Mob:
    def __init__(self):
        self.hp = 10
        self.rect = mob_image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()
    def kill(self):
        self.hp = 10
        game.coins += 1

class GameClicker:
    def __init__(self):
        self.coins = 0
        self.mobs = [Mob()]
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click()
            
            screen.fill(white)
            for mob in self.mobs:
                screen.blit(mob_image, mob.rect)
            self.draw_text(f'Coins: {self.coins}', 10,10)

            pygame.display.update()
    def handle_click(self):
        for mob in self.mobs:
            if mob.rect.collidepoint(pygame.mouse.get_pos()):
                mob.hit()
    def draw_text(self, text, x ,y):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, black)
        screen.blit(text_surface, (x,y))

game = GameClicker()
game.run()