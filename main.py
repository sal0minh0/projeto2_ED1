import sys
import os

# Adicionar diretorio Pai para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Clinica import HistoricoPacientes, GerenciadorEmergencia, CadastroMedicos
from Eventos import HistoricoEventos, FilaDeEventos, ArvoreParticipantes
from Restaurante import Pedido, 

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
        
    def run(self):
        self.janela_principal.mainloop()

if __name__ == '__main__':
    app = Main()
    app.run()