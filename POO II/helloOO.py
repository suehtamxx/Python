import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#crie uma classe minhframe que herde de tk.Frame e contenha dois botoes. usar dentro da classe principal
'''
class MyFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.__create_widgets()

    def __create_widgets(self):
        ttk.Button(self, text='Clique em mim se quiser ser feliz', command=self.say_hello).grid(row=0, column=0)
        ttk.Button(self, text='Vai me abandonar?', command=self.master.destroy).grid(row=0, column=1)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)
            
    def say_hello(self):
        showinfo(title='VAMO', message='Você será feliz e o seu time também, tmj!')

#usando dentro da classe principal
class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Janela?')
        window_width = 540
        window_height = 640
        self.geometry(f'{window_width}x{window_height}')
        self.resizable(False, False)
        self.attributes('-topmost', 0.85)
        MyFrame(self).grid(row=0, column=0)
                

'''
#criar um miniaplicatico orientado a objetos, criar uma classe que represente um bloco de notas: um texto e um botao salvar
#ao clicar o conteudo deve ser exibido no terminal

class Notepad(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        ttk.Label(self,text='Notepad').grid(row=0, column=0)
        tk.Text(self).grid(row=1, column=0)
        ttk.Button(self,text='Salvar').grid(row=2, column=0)
        
        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)
            
class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Janela?')
        window_width = 540
        window_height = 640
        self.geometry(f'{window_width}x{window_height}')
        self.resizable(False, False)
        self.attributes('-topmost', 0.85)
        Notepad(self).grid(row=0, column=0)
        
if __name__ == '__main__':
    #app = Aplication()
    #app.mainloop()
    
    app = Aplication()
    app.mainloop()