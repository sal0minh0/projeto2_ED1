import sys
import os

# Adicionando o diretório "Restaurante" ao caminho de busca de módulos do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Estruturas import Pilha, Fila, ArvoreBinaria

class Restaurante:
    