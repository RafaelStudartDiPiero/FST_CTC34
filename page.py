from tkinter import *
from fst.fst import auto_complete_fst, read_fst
from levenshtein.levenshtein import SparseLevenshteinAutomaton

class SisBanco:
    def __init__(self, master = None):
        self.fst = read_fst()
        self.comandos = []
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()

        self.titulo = Label(self.container1, text=f'CTC-34')
        self.titulo["font"]= ("Calibri", "9", "bold")
        self.titulo.pack(side=LEFT)       

        self.lblpalavra = Label(self.container2, text=f'digite uma palavra:')
        self.lblpalavra["font"]= ("Calibri", "9", "bold")
        self.lblpalavra.pack(side=LEFT)         

        self.v = StringVar()
        self.v.trace('w', self.autocomplete) 
        self.txtpalavra= Entry(self.container2, textvariable=self.v)
        self.txtpalavra["width"] = 10
        self.txtpalavra["font"] = self.fonte
        self.txtpalavra.pack(side="top")
        # self.txtpalavra.bind("<Key>", lambda x: self.autocomplete(x))


        self.lblautocomplete = Label(self.container3, text="Autocomplete:", font=self.fonte, width = 15)
        self.lblautocomplete.pack(side=LEFT)
        
        self.lblcomplete1 = Label(self.container4, font=self.fonte, width = 15)
        self.lblcomplete1.pack()

        self.lblcomplete2 = Label(self.container5, font=self.fonte, width = 15)
        self.lblcomplete2.pack()

        self.lblcomplete3 = Label(self.container6, font=self.fonte, width = 15)
        self.lblcomplete3.pack()

        self.lblcomplete4 = Label(self.container7, font=self.fonte, width = 15)
        self.lblcomplete4.pack()

        self.lblcomplete5 = Label(self.container8, font=self.fonte, width = 15)
        self.lblcomplete5.pack()

    def autocomplete(self, *args):
        self.lblcomplete1["text"] = ""
        self.lblcomplete2["text"] = ""
        self.lblcomplete3["text"] = ""
        self.lblcomplete4["text"] = ""
        self.lblcomplete5["text"] = ""

        input = self.txtpalavra.get()
        lista = auto_complete_fst(input, self.fst)
        if lista == "Não existe":
            return
        automaton = SparseLevenshteinAutomaton(input)
        if len(lista)>0:
            if automaton.read_input(lista[0]):
                 self.lblcomplete1.config(fg= "red")
            self.lblcomplete1["text"] = lista[0]
        if len(lista)>1:
            if automaton.read_input(lista[1]):
                 self.lblcomplete2.config(fg= "red")
            self.lblcomplete2["text"] = lista[1]
        if len(lista)>2:
            if automaton.read_input(lista[2]):
                 self.lblcomplete3.config(fg= "red")
            self.lblcomplete3["text"] = lista[2]
        if len(lista)>3:
            if automaton.read_input(lista[3]):
                 self.lblcomplete4.config(fg= "red")
            self.lblcomplete4["text"] = lista[3]
        if len(lista)>4:
            if automaton.read_input(lista[4]):
                 self.lblcomplete5.config(fg= "red")
            self.lblcomplete5["text"] = lista[4]

        # while i<5 and i<len(lista):
        #     locals()["self.lblcomplete" + str(i+1)]["text"] = lista[i]
        #     i+=1
            

    # def VerificarSaldo(self):
    #     verifica = Command.VerificarSaldo(self.cliente)
    #     saldo_cliente = verifica.execute()
    #     self.txtsaldo.delete(0, END)
    #     self.txtsaldo.insert(INSERT, saldo_cliente)
    #     self.comandos.append("Verificou o saldo")
    #     self.MostrarHistorico()
    #     self.lblextrato1["text"] = ""
    #     self.lblextrato2["text"] = ""

    # def Transferir(self):

    #     valor = self.txttransferencia.get()
    #     transfere = Command.Transferir(self.cliente, valor)
    #     transfere.execute()

    #     self.txttransferencia.delete(0, END)
    #     self.comandos.append(f'transferiu {valor} reais')
    #     self.MostrarHistorico()
    #     self.lblextrato1["text"] = ""
    #     self.lblextrato2["text"] = ""
    #     self.txtsaldo.delete(0, END)

    # def Receber(self):

    #     valor = self.txtreceber.get()
    #     recebe = Command.Receber(self.cliente, valor)
    #     recebe.execute()


    #     self.txtreceber.delete(0, END)
    #     self.comandos.append(f'recebeu {valor} reais')
    #     self.MostrarHistorico()
    #     self.lblextrato1["text"] = ""
    #     self.lblextrato2["text"] = ""
    #     self.txtsaldo.delete(0, END)

    

    # def MostrarHistorico(self):
    #     self.lblhistorico1["text"] = "Historico:"

    #     if len(self.comandos)-3 >= 0:
    #         self.lblhistorico4["text"] =self.comandos[len(self.comandos)-3]

    #     if len(self.comandos)-2 >= 0:
    #         self.lblhistorico3["text"] =self.comandos[len(self.comandos)-2]

    #     if len(self.comandos)-1 >= 0:
    #         self.lblhistorico2["text"] =self.comandos[len(self.comandos)-1]


root = Tk()
SisBanco(root)
root.mainloop()