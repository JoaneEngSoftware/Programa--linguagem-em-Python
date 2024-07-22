print("Exemplo de captura de excções")
try:
   numero = int(input("Digite um número inteiro: "))
   resultado = 10 / numero
except ValueError as e:
    print(f"Erro de value error: ")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operação finalizada")