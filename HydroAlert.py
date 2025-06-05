# coding=utf-8
from datetime import datetime
import uuid

usuarios_cadastrados = []
sensores_cadastrados = []
alertas = []

mensagemEmergencia = "Sua região está em alerta de emergência! \nEvacue a área! \nClique no link a seguir para calcular uma rota de fuga. \nhttps://hydroalert.com.br/rotafuga"
mensagemAtencao = "Sua região está em alerta de atenção! \nProcure abrigo e fique atento às atualizações."
mensagemObservacao = "Sua região está em alerta de observação! \nFique atento às atualizações."

# Base
def main():
    exibirMensagemInicial()
    menu()

def menu():
    while True:    
        print('\n-----------Menu-----------')
        print('Opção 1: Gestão de usuários')
        print('Opção 2: Gestão de sensores')
        print('Opção 3: Ativar sensores')
        print('Opção 4: Visualizar alertas')
        print('Opção 5: Gerar alerta manual')
        print('Opção 6: Sair do sistema')

        opicao = input('\nDigite a sua opção: ')

        match opicao:
            case '1':
                gestaoUsuarios()
            case '2':
                gestaoDeSensores()
            case '3':
                ativarSensores()
            case '4':
                visualizarAlertas()
            case '5':
                gerarAlertaManual()
            case '6':
                print("Encerrando o sistema. Até logo!")
                exit()
            case _:
                print("Digite uma opção válida.")

def exibirMensagemInicial():
    print("Bem-vindo ao HydroAlert!")


# Usuários
def gestaoUsuarios():
    while True:        
        print("\nOpção 1: Cadastrar usuário")
        print("Opção 2: Visualizar usuários")
        print("Opção 3: Remover usuários")
        print("Opção 4: Voltar ao menu principal")

        resp = input('\nDigite sua opção: ')

        if resp == '1':
            cadastrarUsuario()
            break
        elif resp == '2':
            visualizarUsuarios()
            break
        elif resp == '3': 
            removerUsuario()
            break
        elif resp == '4':
            menu()
            break
        else:
            print('Digite apenas o número das opções.')

