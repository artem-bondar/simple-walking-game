from tkinter import *
root = Tk()
#Глобальные переменные
hero_position = [0,0,0,'N']
HeroUp = PhotoImage(file="textures/HeroUp.png")
HeroDown = PhotoImage(file="textures/HeroDown.png")
HeroLeft = PhotoImage(file="textures/HeroLeft.png")
HeroRight = PhotoImage(file="textures/HeroRight.png")
HeroPositionImage = {'N':HeroUp,'E':HeroRight,'S':HeroDown,'W':HeroLeft}
t000 = PhotoImage(file="textures/empty.png")
t001 = PhotoImage(file="textures/grass.png")
t002 = PhotoImage(file="textures/grass2.png")
t003 = PhotoImage(file="textures/grass3.png")
t004 = PhotoImage(file="textures/grass4.png")
t005 = PhotoImage(file="textures/sand.png")
t006 = PhotoImage(file="textures/needles.png")
t007 = PhotoImage(file="textures/water.png")
t008 = PhotoImage(file="textures/water2.png")
t009 = PhotoImage(file="textures/water3.png")
t010 = PhotoImage(file="textures/stone.png")
t011 = PhotoImage(file="textures/stone2.png")
t012 = PhotoImage(file="textures/stone3.png")
t013 = PhotoImage(file="textures/snow.png")
t014 = PhotoImage(file="textures/moss.png")
t015 = PhotoImage(file="textures/brick.png")
t016 = PhotoImage(file="textures/board.png")
t017 = PhotoImage(file="textures/cheese.png")
t018 = PhotoImage(file="textures/black.png")
all_textures = {'000':t000,'001':t001,'002':t002,'003':t003,'004':t004,'005':t005,'005':t005,'006':t006,'007':t007,'008':t008,'009':t009,'010':t010,'011':t011,'012':t012,'013':t013,'014':t014,'015':t015,'016':t016,'017':t017,'018':t018}
walkable_textures = [t000,t001,t002,t003,t004,t005,t010,t011,t013,t014,t016,t017]
#Классы
class map_generator:
    def __init__(self):
        self.id = 0
        self.neighbours = [0,0,0,0]
        self.name = ""
        self.description = "" 
        self.map = []
        self.sprites = []
        for i in range(17):
            self.map.append([])
            self.sprites.append([])
            for j in range(17):
                self.map[i].append(all_textures['000'])
                self.sprites[i].append((all_sprites['000'],None))
    def render(self,window):
        global map_window,hero_position
        hero_position[0] = self.id
        map_window.destroy()
        map_window = Canvas(window,width=561,height=561,bd=0)
        map_window.place(x=0,y=0)
        for i in range(17):
            for j in range(17):
                map_window.create_image(18+j*33,18+i*33,image=self.map[i][j])
                if self.sprites[i][j] != (s000,None) :
                    if self.sprites[i][j][1] != None:
                        map_window.create_image(18+j*33,18+i*33,image=self.sprites[i][j][0])
                    elif self.sprites[i][j][0] != t000:
                        map_window.create_image(18+j*33,18+i*33,image=self.sprites[i][j][0])
    def load_textures(self,texture_pack):
        for i in range(17):
            for j in range(17):
                self.map[i][j] = all_textures[texture_pack[i][j]]
    def load_sprites(self,sprite_pack):
        for i in range(17):
            for j in range(17):
                if type(sprite_pack[i][j]) != str:
                    self.sprites[i][j] = (sprite_pack[i][j].texture,sprite_pack[i][j])
                else:
                    self.sprites[i][j] = (all_sprites[sprite_pack[i][j]],None)
    def load_map(self):
        txt = open("maps/map"+str(self.id)+".txt",'r')
        for i in range(17):
            self.map[i] = txt.readline().split()
            for j in range(17):
                self.map[i][j] = all_textures[self.map[i][j]]
        txt.close()
class teleporter:
    def __init__(self,input_texture,input_target_coordinates): #Пример ввода: '000',[0,0,0,'N']
        global all_sprites
        self.texture = all_sprites[input_texture] 
        self.target_coordinates = input_target_coordinates 
        def teleport():
            global hero_position,HeroPositionImage,all_maps
            all_maps[self.target_coordinates[0]].render(root)
            for i in range(4):
                hero_position[i] = self.target_coordinates[i]
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage[hero_position[3]])
        self.function = lambda: 0
        self.function_on_spot = teleport
