nome = input("Digite seu nome: ")
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = 2026
altura = float(input("Digite a sua altura (em metros): "))

idade = ano_atual - ano_nasc

print(
    f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído."
)
