import tkinter as tk

def criar_interface():
    def limpar_display():
        campo_display.delete(0, tk.END)
        campo_display.focus()

    def deletar_ultimo():
        pos = campo_display.index(tk.INSERT)
        if pos > 0:
            campo_display.delete(pos - 1, pos)
        campo_display.focus()

    def adicionar_caractere(caractere):
        pos = campo_display.index(tk.INSERT)
        campo_display.insert(pos, str(caractere))
        campo_display.focus()

    def adicionar_parenteses():
        pos = campo_display.index(tk.INSERT)
        campo_display.insert(pos, "()")
        campo_display.icursor(pos + 1)
        campo_display.focus()

    def calcular():
        try:
            exp = campo_display.get().replace(',', '.')
            resultado = str(eval(exp))
            if resultado.endswith('.0'):
                resultado = resultado[:-2]
            
            campo_display.delete(0, tk.END)
            campo_display.insert(0, resultado.replace('.', ','))
        except:
            campo_display.delete(0, tk.END)
            campo_display.insert(0, "Erro")
        campo_display.focus()

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

    campo_display = tk.Entry(
        janela, font=('Helvetica', 42),
        bg=COR_FUNDO, fg=COR_TEXTO_NUM, bd=0, justify='right',
        insertbackground=COR_VERDE_NEON
    )
    campo_display.pack(pady=(60, 30), padx=25, fill='x')
    campo_display.focus()

    frame_corpo = tk.Frame(janela, bg=COR_FUNDO)
    frame_corpo.pack(expand=True, fill='both', padx=15, pady=(0, 20))
    
    botoes_layout = [
        ('C', 0, 0, 1), ('«', 0, 1, 1), ('()', 0, 2, 1), ('/', 0, 3, 1),
        ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('*', 1, 3, 1),
        ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('-', 2, 3, 1),
        ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('+', 3, 3, 1),
        ('0', 4, 0, 2), (',', 4, 2, 1), ('=', 4, 3, 1)
    ]

    def criar_comando(valor):
        if valor == 'C': return limpar_display
        if valor == '«': return deletar_ultimo
        if valor == '()': return adicionar_parenteses
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
            elif texto in ['/', '*', '-', '+', '()', '«']:
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