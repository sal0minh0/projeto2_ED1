import sys
import os

# Adicionando o diretório "Restaurante" ao caminho de busca de módulos do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Estruturas.pilha import Pilha
from Estruturas.fila import Fila
from Estruturas.arvore import ArvoreBinaria

class Pedido:
    def __init__(self):
        """Inicializa um pedido com uma lista de itens."""
        self._itens = []
        self._historico = Pilha()  # Pilha para armazenar histórico de modificações
    
    def adicionar_item(self, item):
        """Adiciona um item ao pedido e salva o estado anterior na pilha de histórico."""
        # Cria uma cópia do estado atual para salvar no histórico
        estado_anterior = self._itens.copy()
        
        # Adiciona o novo item
        self._itens.append(item)
        
        # Salva o estado anterior na pilha de histórico
        self._historico.push(estado_anterior)
    
    def remover_item(self, item):
        """Remove um item do pedido, se existir, e salva o estado anterior na pilha de histórico."""
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
        """Desfaz a última modificação no pedido, restaurando o estado anterior."""
        if self._historico.esta_vazia():
            raise IndexError("Não há modificações para desfazer.")
        
        # Restaura o estado anterior
        self._itens = self._historico.pop()
    
    def get_itens(self):
        """Retorna a lista de itens atuais do pedido."""
        return self._itens.copy()
    
    def imprimir_pedido(self):
        """Imprime os itens atuais do pedido."""
        if not self._itens:
            print("Pedido vazio.")
        else:
            print("Itens do pedido:")
            for item in self._itens:
                print(item)

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

class ItemPedido:
    def __init__(self, nome, tempo_preparo):
        """Representa um item de pedido com seu tempo de preparo."""
        self.nome = nome
        self.tempo_preparo = tempo_preparo
    
    def __repr__(self):
        """Representação em string do item."""
        return f"{self.nome} (Tempo: {self.tempo_preparo} min)"

class FilaPedidos:
    def __init__(self):
        """Inicializa a fila de pedidos."""
        self.fila = Fila()
        self.fila_prioridade = []
    
    def adicionar_pedido(self, pedido):
        """Adiciona um pedido à fila, organizando por tempo de preparo."""
        
        # Ordena o pedido pelo tempo de preparo
        pedido_ordenado = sorted(pedido, key=lambda x: x.tempo_preparo)
        
        # Adiciona à fila geral
        self.fila.inserir(pedido_ordenado)
        
        # Adiciona à fila de prioridade (considerando o item mais rápido primeiro)
        self.fila_prioridade.append(pedido_ordenado)
        self.fila_prioridade.sort(key=lambda x: x[0].tempo_preparo)
    
    def proximo_pedido(self):
        """Retorna o próximo pedido da fila, priorizando pedidos com itens mais rápidos de preparo"""

        if self.fila.esta_vazia():
            raise IndexError("Não há pedidos na fila.")
        
        # Remove e retorna o pedido com item mais rápido
        return self.fila.remover()
    
    def visualizar_pedidos(self):
        """Mostra todos os pedidos na fila."""
        print("Pedidos na fila (por ordem de chegada):")
        for i, pedido in enumerate(self.fila.items, 1):
            print(f"Pedido {i}:")
            for item in pedido:
                print(f"  - {item}")
    
    def visualizar_prioridade(self):
        """Mostra pedidos ordenados por prioridade de preparo."""
        print("Pedidos por prioridade (mais rápidos primeiro):")
        for i, pedido in enumerate(self.fila_prioridade, 1):
            print(f"Pedido {i} - Primeiro item: {pedido[0]}")
    
    def quantidade_pedidos(self):
        """Retorna a quantidade de pedidos na fila."""
        return self.fila.tamanho()


# Criando a fila de pedidos
fila_pedidos = FilaPedidos()

# Criando alguns itens com tempos de preparo diferentes
pedido1 = [
    ItemPedido("Refrigerante", 2),
    ItemPedido("Pizza Margherita", 15),
    ItemPedido("Salada", 10)
]

pedido2 = [
    ItemPedido("Suco", 5),
    ItemPedido("Hambúrguer", 12),
    ItemPedido("Batata Frita", 8)
]

# Adicionando pedidos
print("Adicionando pedidos:")
fila_pedidos.adicionar_pedido(pedido1)
fila_pedidos.adicionar_pedido(pedido2)

# Visualizando pedidos
print("\nVisualização por ordem de chegada:")
fila_pedidos.visualizar_pedidos()

# Visualizando prioridades
print("\nVisualização por prioridade:")
fila_pedidos.visualizar_prioridade()

