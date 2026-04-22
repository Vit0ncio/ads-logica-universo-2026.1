tamanho_mb = float(input("Digite o tamanho do arquivo em Megabytes (MB): "))
vel_mbps = int(
    input("Digite a velocidade da internet em Megabits por segundo (Mbps): ")
)

tempo_segundos = int(tamanho_mb / (vel_mbps / 8))
min_inteiros = int(tempo_segundos / 60)
segundos_restantes = tempo_segundos

print(f"{min_inteiros} minutos e {segundos_restantes} segundos")
