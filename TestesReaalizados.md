# 📋 Lista Completa de Testes Manuais

## 1. Gestão de Usuários

### 1.1 Cadastrar Usuário

- [x] **Teste Normal:** Cadastrar usuário com dados válidos
- [x] **Cadastrar múltiplos usuários:** Verificar se IDs são únicos
- [x] **Resposta inválida:** Digitar algo diferente de 's' ou 'm' após cadastro
- [x] **Cadastrar outro usuário:** Testar opção 's'
- [x] **Voltar ao menu:** Testar opção 'm'

### 1.2 Visualizar Usuários

- [x] **Lista vazia:** Visualizar quando não há usuários
- [x] **Lista com usuários:** Verificar se todos os dados aparecem
- [x] **Múltiplos usuários:** Verificar se todos são listados
- [x] **Resposta inválida:** Digitar algo diferente de 's' para voltar
- [x] **Voltar ao menu:** Confirmar que volta ao menu principal

### 1.3 Remover Usuário

- [x] **Lista vazia:** Tentar remover quando não há usuários
- [x] **ID válido:** Remover usuário existente
- [x] **ID inválido:** Tentar remover com ID inexistente
- [x] **Resposta inválida:** Digitar algo diferente de 's' ou 'm' após remoção
- [x] **Remover outro usuário:** Testar opção 's'
- [x] **Voltar ao menu:** Testar opção 'm'

---

## 2. Gestão de Sensores

### 2.1 Adicionar Sensor

- [x] **Teste Normal:** Adicionar sensor com dados válidos

**Validações de Alerta de OBSERVAÇÃO:**

- [x] Valor -1: Digitar valor menor que 0
- [x] Valor 0: Digitar valor 0 (deve aceitar)
- [x] Valor 50: Digitar valor válido entre 0 e 100
- [x] Valor 100: Digitar valor 100 (deve aceitar)
- [x] Valor 101: Digitar valor maior que 100
- [x] Valor não numérico: Digitar texto

**Validações de Alerta de ATENÇÃO:**

- [x] Valor -1: Digitar valor menor que 0
- [x] Valor 0: Digitar valor 0 (deve aceitar)
- [x] Valor 50: Digitar valor válido entre 0 e 100
- [x] Valor 100: Digitar valor 100 (deve aceitar)
- [x] Valor 101: Digitar valor maior que 100

**Validações de Alerta de EMERGÊNCIA:**

- [x] Valor -1: Digitar valor menor que 0
- [x] Valor 0: Digitar valor 0 (deve aceitar)
- [x] Valor 50: Digitar valor válido entre 0 e 100
- [x] Valor 100: Digitar valor 100 (deve aceitar)
- [x] Valor 101: Digitar valor maior que 100

**Finalização do Cadastro:**

- [x] Cadastrar múltiplos sensores: Verificar se IDs são únicos
- [x] Resposta inválida: Digitar algo diferente de 's' ou 'm' após cadastro
- [x] Cadastrar outro sensor: Testar opção 's'
- [x] Voltar ao menu: Testar opção 'm'

### 2.2 Visualizar Sensores

- [x] **Lista vazia:** Visualizar quando não há sensores
- [x] **Lista com sensores:** Verificar se todos os dados aparecem
- [x] **Múltiplos sensores:** Verificar numeração sequencial
- [x] **Resposta inválida:** Digitar algo diferente de 's' para voltar
- [x] **Voltar ao menu:** Confirmar que volta ao menu principal

### 2.3 Remover Sensores

- [x] **Lista vazia:** Tentar remover quando não há sensores
- [x] **ID válido:** Remover sensor existente
- [x] **ID inválido:** Tentar remover com ID inexistente
- [x] **Resposta inválida:** Digitar algo diferente de 's' ou 'm' após remoção
- [x] **Remover outro sensor:** Testar opção 's'
- [x] **Voltar ao menu:** Testar opção 'm'

---

## 3. Ativar Sensores

### 3.1 Sem Sensores Cadastrados

