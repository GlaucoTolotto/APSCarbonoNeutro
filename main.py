import tkinter as tk
from tkinter import messagebox

def calcular_emissoes_co2(tipo_combustivel, consumo_especifico, energia_gerada):
    # Consulta a um dicionário para obter o fator de emissão (valores aproximados)
    fatores_emissao = {
        'diesel': 270,
        'gasolina': 235,
        # Adicione outros combustíveis conforme necessário
    }

    if tipo_combustivel not in fatores_emissao:
        raise ValueError("Tipo de combustível não encontrado.")

    fator_emissao = fatores_emissao[tipo_combustivel]

    # Cálculo da massa de combustível consumida
    massa_combustivel = consumo_especifico * energia_gerada / 1000  # Convertendo para kg

    # Cálculo das emissões de CO2
    emissoes_co2 = massa_combustivel * fator_emissao

    return emissoes_co2

def calcular_creditos_carbono(geracao_solar):
    eficiencia_paineis = 0.8
    # Energia economizada (considerando a eficiência dos painéis)
    energia_economizada = geracao_solar * eficiencia_paineis

    fator_emissao = calcular_emissoes_co2('diesel',(250 * 10), 100000)
    # Redução de emissões
    reducao_emissoes = energia_economizada * fator_emissao

    return reducao_emissoes

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
        resultado_label.config(text=f"Número de placas solares necessárias: {numero_placas:.2f}\n A quantidade de credito gerado foi: {calcular_creditos_carbono(consumo_mensal):.2f}")
    
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

#Label para mostrar o resultado de quantidade de placas
resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=2, columnspan=2, pady=5)

#Inicia a aplicação
root.mainloop()