def cadastrarUsuario():
    nome = input('\nDigite seu nome: ')
    endereco = input('Digite seu endereço: ')
    telefone = input('Digite seu telefone: ')

    usuarios_cadastrados.append({
        "id": uuid.uuid4(),
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
    })
    print(f"Usuário {nome} cadastrado com sucesso!")


    while True:     
        resp = input('Cadastrar outro usuário (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            cadastrarUsuario()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print('Digite apenas s ou m')

def visualizarUsuarios():
    if not usuarios_cadastrados:
        print("\nNenhum usuário cadastrado.")
    else:
        print("\nUsuários cadastrados até agora:")
        
        for usuario in usuarios_cadastrados:
            print(f"id: {usuario['id']}, Nome: {usuario['nome']}, Endereço: {usuario['endereco']}, Telefone: {usuario['telefone']}")

    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu()
            break
        else:
            print("Digite 's' para voltar ao menu.")

def removerUsuario():
    if not usuarios_cadastrados:
        print("\nNão há usuários cadastrados para remover.")
        menu()
        return

    id = input('\nDigite o id do usuário que deseja deletar: ')
    
    usuario_encontrado = None
    
    for usuario in usuarios_cadastrados:
        if str(usuario['id']) == id:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        usuarios_cadastrados.remove(usuario_encontrado)
        print(f"\nUsuário '{usuario_encontrado['nome']}' removido com sucesso!")
    else:
        print(f"\nUsuário não encontrado com o id {id}.")

    while True:     
        resp = input('Remover outro usuário (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            removerUsuario()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print('Digite apenas s ou m')

# Sensores
def gestaoDeSensores():
    while True:    
        print('\nOpcão 1: Adicionar sensores')
        print('Opcão 2: Remover sensores')
        print('Opcão 3: Visualizar sensores')
        print('Opcão 4: Voltar ao menu principal')

        resp = input('\nDigite sua opção: ')
        
        if resp == '1':
            adicionarSensor()
            break
        elif resp == '2':
            removerSensores()
            break
        elif resp == '3':
            visualizarSensores()
            break
        elif resp == '4':
            menu()
            break
        else:
            print('Digite apenas as opções acima!')
        
def adicionarSensor():
    nomeSEN = input('\nDigite o nome do sensor: ')
    Local = input('Digite a localização: ')

    while True:
        alertaOBS = int(input('Digite o valor de alerta de nível OBSERVAÇÃO (Entre 0 e 100): '))
        if alertaOBS < 0 or alertaOBS > 100:
            print("Valor de alerta OBSERVAÇÃO deve estar entre 0 e 100.")
        else:
            break

    while True:
        alertaATE = int(input('Digite o valor de alerta de nível ATENÇÃO (Entre 0 e 100): '))
        if alertaATE < 0 or alertaATE > 100:
            print("Valor de alerta ATENÇÃO deve estar entre 0 e 100.")
        else:
            break

    while True:
        alertaEME = int(input('Digite o valor de alerta de nível EMERGÊNCIA (Entre 0 e 100): '))
        if alertaEME < 0 or alertaEME > 100:
            print("Valor de alerta EMERGÊNCIA deve estar entre 0 e 100.")
        else:
            break

    sensor = {
        "id": uuid.uuid4(),
        "Nome": nomeSEN,
        "Localização": Local,
        "Alerta OBSERVAÇÃO": alertaOBS,
        "Alerta ATENÇÃO": alertaATE,
        "Alerta EMERGÊNCIA": alertaEME,
        "Valor ATUAL": 0,    
    }

    sensores_cadastrados.append(sensor)
    print(f"Sensor {nomeSEN} cadastrado com sucesso!\n")

    while True:
        resp = input('Cadastrar outro sensor (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            adicionarSensor()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print('Digite apenas s ou m')

def removerSensores():
    if not sensores_cadastrados:
        print("\nNão há sensores cadastrados para remover.")
        menu()
        return

    id = input("\nDigite o id do sensor que deseja remover: ")

    sensor_encontrado = None
    for sensor in sensores_cadastrados:
        if str(sensor['id']) == id:
            sensor_encontrado = sensor
            break

    if sensor_encontrado:
        sensores_cadastrados.remove(sensor_encontrado)
        print(f"Sensor '{sensor_encontrado['Nome']}' removido com sucesso!")
    else:
        print("Sensor não encontrado com os dados informados.")

    while True:
        resp = input("\nDeseja remover outro sensor (s) ou voltar ao menu (m)? ").lower()
        if resp == 's':
            removerSensores()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print("Digite apenas 's' ou 'm'.")

def visualizarSensores():
    if not sensores_cadastrados:
        print("\nNenhum sensor cadastrado.")
    else:
        i = 1
        for sensor in sensores_cadastrados:
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

    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu()
            break
        else:
            print("Digite 's' para voltar ao menu.")

# Alertas
def ativarSensores():
    if not sensores_cadastrados:
        print("\nSem sensores cadastrados para serem ativados.")

        while True:
            resp = input("\nVoltar ao menu? (s para sim): ").lower()
            if resp == 's':
                menu()
                break
            else:
                print("Digite 's' para voltar ao menu.")
    else:
        for sensor in sensores_cadastrados:

            while True:
                valor_atual = int(input(f"\nDigite o valor atual do sensor '{sensor['Nome']}': "))
                if valor_atual < 0 or valor_atual > 100:
                    print("Valor inválido. Digite um valor entre 0 e 100.")
                else:
                    break

            sensor['Valor ATUAL'] = valor_atual

            if valor_atual >= sensor['Alerta EMERGÊNCIA']:
                alertaGerado = gerarAlerta("EMERGÊNCIA", mensagemEmergencia, sensor)
                print(f"\nAlerta de EMERGÊNCIA gerado: {alertaGerado['mensagem']}")
            elif valor_atual >= sensor['Alerta ATENÇÃO']:
                alertaGerado = gerarAlerta("ATENÇÃO", mensagemAtencao, sensor)
                print(f"\nAlerta de ATENÇÃO gerado: {alertaGerado['mensagem']}")
            elif valor_atual >= sensor['Alerta OBSERVAÇÃO']:
                alertaGerado = gerarAlerta("OBSERVAÇÃO", mensagemObservacao, sensor)
                print(f"\nAlerta de OBSERVAÇÃO gerado: {alertaGerado['mensagem']}")
            else:
                print(f"Sensor '{sensor['Nome']}' está dentro dos limites normais.")

        while True:
            resp = input("\nDeseja ativar os sensores novamente (s) ou voltar ao menu (m)? ").lower()
            if resp == 's':
                ativarSensores()
                break
            elif resp == 'm':
                menu()
                break
            else:
                print("Digite apenas 's' ou 'm'.")

def gerarAlerta(nivel, mensagem, sensor):
    alerta = {
        "dataHora": datetime.now().strftime('%d/%m/%Y %H:%M'),
        "nivel": nivel,
        "mensagem": f'"{mensagem}"',
        "sensor": sensor
    }

    alertas.append(alerta)
    return alerta

def visualizarAlertas():
    if not alertas:
        print("\nNenhum alerta gerado.")
    else:
        print("\nAlertas gerados:")
        i = 1
        for alerta in alertas:
            print(f"\nAlerta {i}")
            print("-" * 30)
            print(f"Data/Hora: {alerta['dataHora']}")
            print(f"Nível: {alerta['nivel']}")
            print(f"Mensagem: {alerta['mensagem']}")
            print(f"Sensor: {alerta['sensor']}")
            i += 1

    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu()
            break
        else:
            print("Digite 's' para voltar ao menu.")

def gerarAlertaManual():
    while True:
        nivel = input("\nDigite o nível do alerta (EMERGÊNCIA, ATENÇÃO, OBSERVAÇÃO): ").upper()
        if nivel not in ["EMERGÊNCIA", "ATENÇÃO", "OBSERVAÇÃO"]:
            print("Nível de alerta inválido. Deve ser EMERGÊNCIA, ATENÇÃO ou OBSERVAÇÃO.")
        else:
            break

    mensagem = input("Digite a mensagem do alerta: ")
    sensor_id = input("Digite o ID do sensor relacionado ao alerta: ")

    sensor_encontrado = None
    for sensor in sensores_cadastrados:
        if str(sensor['id']) == sensor_id:
            sensor_encontrado = sensor
            break

    if not sensor_encontrado:
        print("Sensor não encontrado.")
    else:
        alertaGerado = gerarAlerta(nivel, mensagem, sensor_encontrado)
        print(f"\nAlerta gerado manualmente: {alertaGerado['mensagem']}")
    
    while True:
        resp = input("Deseja gerar outro alerta (s) ou voltar ao menu (m)? ").lower()
        if resp == 's':
            gerarAlertaManual()
            break
        elif resp == 'm':
            menu()
            return
        else:
            print("Digite apenas 's' ou 'm'.")

main()
