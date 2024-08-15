import tkinter as tk
from tkinter import messagebox

#Função para calcular o número de placas solares necessárias
def calcular_placas():
    try:
        #Obtém o consumo mensal de energia do campo de entrada
        consumo_mensal = float(entry_consumo.get())

        #Produção média mensal de uma placa solar (em kWh)
        producao_placa_mensal = 300  # Ajuste esse valor conforme necessário

        #Calcula o número de placas solares necessárias
        if producao_placa_mensal == 0:
            messagebox.showerror("Erro", "A produção média de uma placa solar não pode ser zero.")
            return
        #Contagem de numeros de placas solares e produção
        numero_placas = consumo_mensal / producao_placa_mensal

        #Exibe o resultado
        resultado_label.config(text=f"Número de placas solares necessárias: {numero_placas:.2f}")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido para o consumo mensal.")

#Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Placas Solares")

#Configuração do layout
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

#Campo para o consumo mensal de energia
tk.Label(frame, text="Consumo mensal de energia (kWh):").grid(row=0, column=0, padx=5, pady=5)
entry_consumo = tk.Entry(frame)
entry_consumo.grid(row=0, column=1, padx=5, pady=5)

#Botão para calcular
calcular_button = tk.Button(frame, text="Calcular", command=calcular_placas)
calcular_button.grid(row=1, columnspan=2, pady=10)

#Label para mostrar o resultado
resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=2, columnspan=2, pady=5)

print(resultado_label)

#Inicia a aplicação
root.mainloop()
