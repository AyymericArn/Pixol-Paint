from tkinter import *
from random import randint
from PIL import ImageGrab

color = 'black'
mode = 0

def click_gauche(event): #fonction peignant la cellule cliquée avec la forme voulue
    x = event.x
    y = event.y
    
    if mode == 0: #si mode normal alors toute la gamme d'outils
        if color == 'white': #si l'outil est la gomme alors une seule forme possible
            can1.create_oval(x-(scale_value_eraser.get()/2), y-(scale_value_eraser.get()/2), x+scale_value_eraser.get()-(scale_value_eraser.get()/2), y+scale_value_eraser.get()-(scale_value_eraser.get()/2), fill=color, outline=color)

        else:
            if form_value.get()==1:
                can1.create_oval(x-(scale_value.get()/2), y-(scale_value.get()/2), x+scale_value.get()-(scale_value.get()/2), y+scale_value.get()-(scale_value.get()/2), fill=color, outline=color)

            elif form_value.get()==2:
                can1.create_rectangle(x-(scale_value.get()/2), y-(scale_value.get()/2), x+scale_value.get()-(scale_value.get()/2), y+scale_value.get()-(scale_value.get()/2), fill=color, outline=color) 
    
            elif form_value.get()==3:
                can1.create_line(x+scale_value.get(), y+scale_value.get(), x, y, width= 1, fill =color)
    
            elif form_value.get()==4:
                if scale_value.get() < 5:
                    multiplier = 6
                else:
                    multiplier = 2
                xrand = randint(-scale_value.get() * multiplier, +scale_value.get() * multiplier)
                yrand = randint(-scale_value.get() * multiplier, +scale_value.get() * multiplier)
             
                can1.create_oval(x + xrand, y + yrand, x + xrand + scale_value.get(), y + yrand + scale_value.get(), fill = color, width = 0)

            elif form_value.get()==5:
                x = event.x -(event.x%c)
                y = event.y -(event.y%c)
                for i in range(pixolSize.get()):
                    x = event.x -(event.x%c) + i*c
                    for i in range (pixolSize.get()):
                        y = event.y -(event.y%c) + i*c
                        can1.create_rectangle(x, y, x+c, y+c, fill=color, outline="white")

    else: #si mode pixol alors seulement dessin en pixels
        x = event.x -(event.x%c)
        y = event.y -(event.y%c)
        for i in range(pixolSize.get()): #boucle permettant d'incrémenter la taille des Pixols
            x = event.x -(event.x%c) + i*c
            for i in range (pixolSize.get()):
                y = event.y -(event.y%c) + i*c
                can1.create_rectangle(x, y, x+c, y+c, fill=color, outline="black")

def click_droit(event): #fonction de raccourci pour la gomme
    if mode == 0: #si mode normal alors gomme normale
        x = event.x
        y = event.y
        can1.create_oval(x-(scale_value_eraser.get()/2), y-(scale_value_eraser.get()/2), x+scale_value_eraser.get()-(scale_value_eraser.get()/2), y+scale_value_eraser.get()-(scale_value_eraser.get()/2), fill='white', outline='white')

    else: #sinon gomme en mode pixels
        x = event.x -(event.x%c)
        y = event.y -(event.y%c)
        can1.create_rectangle(x, y, x+c, y+c, fill="white", outline='black')

def scroll(event): #fonction zoom
    if mode == 0:
	    if event.delta<0:
		    can1.scale("all", event.x, event.y, 0.9, 0.9)
	    elif event.delta>0:
		    can1.scale("all", event.x, event.y, 1.1, 1.1)
       
#fonctions couleur
def red():
    global color
    color = 'red'

def green():
    global color
    color = 'green'

def blue():
    global color
    color = 'blue'

def yellow():
    global color
    color = 'yellow'

def pink():
    global color
    color = 'pink'

def black():
    global color
    color = 'black'

def white():
	global color
	color = 'white'


def erase_all(): #fonction effaçant tout ce qui se trouve dans le canvas
    can1.create_rectangle(0, 0, 2*height, 2*width, fill='white', outline='white')
    if mode == 1:
        grid()

def getter(widget): #fonction qui récupère les coordonnées du canvas et les utilise pour prendre la screenshot
    x=root.winfo_rootx()+widget.winfo_x()
    y=root.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()

    nomFichier = "image"

    ImageGrab.grab((x,y,x1,y1)).save(nomFichier+".jpeg","jpeg")

def saver():
	getter(can1)

# taille de la grille
height = 600
width = 800

c=10

def grid(): #fonction dessinant le tableau
    line_vert()
    line_hor()
    global mode
    mode = 1

