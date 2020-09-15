import pygame

class Enemy:
    def __init__(self, x,img, damage, size,rev):
        self.x =x 
        self.img=img
       # self.image = image
        self.damage = damage
        self.size = size
        self.rev = rev

    def draw(self, sc, H):
        sc.blit(self.img, (self.x,H-self.size ))

    def move(self,W):
            if self.rev==0:
                if self.x==0:
                    self.x=W
                self.x +=-1
            if self.rev==1 or self.rev==-1:
                if self.x==0:
                    self.rev=-1
                if self.x+self.size==W:
                    self.rev=1
                if self.rev==-1:
                    self.x+=1
                if self.rev==1:
                    self.x-=1

    def live(self):
        self._move_()
        self._draw_()
