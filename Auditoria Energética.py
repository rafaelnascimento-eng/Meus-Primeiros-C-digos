print(f"--- CADASTRO DE APARELHOS ---")

lista_aparelhos = []

while True:
    aparelho = {}
    aparelho["nome"] = input(f"Digite o nome do aparelho:").strip()
    aparelho["potência"] = float(input("Digite a potência do aparelho:"))
    aparelho["horas_uso"] = int(input("Digite a quantidade de tempo de uso do aparelho:"))
    
    lista_aparelhos.append(aparelho)

    continuar = input(f"Deseja cadastrar outro aparelho?").upper()
    if "N" in continuar:
        break

consumo_total = 0.0

for aparelho in lista_aparelhos:
    consumo_aparelho = aparelho['potência'] * aparelho['horas_uso'] * 30
    consumo_total += consumo_aparelho
    print(f"{aparelho['nome']} - {consumo_aparelho} kWh")

print(f"--- CONSUMO TOTAL DA RESIDÊNCIA: {consumo_total:.2f} kWh ---")

