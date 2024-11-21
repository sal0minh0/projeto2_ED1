import sys
import os

# Adicionando o diretorio "Clínica" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Estruturas.pilha import Pilha
from Estruturas.fila import Fila
from Estruturas.arvore import ArvoreBinaria

class HistoricoPacientes:
    def __init__(self):
        """Inicializa o histórico de pacientes com uma pilha de ações."""
        self._pilha_acoes = Pilha()
    
    def agendar_consulta(self, paciente, medico, data):
        """Agenda uma consulta e registra a ação para possível desfazer."""
        # Adiciona a consulta ao dicionário de consultas
        self._consultas[paciente] = {
            'medico': medico,
            'data': data
        }
        
        consulta = {
            'acao': 'agendar',
            'paciente': paciente,
            'medico': medico,
            'data': data
        }
        self._pilha_acoes.push(consulta)
        print(f"Consulta agendada: {paciente} com {medico} em {data}")
    
    def atualizar_consulta(self, paciente, novo_medico=None, nova_data=None):
        """Atualiza uma consulta e registra a ação anterior para desfazer."""
        consulta_atual = {
            'acao': 'atualizar',
            'paciente': paciente,
            'medico_antigo': self._consultas.get(paciente, {}).get('medico'),
            'data_antiga': self._consultas.get(paciente, {}).get('data'),
            'novo_medico': novo_medico,
            'nova_data': nova_data
        }
        # Atualiza a consulta 
        if paciente not in self._consultas:
            raise ValueError(f"Não existe consulta para o paciente {paciente}")
        
        if novo_medico:
            self._consultas[paciente]['medico'] = novo_medico
        if nova_data:
            self._consultas[paciente]['data'] = nova_data
        
        self._pilha_acoes.push(consulta_atual)
        print(f"Consulta de {paciente} atualizada")
    
    def desfazer_ultima_acao(self):
        """Desfaz a última ação realizada no histórico de consultas."""
        if self._pilha_acoes.esta_vazia():
            print("Não há ações para desfazer.")
            return
        
        acao_anterior = self._pilha_acoes.pop()
        
        if acao_anterior['acao'] == 'agendar':
            # Remove a consulta agendada
            del self._consultas[acao_anterior['paciente']]
            print(f"Consulta de {acao_anterior['paciente']} desfeita.")
        
        elif acao_anterior['acao'] == 'atualizar':
            # Restaura os valores anteriores
            paciente = acao_anterior['paciente']
            self._consultas[paciente]['medico'] = acao_anterior['medico_antigo']
            self._consultas[paciente]['data'] = acao_anterior['data_antiga']
            print(f"Atualização de {paciente} restaurada.")
    
    def __init__(self):
        """Inicializa o histórico de pacientes."""
        self._pilha_acoes = Pilha()
        self._consultas = {}  # Armazena as consultas correntes
    
    def listar_historico(self):
        """Lista o histórico de ações realizadas."""
        if self._pilha_acoes.esta_vazia():
            print("Não há histórico de ações.")
            return
        
        print("Histórico de Ações:")
        historico_temp = Pilha()
        
        while not self._pilha_acoes.esta_vazia():
            acao = self._pilha_acoes.pop()
            historico_temp.push(acao)
            
            if acao['acao'] == 'agendar':
                print(f"Agendamento: {acao['paciente']} com {acao['medico']} em {acao['data']}")
            elif acao['acao'] == 'atualizar':
                print(f"Atualização: {acao['paciente']} - Médico: {acao['medico_antigo']} -> {acao['novo_medico']}, Data: {acao['data_antiga']} -> {acao['nova_data']}")
        
        # Restaura a pilha original
        while not historico_temp.esta_vazia():
            self._pilha_acoes.push(historico_temp.pop())

# Demonstração do uso da classe HistoricoPacientes
historico = HistoricoPacientes()

# Agendando consultas
historico.agendar_consulta("João Silva", "Dr. Pereira", "2024-06-15")
historico.agendar_consulta("Maria Souza", "Dra. Oliveira", "2024-06-20")

# Atualizando uma consulta
historico.atualizar_consulta("João Silva", novo_medico="Dra. Oliveira")

# Listando o histórico
historico.listar_historico()

# Desfazendo a última ação
historico.desfazer_ultima_acao()

# Listando o histórico novamente
historico.listar_historico()

