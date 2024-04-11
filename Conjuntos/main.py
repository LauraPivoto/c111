# # Coleções
#
# # Tuplas ()
# nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
#
# #Slicing = Fatiar para obter dados importantes
#
# print(nomes[0])
#
# #primeiro parãmetro inclusive, segundo exclusive
# print(nomes[2])
#
# #o último item é o endereço -1
# print(nomes[-2])
#
# #update n podi

# nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
# nomes.append('Bulma')
# nomes[0] = 'Goten'
#
# nomes.remove('trunks')
# del nomes[2]

# #conjuntos
# nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}

#dicionários
# verdade_absoluta = {'verdade':'Laura loves Xico very mucho'}
# #print(verdade_absoluta['verdade'])
#
# pessoa = {'sexo': 'M'}
# pessoa['nome'] = 'Xico'
#
# print(pessoa)

#Coleções aninhadas

#EXERCICIO DA AULA

#Exercício 1

resultado = ['Liverpool', 'Barcelona', 'Bayern', 'Espanyol', 'Sevilla']
#
 #Três primeiros
print(resultado[:3])
 #Dois últimos
print(resultado[3:5])
 #ordena e depois printa
resultado.sort()
print(resultado)
 #posição do Barcelona
print(resultado.index('Barcelona'))

#Exercício 2

modelos1 = {'Xperia 5 III', 'Galaxy S21', 'Pixel 5', 'iPhone 12', 'Xperia 1 III'}
modelos2 = {'Galaxy Note 20', 'Pixel 5', 'OnePlus 8T', 'Xperia 5 III', 'iPhone 12'}

#União dos modelos
print(modelos1 | modelos2)

#intersecção
print(modelos1&modelos2)

#Exercício 3

nome = input('Escolha um nome')
nota = input('Digite sua nota')

alunos = {'nome': nome, 'nota': nota}

if(alunos['nota'] >= '60'):
    print('AP')
else:
    print('RP')

print(alunos)