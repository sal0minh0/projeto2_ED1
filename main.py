import sys
import os

# Adicionar diretorio Pai para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Clinica.clinica import HistoricoPacientes, GerenciadorEmergencia, CadastroMedicos
from Eventos.evento import HistoricoEventos, FilaDeEventos, ArvoreParticipantes
from Restaurante.restaurante import Pedido, FilaPedidos, GerenciadorMenu

class Main:
    def __init__(self):
        # Clinica
        self.paciente = HistoricoPacientes()
        self.emergencia = GerenciadorEmergencia()
        self.medico = CadastroMedicos()
        # Eventos
        self.historico = HistoricoEventos()
        self.eventos = FilaDeEventos()
        self.participantes = ArvoreParticipantes()
        # Restaurante
        self.pedido = Pedido()
        self.fila_de_pedidos = FilaPedidos()
        self.menu = GerenciadorMenu()
        