lista_ordens = []
ordem_alta = 0
ordens = 0

print("--- RELATÓRIO DE ENTRADA DE MATERIAL ---")

while True:
    ordem = {}
    ordem['equipamento'] = input(f"digite o nome do equipamento: ").strip()
    ordem['problema'] = input(f"digite qual o problema do equipamento: ").strip()
    ordem['status'] = input(f"digite qual nível de prioridade do equipamento (ALTA-MÉDIA-BAIXA): ").strip().upper()
    while True:
        try:
            ordem['tempo_conserto'] = int(input(f"digite o tempo de conserto do equipamento: "))
            break
        except ValueError:
            print(f"digite o tempo em número!")
    lista_ordens.append(ordem)
    ordens += 1
    continuar = input(f"deseja cadastrar mais algum equipamento? (S/N)").strip().upper()
    if "ALTA" == ordem['status']:
        ordem_alta += 1
    if "N" in continuar:
        break

with open("relatório.txt", "w") as arq:
    arq.write("--- RELATÓRIO DE ACOMPANHAMENTO ---\n\n")
    for ordem in lista_ordens:
        arq.write(f"Equipamento: {ordem['equipamento']} - Problema: {ordem['problema']} - Status: {ordem['status']} - Tempo para Conserto: {ordem['tempo_conserto']} horas\n\nve")
    arq.write(f"\nTOTAL DE OS EM STATUS DE PRIORIDADE: {ordem_alta} - TOTAL DE OS CRIADA(S):  {ordens}")
