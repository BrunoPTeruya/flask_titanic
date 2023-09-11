# __init__.py
from flask import Flask
import pickle
from utils.titanic_util import Tratar_Entrada_Api
from waitress import serve

app = Flask(__name__)

with open('models/modelo_DecisionTree.pkl', 'rb') as arquivo:
    modelo_arvore = pickle.load(arquivo)

from . import app