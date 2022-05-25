import random

teste = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

times = {
  "sao-paulo": "Morumbi",
  "real-madrid": "Bernabeu",
  "corinthians": "Impressora",
  "palmeiras": "Chiqueiro"
}

#Cria uma lista com as chaves do dicionário, chaves são as palavras do lado esquerdo dos :
palavras = list(times.keys())
#Sorteia uma das palavras contidas na lista de palavras
palavra = random.choice(palavras)
print(palavra)
#Passa a palavra para pegar a dica
print(times.get(palavra))
#A função pop remove o item do dicionário passando o key como parâmetro
times.pop(palavra)
print(times)
print('-----')

print('1')
print('2')

