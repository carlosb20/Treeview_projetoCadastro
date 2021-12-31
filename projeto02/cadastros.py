from tkinter import *
from tkinter import ttk
from tkinter import messagebox

lista = list()

class Famarcia(Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self.tela()
        self.frame1()
        self.frame2()
        self.botoas()
        self.funcaEntry()
        self.funcaoTreeview()

    def tela(self):
        self.title('Cadastro de Produtos Cosmedico')
        self.geometry('1100x600+30+50')
        self['bg'] = 'silver'
        self.resizable(True,True)
        self.maxsize(1100,600)
        self.minsize(700,300)
        
    def frame1(self):
        self.frametela1 = Frame(self)
        self.frametela1.config(highlightbackground='red')
        self.frametela1.config(highlightthickness=2)
        self.frametela1.place(relx=0.01,rely=0.02,relwidth=0.98,relheight=0.40)

    def frame2(self):
        self.frametela2 = Frame(self)
        self.frametela2.config(highlightbackground='red')
        self.frametela2.config(highlightthickness=2)
        self.frametela2.place(relx=0.01,rely=0.42,relwidth=0.98,relheight=0.56)
    
    def botoas(self):
        self.limpa = Button(self.frametela1,text='Limpa')
        self.limpa.place(relx=0.15,rely=0.04,relwidth=0.07,relheight=0.11)

        self.busca = Button(self.frametela1,text='Busca')
        self.busca.place(relx=0.25,rely=0.04,relwidth=0.07,relheight=0.11) 

        self.novo = Button(self.frametela1,text='Novo',command=self.dados)
        self.novo.place(relx=0.46,rely=0.04,relwidth=0.07,relheight=0.11)

        self.altera = Button(self.frametela1,text='Alterar',command=self.funcao_alterar)
        self.altera.place(relx=0.58,rely=0.04,relwidth=0.07,relheight=0.11)

        self.apaga = Button(self.frametela1,text='Apaga')
        self.apaga.place(relx=0.69,rely=0.04,relwidth=0.07,relheight=0.11)
        
    def funcaEntry(self):


        self.codi = StringVar()
        self.nome = StringVar()
        self.pre = StringVar()
        self.uni = StringVar()
        self.bo = StringVar()

        self.codigo = Label(self.frametela1,text='Codigo')
        self.codigo.place(relx=0.04,rely=0.06,relwidth=0.06,relheight=0.09)

        self.entryCodigo = Entry(self.frametela1,textvariable=self.codi)
        self.entryCodigo.config(font='Arial 15 ')
        self.entryCodigo.place(relx=0.04,rely=0.15,relwidth=0.06,relheight=0.09) 

        self.labelNome = Label(self.frametela1,text='Nome')
        self.labelNome.place(relx=0.03,rely=0.30,relwidth=0.06,relheight=0.09)

        self.entryNome = Entry(self.frametela1,textvariable=self.nome)
        self.entryNome.config(font='Arial 15 ')
        self.entryNome.place(relx=0.04,rely=0.40,relwidth=0.80,relheight=0.13)

        self.labelpreco = Label(self.frametela1,text='Preço')
        self.labelpreco.place(relx=0.03,rely=0.53,relwidth=0.06,relheight=0.09) 

        self.entrypreco = Entry(self.frametela1,textvariable=self.pre)
        self.entrypreco.config(font='Arial 15 ')
        self.entrypreco.place(relx=0.04,rely=0.63,relwidth=0.20,relheight=0.13)

        self.labelunidade = Label(self.frametela1,text='Unidade')
        self.labelunidade.place(relx=0.28,rely=0.53,relwidth=0.06,relheight=0.09)

        self.entryunidade = Entry(self.frametela1,textvariable=self.uni)
        self.entryunidade.config(font='Arial 15 ')
        self.entryunidade.place(relx=0.28,rely=0.63,relwidth=0.20,relheight=0.13)

        self.labelbox = Label(self.frametela1,text='Box')
        self.labelbox.place(relx=0.50,rely=0.53,relwidth=0.06,relheight=0.09)

        self.entrybox = Entry(self.frametela1,textvariable=self.bo)
        self.entrybox.config(font='Arial 15 ')
        self.entrybox.place(relx=0.50,rely=0.63,relwidth=0.20,relheight=0.13)

    def funcaoTreeview(self):

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure('Treeview.Heading',background='yellow',
        rowheight=10,foreground='blue',font= 'Arial 12')

        self.style.map("Treeview",background=[('selected','green')])

 
        self.tree = ttk.Treeview(self.frametela2)
        self.tree['show'] = 'headings'
        self.tree['columns'] = ('codigo','nome','preco','unidade','box')
    
        self.tree.heading('codigo',text='codigo')
        self.tree.heading('nome',text='nome')
        self.tree.heading('preco',text='preco')
        self.tree.heading('unidade',text='unidade')
        self.tree.heading('box',text='box')
        self.tree.bind('<Button-1>',self.dadostreev)
        self.tree.place(relx=0.00,rely=0.00,relwidth=0.98,relheight=0.99)

        self.barras = ttk.Scrollbar(self.frametela2)
        self.tree.configure(yscrollcommand=self.barras.set)
        self.barras.configure(command=self.tree.yview)
        self.barras.place(relx=0.98,rely=0.0,relheight=0.99)

        self.tree.tag_configure('pri',background ='red')
        self.tree.tag_configure('seg',background ='blue')

        cont = 0
        
        for a in lista:
            if cont % 2 == 0:
                self.tree.insert('','end',values=(a[0],a[1],a[2],a[3],a[4]),tags=('pri'))
            else:
                self.tree.insert('','end',values=(a[0],a[1],a[2],a[3],a[4]),tags=('seg'))
            cont += 1
                 
    def dados(self):
        nao = False
        if self.entryCodigo.get() != '' and self.entryNome.get() != '' and self.entrypreco.get() != '' and self.entryunidade.get() != '' and self.entrybox.get() != '':
            if len(lista) > 0:
                for a in lista:
                    if self.entryCodigo.get() == a[0]:
                        messagebox.showinfo('',' Codigo ja existe ')
                        nao = True

                if nao == False:
 
                        lista.append([self.entryCodigo.get(),self.entryNome.get(),
                            self.entrypreco.get(),self.entryunidade.get(),self.entrybox.get()])

            
                        self.funcaoTreeview()
                        
                        self.entryCodigo.delete(0,END)
                        self.entryNome.delete(0,END)
                        self.entrypreco.delete(0,END)
                        self.entryunidade.delete(0,END)
                        self.entrybox.delete(0,END)
                        self.entryCodigo.focus()
            else:
                lista.append([self.entryCodigo.get(),self.entryNome.get(),
                    self.entrypreco.get(),self.entryunidade.get(),self.entrybox.get()])

                self.funcaoTreeview()
                
                self.entryCodigo.delete(0,END)
                self.entryNome.delete(0,END)
                self.entrypreco.delete(0,END)
                self.entryunidade.delete(0,END)
                self.entrybox.delete(0,END)
                self.entryCodigo.focus()

        else:
            messagebox.showerror('Erro','Preencha o Espaço Vazio ')
      
    def dadostreev(self,e):
        res = self.tree.selection()[0]
        ca = self.tree.item(res,'values')
        self.codi.set(ca[0])
        self.nome.set(ca[1])
        self.pre.set(ca[2])
        self.uni.set(ca[3])
        self.bo.set(ca[4])

    def funcao_alterar(self):
        for a in lista:
            if self.entryCodigo.get() in a:
                a[1] = self.entryNome.get()
                a[2] = self.entrypreco.get()
                a[3] = self.entryunidade.get()
                a[4] = self.entrybox.get()
                
        

        
        self.funcaoTreeview()

if __name__ == '__main__':
    res = Famarcia()
    res.mainloop()