- [x] **Lista vazia:** Tentar ativar quando não há sensores
- [x] **Resposta inválida:** Digitar algo diferente de 's' para voltar
- [x] **Voltar ao menu:** Confirmar que volta ao menu principal

### 3.2 Com Sensores Cadastrados

**Para cada sensor, testar valores:**

**Validações de Valor Atual:**

- [x] Valor -1: Digitar valor menor que 0
- [x] Valor 0: Digitar valor 0 (deve aceitar)
- [x] Valor 25: Digitar valor válido
- [x] Valor 100: Digitar valor 100 (deve aceitar)
- [x] Valor 101: Digitar valor maior que 100
- [x] Valor não numérico: Digitar texto

**Geração de Alertas:**

- [x] Valor Normal: Abaixo do alerta de OBSERVAÇÃO
- [x] Alerta OBSERVAÇÃO: Valor >= OBSERVAÇÃO e < ATENÇÃO
- [x] Alerta ATENÇÃO: Valor >= ATENÇÃO e < EMERGÊNCIA
- [x] Alerta EMERGÊNCIA: Valor >= EMERGÊNCIA

**Finalização:**

- [x] Resposta inválida: Digitar algo diferente de 's' ou 'm'
- [x] Ativar novamente: Testar opção 's'
- [x] Voltar ao menu: Testar opção 'm'

---

## 4. Visualizar Alertas

- [x] **Lista vazia:** Visualizar quando não há alertas
- [x] **Lista com alertas:** Verificar todos os dados dos alertas
- [x] **Múltiplos alertas:** Verificar numeração e ordem
- [x] **Diferentes níveis:** Verificar alertas de diferentes níveis
- [x] **Data/Hora:** Verificar se data/hora estão corretas
- [x] **Resposta inválida:** Digitar algo diferente de 's' para voltar
- [x] **Voltar ao menu:** Confirmar que volta ao menu principal

---

## 5. Gerar Alerta Manual

### 5.1 Validação de Nível

- [x] EMERGÊNCIA: Digitar "EMERGÊNCIA" (maiúsculo)
- [x] emergência: Digitar "emergência" (minúsculo)
- [x] Emergência: Digitar "Emergência" (misto)
- [x] ATENÇÃO: Digitar "ATENÇÃO"
- [x] OBSERVAÇÃO: Digitar "OBSERVAÇÃO"
- [x] Nível inválido: Digitar "TESTE" ou outro texto
- [x] Nível vazio: Não digitar nada

### 5.3 ID do Sensor

- [x] **ID válido:** Usar ID de sensor existente
- [x] **ID inválido:** Usar ID inexistente

### 5.4 Finalização

- [x] Resposta inválida: Digitar algo diferente de 's' ou 'm'
- [x] Gerar outro alerta: Testar opção 's'
- [x] Voltar ao menu: Testar opção 'm'

---

## 6. Navegação Geral

### 6.1 Menu Principal

- [x] Opção 1: Gestão de usuários
- [x] Opção 2: Gestão de sensores
- [x] Opção 3: Ativar sensores
- [x] Opção 4: Visualizar alertas
- [x] Opção 5: Gerar alerta manual
- [x] Opção 6: Sair do sistema
- [x] Opção inválida: Digitar 7, 0, -1, texto, etc.

### 6.2 Submenus

- [x] Gestão de usuários: Todas as 4 opções
- [x] Gestão de sensores: Todas as 4 opções
- [x] Opções inválidas: Em cada submenu

---

## 7. Testes de Integração

### 7.1 Fluxo Completo

- [x] Cadastrar usuário → Visualizar → Remover
- [x] Cadastrar sensor → Visualizar → Ativar → Ver alertas
- [x] Cadastrar sensor → Gerar alerta manual → Ver alertas
- [x] Múltiplos usuários e sensores → Ativar todos

### 7.2 Cenários Reais

- [x] Sensor com alertas crescentes: 20 → 40 → 70 → 95
- [x] Múltiplos sensores diferentes: Alguns normais, outros em alerta
- [x] Alertas manuais + automáticos: Misturar tipos de alerta
