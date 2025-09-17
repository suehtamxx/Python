import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
tk.Label(root, text='CORINTHIANS', font=('Arial', 10)).pack()
root.title('Janela?')
window_width = 540
window_height = 540
root.config(background="#F400CF")
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

# Caminho completo para o arquivo do ícone
icon_path = r'C:\Users\Elder Matheus\Documents\Python - Curso\teste.ico'

root.iconbitmap(icon_path)
'''
fields = {}
fields['username_label'] = ttk.Label(root,text='Username:')
fields['username'] = ttk.Entry(root)

fields['password_label'] = ttk.Label(root,text='Password:')
fields['password'] = ttk.Entry(root, show='*')

for field in fields.values():
    field.pack(anchor=tk.W,padx=5,pady=5,fill=tk.X)
    
ttk.Button(text='Login').pack(anchor=tk.W,padx=10,pady=10)
'''

'''
def qualquer():
    if var_1.get():
        var_2.set('Ativado')
    else:
        var_2.set('Desativado')
        
var_1 = tk.BooleanVar()
var_2 = tk.StringVar()

checkbox = ttk.Checkbutton(root,text='Ativar/Desativar',command=qualquer,variable=var_1)
checkbox.pack(side=tk.TOP,pady=20)


lb = ttk.Label(root,text='Desativado',textvariable=var_2)
lb.pack(side=tk.BOTTOM,pady=20)

valor_atual = tk.StringVar(value='10')
ttk.Spinbox(root, from_=16, to=35,textvariable=valor_atual,wrap=True).pack()

'''
#Questao 4
valor = tk.DoubleVar(value=1)
sp = ttk.Spinbox(root, from_=1, to=10,textvariable=valor,wrap=True)
sp.pack(padx=10,pady=10)
lb = ttk.Label(root,textvariable=valor)
lb.pack(padx=10,pady=10)

current_var = tk.StringVar()

cb = ttk.Combobox(root,values=['Manha', 'Tarde', 'Noite'],state='readonly',textvariable=current_var)


cb.pack(fill=tk.X,padx=10,pady=10)

label = ttk.Label(root,textvariable=current_var)
label.pack(side=tk.TOP,padx=5,pady=5)


root.mainloop()