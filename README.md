### Auditoria Energética Residencial com Python ###

Este é um script em Python desenvolvido para automatizar o processo de levantamento de carga e cálculo de consumo elétrico residencial mensal ($kWh/\text{mês}$). O sistema permite o cadastro dinâmico de múltiplos aparelhos, processa os dados individualmente e gera um relatório com o consumo total da residência.

## Funcionalidades ##

* **Cadastro Dinâmico:** Loop interativo que permite cadastrar quantos aparelhos forem necessários sem interrupção.
* **Estrutura de Dados Robusta:** Armazenamento dos aparelhos em dicionários encapsulados dentro de uma lista principal.
* **Cálculo Automatizado:** Processamento do consumo mensal com base na potência ($kW$) e horas de uso diário.
 
## Tecnologias Utilizadas ##

* **Python 3** (Controle de fluxo com `while True`/`break`, laço `for`, manipulação de listas e dicionários)
* **Git & GitHub** (Versionamento de código)
*  ## Evolução: Blindagem de Dados e Tratamento de Erros (try/except)

Na versão mais recente do script (`Auditoria_Energetica_Blindada.py`), o sistema recebeu uma camada de segurança profissional para mitigar o erro humano na entrada de dados:

* **Tratamento de Exceções (`try` / `except ValueError`):** Se o usuário digitar letras ou símbolos inválidos nos campos de **Potência (kW)** ou **Horas de Uso**, o sistema não quebra ("crasha"). Ele captura o erro, exibe uma mensagem amigável e solicita o dado novamente.
* **Validação de Fluxo Textual:** A pergunta de continuidade (`S/N`) foi blindada com um laço de repetição que insiste na resposta correta, impedindo que o programa feche por comandos inválidos.
* **Laços Aninhados (`while` dentro de `while`):** Garantem que o usuário só avance no cadastro após preencher cada campo de forma 100% correta, sem perder o progresso do que já foi digitado.

## Como Rodar o Projeto ##

1. Certifique-se de ter o Python 3 instalado.
2. Execute o script no terminal:
   ```bash
   python3 Auditoria_Energetica_Blindada.py
