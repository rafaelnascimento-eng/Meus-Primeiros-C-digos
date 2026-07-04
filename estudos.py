medidor = {"id": 7742, "cliente": "Indústria ABC", "tensão_nominal": 380, "status": "Operacional"}

medidor["status"] = "Manutenção"

medidor["tecnico"] = "Rafael"

print(medidor.get("localização", "Gaveta nao encontrada"))