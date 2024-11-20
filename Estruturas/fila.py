class Fila:
    def __init__(self):
        # Inicializa a fila como uma lista vazia
        self.items = []
    
    def esta_vazia(self):
        """Verifica se a fila está vazia"""
        return len(self.items) == 0
    
    def inserir(self, item):
        """Insere um item no final da fila"""
        self.items.append(item)
    
    def remover(self):
        """Remove o primeiro item da fila."""
        if self.esta_vazia():
            raise IndexError("Impossível remover de uma fila vazia")
        return self.items.pop(0)
    
    def buscar(self, valor):
        """Busca um valor na fila."""
        try:
            return self.items.index(valor)
        except ValueError:
            return -1
    
    def tamanho(self):
        """Retorna o número de elementos na fila"""
        return len(self.items)
    
    def primeiro(self):
        """Retorna o primeiro item da fila sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("Fila está vazia")
        return self.items[0]
    
    def __str__(self):
        """Representar a fila"""
        return str(self.items)


def main():
    # Criando uma nova fila
    fila = Fila()
    
    # Inserindo elementos
    print("Inserindo elementos:")
    fila.inserir(10)
    fila.inserir(20)
    fila.inserir(30)
    print(fila)  # Mostra o estado atual da fila
    
    # Removendo elemento
    print("\nRemovendo elemento:")
    removido = fila.remover()
    print(f"Elemento removido: {removido}")
    print(fila)
    
    # Buscando elemento
    print("\nBuscando elementos:")
    indice_20 = fila.buscar(20)
    indice_50 = fila.buscar(50)
    print(f"Índice do 20: {indice_20}")
    print(f"Índice do 50: {indice_50}")
    

    print("\nOutras informações:")
    print(f"Tamanho da fila: {fila.tamanho()}")
    print(f"Primeiro elemento: {fila.primeiro()}")
    print(f"Está vazia? {fila.esta_vazia()}")


if __name__ == "__main__":
    main()