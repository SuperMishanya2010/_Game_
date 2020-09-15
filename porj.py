import pygame
import random
import time
import sqlite3


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


from Enemys import Enemy
from player import Player
from os import path
pygame.init()
W = 1250 # width - ширина
H = 700 # height - высота

x = W // 2
y = H // 2


fps = pygame.time.Clock()



music = pygame.mixer.music.load('C:/Users/morom/Desktop/гама/bang/zigota.mp3')
pygame.mixer.music.play(-1, 0.0)



sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Игра")
img = pygame.image.load(r'C:\Users\morom\Desktop\гама\bang\dan.jpg')
img1 = pygame.image.load(r'C:\Users\morom\Desktop\гама\bang\krol.png')
img2= pygame.image.load(r'C:\Users\morom\Desktop\гама\bang\dedd.jpg')
img3= pygame.image.load(r'C:\Users\morom\Desktop\гама\bang\game_over.png')

#img4= pygame.image.load(r'C:\Users\morom\Downloads\zalivka.')
connect = sqlite3.connect('enemys.db')
cursor = connect.cursor()
#cursor.execute('CREATE TABLE enemys(size INT,rev INT)')
cursor.execute('INSERT INTO enemys VALUES(85,0)')
cursor.execute('INSERT INTO enemys VALUES(85,1)')
cursor.execute('''SELECT * FROM enemys''')
data_from_db = cursor.fetchall()
#print(*data_from_db, sep='\n')
#print(data_from_db[0][0])


Black_E=Enemy(W, img , 20, data_from_db[0][0], data_from_db[0][1])
Red_E=Enemy(W,img1,10,data_from_db[1][0],data_from_db[1][1])
Pl=Player(500,H-100,95,img2)
print(H-Red_E.size)


def hit(Enemy,Player):
    if Player.y+Player.size>H-Enemy.size and Player.x+Player.size>Enemy.x and Player.x<Enemy.x+Enemy.size:
        sc.blit(img3,(W/2-435,100 ))
        music = pygame.mixer.music.load('C:/Users/morom/Desktop/гама/bang/orrr.mp3')
        pygame.mixer.music.play(-1, 0.0)
        r=pygame.time.get_ticks()
        font = pygame.font.Font(None, 50)
        strin="Ваш счет: " + str(r/1000)+ ' секунды'
        text = font.render(strin,True,[0,0,0])
        sc.blit(text, [450,H-85])
        pygame.display.update()
        time.sleep(4)
        exit()


def draw():
    sc.fill((255, 255, 255))
    Black_E.draw(sc,H)
    Red_E.draw(sc,H)
    Pl._draw_(sc,H)
    pygame.display.update()


nn=0
mm=0
j=0
pygame.init()

jump = pygame.mixer.Sound('C:/Users/morom/Downloads/jump.wav')


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    nn+=1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if j!=-1:
            jump.play()
            j=1
    if j==1:
        Pl.y-=(Pl.y-440)//10
    if Pl.y<=H-250:
        j=-1
    if j==-1:
        Pl.y+=(Pl.y-440)//10
    if Pl.y>=H-Pl.size:
        j=0

    Pl.move()
    draw()
    Red_E.move(W)
    if nn>1000:
        Black_E.move(W)
    hit(Black_E,Pl)
    hit(Red_E,Pl)

   
    fps.tick(120)

