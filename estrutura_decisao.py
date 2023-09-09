idade = int (input('Digite a idade da pessoa: '))
if idade > 18:
    print('Maior de idade')
else:
    print('Menor de idade')


A = input ('Informe um valor para a variável A: ')
B = input ('Infore um valor para a variável B: ')

if (A > B):
    aux = A;
    A = B;
    B = aux;

print ('O valor da variável A agora é: ', A);
print ('O valor da variável B agora é: ', B);