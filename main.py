import customtkinter as ctk
from telas import cadastrar_paciente

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Menu Prontuário')
app.geometry('700x500')

def menu_inicial():
    menu_titulo = ctk.CTkLabel(
        app,
        text='Menu',
        font=('Times New Roman', 50)
    )
    menu_titulo.pack(pady=30)

    # Frame principal para agrupar os pares de número + botão
    frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
    frame_botoes.pack(pady=20)

    # Linha 1: Label "1." + Botão cadastrar
    linha1 = ctk.CTkFrame(frame_botoes, fg_color="transparent")
    linha1.pack(pady=10)

    label1 = ctk.CTkLabel(linha1, text='1.', width=30, anchor='w')
    label1.pack(side='left')

    botao_cadastrar = ctk.CTkButton(
        linha1,
        text='Cadastrar novo paciente',
        fg_color='#0047ff',
        hover_color='#0033cc',
        width=200,
        anchor='w',
        command=lambda: cadastrar_paciente.janelaProntuario(app)
    )


    botao_cadastrar.pack(side='left')

    # Linha 2: Label "2." + Botão ver prontuário
    linha2 = ctk.CTkFrame(frame_botoes, fg_color="transparent")
    linha2.pack(pady=10)

    label2 = ctk.CTkLabel(linha2, text='2.', width=30, anchor='w')
    label2.pack(side='left')

    botao_ver_prontuario = ctk.CTkButton(
        linha2,
        text='Ver prontuários',
        fg_color='#0047ff',
        hover_color='#0033cc',
        width=200,
        anchor='w'
    )
    botao_ver_prontuario.pack(side='left')

    # Linha 3: Label "3." + Botão Sair
    linha3 = ctk.CTkFrame(frame_botoes, fg_color="transparent")
    linha3.pack(pady=10)

    label3 = ctk.CTkLabel(linha3, text='2.', width=30, anchor='w')
    label3.pack(side='left')

    botao_sair = ctk.CTkButton(
        linha3,
        text='Sair',
        fg_color='#0047ff',
        hover_color='#0033cc',
        width=200,
        anchor='w'
    )
    botao_sair.pack(side='left')
    

menu_inicial()
app.mainloop()
