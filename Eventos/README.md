## Metodos usados nessa pasta que tem inputs


metodo __init__() da classe HistoricoEventos:

        input:

        tamanho_maximo: Número máximo de eventos a serem armazenados

metodo adicionar_evento():

        input:
        
        evento: Evento a ser adicionado ao histórico

metodo __init__() da classe Participante:

        inputs:

            numero_inscricao (inteiro): Número único de identificação
            nome (string): Nome completo do participante
            email (string): Email do participante
            tipo_inscricao (string): Tipo de inscrição (regular, prioritário, etc.)

metodo inserir_participante():

        inputs:

            nome (string): Nome do participante
            email (string): Email do participante
            tipo_inscricao (string, opcional): Tipo de inscrição

metodo inserir_recursivo():

        inputs:

            no_atual (No): Nó atual na árvore
            participante (Participante): Participante a ser inserido

metodo buscar_por_numero_inscricao():

        inputs:

            numero_inscricao (inteiro): Número de inscrição a ser buscado

buscar_recursivo():

        inputs:

            no_atual (No): Nó atual na árvore
            numero_inscricao (inteiro): Número de inscrição a ser buscado

metodo buscar_por_nome():

        input:

            nome (string): Nome ou parte do nome a ser buscado

metodo buscar_por_nome_recursivo():

        inputs:

            no_atual (No): Nó atual na árvore
            nome_busca (string): Nome ou parte do nome a ser buscado
            resultados (lista): lista para armazenar resultados

metodo ordenar_recursivo();

        inputs:

            no_atual (No): Nó atual na árvore
            resultados (lista): lista para armazenar resultados
        