from tkinter import *
window = Tk()
saved = 0
def get_texture(event):
    global selected_texture
    selected_texture[0] = all_textures[all_texture_buttons[event.widget]]
    selected_texture[1] = all_texture_buttons[event.widget]
    show_selected_texture.config(image=selected_texture[0])
def paint(event):
    global selected_texture,map_buttons
    event.widget.config(image=selected_texture[0])
    map_buttons[event.widget][2] = selected_texture[1]
def print_map():
    output = []
    for i in range(17):
        output.append([])
        for j in range(17):
            for n in map_buttons.values():
                if n[0]==i and n[1]==j:
                    output[i].append(n[2])
    print(output)
def save_map():
    global saved
    saved+=1
    txt = open("editor/map"+str(saved)+".txt","w")
    for i in range(17):
        for j in range(17):
            for n in map_buttons.values():
                if n[0]==i and n[1]==j:
                    txt.write(n[2]+" ")
        txt.write("\n")
    txt.close()
def paste():
    global map_buttons
    for i in map_buttons:
        i.config(image=selected_texture[0])
        map_buttons[i][2]=selected_texture[1]
def load():
    input_map = list(eval(input()))
    for i in range(17):
        for j in range(17):
            for n in map_buttons.keys():
                if map_buttons[n][0]==i and map_buttons[n][1]==j:
                    n.config(image=all_textures[input_map[i][j]])
                    map_buttons[n][2] = input_map[i][j]
def from_file_load():
    for i in range(17):
        input_line = input().split()
        for j in range(17):
            for n in map_buttons.keys():
                if map_buttons[n][0]==i and map_buttons[n][1]==j:
                    n.config(image=all_textures[input_line[j]])
                    map_buttons[n][2] = input_line[j]
map_frame = Frame(window,bd=0)
map_frame.grid(row=0,column=0,rowspan=2)
buttons_frame = Frame(window,bd=0)
buttons_frame.grid(row=1,column=1)
info_frame = Frame(window,bd=0)
info_frame.grid(row=0,column=1)
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
all_texture_buttons = {}
for i in all_textures.keys():
    texture_button = Button(buttons_frame,image=all_textures[i])
    texture_button.bind('<Button-1>',get_texture)
    all_texture_buttons[texture_button] = i
    l = int(i)%10
    m = int(i)//10
    texture_button.grid(row=l,column=m)
selected_texture=[t000,'000']
map_buttons = {}
for i in range(17):
    for j in range(17):
        map_button = Button(map_frame,image=t000,bd=0)
        map_button.bind('<Button-1>',paint)
        map_buttons[map_button] = [i,j,'000']
        map_button.grid(row=i,column=j)
show_selected_texture = Button(info_frame,image=t000,command=paste)
show_selected_texture.grid(row=2,column=0)
print_button = Button(info_frame,text="PRINT MAP",command = print_map)
print_button.grid(row=1,column=0)
save_in_file_button = Button(info_frame,text="SAVE IN TXT",command = save_map)
save_in_file_button.grid(row=0,column=0)
load_button = Button(info_frame,text="CLS LOAD",command=load)
load_button.grid(row=1,column=1)
load_from_file_button = Button(info_frame,text="TXT LOAD",command=from_file_load)
load_from_file_button.grid(row=0,column=1)
window.mainloop()