def line_vert():
    c_x = 0
    while c_x != width+c:
        can1.create_line(c_x,0,c_x,height+c,width=1,fill='black')
        c_x+=c
        
def line_hor():
    c_y = 0
    while c_y != height+c:
        can1.create_line(0,c_y,width+c,c_y,width=1,fill='black')
        c_y+=c
       
def sheet():
    if mode == 1:
        sheet_vert()
        sheet_hor()

def sheet_vert():
    c_x = 0
    while c_x != width+c:
        can1.create_line(c_x,0,c_x,height+c,width=1,fill='white')
        c_x+=c
    global mode
    mode=0

def sheet_hor():
    c_y = 0
    while c_y != height+c:
        can1.create_line(0,c_y,width+c,c_y,width=1,fill='white')
        c_y+=c

#programme "principal"
root = Tk()

root.wm_title("Pixol Paint")
#root.wm_state(newstate="zoomed")
	
menu_bar = Menu(root) #menu parent

# crée les sous-menus
file_menu = Menu(menu_bar, tearoff=0)
mode_menu = Menu(menu_bar, tearoff=0)

# Commandes des sous-menu
file_menu.add_command(label="Nouveau", command=erase_all)
file_menu.add_command(label="Enregistrer au format JPEG...", command=saver)
file_menu.add_command(label="Quitter", command=root.destroy)
mode_menu.add_command(label="Normal", command=sheet)
mode_menu.add_command(label="Grille", command=grid)

#liaison des sous-menus au menu
menu_bar.add_cascade(label="Fichier", menu=file_menu)
menu_bar.add_cascade(label="Mode", menu=mode_menu)

root.config(menu=menu_bar)

can1 = Canvas(root, width =width, height =height, bg ='white', borderwidth=2)
can1.bind("<B1-Motion>", click_gauche)
can1.bind("<Button-1>", click_gauche)
can1.bind("<B3-Motion>", click_droit)
can1.bind("<MouseWheel>", scroll)
can1.pack(side =TOP, padx =50, pady =5)

#image utilisée pour le bouton de la gomme
eraserPic = PhotoImage(file= "icones/gomme_01.png")

#boutons
b_red = Button(root, bg ='red', command =red, height=1, width=2)
b_green = Button(root, bg = 'green', command =green, height=1, width=2)
b_blue = Button(root, bg = 'blue', command =blue, height=1, width=2)
b_yellow = Button(root, bg = 'yellow', command =yellow, height=1, width=2)
b_pink = Button(root, bg = 'pink', command =pink, height=1, width=2)
b_black = Button(root, bg = 'black', command =black, height=1, width=2)
eraser = Button(root, image= eraserPic, command=white)

form_value = IntVar()
Radiobutton(root, text="Pinceau Rond", variable= form_value, value=1).pack(side =LEFT, padx =3, pady =3)
Radiobutton(root, text="Pinceau Carré", variable= form_value, value=2).pack(side =LEFT, padx =3, pady =3)
Radiobutton(root, text="Plume", variable= form_value, value=3).pack(side =LEFT, padx =3, pady =3)
Radiobutton(root, text="Spray", variable= form_value, value=4).pack(side =LEFT, padx =3, pady =3)
Radiobutton(root, text="Pixol", variable= form_value, value=5).pack(side =LEFT, padx =3, pady =3)

b_red.pack(side =LEFT, padx =3, pady =3)
b_green.pack(side =LEFT, padx =3, pady =3)
b_blue.pack(side =LEFT, padx =3, pady =3)
b_yellow.pack(side =LEFT, padx =3, pady =3)
b_pink.pack(side=LEFT, padx =3, pady=3)
b_black.pack(side =LEFT, padx =3, pady =3)
eraser.pack(side =LEFT, padx =3, pady=3)

b_erase = Button(root, text ='Tout effacer', bitmap = "error", command =erase_all)
b_erase.pack(side =LEFT, padx =3, pady =3)

#curseurs de taille
scale_value = IntVar()
cursor = Scale(root, orient='horizontal', from_=1, to=25, label='taille de la brosse', variable= scale_value, length=200)
cursor.pack(side =BOTTOM, anchor = E)

scale_value_eraser = IntVar()
cursor = Scale(root, orient='horizontal', from_=15, to=50, label='taille de la gomme', variable= scale_value_eraser, length=200)
cursor.pack(side = BOTTOM, anchor = E)

pixolSize = IntVar()
cursor = Scale(root, orient='vertical', from_=1, to=4, label='taille des pixels', variable=pixolSize, length=100)
cursor.pack(side =BOTTOM, anchor = E)

root.mainloop()