from pygame import *
from time import sleep


class GameSprite(sprite.Sprite):
    def __init__(self, picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Enemy(GameSprite):
    def __init__(self, picture,w,h,x,y, xspeed,yspeed): 
        super().__init__(picture,w,h,x,y) 
        self.xspeed = xspeed
        self.yspeed = yspeed




class Player(GameSprite):
    def __init__(self, picture,w,h,x,y, xspeed,yspeed): 
        super().__init__(picture,w,h,x,y)
        self.xspeed = xspeed
        self.yspeed = yspeed
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        self.xspeed = 0
        self.yspeed = 0

class TEXT():
    def __init__(self, text,fsize,color,x,y):
        self.text
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def create_money():
    moneys = []
    sirnik1 = GameSprite('COIN.png',60,60,690,495)
    moneys.append(sirnik1)from pygame import *
from time import sleep


class GameSprite(sprite.Sprite):
    def __init__(self, picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Enemy(GameSprite):
    def __init__(self, picture,w,h,x,y, xspeed,yspeed): 
        super().__init__(picture,w,h,x,y) 
        self.xspeed = xspeed
        self.yspeed = yspeed




class Player(GameSprite):
    def __init__(self, picture,w,h,x,y, xspeed,yspeed): 
        super().__init__(picture,w,h,x,y)
        self.xspeed = xspeed
        self.yspeed = yspeed
    def update(self):
        self.rect.x += self.xspeed
        platforms_touched = sprite.spritecollide(self,walls,False)
        if self.xspeed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.xspeed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.xspeed = 0
        self.rect.y += self.yspeed
        platforms_touched = sprite.spritecollide(self,walls,False)
        if self.yspeed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.yspeed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        self.yspeed = 0

class TEXT():
    def __init__(self, text,fsize,color,x,y):
        self.text
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def create_money():
    moneys = []
    sirnik1 = GameSprite('COIN.png',60,60,690,495)
    moneys.append(sirnik1)
    sirnik2 = GameSprite('COIN.png',60,60,1595,500)
    moneys.append(sirnik2)
    sirnik3 = GameSprite('COIN.png',60,60,1840,40)
    moneys.append(sirnik3)
    sirnik4 = GameSprite('COIN.png',60,60,495,295)
    moneys.append(sirnik4)
    sirnik5 = GameSprite('COIN.png',60,60,1190,300)
    moneys.append(sirnik5)
    return moneys

walls = sprite.Group()

walls.add(GameSprite('wall_xxxx.jpg',50,200,200,200))
walls.add(GameSprite('wall_yyyy.jpg',300,50,400,200))
walls.add(GameSprite('wall_xxxx.jpg',50,424,200,600))
walls.add(GameSprite('wall_xxxx.jpg',50,424,400,400))
walls.add(GameSprite('wall_xxxx.jpg',50,250,850,0))
walls.add(GameSprite('wall_xxxx.jpg',50,300,1100,150))
walls.add(GameSprite('wall_yyyy.jpg',250,50,400,824))
walls.add(GameSprite('wall_xxxx.jpg',50,250,600,400))
walls.add(GameSprite('wall_yyyy.jpg',300,50,650,400))
walls.add(GameSprite('wall_yyyy.jpg',150,50,650,600))
walls.add(GameSprite('wall_xxxx.jpg',50,274,800,600))
walls.add(GameSprite('wall_xxxx.jpg',50,250,950,400))
walls.add(GameSprite('wall_xxxx.jpg',50,450,1300,0))
walls.add(GameSprite('wall_yyyy.jpg',200,50,950,600))
walls.add(GameSprite('wall_xxxx.jpg',50,274,1100,600))
walls.add(GameSprite('wall_yyyy.jpg',200,50,800,824))
walls.add(GameSprite('wall_xxxx.jpg',50,424,1300,650))
walls.add(GameSprite('wall_yyyy.jpg',450,50,1300,650))
walls.add(GameSprite('wall_xxxx.jpg',50,350,1700,350))
walls.add(GameSprite('wall_yyyy.jpg',225,50,1475,350))
walls.add(GameSprite('wall_yyyy.jpg',625,50,1475,150))
walls.add(GameSprite('wall_xxxx.jpg',50,224,1500,850)) 
walls.add(GameSprite('wall_yyyy.jpg',150,50,1650,850)) 
walls.add(GameSprite('wall_xxxx.jpg',85,50,1475,505))

end = GameSprite('Portal.png',100,100,1370,920)

tochki = []

tochka11 = GameSprite('tochka.png',1,1,275,300)
tochki.append(tochka11)
tochka12 = GameSprite('tochka.png',1,1,1075,300)
tochki.append(tochka12)
tochka21 = GameSprite('tochka.png',1,1,275,925)
tochki.append(tochka21)
tochka22 = GameSprite('tochka.png',1,1,1265,925)
tochki.append(tochka22)
tochka31 = GameSprite('tochka.png',1,1,1195,20)
tochki.append(tochka31)
tochka32 = GameSprite('tochka.png',1,1,1195,965)
tochki.append(tochka32)
tochka41 = GameSprite('tochka.png',1,1,1385,615)
tochki.append(tochka41)
tochka42 = GameSprite('tochka.png',1,1,1385,20)
tochki.append(tochka42)
tochka51 = GameSprite('tochka.png',1,1,1385,750)
tochki.append(tochka51)
tochka52 = GameSprite('tochka.png',1,1,1840,750)
tochki.append(tochka52)



player = Player('monkey3.png',75,75,15,900,12,8)

bobrs = []

bobr1 = Enemy('BOBR1.png',75,75,500,285,-10,0)
bobr2 = Enemy('BOBR1.png',75,75,300,915,-10,0)
bobr3 = Enemy('BOBR1.png',75,75,1180,890,0,8)
bobr4 = Enemy('BOBR1.png',75,75,1370,50,0,8)
bobr5 = Enemy('BOBR1.png',75,75,1385,735,-10,0)

bobrs.append(bobr1)
bobrs.append(bobr2)
bobrs.append(bobr3)
bobrs.append(bobr4)
bobrs.append(bobr5)


window = display.set_mode((1920, 1024),FULLSCREEN)
display.set_caption("Monkey's Adventures")
t609 = transform.scale(image.load('T609.jpg'),(1920,1024))
start = transform.scale(image.load('START.png'),(1920,1024))
picture = transform.scale(image.load('kos.jpg'),(1920, 1024))
won = transform.scale(image.load('WON.png'),(1920, 1024))
lose = transform.scale(image.load('lose.png'),(1920,1024))

#window.blit(t609,(0,0))
#display.update()
#sleep(2)
#window.blit(start,(0,0))
#display.update()
#sleep(2)

tm = 0
moneysmake = create_money()

run = True
clock = time.Clock()

    
while run:        
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT or keys_pressed[K_ESCAPE]:
            run = False
    
    window.blit(picture, (0,0))


    walls.draw(window)

    
    
    
    end.reset()

    player.reset()
    
    if len(moneys) != 0:
        for i in (moneys):
            i.reset()
        for i in (moneys):
            if sprite.collide_rect(player, i):
                moneys.remove(i)
    
    
    if len(bobrs) != 0:
        for i in bobrs:
            i.reset()
        for i in bobrs:
            
            if sprite.collide_rect(i,tochki[tm]):
                i.xspeed *= -1.
                i.yspeed *= -1.
            tm += 1
            if sprite.collide_rect(i,tochki[tm]):
                i.xspeed *= -1.
                i.yspeed *= -1.
            tm += 1
            if tm == 10:
                tm = 0
        for i in bobrs:
            i.rect.x += i.xspeed
            i.rect.y += i.yspeed

        for i in bobrs:
            if sprite.collide_rect(i,player):
                window.blit(lose, (0,0))
                display.update()
                player.rect.x = 15
                player.rect.y = 900
                sleep(1)
                window.blit(picture, (0,0))
        

     
    



   
    
    

    
    
    if keys_pressed[K_a] and player.rect.x > 5: 
        player.xspeed = -10
        player.yspeed = 0
    if keys_pressed[K_d] and player.rect.x < 1840:
        player.xspeed = 10
        player.yspeed = 0
    if keys_pressed[K_w] and player.rect.y > 5:
        player.xspeed = 0
        player.yspeed = -8    
    if keys_pressed[K_s] and player.rect.y < 945:
        player.xspeed = 0
        player.yspeed = 8
    
    if keys_pressed[K_a] and keys_pressed[K_w] and player.rect.x > 5 and player.rect.y > 5:
        player.xspeed = -10
        player.yspeed = -8
    if keys_pressed[K_a] and keys_pressed[K_s] and player.rect.y < 945 and player.rect.x > 5:
        player.xspeed = -10
        player.yspeed = 8
    if keys_pressed[K_d] and keys_pressed[K_w] and player.rect.x < 1840 and player.rect.y > 5:
        player.xspeed = 10
        player.yspeed = -8
    if keys_pressed[K_d] and  keys_pressed[K_s] and player.rect.x < 1840 and player.rect.y < 945:
        player.xspeed = 10
        player.yspeed = 8


    if sprite.collide_rect(end,player):
        window.blit(won, (0,0))
        display.update()
        sleep(3)
        run = False
        
        




    player.update()

    clock.tick(100)
    display.update()
    sirnik2 = GameSprite('COIN.png',60,60,1595,500)
    moneys.append(sirnik2)
    sirnik3 = GameSprite('COIN.png',60,60,1840,40)
    moneys.append(sirnik3)
    sirnik4 = GameSprite('COIN.png',60,60,495,295)
    moneys.append(sirnik4)
    sirnik5 = GameSprite('COIN.png',60,60,1190,300)
    moneys.append(sirnik5)
    return moneys

walls = sprite.Group()

walls.add(GameSprite('wall_xxxx.jpg',50,200,200,200))
walls.add(GameSprite('wall_yyyy.jpg',300,50,400,200))
walls.add(GameSprite('wall_xxxx.jpg',50,424,200,600))
walls.add(GameSprite('wall_xxxx.jpg',50,424,400,400))
walls.add(GameSprite('wall_xxxx.jpg',50,250,850,0))
walls.add(GameSprite('wall_xxxx.jpg',50,300,1100,150))
walls.add(GameSprite('wall_yyyy.jpg',250,50,400,824))
walls.add(GameSprite('wall_xxxx.jpg',50,250,600,400))
walls.add(GameSprite('wall_yyyy.jpg',300,50,650,400))
walls.add(GameSprite('wall_yyyy.jpg',150,50,650,600))
walls.add(GameSprite('wall_xxxx.jpg',50,274,800,600))
walls.add(GameSprite('wall_xxxx.jpg',50,250,950,400))
walls.add(GameSprite('wall_xxxx.jpg',50,450,1300,0))
walls.add(GameSprite('wall_yyyy.jpg',200,50,950,600))
walls.add(GameSprite('wall_xxxx.jpg',50,274,1100,600))
walls.add(GameSprite('wall_yyyy.jpg',200,50,800,824))
walls.add(GameSprite('wall_xxxx.jpg',50,424,1300,650))
walls.add(GameSprite('wall_yyyy.jpg',450,50,1300,650))
walls.add(GameSprite('wall_xxxx.jpg',50,350,1700,350))
walls.add(GameSprite('wall_yyyy.jpg',225,50,1475,350))
walls.add(GameSprite('wall_yyyy.jpg',625,50,1475,150))
walls.add(GameSprite('wall_xxxx.jpg',50,224,1500,850)) 
walls.add(GameSprite('wall_yyyy.jpg',150,50,1650,850)) 
walls.add(GameSprite('wall_xxxx.jpg',85,50,1475,505))

end = GameSprite('Portal.png',100,100,1370,920)

tochki = []

tochka11 = GameSprite('tochka.png',50,50,300,300)
tochki.append(tochka11)
tochka12 = GameSprite('tochka.png',50,50,1025,300)
tochki.append(tochka12)
tochka21 = GameSprite('tochka.png',50,50,300,925)
tochki.append(tochka21)
tochka22 = GameSprite('tochka.png',50,50,1195,925)
tochki.append(tochka22)
tochka31 = GameSprite('tochka.png',50,50,1195,50)
tochki.append(tochka31)
tochka32 = GameSprite('tochka.png',50,50,1195,925)
tochki.append(tochka32)
tochka41 = GameSprite('tochka.png',50,50,1385,575)
tochki.append(tochka41)
tochka42 = GameSprite('tochka.png',50,50,1385,50)
tochki.append(tochka42)
tochka51 = GameSprite('tochka.png',50,50,1385,750)
tochki.append(tochka51)
tochka52 = GameSprite('tochka.png',50,50,1840,750)
tochki.append(tochka52)



player = Player('monkey3.png',75,75,15,900,12,8)

bobrs = []

bobr1 = Enemy('BOBR1.png',75,75,300,285,-0.5,0)
bobr2 = Enemy('BOBR1.png',75,75,300,915,-0.5,0)
bobr3 = Enemy('BOBR1.png',75,75,1180,925,0,0.267)
bobr4 = Enemy('BOBR1.png',75,75,1370,50,0,0.267)
bobr5 = Enemy('BOBR1.png',75,75,1385,735,-0.5,0)

bobrs.append(bobr1)
bobrs.append(bobr2)
bobrs.append(bobr3)
bobrs.append(bobr4)
bobrs.append(bobr5)


window = display.set_mode((1920, 1024),FULLSCREEN)
display.set_caption("Monkey's Adventures")
t609 = transform.scale(image.load('T609.jpg'),(1920,1024))
start = transform.scale(image.load('START.png'),(1920,1024))
picture = transform.scale(image.load('kos.jpg'),(1920, 1024))
won = transform.scale(image.load('WON.png'),(1920, 1024))
lose = transform.scale(image.load('lose.png'),(1920,1024))

#window.blit(t609,(0,0))
#display.update()
#sleep(2)
#window.blit(start,(0,0))
#display.update()
#sleep(2)
gl = 0
tm = 0
moneys = create_money()

run = True
clock = time.Clock()

    
while run:        
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT or keys_pressed[K_ESCAPE]:
            run = False
    
    window.blit(picture, (0,0))


    walls.draw(window)

    for i in tochki:
        i.reset()
    
    
    end.reset()

    player.reset()
    
    if len(moneys) != 0:
        for i in (moneys):
            i.reset()
        for i in (moneys):
            if sprite.collide_rect(player, i):
                moneys.remove(i)
    
    
    if len(bobrs) != 0:
        for i in bobrs:
            i.reset()
        for i in range(len(bobrs)):
            
            if sprite.collide_rect(bobrs[i],tochki[tm]):
                bobrs[i].xspeed *= -1.
                bobrs[i].yspeed *= -1.
            tm += 1
            if sprite.collide_rect(bobrs[i],tochki[tm]):
                bobrs[i].xspeed *= -1.
                bobrs[i].yspeed *= -1.
            tm += 1
            if tm == 10:
                tm = 0
        for i in bobrs:
            i.rect.x += i.xspeed
            i.rect.y += i.yspeed

        for i in bobrs:
            if sprite.collide_rect(i,player):
                window.blit(lose, (0,0))
                display.update()
                player.rect.x = 15
                player.rect.y = 900
                sleep(1)
                window.blit(picture, (0,0))
        

     
    # if len(bobrs2) != 0:
    #     for i in bobrs2:
    #         i.reset()
    #     for i in bobrs2:
    #         if sprite.collide_rect(i,tochka21):
    #             mbspeed2 += 1
    #         elif sprite.collide_rect(i,tochka22):
    #             mbspeed2 -= 1
        
    #     for i in bobrs2:
    #         if sprite.collide_rect(i,player):
    #             window.blit(lose, (0,0))
    #             display.update()
    #             player.rect.x = 15
    #             player.rect.y = 900
    #             sleep(1)
    #             window.blit(picture, (0,0))
    #     i.rect.x += mbspeed2
    
    # if len(bobrs3) != 0:
    #     for i in bobrs3:
    #         i.reset()
    #     for i in bobrs3:
    #         if sprite.collide_rect(i,tochka22):
    #             pbspeed3 -= 0.8
    #         elif sprite.collide_rect(i,tochka31):
    #             pbspeed3 += 0.8
        
    #     for i in bobrs3:
    #         if sprite.collide_rect(i,player):
    #             window.blit(lose, (0,0))
    #             display.update()
    #             player.rect.x = 15
    #             player.rect.y = 900
    #             sleep(1)
    #             window.blit(picture, (0,0))
    #     i.rect.y += pbspeed3 

    # if len(bobrs4) != 0:
    #     for i in bobrs4:
    #         i.reset()
    #     for i in bobrs4:
    #         if sprite.collide_rect(i,tochka41):
    #             pbspeed4 -= 0.8
    #         elif sprite.collide_rect(i,tochka42):
    #             pbspeed4 += 0.8        
    #     for i in bobrs4:
    #         if sprite.collide_rect(i,player):
    #             window.blit(lose, (0,0))
    #             display.update()
    #             player.rect.x = 15
    #             player.rect.y = 900
    #             sleep(1)
    #             window.blit(picture, (0,0))
    #     i.rect.y += pbspeed4        
              

    # if len(bobrs5) != 0:
    #     for i in bobrs5:
    #         i.reset()
    #     for i in bobrs5:
    #         if sprite.collide_rect(i,tochka51):
    #             mbspeed5 += 1 
    #         elif sprite.collide_rect(i,tochka52):
    #             mbspeed5 -= 1
    #     for i in bobrs5:
    #         if sprite.collide_rect(i,player):
    #             window.blit(lose, (0,0))
    #             display.update()
    #             player.rect.x = 15
    #             player.rect.y = 900
    #             sleep(1)
    #             window.blit(picture, (0,0))
    #     i.rect.x += mbspeed5          



   
    
    

    
    
    if keys_pressed[K_a] and player.rect.x > 5: 
        player.xspeed = -10
        player.yspeed = 0
    if keys_pressed[K_d] and player.rect.x < 1840:
        player.xspeed = 10
        player.yspeed = 0
    if keys_pressed[K_w] and player.rect.y > 5:
        player.xspeed = 0
        player.yspeed = -8    
    if keys_pressed[K_s] and player.rect.y < 945:
        player.xspeed = 0
        player.yspeed = 8
    
    if keys_pressed[K_a] and keys_pressed[K_w] and player.rect.x > 5 and player.rect.y > 5:
        player.xspeed = -10
        player.yspeed = -8
    if keys_pressed[K_a] and keys_pressed[K_s] and player.rect.y < 945 and player.rect.x > 5:
        player.xspeed = -10
        player.yspeed = 8
    if keys_pressed[K_d] and keys_pressed[K_w] and player.rect.x < 1840 and player.rect.y > 5:
        player.xspeed = 10
        player.yspeed = -8
    if keys_pressed[K_d] and  keys_pressed[K_s] and player.rect.x < 1840 and player.rect.y < 945:
        player.xspeed = 10
        player.yspeed = 8


    if sprite.collide_rect(end,player):
        window.blit(won, (0,0))
        display.update()
        sleep(3)
        run = False
        
        




    player.update()

    clock.tick(100)
    display.update()
