import customtkinter as ctk

def janelaProntuario(app):
    # Limpar widgets existentes da janela
    for widget in app.winfo_children():
        widget.destroy()

    # Título da tela
    titulo = ctk.CTkLabel(
        app,
        text='Cadastrar Paciente',
        font=('Times New Roman', 40)
    )
    titulo.pack(pady=20)

    # Campo: Nome
    entrada_nome = ctk.CTkEntry(app, placeholder_text='Nome do paciente', width=300)
    entrada_nome.pack(pady=10)

    # Campo: Idade
    entrada_idade = ctk.CTkEntry(app, placeholder_text='Idade', width=300)
    entrada_idade.pack(pady=10)

    # Botão: Salvar
    botao_salvar = ctk.CTkButton(app, text='Salvar', fg_color='#007acc')
    botao_salvar.pack(pady=20)

    # Botão: Voltar ao menu
    botao_voltar = ctk.CTkButton(app, text='Voltar ao Menu', fg_color='#444',
                                  command=lambda: voltar_menu(app))
    botao_voltar.pack(pady=10)

def voltar_menu(app):
    from main import menu_inicial  # ajuste o nome do seu arquivo principal se não for "main.py"
    menu_inicial()
    

if __name__ == "__main__":
    import customtkinter as ctk

    ctk.set_appearance_mode('dark')
    app = ctk.CTk()
    app.title('Teste - Prontuário')
    app.geometry('700x500')

    janelaProntuario(app)

    app.mainloop()
