# Funções são estruturas que possibilitam a separação da programação em blocos.

# Definição da função, divida em: nome, parâmetros e corpo
# def nome_da_funcao (parâmetro) :
# <instruções>
# return 'valor do retorno'

def mensagem1 ():
    print ('Hello World!')

def mensagem2 ():
    return 'Olá Mundo'

mensagem1()

# Pegamos o return da função mensagem2 e alocamos numa variável texto
texto = mensagem2()
print (texto)