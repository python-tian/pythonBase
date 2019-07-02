#完善向日葵的类
#把向日葵添加到地图上面去，按鼠标左键，添加向日葵
import pygame,sys,random
#设置主窗口的宽高
SCREEN_WEIGHT=800
SCREEN_HEIGHT=560
#创建一个地图类
class Map():
    image_list=['imgs/map1.png','imgs/map2.png']
    def __init__(self,x,y,image_index):
        self.position=(x,y)#给地图一个坐标的属性
        self.image=pygame.image.load(Map.image_list[image_index])#给地图一个图片的属性
        #给一个属性
        #是否可以种植
        self.can_grow=True
    #把地图调到主窗口中
    def displaymap(self):
        MainGame.window.blit(self.image,self.position)
#创建一个植物类（父类），不过他要继承游戏精灵
class Plant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.live=True
#创建一个向日葵类（子类）
class Sunflower(Plant):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load('imgs/sunflower.png')#调用模块的功能，返回一个新的表面
        self.rect=self.image.get_rect()#调用模块的方法，表面.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.price=500
        self.hp=100
        #给一个时间计时器
        self.time_count=0
    #向日葵开始生产那个阳光
    def grounce(self):
        self.time_count+=1
        if self.time_count==30:
            MainGame.money+=5
            self.time_count=0


    #把向日葵调窗口中去
    def display_sunflower(self):
        MainGame.window.blit(self.image,self.rect)
