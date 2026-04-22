idade = int(input("Digite a sua idade: "))
anos_exp = int(input("Digite a quantidade dos anos de experiência: "))

acesso = idade >= 18 and anos_exp > 2

print(f"Acesso liberado: {acesso}")
