import pygame

class Player:
    def __init__(self, x,y, size, img):
        self.x =x 
        self.y =y 
        self.size = size
        self.img = img

    def _draw_(self, sc, H):
        sc.blit(self.img, (self.x,self.y ))

    def _move_right_(self):
            self.x += 5
    def _move_left_(self):
            self.x -= 5
    def _move_up_(self):
            self.y-=1
    def _move_down_(self):
            self.y+=1
    def _rotate_(self):
        self.img = pygame.transform.rotate(self.img, 2)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                self._move_left_()
        if keys[pygame.K_RIGHT]:
                self._move_right_()
