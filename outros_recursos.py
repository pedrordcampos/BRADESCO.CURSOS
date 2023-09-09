# A função open() é utilizada para a abertura dos arquivos. Sua sintaxe é: arquivo = open('arquivo.txt', 'w')

# A função write() é utilizada para gravar informações em um arquivo existente. 
# Sua sintaxe é: 
# arquivo.write('Curso Python n')
# arquivo.write('Aula prática)

# Função close() é muito importante para encerrar um arquivo, após a sua utilização
# Sua sintaxe é: arquivo.close()

arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula prática')
arquivo.close()

# A função read() realiza a leitura do arquivo
# Sua sintaxe é leitura=open('arquivo.txt', 'r')
# print leitura.read()
# leitura.close()

leitura = open ('arqText.txt', 'r')
print(leitura.read())
leitura.close()

# r -> abre o arquivo somente para a leitura. O arquivo já deve existir
# r+ -> abre o arquivo para leitura e escrita
# w -> abre o arquivo somente para a escrita
# w+ -> abre o arquivo para escrita e leitura
# a -> abre o arquivo para a escrita no final do arquivo
# a+ -> abre o arquivo para escrita no final do arquivo e leitura

