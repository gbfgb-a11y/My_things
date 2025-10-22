from tkinter import *; import re; import random
t = Tk()
t.geometry('1000x600')
t.title('Snoopships')
ship0 = PhotoImage(file=r'C:\Users\denke\Desktop\SOMETHING\supercalculator_\snoop_ship_yo.png')
ship = ship0.subsample(11, 11)
burning_ship = PhotoImage(file=r'C:\Users\denke\Desktop\SOMETHING\supercalculator_\snoop_hitted1.png')
ship_burning = burning_ship.subsample(11,11)
fell_in_water1 = PhotoImage(file=r'C:\Users\denke\Desktop\SOMETHING\supercalculator_\dead.png')
fell_in_water = fell_in_water1.subsample(5,5)
water_= PhotoImage(file=r'C:\Users\denke\Desktop\SOMETHING\supercalculator_\water].png')
water=water_.subsample(5,3)
t.iconphoto(False,ship)
f1=Frame(t, borderwidth='1', relief='sunken').place(x='0',y='100',width='498',height='500')
f2=Frame(t, borderwidth='1', relief='sunken').place(x='500',y='100',width='498',height='500')
snuplab = Label(t, image=ship).place(x='0',y='0')
letters = ['A','B','C','D','E']; numbers = [1,2,3,4,5]; map_player={}; map_bot={}; map_list=[]
player_values=[]; want=True;buttons_player = {}; bot_choosed=[]; ggg=True; bot_values=[];player=True;bot=True
buttons_bot = {};countsh=0; total=0;hitted=0;accuracity=0
def attack(square):
    global bot,player,bot_values, total,hitted,accuracity
    for i in map_list:
        bot_values.append(map_bot.get(i))
    if 'Bot' not in bot_values:
        bot=False
        Label(t,text='You Won', font=('Arial', 14)).place(x='300',y='20',width='350',height='60')
    if bot and player:   
        if map_bot[square] == 'Bot':
            map_bot[square] = 'Hitted'
            buttons_bot[square].config(image=ship_burning)
            hitted+=1
        elif map_bot[square] is None:
            map_bot[square] = 'Fell in water'
            buttons_bot[square].config(image=fell_in_water)
        if map_bot[square] == 'Fell in water':
            pass
        if map_bot[square] == 'Hitter':
            pass
        total+=1
        bot_attack()
    bot_values=[]
    accuracity=(hitted/total)*100
    Label(t,text=f'''
        ### Total attemptions: {total}
        ### Your hitted targets: {hitted}
        ### Your accuracity: {round(accuracity)}%
''', font=('Arial', 14)).place(x='750',y='0',width='250',height='100')

def putships(square):
    global countsh,bot,player
    if map_player[square] is None:
        if countsh != 5:
            map_player[square] = 'Player'
            buttons_player[square].config(image=ship)
            countsh+=1
def bot_attack():
    global ggg, bot,player, player_values ,total,hitted,accuracity
    for i in map_list:
        player_values.append(map_player.get(i))
    if 'Player' not in player_values:
        player=False
        Label(t,text='You Loosed', font=('Arial', 14)).place(x='300',y='20',width='350',height='60')
    if bot and player:   
        while True:  
            hq = random.choice(map_list)
            if hq not in bot_choosed:
                yy=map_player.get(hq)
                if yy == 'Player':
                    map_player.update({hq:'Hitted'})
                    buttons_player[hq].config(image=ship_burning)
                if yy == None:
                    map_player.update({hq:'Fell in water'})
                    buttons_player[hq].config(image=fell_in_water)
                bot_choosed.append(hq)
                break
    player_values=[]
    Label(t,text=f'''
        ### Total attemptions: {total}
        ### Your hitted targets: {hitted}
        ### Your accuracity: {round(accuracity)}%
''',font=('Arial', 14)).place(x='750',y='0',width='250',height='100')
            
def generete():
    for a in letters:
        for i in numbers:
            map_list.extend({a+str(i)})
    for i in map_list:
            map_bot.update({i:None})
            map_player.update({i:None})
    for a in range(6):   
            u = random.choice(map_list)
            map_bot.update({u:'Bot'})
generete()
w, h = 0, 100
for square in map_list:
    state = map_player[square]
    img = ship if state == 'Player' else water
    #if countsh < 5:    
    btn = Button(t, image=img, command=lambda s=square: putships(s))
    btn.place(x=w, y=h, width=100, height=100)
    buttons_player[square] = btn
    #else:
    #    btn = Button(t, image=img)
    #    btn.place(x=w, y=h, width=100, height=100)
    w += 100
    if w >= 500:
        w = 0
        h += 100
wp, hp = 500, 100
for square in map_list:
    state = map_bot[square]
    img = water
    btn = Button(t, image=img, command=lambda s=square: attack(s))
    btn.place(x=wp, y=hp, width=100, height=100)
    buttons_bot[square] = btn
    wp += 100
    if wp >= 1000:
        wp = 500
        hp += 100

t.mainloop()



