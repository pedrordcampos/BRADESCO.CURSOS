# O conceito de variável em Python é representado por um objeto, logo toda variável é uma referência.
# Não é necessário declarar as variáveis no início do programa.

codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True

# Verificar o tipo da variável, no caso é float
tipo = type (salario)

print (salario)
print (tipo)

# Para concatenar, utilizamos a vírgula (,)

print('Código: ', codigo, 'Nome: ', nome, 'O salário atual é de ', salario)

# É possível utilizar o sinal de mais (+) para concatenar, mas devemos converter os valores para string (str) antes da variável

print ('Código: '+ str(codigo))

# Identificadores 
# Máscara

# %d ou %i = inteiro 
# %f = float
# %ld = long int
# %e ou %E = exponencial
# %c ou %s= char
# %o = formato octal
# %x ou %X = hexadecimal
# %r = boolean

print('Codigo: %d' % codigo)
print('nome: %s' % nome)
print('Salario: %.2f' % salario)
print('Ativo: %r' % situacao)
