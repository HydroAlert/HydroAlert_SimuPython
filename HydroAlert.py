"""
Fernando Bellegarde - RM564169
Henrique Castro - RM564560
Otavio Inaba - RM565003
"""
# coding=utf-8
# Define a codificação do arquivo como UTF-8 para suportar caracteres especiais no terminal.

from datetime import datetime # Importa a classe datetime para trabalhar com datas e horas.
import uuid # Importa a biblioteca uuid para gerar ids únicos e aleatorios.

# Listas globais para armazenar os dados do sistema (Simula banco de dados local).
usuarios_cadastrados = []
sensores_cadastrados = []
alertas = []

# Mensagens padrão para os diferentes níveis de alerta.
mensagemEmergencia = "Sua região está em alerta de emergência! \nEvacue a área! \nClique no link a seguir para calcular uma rota de fuga. \nhttps://hydroalert.com.br/rotafuga"
mensagemAtencao = "Sua região está em alerta de atenção! \nProcure abrigo e fique atento às atualizações."
mensagemObservacao = "Sua região está em alerta de observação! \nFique atento às atualizações."

# --- Base do Sistema ---
def main():
    """Função principal que inicia o sistema."""
    exibirMensagemInicial() # Exibe a mensagem de boas-vindas.
    menu() # Inicia o loop do menu principal.

def menu():
    """Exibe o menu principal e gerencia a navegação entre as opções."""
    while True: # Loop infinito para manter o menu ativo até que o usuário saia.
        print('\n-----------Menu-----------')
        print('Opção 1: Gestão de usuários')
        print('Opção 2: Gestão de sensores')
        print('Opção 3: Ativar sensores')
        print('Opção 4: Visualizar alertas')
        print('Opção 5: Gerar alerta manual')
        print('Opção 6: Sair do sistema')
        opicao = input('\nDigite a sua opção: ') # Salva a opção do usuário.

        # Usa match/case para direcionar para a função correspondente à opção escolhida.
        match opicao:
            case '1':
                gestaoUsuarios() # Chama a gestão de usuários.
            case '2':
                gestaoDeSensores() # Chama a gestão de sensores.
            case '3':
                ativarSensoresInput() # Chama a ativação de sensores.
            case '4':
                visualizarAlertasInput() # Chama a visualização de alertas.
            case '5':
                gerarAlertaManualInput() # Chama a geração manual de alerta.
            case '6':
                print("Encerrando o sistema. Até logo!")
                exit() # Encerra a execução do programa.
            case _:
                print("Digite uma opção válida.") # Caso o usuario digite algo diferente das opções.

def exibirMensagemInicial():
    """Exibe a mensagem de boas-vindas do sistema."""
    print("Bem-vindo ao HydroAlert!")

# --- Usuários - Frontend ---
def gestaoUsuarios():
    """Menu de gestão de usuários."""
    while True: # Loop para o submenu de usuários.
        print("\nOpção 1: Cadastrar usuário")
        print("Opção 2: Visualizar usuários")
        print("Opção 3: Remover usuários")
        print("Opção 4: Voltar ao menu principal")
        resp = input('\nDigite sua opção: ') # Salva a opção do usuário.

        # Direciona para a função de frontend correspondente.
        if resp == '1':
            cadastrarUsuarioInput()
            break # Sai do loop do submenu após a ação.
        elif resp == '2':
            visualizarUsuariosInput()
            break # Sai do loop do submenu após a ação.
        elif resp == '3':
            removerUsuarioInput()
            break # Sai do loop do submenu após a ação.
        elif resp == '4':
            menu() # Volta para o menu principal.
            break # Sai do loop do submenu.
        else:
            print('Digite apenas o número das opções.') # Caso o usuario digite algo diferente das opções.

