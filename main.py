import sys
import os

# Adicionar diretorio Pai para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Clinica import Paciente
from Eventos import Evento
from Restaurante import Restaurante

# Tela Principal
class Main:
    def __init__(self):
        # Clinica
        self.paciente = Paciente()
        # Eventos
        self.eventos = Evento()
        # Restaurante
        self.restaurante = Restaurante()
        
    def run(self):
        self.janela_principal.mainloop()

# Executar a aplicação
if __name__ == '__main__':
    app = Main()
    app.run()