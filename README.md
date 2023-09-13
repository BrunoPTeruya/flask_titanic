# Projeto Flask

Este é o repositório para o meu projeto Flask. A estrutura do projeto está organizada da seguinte forma:
```
C:.
│ app.py                  - Arquivo principal da aplicação, onde são definidas as rotas e inicializada a aplicação Flask.
│ README.md               - Este arquivo, que contém uma descrição da estrutura do projeto.
│ requirements.txt        - Arquivo que lista todas as dependências necessárias para rodar a aplicação.
│ startup.py              - Script executado na inicialização da aplicação, contendo configurações iniciais.
│ init.py                 - Arquivo para tratar o diretório como um pacote Python, facilitando os imports.
│
├───models
│ modelo_DecisionTree.pkl - Arquivo que contém o modelo de árvore de decisão pré-treinado, usado para fazer previsões na aplicação.
│
├───templates
│ template.html          - Template HTML usado para renderizar a interface de usuário da aplicação.
│
└───utils
titanic_util.py          - Arquivo contendo funções auxiliares e utilitárias usadas em toda a aplicação.
```

## Instruções para Instalação

1. Clone este repositório.
2. Navegue até o diretório do projeto.
3. Instale as dependências usando o comando: `pip install -r requirements.txt`.
4. Execute o arquivo `startup.py` para configurar o ambiente: `python startup.py`.
5. Inicie a aplicação com o comando: `python app.py`.

Agora, a aplicação deve estar rodando e você pode acessá-la através do seu navegador de internet no endereço: `http://localhost:5000`.
