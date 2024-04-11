import numpy as np
import csv

# Numeros aleatorios
# Tem como gerar numeros aleatorios gerar nas mesmas maquinas? Posso plantar a mesma semente (seed)
# np.random.seed(10)
# arr = np.random.randint(1, 11, 15)  # 5 Números aleatorios de 10 a 20
# print(arr)

# Elementos únicos
# print(np.unique(arr, return_counts=True))  # Numeros sem ser repetidos e ja ordenados. O 10 nunca aparece

# Operações em matrizes
# Slide 19 exercicio 2
# np.random.seed(5)
# mtz = np.random.randint(1, 11, 9).reshape(3, 3)
# print(mtz)

# print(mtz.sum(axis=0)) # Somar as 3 colunas
# print(mtz.sum(axis=1 [0])) # Somar a linha 0
# print(mtz.mean(axis=0 [1])) # A media dos valores da coluna do meio.

# Broadcasting = transmitir. Operação entre um Escalar(número avulso) x Array(vários elementos)
# print(mtz*2)

# ----------------------------------------------------

# Conceito de condicional:
# Dessa matriz eu quero extrair apenas os elementos pares:
# arr3 = mtz % 2 == 0
# print(arr3)  # Responde true ou false somente, mas eu quero os valores

# arr4 = mtz[mtz % 2 == 0]
# print(arr4)  # Onde for true, mostra os valores para mim, aonde for false, nao mostre).

# Apenas os elementos que tem os valores maiores que a media da minha matriz:
# cond = mtz > mtz.mean()
# print(cond)  # Resposta em true e false
# print(mtz[cond])  # Aonde for true, mostrar. Aonde for false, nao mostrar
# print('\n')

# Trabalhando com padrões textuais:
# arr5 = np.array(['Giovanni', 'Isaque', 'Luiza', 'Raissa'])
# print(np.char.find(arr5,'s'))  # Filtrando os nomes que tem a letra s, resposta: [-1,1,3] (Retornou a posição da letra em que esse critério esta), Giovanni e luiza retornaram -1.
# A posição do nome Isaque e Raissa foi 0 e 3 (Sempre mostra a posição da 1 letra)

# arr6 = arr5[np.char.find(arr5, 's') >= 0]
# print(arr6)

# Boa prática: Escreva tudo em maiusculo ou tudo em minusculo, mais facil depois para procurar ao fazer a busca

# Exercício:

# np.random.seed(5)
# array1 = np.random.randn(10)
# print(array1)

# array2 = array1*100
# print(array2)
# print(array2.astype(int))

# np.random.seed(10)
# array3 = np.random.randint(1, 51, size=(4, 4))
# print(array3)

# list1 = array3.mean(axis=0)
# list2 = array3.mean(axis=1)
# print(list1.max())
# print(list2.max())

# print(np.unique(array3, return_counts=True))

# valores_unicos, contagens = np.unique(array3, return_counts=True)
# valores_aparecem_duas_vezes = valores_unicos[contagens == 2]
# print(valores_aparecem_duas_vezes)

# Ler arquivo csv
#space_data = np.genfromtxt('./space.csv', delimiter=";", dtype=None, names=True, encoding='utf-8')

#sucess = space_data[space_data["Status_Mission"] == "Success"]
#avg = sucess.size / space_data.size
#print(f'{avg}%')

#media = space_data[space_data["Cost"] > 0]['Cost'].mean()
#print(media)

# Crie um filtro para selecionar apenas as linhas onde 'Location' contém 'USA'
#filtro_usa = space_data['Location']
#arr = filtro_usa[np.char.find(filtro_usa,'USA') >= 0]
#print(arr.size)

#filtro_space_x = space_data[space_data['Company_Name'] == 'SpaceX']
#arr = filtro_space_x['Cost'].max()
#print(arr)

#companies = np.unique(space_data["Company_Name"])
#for company in companies:
#    qnt_company = space_data[space_data["Company_Name"] == company].size
#    print(f"{company} : {qnt_company}")

nomes = ('Go', 'Ku', 'Ve', 'Ki')
print(nomes[-1])

