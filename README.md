# HydroAlert: Sistema de Monitoramento Hidrológico

## 📝 Descrição do Projeto

O HydroAlert é conceitualmente um sistema inteligente e abrangente de monitoramento e alerta de enchentes. A solução completa visa utilizar dados em tempo real de sensores hidrológicos, integrar informações de serviços meteorológicos e aplicar inteligência artificial para prever com antecedência situações de risco. O sistema ideal monitoraria continuamente níveis de rios, volumes de chuva e outros indicadores, utilizando modelos preditivos para identificar a probabilidade de enchentes.

Quando um risco elevado é detectado pela solução completa, alertas automáticos e personalizados seriam gerados e enviados por canais como Telegram e WhatsApp. Além disso, o sistema seria capaz de sugerir rotas de fuga seguras e otimizadas, considerando áreas afetadas, mapas de risco e dados em tempo real sobre o avanço da enchente, garantindo uma evacuação rápida e segura. A solução também incluiria uma interface visual robusta para operadores e administradores.

Este projeto atua em Python no terminal e serve como uma simulação simplificada e um protótipo funcional de algumas das funcionalidades centrais da solução HydroAlert. Ele foca na gestão básica de usuários e sensores e na simulação da ativação de sensores para gerar alertas simples baseados em limites predefinidos, além da gestão manual e visualização desses alertas.

## ✨ Funcionalidades

### Gestão de Usuários:

- Cadastrar novos usuários (Nome, Endereço, Telefone)
- Visualizar a lista de usuários cadastrados
- Remover usuários pelo ID

### Gestão de Sensores:

- Adicionar novos sensores (Nome, Localização, Níveis de Alerta: Observação, Atenção, Emergência)
- Visualizar a lista de sensores cadastrados com seus detalhes
- Remover sensores pelo ID

### Ativação de Sensores:

- Simular a leitura do valor atual para cada sensor cadastrado
- Gerar automaticamente alertas com base nos níveis configurados do sensor e o valor lido

### Visualização de Alertas:

- Exibir o histórico de todos os alertas gerados (automáticos e manuais)

### Geração Manual de Alertas:

- Permitir a criação de alertas de forma manual, especificando nível, mensagem e sensor relacionado.

## 🚀 Como Executar o Sistema

### Pré-requisitos

Python 3.6 ou superior instalado.

### Instalação

- Salve o código Python em um arquivo (ex: hydroalert.py).
- Não há dependências externas, as bibliotecas datetime e uuid são nativas do Python.

### Execução

- Abra o terminal ou prompt de comando.
- Navegue até o diretório onde você salvou o arquivo hydroalert.py.
- Execute o comando:

```bash
  python hydroalert.py
```

## 🏗️ Arquitetura do Código

O código foi estruturado seguindo o princípio de separação de responsabilidades:

- **Frontend (Funções \*Input):** Responsável pela interação com o usuário no terminal (coleta de inputs e exibição de outputs).
- **Backend (Funções sem sufixo \*Input):** Contém a lógica de negócio e manipulação dos dados (listas usuarios_cadastrados, sensores_cadastrados, alertas).

As funções de frontend chamam as funções de backend, passando os dados coletados como parâmetros e recebendo os resultados através de retornos.

## Equipe

[@Rickkcastro](https://github.com/RickkCastro) - Henrique Castro de Matos - [Linkedin](https://www.linkedin.com/in/rickkcastro/) <br>
[@fernandoBellegarde](https://github.com/fernandoBellegarde) - Fernando Medeiros Camargo Bellegarde - [Linkedin](https://www.linkedin.com/in/fernandobellegarde/) <br>
[@Otaaviio](https://github.com/Otaaviio) - Otávio Inaba - [Linkedin](https://www.linkedin.com/in/otávio-inaba-46379124a/) <br>
