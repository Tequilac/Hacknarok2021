import pygame


class City(pygame.sprite.Sprite):
    def __init__(self, name, pops, image_file, law, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file), (70, 62))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self.name = name
        self.pops = pops
        self.x_cords, self.y_cords = location
        self.law = law
