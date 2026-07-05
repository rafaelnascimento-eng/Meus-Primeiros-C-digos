### Auditoria Energética Residencial com Python ###

Este é um script em Python desenvolvido para automatizar o processo de levantamento de carga e cálculo de consumo elétrico residencial mensal ($kWh/\text{mês}$). O sistema permite o cadastro dinâmico de múltiplos aparelhos, processa os dados individualmente e gera um relatório com o consumo total da residência.

## Funcionalidades ##

* **Cadastro Dinâmico:** Loop interativo que permite cadastrar quantos aparelhos forem necessários sem interrupção.
* **Estrutura de Dados Robusta:** Armazenamento dos aparelhos em dicionários encapsulados dentro de uma lista principal.
* **Cálculo Automatizado:** Processamento do consumo mensal com base na potência ($kW$) e horas de uso diário.
 
## Tecnologias Utilizadas ##

* **Python 3** (Controle de fluxo com `while True`/`break`, laço `for`, manipulação de listas e dicionários)
* **Git & GitHub** (Versionamento de código)

## Como Rodar o Projeto ##

1. Certifique-se de ter o Python 3 instalado.
2. Execute o script no terminal:
   ```bash
   python3 auditoria.py
