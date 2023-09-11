import tkinter as tk
import requests
import json

# Função para enviar uma solicitação à API
def fazer_previsao():
    # Capturar os valores dos campos de entrada
    Title = title_entry.get()
    Age = age_entry.get()
    pclass = pclass_entry.get()

    # Criar um dicionário com os dados de entrada
    dados_entrada = {
        'Title': Title,
        'Age': Age,
        'Pclass': pclass
    }

    # Enviar a solicitação POST para a API
    try:
        resposta = requests.post('http://127.0.0.1:5000/prever', json=dados_entrada)

        if resposta: # testando respostas
            resultado_label.config(text=resposta.text)
            #resultado_label.config(resposta.headers)
            #resultado_label.config(text=dados_entrada)
        else:
            resultado_label.config(text='Response Failed')
        resposta_json = resposta.json()
        texto = resposta_json['previsao']
        if(texto.len() == 0):
            texto = resposta_json['erro']

        # Exibir a previsão na interface
        #resultado_label.config(text=f'Previsão: {previsao[0]}')
        #resultado_label.config('Belo')
        #resultado_label.config(text=f'Previsão: {texto[0]}')
    except Exception as e:
        resultado_label.config(text=f'Erro: 1 {str(e)}')
    

# Configurar a janela da interface
janela = tk.Tk()
janela.title('Interface de Previsão')

# Criar campos de entrada para title, Age e Pclass
title_label = tk.Label(janela, text='title:')
title_label.pack()
title_entry = tk.Entry(janela)
title_entry.pack()

age_label = tk.Label(janela, text='Age:')
age_label.pack()
age_entry = tk.Entry(janela)
age_entry.pack()

pclass_label = tk.Label(janela, text='Pclass:')
pclass_label.pack()
pclass_entry = tk.Entry(janela)
pclass_entry.pack()

# Botão para fazer a previsão
prever_button = tk.Button(janela, text='Prever', command=fazer_previsao)
prever_button.pack()

# Rótulo para exibir a previsão
resultado_label = tk.Label(janela, text='')
resultado_label.pack()

# Iniciar a interface
janela.mainloop()