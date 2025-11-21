# NotaryAI - Protótipo de Lógica em Python (Global Solution)

## 1. 🚀 Visão Geral do Projeto

O **NotaryAI** é um assistente virtual (chatbot) projetado para **desmistificar e simplificar** o processo burocrático de registro de imóveis no Brasil. Este protótipo, desenvolvido em **Python, foca na demonstração dos requisitos de **lógica de programação** para simular as principais funcionalidades do sistema: Cadastro, Solicitação de Pedidos e Consulta de Andamento.

O projeto se alinha ao tema **"O Futuro do Trabalho"**, automatizando tarefas repetitivas e fornecendo orientação clara ao cidadão, tornando os serviços de cartório mais acessíveis e justos.

---

## 2. 📋 Requisitos Técnicos Cumpridos (Python)

O script **`sistema_notaryai_bot.py`** demonstra o uso dos seguintes conceitos básicos da linguagem, :

| Requisito | Demonstração no Código |
| :--- | :--- |
| **Variáveis e Tipos de Dados** | Uso de `int`, `str`, **Listas** (`DB_USUARIOS`) e **Dicionários** (`BASE_PROTOCOLO`). |
| **Manipulação de Listas** | Adição de novos usuários à `DB_USUARIOS` e iteração sobre o `BASE_CONHECIMENTO_MENU`. |
| **Manipulação de Strings** | Uso de `.strip()`, `.replace()`, `.lower()`, `.upper()` e concatenação (`f"{...}"`) para formatação e validação de texto (ex: `validar_cpf`). |
| **Funções (Com Parâmetros)** | Múltiplas funções (`cadastrar_usuario`, `validar_cpf`, `consultar_chatbot`) com parâmetros (`primeiro_acesso`) e retorno de valores (`bool`). |
| **Estrutura de Controle (IF/ELIF/ELSE)** | Usada na validação de dados, na lógica de andamento do pedido (`consultar_andamento_pedido`) e no controle do fluxo do menu. |
| **Estrutura de Controle (WHILE/FOR)** | O `WHILE True` é usado para o loop principal do menu e o `FOR` é usado para iterar sobre a lista de usuários e exibir o menu de consultas. |

---

## 3. 🗺️ Estrutura de Fluxo do Sistema

O programa adota um fluxo de acesso estrito:

1.  **Início Obrigatório:** A execução do script começa diretamente na função **Cadastro Obrigatório**. Um cadastro bem-sucedido é necessário para entrar no menu principal.
2.  **Menu Principal (Usuário Padrão):** Focado em serviços essenciais para o cidadão.
3.  **🔒 Área Restrita (ADMIN):** Contém as funcionalidades de gestão de dados e cadastros adicionais.

### Funcionalidades do Menu Principal

| Opção | Ação | Descrição |
| :---: | :--- | :--- |
| **1** | Fazer Novo Pedido | Simula o envio de uma solicitação e gera um novo **Protocolo**. |
| **2** | Consultar Andamento | Permite consultar um protocolo e retorna o **Status** (`Em Análise`, `Pronto para Retirada`, etc.), com orientação sobre o próximo passo. |
| **3** | Consultar Assistente | Acesso ao menu de **FAQ** e às opções de **Contato** (`Telefone`, `Falar com Escrevente`). |
| **4** | **🔒 Cadastro Adicional** | Permite adicionar novos registros ao sistema (operação de administrador). |
| **5** | **🔒 Listar Usuários** | Exibe todos os registros de usuários (operação de administrador). |
| **6** | Sair do Programa | Encerra a execução do script. |

---

## 4. ⚙️ Como Executar

Este script é **autônomo** e não possui dependências, utilizando apenas os recursos nativos do Python 3.

1.  **Salve** o código fornecido em um arquivo chamado **`sistema_notaryai_bot.py`**.
2.  **Abra o Terminal** (ou prompt de comando) na pasta onde o arquivo foi salvo.
3.  **Execute** o script usando o comando:

```bash
python sistema_notaryai_bot.py
Protocolos de Teste (Opção 2)Para testar a lógica de andamento do pedido, utilize um dos seguintes protocolos:999000: Retorna status Em Análise.
555000: Retorna status Pronto para Retirada.
100000: Retorna status Pendente (Ação necessária).
#=============Integrantes==================#
Wenderson da Silva Santos,RM: 567847
Douglas Taveira Vilella Roberto,RM: 567846
Igor Davi Avelar Rosa Cesário,RM: 568163