class ifrit():
    def __init__(self,input_texture,name_input):
        global all_sprites
        self.texture = all_sprites[input_texture] 
        self.name = name_input
        self.username = ""
        def dialog():
            def enter(event):
                def reply():
                    rad0.destroy()
                    rad1.destroy()
                    rad2.destroy()
                    rad3.destroy()
                    ok.destroy()
                    if var.get() == 0:
                        info.config(text="-Ну и катись колобком дальше.",anchor=W)
                    elif var.get() == 1:
                        info.config(text="-Слышь, ты с какого района вообще, а? Пшел на.",anchor=W)
                    elif var.get() == 2:
                        info.config(text="*Элементаль промолчал*",anchor=W)
                    elif var.get() == 3:
                        info.config(text="-...",anchor=W)
                if self.username == "":
                    self.username = entry.get()
                    info.config(text="-Что привело тебя в мою обитель, "+entry.get()+"?",anchor=W)
                else:
                    info.config(text="-Что привело тебя в мою обитель, "+self.username+"?",anchor=W)
                entry.destroy()
                var=IntVar()
                var.set(0)
                rad0 = Radiobutton(talk,text="-Так зашел.",variable=var,value=0)
                rad1 = Radiobutton(talk,text="-Пофиг. Есть мобила позвонить?",variable=var,value=1)
                rad2 = Radiobutton(talk,text="-Миссия важная выдана мне.",variable=var,value=2)
                rad3 = Radiobutton(talk,text="*Промолчать*",variable=var,value=3)
                rad0.pack(anchor=W)
                rad1.pack(anchor=W)
                rad2.pack(anchor=W)
                rad3.pack(anchor=W)
                ok = Button(talk,text="OK",command=reply)
                ok.pack()
            talk = Toplevel(root)
            talk.focus()
            info = Label(talk,text="-Я могучий и древнейший элементаль огня, именуемый "+self.name+".\n-Каково же твое имя, странник?",fg='red')
            info.pack()
            entry = Entry(talk)
            entry.pack()
            if self.username != "":
                enter(1)
            talk.bind("<Return>",enter)
        self.function = dialog
#Глобальные переменные, использующие классы: спрайты
s000 = PhotoImage(file="sprites/empty.png")
s001 = PhotoImage(file="sprites/manhole.png")
s002 = PhotoImage(file="sprites/ledder.png")
s003 = PhotoImage(file="sprites/fire elementile.png")
all_sprites = {'000':s000,'001':s001,'002':s002,'003':s003}
walkable_sprites = [s000,s001,s002]
manhole1 = teleporter('001',[10,2,14,'N'])
manhole2 = teleporter('001',[10,14,5,'S'])
ledder1 = teleporter('002',[1,5,1,'N'])
ledder2 = teleporter('002',[2,12,13,'S'])
fire = ifrit('003','Lambda Velorum')
sprite_pack1=[['000', '000', fire, '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000',manhole1, '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000']]
sprite_pack2=[['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', manhole2, '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000']]
sprite_pack10=[['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', ledder2, '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', ledder1, '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000']]
sprite_pack11=[['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', fire, '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000'], ['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000']]
#Классовые переменные
map1=map_generator()
map1.id=1
map1.name='Start'
map1.neighbours=[2,3,4,5]
map1.load_map()
map1.load_sprites(sprite_pack1)

map2=map_generator()
map2.id=2
map2.name='2-test'
map2.neighbours=[0,7,1,6]
map2.load_map()
map2.load_sprites(sprite_pack2)

map3=map_generator()
map3.id=3
map3.name='3-test'
map3.neighbours=[7,0,8,1]
map3.load_map()

map4=map_generator()
map4.id=4
map4.name='4-test'
map4.neighbours=[1,8,0,9]
map4.load_map()

map5=map_generator()
map5.id=5
map5.name='5-test'
map5.neighbours=[6,1,9,0]
map5.load_map()

map6=map_generator()
map6.id=6
map6.name='6-test'
map6.neighbours=[0,2,5,0]
map6.load_map()

map7=map_generator()
map7.id=7
map7.name='7-test'
map7.neighbours=[0,0,3,2]
map7.load_map()

map8=map_generator()
map8.id=8
map8.name='8-test'
map8.neighbours=[3,0,0,4]
map8.load_map()

map9=map_generator()
map9.id=9
map9.name='9-test'
map9.neighbours=[5,4,0,0]
map9.load_map()

map10=map_generator()
map10.id=10
map10.name='Canalisation'
map10.neighbours=[11,0,0,0]
map10.load_map()
map10.load_sprites(sprite_pack10)

map11=map_generator()
map11.id=11
map11.name='Canalisation 2'
map11.neighbours=[0,0,10,0]
map11.load_map()
map11.load_sprites(sprite_pack11)

all_maps = {map1.id:map1,map2.id:map2,map3.id:map3,map4.id:map4,map5.id:map5,map6.id:map6,map7.id:map7,map8.id:map8,map9.id:map9,map10.id:map10,map11.id:map11}

hero_position = [1,0,0,'N']

