import customtkinter as ctk
import csv
import os

ARQUIVO_CSV = 'pacientes.csv'

CAMPOS = [
    'Nome', 'RG', 'CPF', 'CNS', 'Moradia', 'Contato',
    'Unidade de Saúde', 'Problemas de Saúde', 'Medicações em Uso',
    'Sinais Vitais', 'Odontologia', 'Conduta Médica', 'Outras Demandas'
]

def salvar_pacientes_csv(lista):
    with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        writer.writeheader()
        for paciente in lista:
            paciente['Sinais Vitais'] = str(paciente['Sinais Vitais'])
            writer.writerow(paciente)

def carregar_pacientes_csv():
    pacientes = []
    if os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as arquivo:
            reader = csv.DictReader(arquivo)
            for linha in reader:
                linha['Sinais Vitais'] = eval(linha['Sinais Vitais'])
                pacientes.append(linha)
    return pacientes

# Interface gráfica
def janelaProntuario(app):
    for widget in app.winfo_children():
        widget.destroy()

    # Centro da tela
    frame = ctk.CTkFrame(app)
    frame.pack(pady=20, expand=True)

    ctk.CTkLabel(frame, text='Cadastrar Paciente', font=('Times New Roman', 30)).pack(pady=15)

    entradas = {}

    def criar_entrada(nome, placeholder):
        entradas[nome] = ctk.CTkEntry(frame, placeholder_text=placeholder, width=400)
        entradas[nome].pack(pady=5)

    criar_entrada('Nome', 'Nome completo')
    criar_entrada('RG', 'RG')
    criar_entrada('CPF', 'CPF')
    criar_entrada('CNS', 'CNS')
    criar_entrada('Moradia', 'Endereço ou situação de moradia')
    criar_entrada('Contato', 'Telefone ou outro contato')
    criar_entrada('Unidade de Saúde', 'Unidade de Saúde')
    criar_entrada('Problemas de Saúde', 'Problemas de Saúde')
    criar_entrada('Medicações em Uso', 'Medicações em Uso')

    # Sinais vitais em linha
    sinais_frame = ctk.CTkFrame(frame)
    sinais_frame.pack(pady=10)
    sinais = {}
    for sinal in ['PA', 'FC', 'SAT', 'DEXTRO']:
        sinais[sinal] = ctk.CTkEntry(sinais_frame, placeholder_text=sinal, width=90)
        sinais[sinal].pack(side='left', padx=5)

    criar_entrada('Odontologia', 'Odontologia')
    criar_entrada('Conduta Médica', 'Conduta Médica')
    criar_entrada('Outras Demandas', 'Outras Demandas')

    def salvar():
        paciente = {campo: entradas[campo].get() for campo in entradas}
        paciente['Sinais Vitais'] = {k: sinais[k].get() for k in sinais}
        pacientes = carregar_pacientes_csv()
        pacientes.append(paciente)
        salvar_pacientes_csv(pacientes)
        ctk.CTkLabel(frame, text='Paciente salvo!', text_color='green').pack(pady=5)

    ctk.CTkButton(frame, text='Salvar', command=salvar, fg_color='#007acc').pack(pady=10)
    ctk.CTkButton(frame, text='Ver Pacientes no Terminal', command=lambda: mostrar_pacientes_terminal(), fg_color='#444').pack()

def mostrar_pacientes_terminal():
    pacientes = carregar_pacientes_csv()
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for i, paciente in enumerate(pacientes, start=1):
            print(f"\nPaciente {i}:")
            for chave, valor in paciente.items():
                print(f"{chave}: {valor}")

if __name__ == '__main__':
    ctk.set_appearance_mode('dark')
    app = ctk.CTk()
    app.geometry('800x700')
    app.title('Prontuário de Pacientes')

    janelaProntuario(app)
    app.mainloop()
