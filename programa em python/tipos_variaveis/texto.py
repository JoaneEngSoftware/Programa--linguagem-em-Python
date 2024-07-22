# Declaração
nome_completo = "Joane Isabel"

nome_completo_aspas = """Joane
Isabel"""

nome_completo_quebra = "Joane \
Isbel"
    
nome = "Joane"
sobrenome = "Isabel"
    
    # Formatação
print("Nome completo (la forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Joane" + "Isabel")
print("Nome completo (4a forma):" + "Joane", "Isabel")
print("Nome completo (5a forma):". nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (9a forma): {} {}".format(sobrenome, nome))