class GerenciadorEmergencia:
    def __init__(self):
        """Inicializa o gerenciador de emergência com filas de prioridade."""
        self._fila_alta_prioridade = Fila()
        self._fila_media_prioridade = Fila()
        self._fila_baixa_prioridade = Fila()
        
        # Histórico de atendimentos para relatórios
        self._historico_atendimentos = []
    
    def adicionar_paciente(self, paciente, prioridade):
        """Adiciona um paciente à fila de acordo com sua prioridade."""
        paciente_info = {
            'nome': paciente.get('nome'),
            'idade': paciente.get('idade'),
            'sintomas': paciente.get('sintomas'),
            'prioridade': prioridade
        }
        
        if prioridade == 'alta':
            self._fila_alta_prioridade.inserir(paciente_info)
            print(f"Paciente {paciente_info['nome']} adicionado à fila de ALTA prioridade.")
        elif prioridade == 'media':
            self._fila_media_prioridade.inserir(paciente_info)
            print(f"Paciente {paciente_info['nome']} adicionado à fila de MÉDIA prioridade.")
        elif prioridade == 'baixa':
            self._fila_baixa_prioridade.inserir(paciente_info)
            print(f"Paciente {paciente_info['nome']} adicionado à fila de BAIXA prioridade.")
        else:
            raise ValueError("Prioridade inválida. Use 'alta', 'media' ou 'baixa'.")
    
    def chamar_proximo_paciente(self):
        """Chama o próximo paciente para atendimento seguindo a ordem de prioridade."""
        # Prioridade: alta > media > baixa
        if not self._fila_alta_prioridade.esta_vazia():
            paciente = self._fila_alta_prioridade.remover()
            status = "ALTA PRIORIDADE"
        elif not self._fila_media_prioridade.esta_vazia():
            paciente = self._fila_media_prioridade.remover()
            status = "MÉDIA PRIORIDADE"
        elif not self._fila_baixa_prioridade.esta_vazia():
            paciente = self._fila_baixa_prioridade.remover()
            status = "BAIXA PRIORIDADE"
        else:
            print("Todas as filas estão vazias. Não há pacientes para atender.")
            return None
        
        # Registra atendimento no histórico
        paciente['status_atendimento'] = status
        self._historico_atendimentos.append(paciente)
        
        print(f"Próximo paciente: {paciente['nome']} - {status}")
        return paciente
    
    def calcular_tempo_espera(self):
        """Calcula o tempo de espera estimado para cada fila de prioridade."""
        tempo_medio_atendimento = 20  # minutos
        
        return {
            'alta_prioridade': len(self._fila_alta_prioridade.items) * tempo_medio_atendimento,
            'media_prioridade': len(self._fila_media_prioridade.items) * tempo_medio_atendimento,
            'baixa_prioridade': len(self._fila_baixa_prioridade.items) * tempo_medio_atendimento
        }
    
    def gerar_relatorio_atendimentos(self):
        """Gera um relatório detalhado dos atendimentos realizados."""
        if not self._historico_atendimentos:
            print("Não há atendimentos registrados.")
            return []
        
        print("\n--- Relatório de Atendimentos ---")
        for atendimento in self._historico_atendimentos:
            print(f"Paciente: {atendimento['nome']}")
            print(f"Idade: {atendimento['idade']}")
            print(f"Sintomas: {atendimento['sintomas']}")
            print(f"Status: {atendimento['status_atendimento']}")
            print("---")
        
        return self._historico_atendimentos
    
    def status_atual_filas(self):
        """Mostra o status atual de todas as filas de prioridade."""
        print("\n--- Status Atual das Filas ---")
        print(f"Alta Prioridade: {len(self._fila_alta_prioridade.items)} pacientes")
        print(f"Média Prioridade: {len(self._fila_media_prioridade.items)} pacientes")
        print(f"Baixa Prioridade: {len(self._fila_baixa_prioridade.items)} pacientes")

    # Demonstração do uso do Gerenciador de Emergência
emergencia = GerenciadorEmergencia()

# Adicionar pacientes com diferentes prioridades
emergencia.adicionar_paciente({
    'nome': 'João Silva',
    'idade': 45,
    'sintomas': 'Dor no peito'
}, prioridade='alta')

emergencia.adicionar_paciente({
    'nome': 'Maria Santos',
    'idade': 32,
    'sintomas': 'Febre alta'
}, prioridade='media')

emergencia.adicionar_paciente({
    'nome': 'Pedro Oliveira',
    'idade': 28,
    'sintomas': 'Torção no tornozelo'
}, prioridade='baixa')

# Verificar status das filas
emergencia.status_atual_filas()

# Calcular tempo de espera
tempos_espera = emergencia.calcular_tempo_espera()
print("\nTempos de Espera Estimados:")
for prioridade, tempo in tempos_espera.items():
    print(f"{prioridade.replace('_', ' ').title()}: {tempo} minutos")

# Chamar próximo paciente (alta prioridade)
emergencia.chamar_proximo_paciente()

# Gerar relatório de atendimentos
emergencia.gerar_relatorio_atendimentos()

class CadastroDadosMedico:
    def __init__(self, nome, crm, especialidade, disponibilidade):
        """Representa os dados de um médico."""
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.disponibilidade = disponibilidade
    
    def __str__(self):
        """Representação em string dos dados do médico."""
        return f"{self.nome} - CRM: {self.crm} - {self.especialidade}"

