# ==============================================================================
# INFORMAÇÕES OBRIGATÓRIAS (Conforme solicitado no request.pdf)
# Integrante: Wenderson da Silva Santos - RM: 567847
# Integrante: [Douglas Taveira Vilella Roberto - RM: 567846 ]
#Integrante: [Igor Davi Avelar Rosa Cesário	RM : 568163  ]
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BASE DE DADOS E VARIÁVEIS GLOBAIS
# ------------------------------------------------------------------------------

DB_USUARIOS = []
proximo_id = 1

# Base de protocolos de pedido para simular o andamento
BASE_PROTOCOLO = {
    "999000": {"status": "Em Análise", "descricao": "Seu pedido foi recebido e está em fase de verificação documental."},
    "555000": {"status": "Pronto para Retirada", "descricao": "Seu documento está pronto. Dirija-se ao guichê B do cartório para a retirada."},
    "100000": {"status": "Pendente", "descricao": "Falta o pagamento da taxa ITBI. O processo está parado. Contate a prefeitura."},
}

# Base de Conhecimento para o menu de consulta (FAQ)
BASE_CONHECIMENTO_MENU = [
    {"opcao": "ITBI (Imposto de Transmissao)", "chave": "itbi", "resposta": "O ITBI e um imposto municipal obrigatorio para transferencia de propriedade."},
    {"opcao": "Matricula do Imovel", "chave": "matricula", "resposta": "A matricula e a certidao de nascimento do imovel, contendo todo o historico."},
    {"opcao": "Busca de Cartorio/Localizacao", "chave": "cartorio", "resposta": "A busca de cartorio e feita por localizacao para o cartorio da circunscricao."}
]

# ------------------------------------------------------------------------------
# 2. FUNÇÕES DE UTILIDADE E VALIDAÇÃO
# ------------------------------------------------------------------------------

def _pausar():
    """Funcao auxiliar para pausar a execucao."""
    input("\nPressione Enter para continuar...")

def _validar_string_vazia(texto: str) -> bool:
    """Verifica se uma string e vazia apos remover espacos."""
    if len(texto.strip()) > 0:
        return True
    else:
        return False

def validar_cpf(cpf_str: str) -> bool:
    """Valida o formato do CPF (tamanho e se e numerico)."""
    cpf_limpo = cpf_str.strip().replace('.', '').replace('-', '')
    e_numero = True
    for caractere in cpf_limpo: 
        if caractere not in '0123456789':
            e_numero = False
            break

    if len(cpf_limpo) == 11 and e_numero:
        return True
    else:
        return False

# ------------------------------------------------------------------------------
# 3. FUNÇÕES DE CADASTRO E ADMINISTRAÇÃO
# ------------------------------------------------------------------------------

def cadastrar_usuario(primeiro_acesso: bool):
    """
    Gerencia a entrada de dados do usuário.
    Retorna True se o cadastro for bem-sucedido, False caso contrário.
    """
    global proximo_id
    
    if primeiro_acesso:
        print("\n\n=== 🚀 BEM-VINDO - CADASTRO OBRIGATÓRIO 📋 ===")
        print("Preencha para acessar o sistema.")
    else:
        print("\n\n=== 🔒 ÁREA RESTRITA - CADASTRO ADICIONAL 📋 ===")
    
    nome = input("Nome Completo: ")
    cpf = input("CPF (apenas numeros): ")
    perfil = input("Perfil (Cidadao/Profissional): ").strip().capitalize()
    
    if not _validar_string_vazia(nome) or not _validar_string_vazia(cpf):
        print("\n❌ ERRO: Nome e CPF sao obrigatorios.")
        _pausar()
        return False
    
    if not validar_cpf(cpf):
        print("\n❌ ERRO: CPF invalido. Verifique o formato.")
        _pausar()
        return False

    # Habilidades: Opcional
    habilidades_lista = []
    resposta_habilidade = input("Deseja adicionar habilidades? (s/n): ").strip().lower()
    
    if resposta_habilidade == 's':
        print("\nAdicione suas Habilidades (digite 'fim' para terminar):")
        while True:
            habilidade = input(f"Habilidade #{len(habilidades_lista) + 1}: ").strip()
            if habilidade.lower() == 'fim':
                break
            elif _validar_string_vazia(habilidade):
                habilidades_lista.append(habilidade.capitalize())
    
    novo_usuario = {
        "id": proximo_id,
        "nome": nome,
        "cpf": cpf,
        "perfil": perfil,
        "habilidades": habilidades_lista
    }
    
    DB_USUARIOS.append(novo_usuario)
    proximo_id = proximo_id + 1
    
    print(f"\n✅ CADASTRO CONCLUÍDO! ID: {novo_usuario['id']}.")
    _pausar()
    return True