#Функции
def interact(event):
    global hero_position
    if hero_position[3] == 'N' and hero_position[2] != 0 and all_maps[hero_position[0]].sprites[hero_position[2]-1][hero_position[1]][1] != None:
        all_maps[hero_position[0]].sprites[hero_position[2]-1][hero_position[1]][1].function()
    elif hero_position[3] == 'S' and hero_position[2] != 16 and all_maps[hero_position[0]].sprites[hero_position[2]+1][hero_position[1]][1] != None:
        all_maps[hero_position[0]].sprites[hero_position[2]+1][hero_position[1]][1].function()
    elif hero_position[3] == 'W' and hero_position[1] != 0 and all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]-1][1] != None:
        all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]-1][1].function()
    elif hero_position[3] == 'E' and hero_position[1] != 16 and all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]+1][1] != None:
        all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]+1][1].function()
    elif all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][1] != None:
        all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][1].function_on_spot()
def move_down(event):
    global hero_position,HeroPositionImage,all_maps,all_sprites
    if hero_position[3] != 'S':
        hero_position[3] = 'S'
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['S'])
    else:
        if hero_position[2] != 16 and all_maps[hero_position[0]].map[hero_position[2]+1][hero_position[1]] in walkable_textures and all_maps[hero_position[0]].sprites[hero_position[2]+1][hero_position[1]][0] in walkable_sprites:
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
            hero_position[2]+=1 
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['S'])
        elif hero_position[2] == 16:
            if all_maps[hero_position[0]].neighbours[2] != 0 and all_maps[all_maps[hero_position[0]].neighbours[2]].map[0][hero_position[1]] in walkable_textures and all_maps[all_maps[hero_position[0]].neighbours[2]].sprites[0][hero_position[1]][0] in walkable_sprites:
                hero_position[2] = 0
                all_maps[all_maps[hero_position[0]].neighbours[2]].render(root)
                map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['S'])
def move_up(event):
    global hero_position,HeroPositionImage,all_maps,all_sprites
    if hero_position[3] != 'N':
        hero_position[3] = 'N'
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['N'])
    else:
        if hero_position[2] != 0 and all_maps[hero_position[0]].map[hero_position[2]-1][hero_position[1]] in walkable_textures and all_maps[hero_position[0]].sprites[hero_position[2]-1][hero_position[1]][0] in walkable_sprites:
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
            hero_position[2]-=1 
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['N'])
        elif hero_position[2] == 0:
            if all_maps[hero_position[0]].neighbours[0] != 0 and all_maps[all_maps[hero_position[0]].neighbours[0]].map[16][hero_position[1]] in walkable_textures and all_maps[all_maps[hero_position[0]].neighbours[0]].sprites[16][hero_position[1]][0] in walkable_sprites:
                hero_position[2] = 16
                all_maps[all_maps[hero_position[0]].neighbours[0]].render(root)
                map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['N'])
def move_right(event):
    global hero_position,HeroPositionImage,all_maps,all_sprites
    if hero_position[3] != 'E':
        hero_position[3] = 'E'
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['E'])
    else:
        if hero_position[1] != 16 and all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]+1] in walkable_textures and all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]+1][0] in walkable_sprites:
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
            hero_position[1]+=1 
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['E'])
        elif hero_position[1] == 16:
            if all_maps[hero_position[0]].neighbours[1] != 0 and all_maps[all_maps[hero_position[0]].neighbours[1]].map[hero_position[2]][0] in walkable_textures and all_maps[all_maps[hero_position[0]].neighbours[1]].sprites[hero_position[2]][0][0] in walkable_sprites:
                hero_position[1] = 0
                all_maps[all_maps[hero_position[0]].neighbours[1]].render(root)
                map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['E'])
def move_left(event):
    global hero_position,HeroPositionImage,all_maps,all_sprites
    if hero_position[3] != 'W':
        hero_position[3] = 'W'
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
        map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['W'])
    else:
        if hero_position[1] != 0 and all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]-1] in walkable_textures and all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]-1][0] in walkable_sprites:
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].map[hero_position[2]][hero_position[1]])
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=all_maps[hero_position[0]].sprites[hero_position[2]][hero_position[1]][0])
            hero_position[1]-=1 
            map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['W'])
        elif hero_position[1] == 0:
            if all_maps[hero_position[0]].neighbours[3] != 0 and all_maps[all_maps[hero_position[0]].neighbours[3]].map[hero_position[2]][16] in walkable_textures and all_maps[all_maps[hero_position[0]].neighbours[3]].sprites[hero_position[2]][16][0] in walkable_sprites:
                hero_position[1] = 16
                all_maps[all_maps[hero_position[0]].neighbours[3]].render(root)
                map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['W'])
#Ткинтер
root.geometry('565x565')
root.bind("<Return>",interact)
root.bind("<Down>",move_down)
root.bind("<Up>",move_up)
root.bind("<Right>",move_right)
root.bind("<Left>",move_left)
map_window = Canvas(root,width=561,height=561,bd=0)
map1.render(root)
map_window.create_image(18+hero_position[1]*33,18+hero_position[2]*33,image=HeroPositionImage['N'])
root.mainloop()
