class Pilha:
    def __init__(self):
        """Inicializa uma pilha vazia usando uma lista."""
        self._itens = []
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self._itens) == 0
    
    def push(self, item):
        """Insere um item no topo da pilha."""
        self._itens.append(item)
    
    def pop(self):
        """Remove o topo da pilha.
        """
        if self.esta_vazia():
            raise IndexError("Pilha está vazia. Não é possível remover elementos.")
        return self._itens.pop()
    
    def top(self):
        """Retorna o item do topo da pilha."""
        if self.esta_vazia():
            raise IndexError("Pilha está vazia. Não há elementos para visualizar.")
        return self._itens[-1]
    
    def tamanho(self):
        """Retorna o número de elementos na pilha."""
        return len(self._itens)
    
    def imprimir(self):
        """Imprime quais são os elementos dessa pilha."""
        if self.esta_vazia():
            print("Pilha vazia.")
        else:
            print("Pilha (do topo para a base):")
            for item in reversed(self._itens):
                print(item)

def main():
    # Criando uma nova pilha
    pilha = Pilha()
    
    # Inserindo elementos
    print("Inserindo elementos:")
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    pilha.imprimir()
    
    # Verificando o topo
    print("\nTopo da pilha:", pilha.top())
    
    # Removendo elemento
    print("\nRemovendo elemento:", pilha.pop())
    pilha.imprimir()
    
    # Verificando tamanho
    print("\nTamanho da pilha:", pilha.tamanho())

if __name__ == "__main__":
    main()