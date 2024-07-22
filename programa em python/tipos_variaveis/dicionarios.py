# Criando um dicionário de exemplo
pessoa = {"nome": "Joane", "idade": 21, "cidade": "Campo Formoso"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Jesus"
print("Sobrenome:", pessoa ["sobrenome"])
print("Meu dicionário de exemplo:", pessoa)

pessoa["idade"] = 22
print("Idade atualizada:", pessoa["idade"])

#Removendo um por chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()
chaves = pessoa.keys()
print('chaves do dicionário:', chaves)
print('Primeira chave:', chaves[0])

# Método values
valores = list(pessoa.values())
print('Valores do dicionários:', valores)
print('primeiro valor do dicionários:', valores[0])

# Método items
itens = pessoa.items()
print('Pares chave-valor do dicionário:', itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][2]))