def listar_usuarios():
    """Exibe todos os usuários cadastrados (Funcao de Administracao)."""
    print("\n\n=== 🔒 ÁREA RESTRITA - LISTA DE USUÁRIOS 🔒 ===")
    
    if not DB_USUARIOS:
        print("\nNenhum usuario cadastrado ainda.")
    else:
        for usuario in DB_USUARIOS:
            print("-" * 30)
            print(f"ID: {usuario['id']} | Nome: {usuario['nome']}")
            print(f"Perfil: {usuario['perfil']} | CPF: {usuario['cpf']}")
            print(f"Habilidades: {' | '.join(usuario['habilidades']) if usuario['habilidades'] else 'Nenhuma'}")
        print("-" * 30)
    
    _pausar()
    
# ------------------------------------------------------------------------------
# 4. FUNÇÕES DE SERVIÇO (USUÁRIO PADRÃO)
# ------------------------------------------------------------------------------

def fazer_novo_pedido():
    """Simula o envio de um novo pedido de serviço."""
    print("\n\n=== 📝 NOVO PEDIDO DE SERVIÇO ===")
    
    tipo_servico = input("Qual tipo de serviço deseja (ex: Registro, Averbação, Certidão): ").strip()
    documentos_necessarios = "Matrícula, RG, CPF, Certidão de Casamento." # Simulação
    
    print(f"\n➡️ Para '{tipo_servico}', os documentos necessários são: {documentos_necessarios}")
    print("O processamento pode levar até 10 dias úteis.")
    
    # Gera um protocolo simulado
    novo_protocolo = str(proximo_id * 100000)
    
    print(f"\n✅ Pedido registrado com sucesso!")
    print(f"Seu Protocolo de Acompanhamento é: {novo_protocolo}")
    
    # Adiciona o novo protocolo à base de dados para simulação
    BASE_PROTOCOLO[novo_protocolo] = {"status": "Em Análise", "descricao": "Seu pedido foi recebido e está em fase de verificação inicial."}
    
    _pausar()

def consultar_andamento_pedido():
    """Consulta o andamento de um pedido usando um protocolo."""
    print("\n\n=== 🔍 CONSULTA DE ANDAMENTO DO PEDIDO ===")
    protocolo = input("Digite o número do Protocolo (ex: 999000 ou 555000): ").strip()
    
    print("-" * 30)
    
    if protocolo in BASE_PROTOCOLO:
        status_pedido = BASE_PROTOCOLO[protocolo]["status"]
        descricao = BASE_PROTOCOLO[protocolo]["descricao"]
        
        print(f"Protocolo: {protocolo}")
        print(f"Status Atual: {status_pedido.upper()}")
        print(f"Descrição: {descricao}")
        
        # Lógica de decisão para o usuário
        if status_pedido == "Pronto para Retirada":
            print("\n🎉 O pedido está PRONTO! Você já pode retirá-lo no cartório.")
        elif status_pedido == "Em Análise":
            print("\n⏳ O pedido está sendo processado. Aguarde novas atualizações.")
        elif status_pedido == "Pendente":
            print("\n⚠️ AÇÃO NECESSÁRIA! Resolva a pendência para prosseguir.")
        
        if status_pedido == "Pendente" or status_pedido == "Em Análise":
             print("\n📞 Em caso de dúvidas sobre o andamento, contate a telefonista no (11) 9999-8888.")
            
    else:
        print(f"❌ ERRO: Protocolo '{protocolo}' não encontrado na nossa base.")
        print("Verifique o número ou utilize a opção 'Falar com Escrevente' para ajuda.")
        
    print("-" * 30)
    _pausar()

