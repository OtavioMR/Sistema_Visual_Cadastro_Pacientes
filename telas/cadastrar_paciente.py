import customtkinter as ctk

def janelaProntuario(app):
    for widget in app.winfo_children():
        widget.destroy()

    prontuario_sair = ctk.CTkButton(
    app,
    text='Menu',
    font=('Times New Roman', 50)
    )

      
    prontuario_sair.pack(pady=30)

