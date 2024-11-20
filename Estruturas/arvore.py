class No:
    def __init__(self, valor):
        """Inicializa um nó dessa árvore."""
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        """Inicializa uma árvore binária vazia."""
        self.raiz = None
    
    def inserir(self, valor):
        """Insere um novo valor na árvore binária."""
        if not self.raiz:
            self.raiz = No(valor)
        else:
            self.inserir_recursivo(self.raiz, valor)
    
    def inserir_recursivo(self, no_atual, valor):
        """Inserção recursiva."""
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self.inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self.inserir_recursivo(no_atual.direita, valor)
    
    def buscar(self, valor):
        """Busca um valor nessa árvore."""
        return self.buscar_recursivo(self.raiz, valor)
    
    def buscar_recursivo(self, no_atual, valor):
        """ Busca recursiva."""
        if no_atual is None:
            return False
        
        if no_atual.valor == valor:
            return True
        
        if valor < no_atual.valor:
            return self.buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self.buscar_recursivo(no_atual.direita, valor)
    
    def remover(self, valor):
        """Remove um valor da árvore."""
        self.raiz = self.remover_recursivo(self.raiz, valor)
    
    def remover_recursivo(self, no_atual, valor):
        """Remoção recursiva."""
        if no_atual is None:
            return None
        
        # Encontrar o nó a ser removido
        if valor < no_atual.valor:
            no_atual.esquerda = self.remover_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self.remover_recursivo(no_atual.direita, valor)
        else:
            # Caso 1: Nó folha 
            if no_atual.esquerda is None and no_atual.direita is None:
                return None
    
            # Caso 2: Nó com apenas um filho
            if no_atual.esquerda is None:
                return no_atual.direita
            if no_atual.direita is None:
                return no_atual.esquerda
            
            # Caso 3: Nó com dois filhos
            menor_valor = self.encontrar_menor_valor(no_atual.direita)
            no_atual.valor = menor_valor
            no_atual.direita = self.remover_recursivo(no_atual.direita, menor_valor)
        
        return no_atual
    
    def encontrar_menor_valor(self, no):
        """Encontra o menor valor em uma subárvore."""
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor
    
    def ordenar(self):
        """Percorre a árvore em ordem."""
        resultado = []
        self.ordenar_recursivo(self.raiz, resultado)
        return resultado
    
    def ordenar_recursivo(self, no_atual, resultado):
        """
        Método auxiliar para percurso em-ordem recursivo.
        
        Args:
            no_atual: Nó atual
            resultado: Lista para armazenar os valores
        """
        if no_atual:
            self.ordenar_recursivo(no_atual.esquerda, resultado)
            resultado.append(no_atual.valor)
            self.ordenar_recursivo(no_atual.direita, resultado)

def main():
    # Criar uma árvore
    arvore = ArvoreBinaria()
    
    # Inserir valores
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arvore.inserir(valor)
    
    # Imprimir árvore em ordem
    print("Árvore em ordem:", arvore.ordenar())
    
    # Buscar valores
    print("Busca 40:", arvore.buscar(40))  # True
    print("Busca 55:", arvore.buscar(55))  # False
    
    # Remover valores
    arvore.remover(30)
    print("Árvore após remover 30:", arvore.ordenar())
    
    arvore.remover(50)
    print("Árvore após remover 50:", arvore.ordenar())

if __name__ == "__main__":
    main()