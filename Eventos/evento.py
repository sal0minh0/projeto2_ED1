import sys
import os

# Adicionando o diretorio "Eventos" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Estruturas import Pilha, Fila, ArvoreBinaria
from Estruturas.arvore import No

class HistoricoEventos:
    def __init__(self, tamanho_maximo=10):
        """Inicializa um histórico de eventos com um tamanho máximo opcional."""
        self._pilha = Pilha()
        self._tamanho_maximo = tamanho_maximo
    
    def adicionar_evento(self, evento):
        """Adiciona um novo evento ao histórico."""
        # Se atingir o tamanho máximo, remove o evento mais antigo (base da pilha)
        if self._pilha.tamanho() >= self._tamanho_maximo:
            # Remove o elemento na base da pilha (primeiro adicionado)
            self._pilha._itens.pop(0)
        
        # Adiciona o novo evento no topo da pilha
        self._pilha.push(evento)
    
    def voltar_evento(self):
        """Retorna ao evento anterior no histórico."""
        return self._pilha.pop()
    
    def evento_atual(self):
        """Retorna o evento mais recente."""
        return self._pilha.top()
    
    def imprimir_historico(self):
        """Imprime todos os eventos no histórico (do mais recente para o mais antigo)."""
        print("Histórico de Eventos:")
        self._pilha.imprimir()
    
    def limpar_historico(self):
        """Limpa o histórico de eventos."""
        self._pilha = Pilha()
    
    def tamanho_historico(self):
        """Retorna o número de eventos no histórico."""
        return self._pilha.tamanho()

# Demonstração do uso da classe HistoricoEventos
historico = HistoricoEventos(tamanho_maximo=5)

# Adicionando alguns eventos
print("Adicionando eventos:")
historico.adicionar_evento("Página inicial")
historico.adicionar_evento("Catálogo de produtos")
historico.adicionar_evento("Detalhes do produto A")
historico.adicionar_evento("Carrinho de compras")

# Imprimindo o histórico
historico.imprimir_historico()

# Voltando para um evento anterior
print("\nVoltando para o evento anterior:")
ultimo_evento = historico.voltar_evento()
print(f"Evento removido: {ultimo_evento}")

# Verificando o evento atual
print("\nEvento atual:")
print(historico.evento_atual())

# Verificando o tamanho do histórico
print(f"\nTamanho do histórico: {historico.tamanho_historico()}")

class FilaDeEventos(Fila):
    def __init__(self):
        """Inicializa a fila de eventos com duas filas"""
        super().__init__()
        self.fila_de_prioridade = []
        self.fila_geral = []
    
    def inserir_prioritario(self, inscrito):
        """Insere um inscrito na fila prioritária."""
        self.fila_de_prioridade.append(inscrito)
    
    def inserir_regular(self, inscrito):
        """Insere um inscrito na fila geral."""
        self.fila_geral.append(inscrito)
    
    def remover_inscrito(self):
        """Remove um inscrito, priorizando a fila prioritária."""
        if self.fila_de_prioridade:
            return self.fila_de_prioridade.pop(0)
        elif self.fila_geral:
            return self.fila_geral.pop(0)
        else:
            raise IndexError("Não há inscritos para remover")
    
    def total_inscritos(self):
        """Retorna o número total de inscritos."""
        return len(self.fila_de_prioridade) + len(self.fila_geral)
    
    def status_inscricoes(self):
        """Retorna informações sobre o status das inscrições."""
        return {
            "inscritos_prioritarios": len(self.fila_de_prioridade),
            "inscritos_gerais": len(self.fila_geral),
            "total_inscritos": self.total_inscritos()
        }
    
    def __str__(self):
        """Representação em string da fila de eventos."""
        return (f"Fila de Eventos\n"
                f"Prioritários: {self.fila_de_prioridade}\n"
                f"Fila Geral: {self.fila_geral}")

# Demonstração do uso da FilaDeEventos
evento = FilaDeEventos()

# Inserindo inscritos prioritários
print("Inscrevendo palestrantes:")
evento.inserir_prioritario({"nome": "Maria Silva", "cargo": "Palestrante Principal"})
evento.inserir_prioritario({"nome": "João Souza", "cargo": "Organizador"})

# Inserindo inscritos regulares
print("\nInscrevendo participantes regulares:")
evento.inserir_regular({"nome": "Pedro Santos", "tipo": "Estudante"})
evento.inserir_regular({"nome": "Ana Oliveira", "tipo": "Profissional"})
evento.inserir_regular({"nome": "Carlos Pereira", "tipo": "Estudante"})

# Mostrando status das inscrições
print("\nStatus das Inscrições:")
print(evento.status_inscricoes())

# Removendo inscritos
print("\nRemovendo inscritos:")
print("Primeiro inscrito removido:", evento.remover_inscrito())
print("Segundo inscrito removido:", evento.remover_inscrito())

# Status atualizado
print("\nStatus Atualizado:")
print(evento.status_inscricoes())

