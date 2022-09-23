from msilib.schema import ComboBox
from optparse import Values
import tkinter as tk
import datetime as dt
from tkinter import NSEW, mainloop, ttk

lista_tipos=["Galão","Caixas","Saco","Unidade"]
lista_codigos=[]

janela=tk.Tk()

#criação da função

def inserir_codigo():
    descricao=entry_descricao.get()
    tipo=combobox_selecionar_tipo.get()
    quantidade=entry_quant.get()
    data_criacao=dt.datetime.now()
    data_criacao=data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo=len(lista_codigos)+1
    codigo_str="COD-{}".format(codigo)
    lista_codigos.append((codigo_str,descricao,tipo,quantidade,data_criacao))

#titulo da janela
janela.title("Ferramenta de cadastro de materiais")

label_descricao = tk.Label(text="descrição do material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao= tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text='Tipo da unidade do material')
label_tipo_unidade.grid(row=3,column=0,padx=10,pady=10,sticky='nswe', columnspan=2)

combobox_selecionar_tipo= ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nwse', columnspan=2)

label_quant=tk.Label(text="Quantidade na unidade do material:")
label_quant.grid(row=4,column=0,padx=10,pady=10,sticky='nswe', columnspan=2)

entry_quant=tk.Entry()
entry_quant.grid(row=4,column=2,padx=10,pady=10,sticky='nswe', columnspan=2)

botao_criar_codigo=tk.Button(text="Criar Código", command=inserir_codigo)
botao_criar_codigo.grid(row=5,column=0,padx=10,pady=10,sticky='nswe', columnspan=4)

print(lista_codigos)

janela.mainloop()