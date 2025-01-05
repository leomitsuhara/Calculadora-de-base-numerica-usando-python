from tkinter import *
from tkinter import ttk

# cores
co0 = "#444466"  # preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e89613"  # laranja

janela = Tk()
janela.title('Conversor de Base Numérica')
janela.geometry('400x310')
janela.configure(bg=co1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

# dividindo a janela em dois frames

frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0)  
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0)

# configurando frame cima
app_nome = Label(frame_cima, text="Conversor de Base Numérica", relief=FLAT, anchor='center', font=('System 20'), bg=co2, fg=co1)
app_nome.place(x=10, y=15)

# configurando frame baixo

bases = ['BINÁRIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x=35, y= 10)

e_valor = Entry(frame_baixo, width=9, justify='center', font=("",13), highlightthickness=1, relief='solid')
e_valor.place(x=160, y=10)

# Resultado
resultado = Label(frame_baixo, text="Resultado", font=('Ivy 14 bold'), bg=co1, fg=co4)
resultado.place(x=35, y=100)

# Função para conversão
def converter():
    valor = e_valor.get()
    base = combo.get()

    if base == 'BINÁRIO':
        try:
            resultado['text'] = f"Decimal: {int(valor, 2)}\nOctal: {oct(int(valor, 2))[2:]}\nHexadecimal: {hex(int(valor, 2))[2:].upper()}"
        except ValueError:
            resultado['text'] = "Valor Inválido"
    elif base == 'OCTAL':
        try:
            resultado['text'] = f"Binário: {bin(int(valor, 8))[2:]}\nDecimal: {int(valor, 8)}\nHexadecimal: {hex(int(valor, 8))[2:].upper()}"
        except ValueError:
            resultado['text'] = "Valor Inválido"
    elif base == 'DECIMAL':
        try:
            resultado['text'] = f"Binário: {bin(int(valor))[2:]}\nOctal: {oct(int(valor))[2:]}\nHexadecimal: {hex(int(valor))[2:].upper()}"
        except ValueError:
            resultado['text'] = "Valor Inválido"
    elif base == 'HEXADECIMAL':
        try:
            resultado['text'] = f"Binário: {bin(int(valor, 16))[2:]}\nOctal: {oct(int(valor, 16))[2:]}\nDecimal: {int(valor, 16)}"
        except ValueError:
            resultado['text'] = "Valor Inválido"

# Botão para realizar a conversão
botao_converter = Button(frame_baixo, text="Converter", font=("Ivy 12 bold"), bg=co5, fg=co1, command=converter)
botao_converter.place(x=160, y=50)

janela.mainloop()