# Processando pedidos
print("\nProcessando pedidos:")
while fila_pedidos.quantidade_pedidos() > 0:
    print("\nPróximo pedido:")
    pedido = fila_pedidos.proximo_pedido()
    for item in pedido:
        print(f"Preparando: {item}")

class ItemMenu:
    def __init__(self, nome, preco, categoria):
        """ Representa um item do menu com informações de popularidade."""
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.vendas_total = 0
        self.total_pedidos = 0

    def registrar_venda(self, quantidade):
        """ Registra uma venda do item."""
        self.vendas_total += quantidade
        self.total_pedidos += 1

    def obter_popularidade(self):
        """ Calcula a popularidade do item baseado no número de vendas."""
        return self.vendas_total / max(self.total_pedidos, 1)

    def __repr__(self):
        """Representação em string do item."""
        return f"{self.nome} (R${self.preco:.2f}) - Popularidade: {self.obter_popularidade():.2f}"

    def __lt__(self, other):
        """Less than comparison based on popularity"""
        return self.obter_popularidade() < other.obter_popularidade()

    def __gt__(self, other):
        """Greater than comparison based on popularity"""
        return self.obter_popularidade() > other.obter_popularidade()

    def __eq__(self, other):
        """Equality comparison based on popularity"""
        return self.obter_popularidade() == other.obter_popularidade()

class GerenciadorMenu:
    def __init__(self):
        """Inicializa o gerenciador de menu com árvores de popularidade."""
        self.arvore_popularidade = ArvoreBinaria()
        self.menu = {}  # Dicionário para acesso rápido por nome
    
    def adicionar_item(self, nome, preco, categoria):
        """Adiciona um novo item ao menu."""
        item = ItemMenu(nome, preco, categoria)
        self.menu[nome] = item
        
        # Insere na árvore de popularidade
        self.arvore_popularidade.inserir(item)
        
        return item
    
    def registrar_venda(self, nome, quantidade=1):
        """Registra uma venda de um item específico."""
        if nome not in self.menu:
            raise ValueError(f"Item {nome} não encontrado no menu.")
        
        item = self.menu[nome]
        item.registrar_venda(quantidade)
    
    def consultar_item(self, nome):
        """Consulta as informações de um item específico."""
        if nome not in self.menu:
            raise ValueError(f"Item {nome} não encontrado no menu.")
        
        return self.menu[nome]
    
    def listar_mais_populares(self, limite=5):
        """Lista os itens mais populares baseado na popularidade."""
        # Obtém todos os itens em ordem decrescente de popularidade
        todos_itens = sorted(
            self.menu.values(), 
            key=lambda x: x.obter_popularidade(), 
            reverse=True
        )
        
        return todos_itens[:limite]
    def listar_por_categoria(self, categoria):
        """Lista itens de uma categoria específica."""
        return [
            item for item in self.menu.values() 
            if item.categoria == categoria
        ]
    
    def imprimir_menu_completo(self):
        """Imprime o menu completo com detalhes de cada item."""
        print("Menu Completo:")
        for item in sorted(self.menu.values(), key=lambda x: x.nome):
            print(item)

# Criar gerenciador de menu
gerenciador = GerenciadorMenu()

# Adicionar itens ao menu
gerenciador.adicionar_item("Pizza Margherita", 35.00, "Pizza")
gerenciador.adicionar_item("Pizza Calabresa", 40.00, "Pizza")
gerenciador.adicionar_item("Hambúrguer", 25.00, "Lanches")
gerenciador.adicionar_item("Salada Caesar", 22.00, "Saladas")
gerenciador.adicionar_item("Refrigerante", 5.00, "Bebidas")
gerenciador.adicionar_item("Suco Natural", 8.00, "Bebidas")

# Registrar algumas vendas
gerenciador.registrar_venda("Pizza Margherita", 10)
gerenciador.registrar_venda("Hambúrguer", 15)
gerenciador.registrar_venda("Pizza Calabresa", 5)
gerenciador.registrar_venda("Refrigerante", 20)

# Imprimir menu completo
print("Menu Completo:")
gerenciador.imprimir_menu_completo()

# Consultar itens mais populares
print("\nItens Mais Populares:")
for item in gerenciador.listar_mais_populares():
    print(item)

# Listar itens por categoria
print("\nPizzas:")
for pizza in gerenciador.listar_por_categoria("Pizza"):
    print(pizza)

# Consultar um item específico
print("\nDetalhes do Hambúrguer:")
print(gerenciador.consultar_item("Hambúrguer"))