def consultar_chatbot():
    """Funcao que gerencia o menu de consulta e contato (FAQ)."""
    while True:
        print("\n\n=== 🤖 ASSISTENTE NOTARYAI - FAQ E CONTATO 🤖 ===")
        print("Escolha uma opcao de consulta:")
        
        contador = 1
        for item in BASE_CONHECIMENTO_MENU: 
            print(f"{contador}. {item['opcao']}")
            contador = contador + 1

        total_opcoes_fixas = len(BASE_CONHECIMENTO_MENU)
        print(f"{total_opcoes_fixas + 1}. Telefone pra Contato / Email")
        print(f"{total_opcoes_fixas + 2}. Falar com Escrevente (Encaminhamento)")
        print(f"{total_opcoes_fixas + 3}. Sair da Consulta")
        print("---------------------------------------------")

        escolha = input("Digite o numero da opcao: ").strip()

        if escolha.isdigit():
            escolha_int = int(escolha)
        else:
            escolha_int = 0

        resposta_final = ""
        
        if escolha_int >= 1 and escolha_int <= total_opcoes_fixas:
            item_escolhido = BASE_CONHECIMENTO_MENU[escolha_int - 1]
            resposta_final = f"FAQ - {item_escolhido['opcao']}:\n{item_escolhido['resposta']}"
        elif escolha_int == total_opcoes_fixas + 1:
            resposta_final = "INFORMACOES DE CONTATO:\nTelefone: (11) 9999-8888 | Email: atendimento@notaryai.com.br"
        elif escolha_int == total_opcoes_fixas + 2:
            resposta_final = "ENCAMINHAMENTO:\nUm profissional (Escrevente) sera notificado para te retornar em ate 48h. Forneca seu nome completo e telefone para contato."
        elif escolha_int == total_opcoes_fixas + 3:
            print("\nRetornando ao Menu Principal...")
            _pausar()
            break 
        else:
            resposta_final = "Opcao invalida. Por favor, digite um numero valido do menu."
        
        print("\n--- Resposta do NotaryAI ---")
        print(resposta_final)
        print("---------------------------\n")
        
        if not (escolha_int == total_opcoes_fixas + 3):
             _pausar()


# ------------------------------------------------------------------------------
# 5. FUNÇÃO PRINCIPAL DO PROGRAMA (MENU)
# ------------------------------------------------------------------------------

def menu_principal():
    """Gerencia o fluxo de execucao, começando pelo cadastro obrigatorio."""
    
    # 1. ETAPA OBRIGATÓRIA INICIAL: CADASTRO
    cadastro_concluido = cadastrar_usuario(primeiro_acesso=True)

    if not cadastro_concluido:
        print("\nNao foi possivel iniciar o sistema sem um cadastro valido.")
        return

    # 2. LOOP DO MENU PRINCIPAL (APÓS CADASTRO)
    while True:
        print("\n\n=============================================")
        print("  SISTEMA NOTARYAI - MENU PRINCIPAL          ")
        print("=============================================")
        print("1. Fazer Novo Pedido")
        print("2. Consultar Andamento do Pedido")
        print("3. Consultar Assistente (FAQ / Contato)")
        print("---------------------------------------------")
        print("🔒 AREA RESTRITA (ADMIN)")
        print("4. Cadastrar Novo Usuario (Adicional)")
        print("5. Listar Usuarios Cadastrados")
        print("---------------------------------------------")
        print("6. Sair do Programa")
        print("=============================================")
        
        escolha = input("Escolha uma opcao: ").strip()
        
        if escolha == '1':
            fazer_novo_pedido()
        elif escolha == '2':
            consultar_andamento_pedido()
        elif escolha == '3':
            consultar_chatbot()
        elif escolha == '4':
            cadastrar_usuario(primeiro_acesso=False) # Opção de Cadastro Adicional na Área Restrita
        elif escolha == '5':
            listar_usuarios() # Opcao de Listar na Área Restrita
        elif escolha == '6':
            print("\nObrigado por utilizar o simulador NotaryAI. Encerrando...")
            break
        else:
            print("\nOpcao invalida. Tente novamente.")
            _pausar()


# Bloco de execucao principal
if __name__ == '__main__':
    menu_principal()