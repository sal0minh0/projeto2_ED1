import sys
import os

# Adicionando o diretorio "Eventos" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Estruturas import Pilha, Fila, ArvoreBinaria

class Evento:
    