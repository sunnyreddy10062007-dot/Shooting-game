import pygame
import random
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 255))
        pygame.draw.polygon(self.image, (0, 128, 255), [(0, 40), (25, 0), (50, 40)])
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(midbottom=(x, y))

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(midtop=(random.randint(40, SCREEN_WIDTH - 40), -40))

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.midtop = (random.randint(40, SCREEN_WIDTH - 40), -40)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()

    player = Player()
    player_group = pygame.sprite.Group(player)
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group(Enemy() for _ in range(6))

    score = 0
    font = pygame.font.SysFont(None, 36)
    shooting = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                shooting = True
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                shooting = False

        keys = pygame.key.get_pressed()
        player_group.update(keys)

        if shooting and len(bullets) < 5:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(bullet)
            shooting = False

        bullets.update()
        enemies.update()

        collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for _ in collisions:
            score += 10
            enemies.add(Enemy())

        screen.fill((10, 10, 30))
        player_group.draw(screen)
        bullets.draw(screen)
        enemies.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
