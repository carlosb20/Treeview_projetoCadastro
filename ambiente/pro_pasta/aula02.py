from tkinter import *
from tkinter import ttk
from pro_pasta.sqldados.sql03 import inserirdados,lista_nome,deleta_nome
from tkinter import messagebox

#lista_nome = list()

num = 0

class ProjetoCadastro(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.titulo_tela()
        self.label_nomes()
        self.label_cpfs()
        self.label_fomes()
        self.label_id()
        self.label_email1()
        self.label_uf1()
        self.label_estado1()
        self.labal_barrio1()
        self.funcao_treenv()
        self.btn()
       
    def titulo_tela(self):
        self.title(' CADASTRAMENTO DE PESSOAS') 

        self.geometry('1200x600+100+50')
        #self['bg'] = 'silver'
        self.config(highlightthickness=4)
        self.configure(highlightcolor='blue')

        frame = Frame(self)
        frame.pack(pady=3)

        frame02 = Frame(frame)
        frame02.configure(highlightbackground='red')
        frame02.configure(highlightthickness=4)
        frame02.pack()

        res = Label(frame02,text='CADASTRAMENTO')
        res.configure(fg='red')
        res.configure(width=90)
        res.configure(font= 'Helvetica 16 bold')
        res.configure(bg= '#ADD8E6')
        res.configure(bd=5)
        res.grid(row = 0, column= 0)

    def label_nomes(self):
        self.label_nome = Label(self,text= 'NOME')
        self.label_nome.configure(font= 'Helvetica 14 bold')
        self.label_nome.configure(bd=6)
        self.label_nome.configure(relief=GROOVE)
        self.label_nome.place(relx=0.01,rely=0.11)

        self.entry_nome = Entry(self,width=30)
        self.entry_nome.configure(font= 'Helvetica 14 bold')
        self.entry_nome.configure(bd=6)
        self.entry_nome.configure(relief=GROOVE)
        self.entry_nome.place(relx=0.07,rely=0.11)

    def label_cpfs(self):
        self.label_cpf = Label(self,text= 'CPF',padx=10)
        self.label_cpf.configure(font= 'Helvetica 14 bold')
        self.label_cpf.configure(bd=6)
        self.label_cpf.configure(relief=GROOVE)
        self.label_cpf.place(relx=0.01,rely=0.18)

        self.entry_cpf = Entry(self,width=30)
        self.entry_cpf.configure(font= 'Helvetica 14 bold')
        self.entry_cpf.configure(bd=6)
        self.entry_cpf.configure(relief=GROOVE)
        self.entry_cpf.place(relx=0.07,rely=0.18)

    def label_fomes(self):
        self.label_fome = Label(self,text= 'FOME')
        self.label_fome.configure(font= 'Helvetica 14 bold')
        self.label_fome.configure(bd=6)
        self.label_fome.configure(relief=GROOVE)
        self.label_fome.place(relx=0.01,rely=0.25)

        self.entry_fome = Entry(self,width=30)
        self.entry_fome.configure(font= 'Helvetica 14 bold')
        self.entry_fome.configure(bd=6)
        self.entry_fome.configure(relief=GROOVE)
        self.entry_fome.place(relx=0.07,rely=0.25)

    def label_id(self):
        self.label_ids = Label(self,text= 'ID',padx=20)
        self.label_ids.configure(font= 'Helvetica 14 bold')
        self.label_ids.configure(bd=6)
        self.label_ids.configure(relief=GROOVE)
        self.label_ids.place(relx=0.01,rely=0.32)

        self.entry_ids = Entry(self,width=30)
        self.entry_ids.configure(font= 'Helvetica 14 bold')
        self.entry_ids.configure(bd=6)
        self.entry_ids.configure(relief=GROOVE)
        self.entry_ids.place(relx=0.07,rely=0.32)

    def label_email1(self):
        self.label_email = Label(self,text= 'EMAIL',padx=7)
        self.label_email.configure(font= 'Helvetica 14 bold')
        self.label_email.configure(bd=6)
        self.label_email.configure(relief=GROOVE)
        self.label_email.place(relx=0.36,rely=0.11)

        self.entry_email = Entry(self,width=30)
        self.entry_email.configure(font= 'Helvetica 14 bold')
        self.entry_email.configure(bd=6)
        self.entry_email.configure(relief=GROOVE)
        self.entry_email.place(relx=0.43,rely=0.11)

    def label_uf1(self):
        self.label_uf = Label(self,text= 'UF',padx=24)
        self.label_uf.configure(font= 'Helvetica 14 bold')
        self.label_uf.configure(bd=6)
        self.label_uf.configure(relief=GROOVE)
        self.label_uf.place(relx=0.36,rely=0.18)

        self.entry_uf = Entry(self,width=30)
        self.entry_uf.configure(font= 'Helvetica 14 bold')
        self.entry_uf.configure(bd=6)
        self.entry_uf.configure(relief=GROOVE)
        self.entry_uf.place(relx=0.43,rely=0.18)

    def label_estado1(self):
        self.label_cidade = Label(self,text= 'CIDADE')
        self.label_cidade.configure(font= 'Helvetica 14 bold')
        self.label_cidade.configure(bd=6)
        self.label_cidade.configure(relief=GROOVE)
        self.label_cidade.place(relx=0.36,rely=0.25)

        self.entry_cidade = Entry(self,width=30)
        self.entry_cidade.configure(font= 'Helvetica 14 bold')
        self.entry_cidade.configure(bd=6)
        self.entry_cidade.configure(relief=GROOVE)
        self.entry_cidade.place(relx=0.43,rely=0.25)

    def labal_barrio1(self):
        self.label_barrio = Label(self,text= 'BARRIO')
        self.label_barrio.configure(font= 'Helvetica 14 bold')
        self.label_barrio.configure(bd=6)
        self.label_barrio.configure(relief=GROOVE)
        self.label_barrio.place(relx=0.36,rely=0.32)

        self.entry_barrio = Entry(self,width=30)
        self.entry_barrio.configure(font= 'Helvetica 14 bold')
        self.entry_barrio.configure(bd=6)
        self.entry_barrio.configure(relief=GROOVE)
        self.entry_barrio.place(relx=0.43,rely=0.32)


    def funcao_treenv(self):

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure('Treeview.Heading',background='yellow',
        rowheight=30,foreground='blue',font= 'Arial 12')

        self.style.map("Treeview",background=[('selected','green')])

        self.trien = ttk.Treeview(self)
        

        self.trien['columns'] ='nome','cpf','fome','indereco','email','uf','cidade','barrio'
        self.trien['show'] ='headings'


        self.trien.column('nome',minwidth=20,width=180)
        self.trien.column('cpf',minwidth=0,width=80)
        self.trien.column('fome',minwidth=0,width=100)
        self.trien.column('indereco',minwidth=0,width=150)
        self.trien.column('email',minwidth=0,width=165)
        self.trien.column('uf',minwidth=0,width=80)
        self.trien.column('cidade',minwidth=0,width=150)
        self.trien.column('barrio',minwidth=0,width=150)
        
        self.trien.heading('nome',text='nome')
        self.trien.heading('cpf',text='cpf')
        self.trien.heading('fome',text='fome')
        self.trien.heading('indereco',text='endereço')
        self.trien.heading('email',text='email')
        self.trien.heading('uf',text='uf')
        self.trien.heading('cidade',text='cidade')
        self.trien.heading('barrio',text='barrio')

        self.trien.place(relx=0.0,rely=0.40,relwidth=0.98,relheight=0.50)
        
        self.va = ttk.Scrollbar(self)
        self.trien.configure(yscrollcommand=self.va.set)
        self.va.place(relx=0.98,rely=0.40,relwidth=0.02,relheight=0.5)

        self.va.config(command=self.trien.yview)

        va = sorted(lista_nome())
        
        self.trien.tag_configure('primeiro',background='#00BFFF')
        self.trien.tag_configure('segundo',background='#87CEEB')

        cont = 0
        for nome in va:
            if cont % 2 == 0:
                self.trien.insert('','end',values=(nome[0],nome[1],nome[2],nome[3],nome[4],nome[5],nome[6],nome[7]),tags=('primeiro'))
            else:
                self.trien.insert('','end',values=(nome[0],nome[1],nome[2],nome[3],nome[4],nome[5],nome[6],nome[7]),tags=('segundo'))
            cont += 1
        
    def btn(self):
        self.botao = Button(self,text='INSERIR',command=self.funcao)
        self.botao.configure(width=20)
        self.botao.configure(bg='green')
        self.botao.configure(fg='white')
        self.botao.configure(bd=4)
        self.botao.configure(font='Calibri 15 bold')
        self.botao.place(relx=0.01,rely=0.91)

        self.sair = Button(self,text='SAIR',command=self.quit)
        self.sair.configure(width=20)
        self.sair.configure(bg='green')
        self.sair.configure(fg='white')
        self.sair.configure(bd=4)
        self.sair.configure(font='Calibri 15 bold')
        self.sair.place(relx=0.20,rely=0.91)

        self.deleta = Button(self,text='DELETA',command=self.deleta_item)
        self.deleta.configure(width=20)
        self.deleta.configure(bg='green')
        self.deleta.configure(fg='white')
        self.deleta.configure(bd=4)
        self.deleta.configure(font='Calibri 15 bold')
        self.deleta.place(relx=0.39,rely=0.91)

        self.pes = Button(self,text='PESQUISA',command=self.procura)
        self.pes.configure(width=10)
        self.pes.configure(bg='green')
        self.pes.configure(fg='white')
        self.pes.configure(bd=4)
        self.pes.configure(font='Calibri 15 bold')
        self.pes.place(relx=0.58,rely=0.91)

        self.pesquisa = Entry(self)
        self.pesquisa.configure(width=25)
        self.pesquisa.configure(bd=4)
        self.pesquisa.configure(font='Calibri 20 bold')
        self.pesquisa.place(relx=0.68,rely=0.91)

        self.pes = Button(self,text='INICIO',command=self.funcao_treenv)
        self.pes.configure(width=10)
        self.pes.configure(bg='green')
        self.pes.configure(fg='white')
        self.pes.configure(bd=4)
        self.pes.configure(font='Calibri 15 bold')
        self.pes.place(relx=0.80,rely=0.20)


    def funcao(self):
        if self.entry_nome.get() != '' and self.entry_cpf.get() != '' and self.entry_fome.get() != '' and self.entry_ids.get() != '' and self.entry_email.get() != '' and self.entry_uf.get() != '' and self.entry_cidade.get() != '' and self.entry_barrio.get() != '':
            
            inserirdados(self.entry_nome.get().strip().title(),self.entry_cpf.get().strip(),
            self.entry_fome.get().strip(),self.entry_ids.get().strip().title(),self.entry_email.get().strip(),
            self.entry_uf.get().strip().title(),self.entry_cidade.get().strip().title(),self.entry_barrio.get().strip().title())

            self.funcao_treenv()

            self.entry_nome.delete(0,END)
            self.entry_cpf.delete(0,END)
            self.entry_fome.delete(0,END)
            self.entry_ids.delete(0,END)
            self.entry_email.delete(0,END)
            self.entry_uf.delete(0,END)
            self.entry_cidade.delete(0,END)
            self.entry_barrio.delete(0,END)

        else:
            res = messagebox.showerror('ERRO !','Peencha o Espoço')
        

    def procura(self):
        if self.pesquisa.get() != '':
            x  = self.trien.get_children()
            for item in x:
                self.trien.delete(item)

            for (nome,cpf,fome,indereco,email,uf,cidade,barrio) in lista_nome():
                if nome[0] in str(self.pesquisa.get()).title():
                    self.trien.insert('','end',values=(nome,cpf,fome,indereco,email,uf,cidade,barrio))
            
        self.pesquisa.delete(0,END)  

    def deleta_item(self):
        try:
            apaga = self.trien.selection()[0]
            ite = self.trien.item(apaga,'values')
            deleta_nome(ite[0])
            self.funcao_treenv()
        except :
            messagebox.showinfo('ERRO!','SELECIONE UM ITEM')
    


if __name__== "__main__":
    root = ProjetoCadastro()
    root['bg'] = 'navy'
    root.iconbitmap('usuario.ico')
    root.attributes('-fullscreen',True)
    root.overrideredirect(True)
    root.mainloop()

