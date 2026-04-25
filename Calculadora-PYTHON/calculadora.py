import tkinter as tk

def criar_interface():
    global expressao_atual
    expressao_atual = ""

    def limpar_display():
        global expressao_atual
        expressao_atual = ""
        texto_display.set("")

    def deletar_ultimo():
        global expressao_atual
        expressao_atual = expressao_atual[:-1]
        texto_display.set(expressao_atual)

    def adicionar_caractere(caractere):
        global expressao_atual
        if caractere == '%':
            expressao_atual += '/100'
        else:
            expressao_atual += str(caractere)
        texto_display.set(expressao_atual)

    def calcular():
        global expressao_atual
        try:
            exp = expressao_atual.replace(',', '.')
            resultado = str(eval(exp))
            if resultado.endswith('.0'):
                resultado = resultado[:-2]
            texto_display.set(resultado.replace('.', ','))
            expressao_atual = resultado
        except:
            texto_display.set("Erro")
            expressao_atual = ""

    # --- Cores ---
    COR_FUNDO = "#000000"        
    COR_BOTAO_PADRAO = "#1A1A1A" 
    COR_VERDE_NEON = "#00FF7F"   
    COR_TEXTO_NUM = "#FFFFFF"    
    COR_C = "#FF3030"            

    janela = tk.Tk()
    janela.title("Calculadora Pro Green")
    janela.geometry("380x600")
    janela.configure(bg=COR_FUNDO)
    janela.resizable(False, False)

    texto_display = tk.StringVar()

    # --- Visor ---
    campo_display = tk.Entry(
        janela, textvariable=texto_display, font=('Helvetica', 48),
        bg=COR_FUNDO, fg=COR_TEXTO_NUM, bd=0, justify='right',
        state='readonly', readonlybackground=COR_FUNDO
    )
    campo_display.pack(pady=(60, 30), padx=25, fill='x')

    frame_corpo = tk.Frame(janela, bg=COR_FUNDO)
    frame_corpo.pack(expand=True, fill='both', padx=15, pady=(0, 20))
    
    botoes_layout = [
        ('C', 0, 0, 1), ('«', 0, 1, 1), ('%', 0, 2, 1), ('/', 0, 3, 1),
        ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('*', 1, 3, 1),
        ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('-', 2, 3, 1),
        ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('+', 3, 3, 1),
        ('0', 4, 0, 2), (',', 4, 2, 1), ('=', 4, 3, 1)
    ]

    def criar_comando(valor):
        if valor == 'C': return limpar_display
        if valor == '«': return deletar_ultimo
        if valor == '=': return calcular
        return lambda: adicionar_caractere(valor)

    for (texto, l, c, span) in botoes_layout:
        if texto == '=':
            bg_color = COR_VERDE_NEON
            fg_color = "#000000"
        else:
            bg_color = COR_BOTAO_PADRAO
            if texto == 'C':
                fg_color = COR_C
            elif texto in ['/', '*', '-', '+', '%', '«']:
                fg_color = COR_VERDE_NEON
            else:
                fg_color = COR_TEXTO_NUM

        btn = tk.Button(
            frame_corpo, text=texto, font=('Helvetica', 18, 'bold'),
            bg=bg_color, fg=fg_color, bd=0, cursor="hand2",
            activebackground="#333333", command=criar_comando(texto)
        )
        btn.grid(row=l, column=c, columnspan=span, sticky="nsew", padx=4, pady=4)

    for i in range(4):
        frame_corpo.grid_columnconfigure(i, weight=1)
    for i in range(5):
        frame_corpo.grid_rowconfigure(i, weight=1)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()