import os
import pickle
from utils.titanic_util import Tratar_Entrada_Api
from waitress import serve
from flask import Flask, request, jsonify, render_template


# Criar uma instância do Flask
app = Flask(__name__)

# Carregar o modelo de árvore de decisão previamente treinado
with open('models/modelo_DecisionTree.pkl', 'rb') as arquivo:
    modelo_arvore = pickle.load(arquivo)

# Teste de conexão Get com o endpoint
@app.route('/teste_conexao', methods=['GET'])
def teste_conexao():
    return jsonify({'mensagem': 'Conexão bem-sucedida!'}), 200

#Conexão Post
@app.route('/prever', methods=['POST', 'GET'])
def prever():
    try:
        dados_entrada = request.form # atua como um meio de capturar os dados enviados através do formulário HTML

        # Verificando se temos as variáveis
        campos_necessarios = ["Title", "Pclass", "Sex", "Age", "Fare", "Embarked", "IsAlone"]
        for campo in campos_necessarios:
            if campo not in dados_entrada:
                return jsonify({'erro': f'Precisa conter {campo}'}), 400

        # Usando função para tratar os dados como foram tratados no notebook        
        dados_tratados = Tratar_Entrada_Api(dados_entrada)

        # Aplicando modelo
        previsao = modelo_arvore.predict(dados_tratados)
        resposta = 'Sobreviveu' if previsao[0] == 1 else 'Morreu'

        return render_template('template.html', resposta=resposta)

    except Exception as e:
        return str(e), 500

# Renderizar o template HTML
@app.route('/')
def home():
    return render_template('template.html')

# Iniciar o flask
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)