# Representação completa
print("\nEstado Atual da Fila:")
print(evento)


class Participante:
    def __init__(self, numero_inscricao, nome, email, tipo_inscricao, valor):
        """Representa um participante com informações detalhadas."""
        self.numero_inscricao = numero_inscricao
        self.nome = nome
        self.email = email
        self.tipo_inscricao = tipo_inscricao
        super().__init__(valor)
    
    def __repr__(self):
        """Representação em string do participante."""
        return f"Participante(#{self.numero_inscricao}, {self.nome})"


class ArvoreParticipantes:
    def __init__(self):
        """Inicializa a árvore de participantes."""
        self.raiz = None
        self.ultimo_numero_inscricao = 0
    
    def gerar_numero_inscricao(self):
        """Gera um número de inscrição único."""
        self.ultimo_numero_inscricao += 1
        return self.ultimo_numero_inscricao
    
    def inserir_participante(self, nome, email, tipo_inscricao='regular'):
        """Insere um novo participante na árvore."""
        numero_inscricao = self.gerar_numero_inscricao()
        novo_participante = Participante(numero_inscricao, nome, email, tipo_inscricao)
        
        if not self.raiz:
            self.raiz = No(novo_participante)
        else:
            self.inserir_recursivo(self.raiz, novo_participante)
        
        return novo_participante
    
    def inserir_recursivo(self, no_atual, participante):
        """Inserção recursiva de participante na árvore."""
        if participante.numero_inscricao < no_atual.valor.numero_inscricao:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(participante)
            else:
                self.inserir_recursivo(no_atual.esquerda, participante)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(participante)
            else:
                self.inserir_recursivo(no_atual.direita, participante)
    
    def buscar_por_numero_inscricao(self, numero_inscricao):
        """Busca um participante pelo número de inscrição."""
        return self.buscar_recursivo(self.raiz, numero_inscricao)
    
    def buscar_recursivo(self, no_atual, numero_inscricao):
        """Busca recursiva por número de inscrição."""
        if no_atual is None:
            return None
        
        if no_atual.valor.numero_inscricao == numero_inscricao:
            return no_atual.valor
        
        if numero_inscricao < no_atual.valor.numero_inscricao:
            return self.buscar_recursivo(no_atual.esquerda, numero_inscricao)
        else:
            return self.buscar_recursivo(no_atual.direita, numero_inscricao)
    
    def buscar_por_nome(self, nome):
        """Busca participantes por nome."""
        resultados = []
        self.buscar_por_nome_recursivo(self.raiz, nome.lower(), resultados)
        return resultados
    
    def buscar_por_nome_recursivo(self, no_atual, nome_busca, resultados):
        """Busca recursiva por nome em toda a árvore."""
        if no_atual is None:
            return
        
        # Verifica se o nome atual corresponde
        if nome_busca in no_atual.valor.nome.lower():
            resultados.append(no_atual.valor)
        
        # Continua a busca em ambos os lados
        self.buscar_por_nome_recursivo(no_atual.esquerda, nome_busca, resultados)
        self.buscar_por_nome_recursivo(no_atual.direita, nome_busca, resultados)
    
    def listar_participantes(self):
        """Lista todos os participantes em ordem de número de inscrição."""
        resultados = []
        self.ordenar_recursivo(self.raiz, resultados)
        return resultados
    
    def ordenar_recursivo(self, no_atual, resultados):
        """Percurso em-ordem para listar participantes.
        
        Args:
            no_atual (No): Nó atual na árvore
            resultados (list): Lista para armazenar resultados
        """
        if no_atual:
            self.ordenar_recursivo(no_atual.esquerda, resultados)
            resultados.append(no_atual.valor)
            self.ordenar_recursivo(no_atual.direita, resultados)


def main():
    # Criando árvore de participantes
    eventos = ArvoreParticipantes()
    
    # Inserindo participantes
    p1 = eventos.inserir_participante("Maria Silva", "maria@email.com", "prioritário")
    p2 = eventos.inserir_participante("João Santos", "joao@email.com")
    p3 = eventos.inserir_participante("Ana Oliveira", "ana@email.com")
    p4 = eventos.inserir_participante("Pedro Souza", "pedro@email.com", "estudante")
    
    # Buscando por número de inscrição
    print("\nBusca por Número de Inscrição:")
    print(eventos.buscar_por_numero_inscricao(p2.numero_inscricao))
    
    # Buscando por nome
    print("\nBusca por Nome:")
    resultado_busca = eventos.buscar_por_nome("silva")
    print("Participantes com 'silva' no nome:")
    for participante in resultado_busca:
        print(participante)
    
    # Listando todos os participantes
    print("\nTodos os Participantes:")
    for participante in eventos.listar_participantes():
        print(f"#{participante.numero_inscricao} - {participante.nome} ({participante.tipo_inscricao})")


if __name__ == "__main__":
    main()
    