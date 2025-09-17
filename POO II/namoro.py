import tkinter as tk
from tkinter import ttk, messagebox
import random

def move_button(event):
    '''Funcao para mover o nao para uma posicao aleatoria'''
    new_x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    new_y = random.randint(0, root.winfo_height() - no_button.winfo_height())
    no_button.place(x=new_x,y=new_y)

def accept_proposal():
    messagebox.showinfo('Resposta','Tmj mano')
    root.destroy()
    
def reject():
    messagebox.showerror('Resposta','Voce nunca vai me pegar')
    
#criacao da janela principal
root = tk.Tk()
root.title('Pedido de namoro')
window_width = 540
window_height = 540
def center_screen(window_width, window_height):
    #pegando as dimensoes da tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #encontrar o ponto central
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    return center_x, center_y

center_x, center_y = center_screen(window_width,window_height)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#metodo para deixar ampliar ou nao a tela
root.resizable(False, False)
#metodo para deixar a tela mais transparente
root.attributes('-topmost', 0.85)

#criacao do titulo
title_label = ttk.Label(
    root,
    text='Aceita namorar comigo?',
    font=('Arial',14)
)
title_label.pack(pady=20)

#criacao do botao sim
yes_button = ttk.Button(
    root,
    text='sim',
    command=accept_proposal
)
yes_button.pack()

#criacao do botao nao
no_button = ttk.Button(
    root,
    text='nao',
    compound=tk.RIGHT,
    command=reject
)
#posicionar o nao em um local inicial
no_button.pack()

#vincular o evento a funcao move_button
no_button.bind('<Enter>', move_button)

root.mainloop()