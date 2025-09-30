#Francisco Nogueira de Queiroz, RM: 566309
#Bernardo Moreira Lopes Sousa, RM: 564103

# Lista para armazenar os dados dos usuários cadastrados
usuarios_cadastrados = []

# Lista para armazenar ocorrências reportadas
ocorrencias_reportadas = []

# Função para verificar o risco de enchente
def verificar_risco():
    print("\n--- Verificação de Risco ---")
    print("Informe o risco atual: ")
    print("1. Entre 0 e 49")
    print("2. Entre 50 e 80")
    print("3. Acima de 80")
    escolha = input("Escolha uma opção (1, 2, 3): ")

    if escolha == "1":
        return "Baixo"
    elif escolha == "2":
        return "Médio"
    elif escolha == "3":
        return "Alto"
    else:
        print("Opção inválida. Considerando risco como 'Desconhecido'.")
        return "Desconhecido"

# Função para exibir o semáforo de risco
def cor_do_semaforo(risco):
    if risco == "Baixo":
        return "Verde"
    elif risco == "Médio":
        return "Amarelo"
    elif risco == "Alto":
        return "Vermelho"
    else:
        return "Cinza"

# Função para visualizar o mapa
def visualizar_mapa():
    print("\n--- Mapa Interativo ---")
    print("Localização atual: Latitude -23.5733, Longitude -46.6232")
    print("Veja o mapa em: http://www.openstreetmap.org/?mlat=-23.5733&mlon=-46.6232#map=15/-23.5733/-46.6232")
    print("Acesse o link acima para ver a localização no navegador.")

# Função para atualizar o status de risco
def atualizar_status():
    risco = verificar_risco()
    cor = cor_do_semaforo(risco)
    print(f"\nStatus de Risco Atual: {risco} (Cor do Semáforo: {cor})")

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")

    usuario = {
        "Nome": nome,
        "E-mail": email,
        "Telefone": telefone,
        "Endereço": endereco
    }

    usuarios_cadastrados.append(usuario)
    print("\nCadastro realizado com sucesso!")

# Função para reportar uma ocorrência
def reportar_ocorrencia():
    print("\n--- Reportar Ocorrência ---")
    descricao = input("Descreva a ocorrência (ex: alagamento, deslizamento, etc.): ")
    local = input("Informe o local da ocorrência: ")

    ocorrencia = {
        "Descrição": descricao,
        "Local": local
    }

    ocorrencias_reportadas.append(ocorrencia)
    print("\nOcorrência registrada com sucesso!")

# Função para mostrar todas as ocorrências reportadas
def mostrar_ocorrencias():
    print("\n--- Ocorrências Reportadas ---")
    if ocorrencias_reportadas:
        indice = 1
        for ocorrencia in ocorrencias_reportadas:
            print(f"\nOcorrência {indice}:")
            print(f"Descrição: {ocorrencia['Descrição']}")
            print(f"Local: {ocorrencia['Local']}")
            indice += 1
    else:
        print("Nenhuma ocorrência foi reportada ainda.")

# Funçao de ver rotas de fuga
def ver_rotas_de_fuga():
    print("\n--- Rotas de Fuga ---")
    print("Estas são rotas seguras próximas à sua localização:")
    print("1. Rua São Paulo → Av. Central → Escola Municipal (Ponto de apoio)")
    print("2. Rua das Flores → Praça Verde → Estádio Regional (Abrigo temporário)")
    print("3. Av. das Águas → Rua da Esperança → Igreja Comunitária (Ponto de encontro)")
    print("Siga as orientações da Defesa Civil local e evite áreas alagadas.")

# Função para mostrar o menu principal
def menu():
    while True:
        ver_menu = input("\nDeseja ver o menu de opções? (s/n): ")
        if ver_menu != 's':
            print("Ok, o sistema continuará executando em segundo plano.")
            break

        print("\n------ Monitor de Enchentes ------")
        print("1. Verificar Risco de Enchente")
        print("2. Visualizar Mapa")
        print("3. Cadastrar Novo Usuário")
        print("4. Reportar Ocorrência")
        print("5. Mostrar Ocorrências Reportadas")
        print("6. Ver Rotas de Fuga")
        print("7. Sair")

        opcao = input("Escolha uma opção (1-7): ")

        if opcao == "1":
            atualizar_status()
        elif opcao == "2":
            visualizar_mapa()
        elif opcao == "3":
            cadastrar_usuario()
        elif opcao == "4":
            reportar_ocorrencia()
        elif opcao == "5":
            mostrar_ocorrencias()
        elif opcao == "6":
            ver_rotas_de_fuga()
        elif opcao == "7":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Tela inicial
print("Bem-vindo ao Alerta Brasil+!")
print("Antes de continuar, por favor cadastre-se.")

while not usuarios_cadastrados:
    cadastrar_usuario()
menu()
