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
                ativarSensoresInput()
            case '4':
                visualizarAlertasInput()
            case '5':
                gerarAlertaManualInput()
            case '6':
                print("Encerrando o sistema. Até logo!")
                exit()
            case _:
                print("Digite uma opção válida.")

def exibirMensagemInicial():
    print("Bem-vindo ao HydroAlert!")

# Usuários - Frontend
def gestaoUsuarios():
    while True:
        print("\nOpção 1: Cadastrar usuário")
        print("Opção 2: Visualizar usuários")
        print("Opção 3: Remover usuários")
        print("Opção 4: Voltar ao menu principal")
        resp = input('\nDigite sua opção: ')
        if resp == '1':
            cadastrarUsuarioInput()
            break
        elif resp == '2':
            visualizarUsuariosInput()
            break
        elif resp == '3':
            removerUsuarioInput()
            break
        elif resp == '4':
            menu()
            break
        else:
            print('Digite apenas o número das opções.')

def cadastrarUsuarioInput():
    nome = input('\nDigite seu nome: ')
    endereco = input('Digite seu endereço: ')
    telefone = input('Digite seu telefone: ')
    usuario = cadastrarUsuario(nome, endereco, telefone)
    print(f"Usuário {usuario['nome']} cadastrado com sucesso!")
    while True:
        resp = input('Cadastrar outro usuário (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            cadastrarUsuarioInput()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print('Digite apenas s ou m')

def visualizarUsuariosInput():
    usuarios = obterUsuarios()
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
    else:
        print("\nUsuários cadastrados até agora:")
        for usuario in usuarios:
            print(f"id: {usuario['id']}, Nome: {usuario['nome']}, Endereço: {usuario['endereco']}, Telefone: {usuario['telefone']}")
    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu()
            break
        else:
            print("Digite 's' para voltar ao menu.")

def removerUsuarioInput():
    usuarios = obterUsuarios()
    if not usuarios:
        print("\nNão há usuários cadastrados para remover.")
        menu()
        return
    
    id = input('\nDigite o id do usuário que deseja deletar: ')
    usuario_removido = removerUsuario(id)
    
    if usuario_removido:
        print(f"\nUsuário '{usuario_removido['nome']}' removido com sucesso!")
    else:
        print(f"\nUsuário não encontrado com o id {id}.")
    
    while True:
        resp = input('Remover outro usuário (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            removerUsuarioInput()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print('Digite apenas s ou m')

# Usuários - Backend
def cadastrarUsuario(nome, endereco, telefone):
    novoUsuario = {
        "id": uuid.uuid4(),
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
    }
    usuarios_cadastrados.append(novoUsuario)
    return novoUsuario

def obterUsuarios():
    return usuarios_cadastrados

def removerUsuario(id):
    for usuario in usuarios_cadastrados:
        if str(usuario['id']) == id:
            usuarios_cadastrados.remove(usuario)
            return usuario
    return None

# Sensores - Frontend
def gestaoDeSensores():
    while True:
        print('\nOpcão 1: Adicionar sensores')
        print('Opcão 2: Remover sensores')
        print('Opcão 3: Visualizar sensores')
        print('Opcão 4: Voltar ao menu principal')
        resp = input('\nDigite sua opção: ')
        if resp == '1':
            adicionarSensorInput()
            break
        elif resp == '2':
            removerSensoresInput()
            break
        elif resp == '3':
            visualizarSensoresInput()
            break
        elif resp == '4':
            menu()
            break
        else:
            print('Digite apenas as opções acima!')

def adicionarSensorInput():
    nomeSEN = input('\nDigite o nome do sensor: ')
    Local = input('Digite a localização: ')
    
    while True:
        alertaOBS_input = input('Digite o valor de alerta de nível OBSERVAÇÃO (Entre 0 e 100): ')
        if alertaOBS_input.isdigit():
            alertaOBS = int(alertaOBS_input)
            if 0 <= alertaOBS <= 100:
                break
            else:
                print("Valor de alerta OBSERVAÇÃO deve estar entre 0 e 100.")
        else:
            print("Digite um número inteiro válido para o valor de alerta OBSERVAÇÃO.")    
    
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

    sensor = adicionarSensor(nomeSEN, Local, alertaOBS, alertaATE, alertaEME)
    print(f"Sensor {sensor['Nome']} cadastrado com sucesso!\n")
    
    while True:
        resp = input('Cadastrar outro sensor (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            adicionarSensorInput()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print('Digite apenas s ou m')

def removerSensoresInput():
    sensores = obterSensores()
    if not sensores:
        print("\nNão há sensores cadastrados para remover.")
        menu()
        return
    
    id = input("\nDigite o id do sensor que deseja remover: ")
    sensor_removido = removerSensor(id)
    
    if sensor_removido:
        print(f"Sensor '{sensor_removido['Nome']}' removido com sucesso!")
    else:
        print("Sensor não encontrado com os dados informados.")
    
    while True:
        resp = input("\nDeseja remover outro sensor (s) ou voltar ao menu (m)? ").lower()
        if resp == 's':
            removerSensoresInput()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print("Digite apenas 's' ou 'm'.")

def visualizarSensoresInput():
    sensores = obterSensores()
    if not sensores:
        print("\nNenhum sensor cadastrado.")
    else:
        i = 1
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
    
    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu()
            break
        else:
            print("Digite 's' para voltar ao menu.")

# Sensores - Backend
def adicionarSensor(nome, localizacao, alertaOBS, alertaATE, alertaEME):
    sensor = {
        "id": uuid.uuid4(),
        "Nome": nome,
        "Localização": localizacao,
        "Alerta OBSERVAÇÃO": alertaOBS,
        "Alerta ATENÇÃO": alertaATE,
        "Alerta EMERGÊNCIA": alertaEME,
        "Valor ATUAL": 0,
    }
    sensores_cadastrados.append(sensor)
    return sensor

def obterSensores():
    return sensores_cadastrados

def removerSensor(id):
    for sensor in sensores_cadastrados:
        if str(sensor['id']) == id:
            sensores_cadastrados.remove(sensor)
            return sensor
    return None

def buscarSensorPorId(id):
    for sensor in sensores_cadastrados:
        if str(sensor['id']) == id:
            return sensor
    return None

def atualizarValorSensor(sensor, valor):
    sensor['Valor ATUAL'] = valor
    return sensor

# Alertas - Frontend
def ativarSensoresInput():
    sensores = obterSensores()
    if not sensores:
        print("\nSem sensores cadastrados para serem ativados.")
        while True:
            resp = input("\nVoltar ao menu? (s para sim): ").lower()
            if resp == 's':
                menu()
                break
            else:
                print("Digite 's' para voltar ao menu.")
    else:
        for sensor in sensores:
            while True:
                valor_atual_input = input(f"\nDigite o valor atual do sensor '{sensor['Nome']}': ")
                if valor_atual_input.isdigit():
                    valor_atual = int(valor_atual_input)
                    if 0 <= valor_atual <= 100:
                        break
                    else:
                        print("Valor inválido. Digite um valor entre 0 e 100.")
                else:
                    print("Digite um número inteiro válido para o valor atual.")

            sensor_atualizado = atualizarValorSensor(sensor, valor_atual)
            alerta_gerado = verificarAlertas(sensor_atualizado)
            
            if alerta_gerado:
                print(f"\nAlerta de {alerta_gerado['nivel']} gerado e enviado para os usuários cadastrados: {alerta_gerado['mensagem']}")
            else:
                print(f"Sensor '{sensor['Nome']}' está dentro dos limites normais.")
        
        while True:
            resp = input("\nDeseja ativar os sensores novamente (s) ou voltar ao menu (m)? ").lower()
            if resp == 's':
                ativarSensoresInput()
                break
            elif resp == 'm':
                menu()
                break
            else:
                print("Digite apenas 's' ou 'm'.")

def visualizarAlertasInput():
    alertas_lista = obterAlertas()
    if not alertas_lista:
        print("\nNenhum alerta gerado.")
    else:
        print("\nAlertas gerados:")
        i = 1
        for alerta in alertas_lista:
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

def gerarAlertaManualInput():
    while True:
        nivel = input("\nDigite o nível do alerta (EMERGÊNCIA, ATENÇÃO, OBSERVAÇÃO): ").upper()
        if nivel not in ["EMERGÊNCIA", "ATENÇÃO", "OBSERVAÇÃO"]:
            print("Nível de alerta inválido. Deve ser EMERGÊNCIA, ATENÇÃO ou OBSERVAÇÃO.")
        else:
            break
    
    mensagem = input("Digite a mensagem do alerta: ")
    sensor_id = input("Digite o ID do sensor relacionado ao alerta: ")
    
    sensor_encontrado = buscarSensorPorId(sensor_id)
    if not sensor_encontrado:
        print("Sensor não encontrado.")
    else:
        alertaGerado = gerarAlerta(nivel, mensagem, sensor_encontrado)
        print(f"\nAlerta gerado manualmente e enviado para usuários cadastrados: {alertaGerado['mensagem']}")
    
    while True:
        resp = input("Deseja gerar outro alerta (s) ou voltar ao menu (m)? ").lower()
        if resp == 's':
            gerarAlertaManualInput()
            break
        elif resp == 'm':
            menu()
            return
        else:
            print("Digite apenas 's' ou 'm'.")

# Alertas - Backend
def gerarAlerta(nivel, mensagem, sensor):
    alerta = {
        "dataHora": datetime.now().strftime('%d/%m/%Y %H:%M'),
        "nivel": nivel,
        "mensagem": f'"{mensagem}"',
        "sensor": sensor
    }
    alertas.append(alerta)
    return alerta

def obterAlertas():
    return alertas

def verificarAlertas(sensor):
    valor_atual = sensor['Valor ATUAL']
    
    if valor_atual >= sensor['Alerta EMERGÊNCIA']:
        return gerarAlerta("EMERGÊNCIA", mensagemEmergencia, sensor)
    elif valor_atual >= sensor['Alerta ATENÇÃO']:
        return gerarAlerta("ATENÇÃO", mensagemAtencao, sensor)
    elif valor_atual >= sensor['Alerta OBSERVAÇÃO']:
        return gerarAlerta("OBSERVAÇÃO", mensagemObservacao, sensor)
    else:
        return None

main()
