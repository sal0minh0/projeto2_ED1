## Metodos usados nessa pasta que tem inputs

metodo adicionar_item():

    input:

        item (string): Item a ser adicionado ao pedido

metodo __init__() da classe ItemPedido:

    inputs:

        nome (string): Nome do item
        tempo_preparo (inteiro): Tempo de preparo em minutos
    
metodo adicionar_pedido():

    inputs:

        pedido (lista): Lista de ItemPedido para o pedido
        
metodo adicionar_item():

    inputs:

        nome (string): Nome do item
        preco (float): Preço do item
        categoria (string): Categoria do item

metodo registringar_venda():
        
    inputs:

        nome (string): Nome do item vendido
        quantidade (inteiro, optional): Quantidade vendida. Padrão é 1.

metodo consultar_item():

    input: 

        nome (string): Nome do item

metodo listar_mais_populares():

    input:

        limite (inteiro, optional): Número máximo de itens a retornar. Padrão é 5.

metodo listar_por_categoria():

    input:

        categoria (string): Categoria desejada