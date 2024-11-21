import sys
import os

# Adicionando o diretório "Restaurante" ao caminho de busca de módulos do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Estruturas import Pilha, Fila, ArvoreBinaria

class Pedido:
    def __init__(self):
        """Inicializa um pedido com uma lista de itens."""
        self._itens = []
        self._historico = Pilha()  # Pilha para armazenar histórico de modificações
    
    def adicionar_item(self, item):
        """
        Adiciona um item ao pedido e salva o estado anterior na pilha de histórico.
        
        Args:
            item (str): Item a ser adicionado ao pedido
        """
        # Cria uma cópia do estado atual para salvar no histórico
        estado_anterior = self._itens.copy()
        
        # Adiciona o novo item
        self._itens.append(item)
        
        # Salva o estado anterior na pilha de histórico
        self._historico.push(estado_anterior)
    
    def remover_item(self, item):
        """
        Remove um item do pedido, se existir, e salva o estado anterior na pilha de histórico.
        
        Args:
            item (str): Item a ser removido do pedido
        
        Returns:
            bool: True se o item foi removido, False caso contrário
        """
        if item in self._itens:
            # Cria uma cópia do estado atual para salvar no histórico
            estado_anterior = self._itens.copy()
            
            # Remove o item
            self._itens.remove(item)
            
            # Salva o estado anterior na pilha de histórico
            self._historico.push(estado_anterior)
            
            return True
        return False
    
    def desfazer(self):
        """
        Desfaz a última modificação no pedido, restaurando o estado anterior.
        
        Raises:
            IndexError: Se não houver modificações para desfazer
        """
        if self._historico.esta_vazia():
            raise IndexError("Não há modificações para desfazer.")
        
        # Restaura o estado anterior
        self._itens = self._historico.pop()
    
    def get_itens(self):
        """
        Retorna a lista de itens atuais do pedido.
        
        Returns:
            list: Lista de itens do pedido
        """
        return self._itens.copy()
    
    def imprimir_pedido(self):
        """Imprime os itens atuais do pedido."""
        if not self._itens:
            print("Pedido vazio.")
        else:
            print("Itens do pedido:")
            for item in self._itens:
                print(item)

def main():
    # Demonstração do uso da classe Pedido
    pedido = Pedido()
    
    # Adicionando itens
    print("Adicionando itens:")
    pedido.adicionar_item("Pizza Margherita")
    pedido.adicionar_item("Refrigerante")
    pedido.imprimir_pedido()
    
    # Removendo um item
    print("\nRemovendo um item:")
    pedido.remover_item("Refrigerante")
    pedido.imprimir_pedido()
    
    # Desfazendo a última modificação
    print("\nDesfazendo a última modificação:")
    pedido.desfazer()
    pedido.imprimir_pedido()
    
    # Tentativa de desfazer novamente
    print("\nDesfazendo novamente:")
    pedido.desfazer()
    pedido.imprimir_pedido()

if __name__ == "__main__":
    main()