def cadastrarUsuarioInput():
    """Coleta dados do usuário via input e chama a função de backend para cadastrar."""
    nome = input('\nDigite seu nome: ') # Coleta nome.
    endereco = input('Digite seu endereço: ') # Coleta endereço.
    telefone = input('Digite seu telefone: ') # Coleta telefone.

    # Chama a função de backend para realizar o cadastro e recebe o usuário criado.
    usuario = cadastrarUsuario(nome, endereco, telefone)

    print(f"Usuário {usuario['nome']} cadastrado com sucesso!") # Exibe feedback do usuario criado.

    # Loop para perguntar se deseja cadastrar outro ou voltar.
    while True:
        resp = input('Cadastrar outro usuário (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            cadastrarUsuarioInput() # Chama a si mesma para novo cadastro.
            break
        elif resp == 'm':
            menu() # Volta para o menu principal.
            break
        else:
            print('Digite apenas s ou m') # Caso o usuario digite algo diferente das opções.

def visualizarUsuariosInput():
    """Obtém a lista de usuários do backend e a exibe no terminal."""
    usuarios = obterUsuarios() # Chama a função de backend para obter a lista.

    if not usuarios:
        print("\nNenhum usuário cadastrado.") # Exibe mensagem se a lista estiver vazia.
    else:
        print("\nUsuários cadastrados até agora:")
        # Itera sobre a lista e exibe os detalhes de cada usuário.
        for usuario in usuarios:
            print(f"id: {usuario['id']}, Nome: {usuario['nome']}, Endereço: {usuario['endereco']}, Telefone: {usuario['telefone']}")

    # Loop para perguntar se deseja voltar ao menu.
    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu() # Volta para o menu principal.
            break
        else:
            print("Digite 's' para voltar ao menu.") # Caso o usuario digite algo diferente das opções.

def removerUsuarioInput():
    """Coleta o ID do usuário a ser removido e chama a função de backend."""
    usuarios = obterUsuarios() # Obtém a lista para verificar se há usuários.
    if not usuarios:
        print("\nNão há usuários cadastrados para remover.")
        menu()
        return # Sai da função se não houver usuários.

    id = input('\nDigite o id do usuário que deseja deletar: ') # Coleta o ID (Frontend).

    # Chama a função de backend para remover e recebe o usuário removido (ou None).
    usuario_removido = removerUsuario(id)

    if usuario_removido:
        print(f"\nUsuário '{usuario_removido['nome']}' removido com sucesso!") # Feedback de sucesso.
    else:
        print(f"\nUsuário não encontrado com o id {id}.") # Feedback de não encontrado.

    # Loop para perguntar se deseja remover outro ou voltar.
    while True:
        resp = input('Remover outro usuário (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            removerUsuarioInput() # Chama a si mesma para nova remoção.
            break
        elif resp == 'm':
            menu() # Volta para o menu principal.
            break
        else:
            print('Digite apenas s ou m') # Caso o usuario digite algo diferente das opções.

# --- Usuários - Backend ---
def cadastrarUsuario(nome, endereco, telefone):
    """Cria um novo dicionário de usuário e o adiciona à lista global."""
    novoUsuario = {
        "id": uuid.uuid4(), # Gera um ID único e aleatório.
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
    }
    usuarios_cadastrados.append(novoUsuario) # Adiciona o novo usuário à lista.
    return novoUsuario # Retorna o usuário criado.

def obterUsuarios():
    """Retorna a lista completa de usuários cadastrados."""
    return usuarios_cadastrados

def removerUsuario(id):
    """Busca um usuário pelo ID e o remove da lista global."""
    for usuario in usuarios_cadastrados:
        if str(usuario['id']) == id: # Compara o ID recebido com o do usuario atual do loop.
            usuarios_cadastrados.remove(usuario) # Remove o usuário da lista.
            return usuario # Retorna o usuário removido.
    return None # Retorna None se o usuário não for encontrado.

# --- Sensores - Frontend ---
def gestaoDeSensores():
    """Menu de gestão de sensores."""
    while True: # Loop para o submenu de sensores.
        print('\nOpcão 1: Adicionar sensores')
        print('Opcão 2: Remover sensores')
        print('Opcão 3: Visualizar sensores')
        print('Opcão 4: Voltar ao menu principal')
        resp = input('\nDigite sua opção: ') # Salva a opção do usuário.

        # Direciona para a função de frontend correspondente.
        if resp == '1':
            adicionarSensorInput()
            break # Sai do loop do submenu.
        elif resp == '2':
            removerSensoresInput()
            break # Sai do loop do submenu.
        elif resp == '3':
            visualizarSensoresInput()
            break # Sai do loop do submenu.
        elif resp == '4':
            menu() # Volta para o menu principal.
            break # Sai do loop do submenu.
        else:
            print('Digite apenas as opções acima!')

def adicionarSensorInput():
    """Coleta dados do sensor via input, incluindo validação dos níveis de alerta."""
    nomeSEN = input('\nDigite o nome do sensor: ') # Coleta nome.
    Local = input('Digite a localização: ') # Coleta localização.

    # Loop e validação para o valor de alerta de OBSERVAÇÃO (entre 0 e 100).
    while True:
        alertaOBS_input = input('Digite o valor de alerta de nível OBSERVAÇÃO (Entre 0 e 100): ')
        if alertaOBS_input.isdigit(): # Verifica se a entrada é um número.
            alertaOBS = int(alertaOBS_input)
            if 0 <= alertaOBS <= 100: # Verifica se está dentro do intervalo.
                break # Sai do loop de validação se for válido.
            else:
                print("Valor de alerta OBSERVAÇÃO deve estar entre 0 e 100.")
        else:
            print("Digite um número inteiro válido para o valor de alerta OBSERVAÇÃO.")

    # Loop e validação para o valor de alerta de ATENÇÃO (entre 0 e 100).
    while True:
        alertaATE_input = input('Digite o valor de alerta de nível ATENÇÃO (Entre 0 e 100): ')
        if alertaATE_input.isdigit():
            alertaATE = int(alertaATE_input)
            if 0 <= alertaATE <= 100:
                break
            else:
                print("Valor de alerta ATENÇÃO deve estar entre 0 e 100.")
        else:
            print("Digite um número inteiro válido para o valor de alerta ATENÇÃO.")

    # Loop e validação para o valor de alerta de EMERGÊNCIA (entre 0 e 100).
    while True:
        alertaEME_input = input('Digite o valor de alerta de nível EMERGÊNCIA (Entre 0 e 100): ')
        if alertaEME_input.isdigit():
            alertaEME = int(alertaEME_input)
            if 0 <= alertaEME <= 100:
                break
            else:
                print("Valor de alerta EMERGÊNCIA deve estar entre 0 e 100.")
        else:
            print("Digite um número inteiro válido para o valor de alerta EMERGÊNCIA.")

    # Chama a função de backend para adicionar o sensor.
    sensor = adicionarSensor(nomeSEN, Local, alertaOBS, alertaATE, alertaEME)

    print(f"Sensor {sensor['Nome']} cadastrado com sucesso!\n") # Feedback.

    # Loop para perguntar se deseja cadastrar outro ou voltar.
    while True:
        resp = input('Cadastrar outro sensor (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            adicionarSensorInput() # Chama a si mesma.
            break
        elif resp == 'm':
            menu() # Volta para o menu principal.
            break
        else:
            print('Digite apenas s ou m')

def removerSensoresInput():
    """Coleta o ID do sensor a ser removido e chama a função de backend."""
    sensores = obterSensores() # Obtém a lista para verificar se há sensores.
    if not sensores:
        print("\nNão há sensores cadastrados para remover.")
        menu()
        return # Sai da função se não houver sensores.

    id = input("\nDigite o id do sensor que deseja remover: ") # Coleta o ID.

    # Chama a função de backend para remover.
    sensor_removido = removerSensor(id)

    if sensor_removido:
        print(f"Sensor '{sensor_removido['Nome']}' removido com sucesso!") # Feedback de sucesso.
    else:
        print("Sensor não encontrado com os dados informados.") # Feedback de não encontrado.

    # Loop para perguntar se deseja remover outro ou voltar.
    while True:
        resp = input("\nDeseja remover outro sensor (s) ou voltar ao menu (m)? ").lower()
        if resp == 's':
            removerSensoresInput() # Chama a si mesma.
            break
        elif resp == 'm':
            menu() # Volta para o menu principal.
            break
        else:
            print("Digite apenas 's' ou 'm'.")

def visualizarSensoresInput():
    """Obtém a lista de sensores do backend e a exibe no terminal."""
    sensores = obterSensores() # Chama a função de backend para obter a lista.

    if not sensores:
        print("\nNenhum sensor cadastrado.") # Exibe mensagem se a lista estiver vazia.
    else:
        print("\nSensores cadastrados:")
        i = 1
        # Itera sobre a lista e exibe os detalhes de cada sensor.
        for sensor in sensores:
            print(f"\nSensor {i}")
            print("-" * 30)
            print(f"id: {sensor['id']}")
            print(f"Nome: {sensor['Nome']}")
            print(f"Localização: {sensor['Localização']}")
            print(f"Alerta OBSERVAÇÃO: {sensor['Alerta OBSERVAÇÃO']}")
            print(f"Alerta ATENÇÃO: {sensor['Alerta ATENÇÃO']}")
            print(f"Alerta EMERGÊNCIA: {sensor['Alerta EMERGÊNCIA']}")
            print(f"Valor ATUAL: {sensor['Valor ATUAL']}")
            i += 1

    # Loop para perguntar se deseja voltar ao menu.
    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu() # Volta para o menu principal.
            break
        else:
            print("Digite 's' para voltar ao menu.")

# --- Sensores - Backend ---
def adicionarSensor(nome, localizacao, alertaOBS, alertaATE, alertaEME):
    """Cria um novo dicionário de sensor e o adiciona à lista global."""
    sensor = {
        "id": uuid.uuid4(), # Gera um ID único.
        "Nome": nome,
        "Localização": localizacao,
        "Alerta OBSERVAÇÃO": alertaOBS,
        "Alerta ATENÇÃO": alertaATE,
        "Alerta EMERGÊNCIA": alertaEME,
        "Valor ATUAL": 0, # Inicializa o valor atual como 0.
    }
    sensores_cadastrados.append(sensor) # Adiciona o novo sensor à lista.
    return sensor # Retorna o sensor criado.

def obterSensores():
    """Retorna a lista completa de sensores cadastrados."""
    return sensores_cadastrados

def removerSensor(id):
    """Busca um sensor pelo ID e o remove da lista global."""
    for sensor in sensores_cadastrados:
        if str(sensor['id']) == id: # Compara o ID recebido com o do sensor atual do loop.
            sensores_cadastrados.remove(sensor) # Remove o sensor da lista.
            return sensor # Retorna o sensor removido.
    return None # Retorna None se o sensor não for encontrado.

def buscarSensorPorId(id):
    """Busca um sensor na lista global pelo seu ID."""
    for sensor in sensores_cadastrados:
        if str(sensor['id']) == id: # Compara o ID recebido com o do sensor atual do loop.
            return sensor # Retorna o sensor se encontrado.
    return None # Retorna None se o sensor não for encontrado.

def atualizarValorSensor(sensor, valor):
    """Atualiza o campo 'Valor ATUAL' de um sensor específico."""
    sensor['Valor ATUAL'] = valor
    return sensor # Retorna o sensor atualizado.

# --- Alertas - Frontend ---
def ativarSensoresInput():
    """Simula a leitura de valores para cada sensor e exibe os resultados."""
    sensores = obterSensores() # Obtém a lista de sensores.

    if not sensores:
        print("\nSem sensores cadastrados para serem ativados.")
        # Loop para voltar ao menu se não houver sensores.
        while True:
            resp = input("\nVoltar ao menu? (s para sim): ").lower()
            if resp == 's':
                menu()
                break
            else:
                print("Digite 's' para voltar ao menu.")
    else:
        # Itera sobre cada sensor para simular a ativação.
        for sensor in sensores:
            # Loop e validação para coletar o valor atual do sensor (entre 0 e 100).
            while True:
                valor_atual_input = input(f"\nDigite o valor atual do sensor '{sensor['Nome']}': ") # Coleta valor.
                if valor_atual_input.isdigit(): # Verifica se a entrada é um número.
                    valor_atual = int(valor_atual_input)
                    if 0 <= valor_atual <= 100: # Verifica se está dentro do intervalo.
                        break # Sai do loop de validação.
                    else:
                        print("Valor inválido. Digite um valor entre 0 e 100.")
                else:
                    print("Digite um número inteiro válido para o valor atual.")

            # Chama a função de backend para atualizar o valor e verificar alertas.
            sensor_atualizado = atualizarValorSensor(sensor, valor_atual)
            alerta_gerado = verificarAlertas(sensor_atualizado)

            if alerta_gerado:
                # Exibe feedback se um alerta foi gerado.
                print(f"\nAlerta de {alerta_gerado['nivel']} gerado e enviado para os usuários cadastrados: {alerta_gerado['mensagem']}")
            else:
                # Exibe feedback se o sensor está normal.
                print(f"Sensor '{sensor['Nome']}' está dentro dos limites normais.")

        # Loop para perguntar se deseja ativar novamente ou voltar.
        while True:
            resp = input("\nDeseja ativar os sensores novamente (s) ou voltar ao menu (m)? ").lower()
            if resp == 's':
                ativarSensoresInput() # Chama a si mesma.
                break
            elif resp == 'm':
                menu() # Volta para o menu principal.
                break
            else:
                print("Digite apenas 's' ou 'm'.")

def visualizarAlertasInput():
    """Obtém a lista de alertas do backend e a exibe no terminal."""
    alertas_lista = obterAlertas() # Chama a função de backend para obter a lista.

    if not alertas_lista:
        print("\nNenhum alerta gerado.") # Exibe mensagem se a lista estiver vazia.
    else:
        print("\nAlertas gerados:")
        i = 1
        # Itera sobre a lista e exibe os detalhes de cada alerta.
        for alerta in alertas_lista:
            print(f"\nAlerta {i}")
            print("-" * 30)
            print(f"Data/Hora: {alerta['dataHora']}")
            print(f"Nível: {alerta['nivel']}")
            print(f"Mensagem: {alerta['mensagem']}")
            # Exibe apenas o nome do sensor para simplificar.
            print(f"Sensor: {alerta['sensor']['Nome']}")
            i += 1

    # Loop para perguntar se deseja voltar ao menu.
    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu() # Volta para o menu principal.
            break
        else:
            print("Digite 's' para voltar ao menu.")

def gerarAlertaManualInput():
    """Coleta dados para gerar um alerta manualmente e chama a função de backend."""
    # Loop e validação para coletar o nível do alerta.
    while True:
        nivel = input("\nDigite o nível do alerta (EMERGÊNCIA, ATENÇÃO, OBSERVAÇÃO): ").upper() # Coleta nível e converte para maiúsculo.
        if nivel not in ["EMERGÊNCIA", "ATENÇÃO", "OBSERVAÇÃO"]: # Verifica se o nível é válido.
            print("Nível de alerta inválido. Deve ser EMERGÊNCIA, ATENÇÃO ou OBSERVAÇÃO.")
        else:
            break # Sai do loop de validação.

    mensagem = input("Digite a mensagem do alerta: ") # Coleta a mensagem.
    sensor_id = input("Digite o ID do sensor relacionado ao alerta: ") # Coleta o ID do sensor.

    # Busca o sensor pelo ID usando a função de backend.
    sensor_encontrado = buscarSensorPorId(sensor_id)

    if not sensor_encontrado:
        print("Sensor não encontrado.") # Feedback se o sensor não existir.
    else:
        # Chama a função de backend para gerar o alerta.
        alertaGerado = gerarAlerta(nivel, mensagem, sensor_encontrado)
        print(f"\nAlerta gerado manualmente e enviado para usuários cadastrados: {alertaGerado['mensagem']}") # Feedback de sucesso.

    # Loop para perguntar se deseja gerar outro alerta ou voltar.
    while True:
        resp = input("Deseja gerar outro alerta (s) ou voltar ao menu (m)? ").lower()
        if resp == 's':
            gerarAlertaManualInput() # Chama a si mesma.
            break
        elif resp == 'm':
            menu() # Volta para o menu principal.
            return # Sai da função.
        else:
            print("Digite apenas 's' ou 'm'.")

# --- Alertas - Backend ---
def gerarAlerta(nivel, mensagem, sensor):
    """Cria um novo dicionário de alerta e o adiciona à lista global."""
    alerta = {
        "dataHora": datetime.now().strftime('%d/%m/%Y %H:%M'), # Registra data e hora atuais.
        "nivel": nivel,
        "mensagem": f'"{mensagem}"', # Armazena a mensagem.
        "sensor": sensor # Armazena o dicionário completo do sensor relacionado.
    }
    alertas.append(alerta) # Adiciona o novo alerta à lista.
    return alerta # Retorna o alerta criado.

def obterAlertas():
    """Retorna a lista completa de alertas gerados."""
    return alertas

def verificarAlertas(sensor):
    """Verifica o valor atual de um sensor e gera um alerta se um limite for atingido."""
    valor_atual = sensor['Valor ATUAL'] # Obtém o valor atual do sensor.

    # Compara o valor atual com os limites de alerta do sensor.
    if valor_atual >= sensor['Alerta EMERGÊNCIA']:
        # Chama a função de backend para gerar alerta de EMERGÊNCIA.
        return gerarAlerta("EMERGÊNCIA", mensagemEmergencia, sensor)
    elif valor_atual >= sensor['Alerta ATENÇÃO']:
        # Chama a função de backend para gerar alerta de ATENÇÃO.
        return gerarAlerta("ATENÇÃO", mensagemAtencao, sensor)
    elif valor_atual >= sensor['Alerta OBSERVAÇÃO']:
        # Chama a função de backend para gerar alerta de OBSERVAÇÃO.
        return gerarAlerta("OBSERVAÇÃO", mensagemObservacao, sensor)
    else:
        return None # Retorna None se nenhum limite for atingido.

# Inicia a execução do programa chamando a função principal.
main()