class CadastroMedicos:
    def __init__(self):
        """Inicializa o sistema de cadastro de médicos com árvores """
        # Árvore por CRM
        self._arvore_crm = ArvoreBinaria()
        
        # Árvores por especialidade
        self._arvores_especialidade = {}
        
        # Dicionário para armazenar médicos completos
        self._medicos_por_crm = {}
    
    def cadastrar_medico(self, nome, crm, especialidade, disponibilidade):
        """Cadastra um novo médico no sistema."""
        # Cria objeto de dados do médico
        medico = CadastroDadosMedico(nome, crm, especialidade, disponibilidade)
        
        # Insere na árvore por CRM
        self._arvore_crm.inserir(crm)
        
        # Mantém registro completo por CRM
        self._medicos_por_crm[crm] = medico
        
        # Cria ou insere na árvore de especialidade
        if especialidade not in self._arvores_especialidade:
            self._arvores_especialidade[especialidade] = ArvoreBinaria()
        
        self._arvores_especialidade[especialidade].inserir(crm)
        
        print(f"Médico {nome} cadastrado com sucesso.")
    
    def buscar_medico_por_crm(self, crm):
        """Busca um médico pelo número do CRM."""
        if self._arvore_crm.buscar(crm):
            return self._medicos_por_crm.get(crm)
        return None
    
    def listar_medicos_por_especialidade(self, especialidade):
        """Lista todos os médicos de uma determinada especialidade."""
        if especialidade not in self._arvores_especialidade:
            print(f"Nenhum médico encontrado na especialidade {especialidade}")
            return []
        
        # Obtém os CRMs da especialidade
        crms_especialidade = self._arvores_especialidade[especialidade].ordenar()
        
        # Converte CRMs para médicos
        medicos_especialidade = [
            self._medicos_por_crm[crm] for crm in crms_especialidade
        ]
        
        return medicos_especialidade
    
    def buscar_medico_disponivel(self, especialidade, dia, hora):
        """Busca médicos disponíveis por especialidade, dia e hora."""
        medicos_disponiveis = []
        
        # Obtém médicos da especialidade
        medicos = self.listar_medicos_por_especialidade(especialidade)
        
        # Filtra médicos disponíveis
        for medico in medicos:
            for disponibilidade in medico.disponibilidade:
                if disponibilidade['dia'] == dia and disponibilidade['hora'] == hora:
                    medicos_disponiveis.append(medico)
                    break
        
        return medicos_disponiveis
    
    def remover_medico(self, crm):
        """Remove um médico do sistema pelo CRM."""
        if crm not in self._medicos_por_crm:
            print(f"Médico com CRM {crm} não encontrado.")
            return
        
        # Obtém dados do médico
        medico = self._medicos_por_crm[crm]
        
        # Remove da árvore de CRM
        self._arvore_crm.remover(crm)
        
        # Remove da árvore de especialidade
        self._arvores_especialidade[medico.especialidade].remover(crm)
        
        # Remove do dicionário
        del self._medicos_por_crm[crm]
        
        print(f"Médico {medico.nome} removido do sistema.")
    
    def gerar_relatorio_especialidades(self):
        """Gera um relatório com a quantidade de médicos por especialidade."""
        relatorio = {}
        for especialidade, arvore in self._arvores_especialidade.items():
            # Obtém lista de CRMs da especialidade
            crms = arvore.ordenar()
            relatorio[especialidade] = len(crms)
        
        return relatorio

    # Demonstração do uso do Cadastro de Médicos
cadastro = CadastroMedicos()

# Cadastrando médicos
cadastro.cadastrar_medico(
    nome="Dr. João Silva", 
    crm="12345", 
    especialidade="Cardiologia",
    disponibilidade=[
        {"dia": "Segunda", "hora": "09:00"},
        {"dia": "Quarta", "hora": "14:00"}
    ]
)

cadastro.cadastrar_medico(
    nome="Dra. Maria Oliveira", 
    crm="67890", 
    especialidade="Cardiologia",
    disponibilidade=[
        {"dia": "Terça", "hora": "10:00"},
        {"dia": "Quinta", "hora": "15:00"}
    ]
)

cadastro.cadastrar_medico(
    nome="Dr. Pedro Santos", 
    crm="54321", 
    especialidade="Neurologia",
    disponibilidade=[
        {"dia": "Segunda", "hora": "11:00"},
        {"dia": "Sexta", "hora": "16:00"}
    ]
)

# Buscando médicos por especialidade
print("\nMédicos de Cardiologia:")
cardiologistas = cadastro.listar_medicos_por_especialidade("Cardiologia")
for medico in cardiologistas:
    print(medico)

# Buscando médicos disponíveis
print("\nMédicos disponíveis - Cardiologia, Segunda, 09:00:")
medicos_disponiveis = cadastro.buscar_medico_disponivel("Cardiologia", "Segunda", "09:00")
for medico in medicos_disponiveis:
    print(medico)

# Gerando relatório de especialidades
print("\nRelatório de Especialidades:")
relatorio = cadastro.gerar_relatorio_especialidades()
for especialidade, quantidade in relatorio.items():
    print(f"{especialidade}: {quantidade} médicos")
