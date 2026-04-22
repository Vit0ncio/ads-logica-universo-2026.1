total_fatias = int(input("Digite o total de fatias: "))
programadores = int(input("Digite o total de programadores: "))

fatias_por_pessoa = int(total_fatias / programadores)
sobra = total_fatias % programadores

print(f"Cada pessoa comerá {fatias_por_pessoa}, sobrando {sobra} fatias na caixa")
