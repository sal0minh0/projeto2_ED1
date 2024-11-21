Metodos usados nessa pasta que tem inputs

metodo agendar_consulta():
        
        inputs:

            paciente (string): Nome do paciente
            medico (string): Nome do médico
            data (string): Data da consulta

metodo atualizar_consulta():
    
        inputs:

            paciente (string): Nome do paciente
            novo_medico (string, opcional): Novo médico da consulta
            nova_data (string, opcional): Nova data da consulta
        
metodo adicionar_paciente():
        
        inputs:

            paciente (dicionario): Informações do paciente
            prioridade (string): Prioridade do atendimento ('alta', 'media', 'baixa')

metodo __init__() da classe CadastringoDadosMedico:

        inputs:

            nome (string): Nome completo do médico
            crm (string): Número do CRM
            especialidade (string): Especialidade médica
            disponibilidade (lista): Dias e horários disponíveis

metodo cadastringar_medico():

        inputs:

            nome (string): Nome completo do médico
            crm (string): Número do CRM
            especialidade (string): Especialidade médica
            disponibilidade (lista): Dias e horários disponíveis

metodo buscar_medico_por_crm():
        
        input:

            crm (string): Número do CRM

metodo listar_medicos_por_especialidade():
        
        inputs:

            especialidade (string): Especialidade médica

metodo buscar_medico_disponivel():
        
        inputs:

            especialidade (string): Especialidade médica
            dia (string): Dia da semana
            hora (string): Horário
        
metodo remover_medico():
        
        inputs:

            crm (string): Número do CRM
    
        
        
        