#创建一个豌豆射手类（子类）
class Peashooter(Plant):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load('imgs/peashooter.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.hp=100
        self.price=50
        self.bullet_count=0
    #设置射手的射击
    def peashot(self):
        #先判断是否可以攻击
        should_fire = False
        for z in MainGame.zombie_list:
            if self.rect.y==z.rect.y and z.rect.x<800:
                should_fire=True

        if self.live and should_fire:
            self.bullet_count+=1
            if self.bullet_count==40:
                bullet=Peabullet(self)
                MainGame.bullet_list.append(bullet)
                self.bullet_count=0

    #加载到主窗口中区
    def display_pea(self):
        MainGame.window.blit(self.image,self.rect)
#创建一个豌豆子弹类
class Peabullet(pygame.sprite.Sprite):
    def __init__(self,peashooter):
        super().__init__()
        self.live = True
        self.image=pygame.image.load('imgs/peabullet.png')
        self.rect=self.image.get_rect()
        self.rect.x=peashooter.rect.x+60
        self.rect.y=peashooter.rect.y+15

        self.damage=100
        self.speed=5
    def move(self):
        if self.rect.x<=SCREEN_WEIGHT:
            self.rect.x+=self.speed
        else:
            self.live=False
    #子弹碰撞僵尸
    def hit_zombie(self):
        for zombie1 in MainGame.zombie_list:
            if pygame.sprite.collide_rect(self,zombie1):
                self.live=False
                zombie1.hp-=self.damage
                if zombie1.hp<=0:
                    zombie1.live=False

    def display_bullet(self):
        MainGame.window.blit(self.image,self.rect)

#定义一个僵尸类
class Zombie(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.live=True
        self.image=pygame.image.load('imgs/zombie.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.damage=10
        self.hp=1000
        self.speed=1
        self.live = True
        self.stop=False
    def move_zombie(self):
        if self.live and self.stop==False:
            self.rect.x-=self.speed
            if self.rect.x<-600:
                MainGame().overgame()
    def hit_plant(self):
        for p in MainGame.plant_list:
            if pygame.sprite.collide_rect(self,p):
                self.stop=True
                p.hp-=self.damage
                if p.hp<=0:
                    p.live=False
                    self.stop=False
                    a=self.rect.x//80
                    b=self.rect.y//80-1
                    map=MainGame.map_list[b][a]
                    map.can_grow=True
    #将僵尸加载到窗口中区
    def display_zombie(self):
        MainGame.window.blit(self.image,self.rect)


#定义一个游戏主线类
class MainGame():
    #创建一个属性类主窗口，首次赋值给None
    window=None
    #设置一个列表存储所有的地图原坐标
    point_list=[]
    #设置一个金钱
    money=500
    #设置一个地图列表，储存所有的地图坐标
    map_list=[]
    #设置一个存储所有植物的列表
    plant_list=[]
    #设置一个储存子弹的列表
    bullet_list=[]
    #创建一个僵尸的列表
    zombie_list=[]
    #计时僵尸
    zombie_count=0
    #即总分数
    grace_count=0
    def __init__(self):
        pass
    #创建初始化主窗口
    def init_window(self):
        #先初始化主窗口
        pygame.display.init()
        #调用模块功能，并返回一个表面（Surface）
        MainGame.window=pygame.display.set_mode((SCREEN_WEIGHT,SCREEN_HEIGHT))
    #获取一个有文字的表面
    def get_Surface_with_concent(self,concent,size,font_name,color):
        #调用模块的文字初始化
        pygame.font.init()
        #创建一个文字,调用模块的功能回返回一个文字
        font=pygame.font.SysFont(font_name,size)
        #根据文字调用模块的功能来创建一个新的表面,模块功能回返回一个新的表面
        sf=font.render(concent,True,color)
        return sf
    def get_zombie_with_concent(self,concent,size,font_name,color):
        #字体初始化
        pygame.font.init()
        #创建字体
        font=pygame.font.SysFont(font_name,size)
        #根据字创建一个新的表面
        sf=font.render(concent,True,color)
        return sf
    def get_grace_with_concent(self,concent,size,font_name,color):
        pygame.font.init()
        font=pygame.font.SysFont(font_name,size)
        sf=font.render(concent,True,color)
        return sf
    #把所有的提地图原坐标存到列表中
    def init_ponit(self):
        for y in range(1,7):
            temp_list=[]
            for x in range(10):
                point=(x,y)
                temp_list.append(point)

            print(temp_list)
            MainGame.point_list.append(temp_list)
    #把所有原坐标全部遍历出来，转换成地图坐标，并存到一个地图类表中

    def init_map(self):
        for maplist in MainGame.point_list:
            temp_map_list=[]
            for p in maplist:
                x=p[0]*80
                y=p[1]*80
                if (p[0]+p[1])%2==0:
                    map=Map(x,y,1)
                else:
                    map=Map(x,y,0)
                temp_map_list.append(map)
            MainGame.map_list.append(temp_map_list)
    #给僵尸一个初始化
    def init_zombie(self):
        for y in range(1,7):
            dis=random.randint(1,5)*100
            zombie=Zombie(800+dis,y*80)
            MainGame.zombie_list.append(zombie)
    #创建事件处理得方法,调用模块功能，返回一个事件列表
    def del_even(self):
        evenlist=pygame.event.get()
        for e in evenlist:
            if e.type==pygame.QUIT:
                print('点击退出按钮')
                self.overgame()
            elif e.type==pygame.MOUSEBUTTONDOWN:
                print('鼠标按钮')
                print(e.pos)
                x=e.pos[0]//80
                y=e.pos[1]//80
                print(x,y)
                map=MainGame.map_list[y-1][x]
                print(map.position)
                #print(e.button)#左键1  按下滚轮2 上转滚轮为4 下转滚轮为5  右键 3
                if e.button==1:
                    if map.can_grow and MainGame.money>50:
                        sunflower=Sunflower(map.position[0],map.position[1])
                        if 0<=x<=9 and y==0:
                            pass
                        else:
                            MainGame.plant_list.append(sunflower)
                            print('植物列表的长度{}'.format(len(MainGame.plant_list)))
                            MainGame.money-=50
                            map.can_grow=False


                elif e.button==3:
                    if map.can_grow and MainGame.money > 50:
                        peashooter=Peashooter(map.position[0],map.position[1])
                        if 0<=x<=9 and y==0:
                            pass
                        else:
                            MainGame.plant_list.append(peashooter)
                            print('植物列表的长度{}'.format(len(MainGame.plant_list)))
                            MainGame.money-=50
                            map.can_grow=False
                elif e.button==2:
                    x=e.pos[0]//80
                    y=e.pos[1]//80-1
                    map=MainGame.map_list[y][x]
                    for p in MainGame.plant_list:
                        if p.rect.x==map.position[0] and p.rect.y==map.position[1]:
                            MainGame.plant_list.remove(p)
                            map.can_grow=True

            elif e.type==pygame.KEYDOWN:
                print('按键按下')

    #把所有的地图都加载到主窗口
    def load_map(self):
        for list in MainGame.map_list:
            for map in list:
                map.displaymap()
    #把所有的植物加载到主窗口中
    def load_plant(self):
        for plant in MainGame.plant_list:
            if plant.live:
                if isinstance(plant,Sunflower):
                    plant.display_sunflower()
                    plant.grounce()
                elif isinstance(plant,Peashooter):
                    plant.display_pea()
                    plant.peashot()
            else:
                MainGame.plant_list.remove(plant)

    #加载子弹
    def load_bullet(self):
        for b in MainGame.bullet_list:
            if b.live:
                b.move()
                b.display_bullet()
                b.hit_zombie()
            else:
                MainGame.bullet_list.remove(b)
    #加载僵尸
    def load_zombie(self):
        for z in MainGame.zombie_list:
            if z.live:
                z.display_zombie()
                z.move_zombie()
                z.hit_plant()
            else:
                MainGame.zombie_list.remove(z)
                MainGame.grace_count+=1

    def startgame(self):
        #调用初始化主窗口
        self.init_window()

        sf1 = self.get_zombie_with_concent('OOOOOOO!!11一大波僵尸来了', 50, 'kaiti', (255, 0, 0))
        self.init_zombie()
        #调用初始化坐标
        self.init_ponit()
        self.init_map()
        while True:
            # 设置主窗口的颜色
            MainGame.window.fill((255,255,255))
            # 调用新的表面
            sf = self.get_Surface_with_concent('剩余的金币{}'.format(MainGame.money), 26, 'kaiti', (255, 0, 0))

            #把那个新的表面调到窗口
            MainGame.window.blit(sf,(260,10))
            #sf1 = self.get_zombie_with_concent('OOOOOOO!!11一大波僵尸来了', 50, 'kaiti', (255, 0, 0))
            sf2=self.get_grace_with_concent('我的分数是{}'.format(MainGame.grace_count),26,'kaiti',(255,0,0))
            MainGame.window.blit(sf2,(520,10))
            #把地图加载进来
            self.load_map()
            #把事件处理加载进来
            self.del_even()
            #把植物加载进来
            self.load_plant()
            #把子弹加载到窗口
            self.load_bullet()
            self.load_zombie()
            MainGame.zombie_count+=1
            if MainGame.zombie_count==500:
                for i in range(5000):
                    MainGame.window.blit(sf1, (160, 100))
                    pygame.display.update()
                for j in range(3):
                    self.init_zombie()
                MainGame.zombie_count=0

            #调用主窗口表面的刷新
            pygame.display.update()



    def overgame(self):
        sys.exit()
#测试类
if __name__ == '__main__':
    #创建一个游戏主线类的对象
    game=MainGame()
    game.startgame()
    #game.init_ponit()