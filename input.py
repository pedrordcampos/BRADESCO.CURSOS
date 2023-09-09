fruta = input('Digite o nome da fruta: ')
print (fruta)

# Entrada de dados de tipos diferentes de string
codigo = int(input('Digite o codigo do funcionario: '))
nome = input('Digite o nome do funcionario: ')
salario = float(input('Informe o salario: '))
ativo = True

print ('Codigo: %d ' % codigo)
print ('Nome %s ' % nome)
print ('Salario %.2f ' % salario)
print ('Ativo %r ' % ativo)

# Sequencia de escapes
# \n = quebra de linha
# \t = tabulação horizontal
# \v = tabulação vertical
# \r = efeito similar a tecla Enter 
# \' = aspas simples
# \" = aspas duplas
# \\ = insere uma barra invertida
# \a = se houver suporte, adiciona um bipe 
# \f = quebra de página
# \u = insere um caractere unicode. Deve acompanhar um código com 4 números