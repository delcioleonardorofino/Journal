---
id: 1
title: Dia 1 | Arquitetura do Sistema de Gestão Escolar
date: 11 de Fevereiro de 2026
description: Qualquer bom sistema deve ser pensado e bem planejado desde o início. Por isso, na fase de desenvolvimento de uma ideia, o primeiro passo é arquitetar.
---


## Índice de Navegação

1. [Visão Geral do Projeto](#1-visão-geral-do-projeto)  
2. [Contexto do Problema e Realidade Institucional](#2-contexto-do-problema-e-realidade-institucional)  
3. [Estratégia Técnica e Decisões Estruturais](#3-estratégia-técnica-e-decisões-estruturais)  
4. [Arquitetura Geral do Sistema](#4-arquitetura-geral-do-sistema)  
5. [Multitenancy: Conceito, Tipos e Modelo Escolhido](#5-multitenancy-conceito-tipos-e-modelo-escolhido)  
6. [Autenticação, Autorização e Segurança](#6-autenticação-autorização-e-segurança)  
7. [Perfis de Usuário e Responsabilidades](#7-perfis-de-usuário-e-responsabilidades)  
8. [Modelagem de Dados e Estrutura Relacional](#8-modelagem-de-dados-e-estrutura-relacional)  
9. [Fluxos Operacionais Principais](#9-fluxos-operacionais-principais)  
10. [Rotas Essenciais do MVP](#10-rotas-essenciais-do-mvp)  
11. [Levantamento Estatístico Escolar (Fase 03 de 03)](#11-levantamento-estatístico-escolar-fase-03-de-03)  
12. [Dificuldades Técnicas e Desafios Arquiteturais](#12-dificuldades-técnicas-e-desafios-arquiteturais)  
13. [Justificativas Arquiteturais e Estratégicas](#13-justificativas-arquiteturais-e-estratégicas)  
14. [Conclusão e Direção Futura](#14-conclusão-e-direção-futura)  

---

## 1. Visão Geral do Projeto

O Sistema de Gestão Escolar (SGE) foi concebido para digitalizar e estruturar os processos administrativos e pedagógicos de escolas públicas/estatais, respeitando a realidade operacional atual — fortemente baseada em papel — e permitindo uma transição gradual e sustentável para o digital.

O foco inicial é o MVP (Minimum Viable Product), cujo objetivo é:

- Gerir estudantes, professores e turmas  
- Controlar o processo de matrícula  
- Permitir lançamento e publicação de notas por disciplina  
- Gerar relatórios por turma  
- Implementar levantamento estatístico escolar  
- Garantir autenticação e autorização por perfil  
- Permitir múltiplas escolas no mesmo sistema (arquitetura multitenant)  

Este sistema não é apenas um CRUD. Ele é uma base institucional digital.

---

# 2. Contexto do Problema e Realidade Institucional

## 2.1 Processo Atual Baseado em Papel

Fluxo típico de matrícula:

1. Estudante compra processo físico  
2. Preenche formulário manualmente  
3. Insere documentos no processo  
4. Entrega na secretaria  
5. Secretaria registra nome em livro  
6. Arquivamento físico  

Esse modelo funciona há anos. Existe forte inércia institucional.

Portanto, o sistema não pode romper abruptamente com o fluxo atual. Ele deve:

- Digitalizar progressivamente  
- Reduzir redundância  
- Melhorar organização  
- Manter compatibilidade com processos existentes  

---

# 3. Estratégia Técnica e Decisões Estruturais

## 3.1 Sistema Online vs Offline

Foi escolhida arquitetura **online (web-based)**.

### Motivos:

- Centralização de dados  
- Suporte a múltiplas escolas  
- Atualizações automáticas  
- Backup centralizado  
- Escalabilidade  
- Menor risco de inconsistência  

Sistema offline exigiria:

- Instalação manual  
- Sincronização complexa  
- Alto risco de fragmentação de dados  

Conclusão: Online é estruturalmente mais sustentável.

---

# 4. Arquitetura Geral do Sistema

Arquitetura em camadas:

Frontend (Web App)  
↓  
API Backend (REST)  
↓  
Base de Dados Relacional  

## Responsabilidades do Backend:

- Autenticação  
- Autorização  
- Regras de negócio  
- Validação  
- Segurança  
- Isolamento entre escolas  
- Controle de permissões  

O frontend apenas consome a API. Toda regra crítica está no backend.

---

# 5. Multitenancy: Conceito, Tipos e Modelo Escolhido

## 5.1 O que é Multitenancy?

Multitenant é uma arquitetura onde um único sistema atende múltiplas organizações independentes (tenants).

No SGE:

- Cada escola é um tenant.  
- Todas utilizam o mesmo sistema.  
- Nenhuma pode visualizar dados de outra.  

---

## 5.2 Tipos de Multitenancy

### 1️⃣ Database por Tenant
Cada escola possui sua própria base de dados.

Vantagens:
- Isolamento total  
- Alta segurança  

Desvantagens:
- Alto custo  
- Complexidade operacional  
- Difícil escalar  

---

### 2️⃣ Schema por Tenant
Uma única base, múltiplos schemas.

Vantagens:
- Bom isolamento  
- Organização clara  

Desvantagens:
- Migrações mais complexas  
- Gestão técnica mais difícil  

---

### 3️⃣ Tabelas Compartilhadas com `school_id` (Modelo Escolhido)

Uma única base.
Tabelas compartilhadas.
Cada registro possui um campo `school_id`.

Exemplo:

students:
- id  
- name  
- birth_date  
- school_id  

Todas as queries filtram por `school_id`.

### Motivos da escolha:

- Simplicidade  
- Ideal para MVP  
- Baixo custo  
- Escalável  
- Fácil manutenção  

Requer disciplina rigorosa no backend para sempre filtrar por `school_id`.

---

# 6. Autenticação, Autorização e Segurança

## 6.1 Fluxo de Login

1. Usuário envia credenciais  
2. Backend valida  
3. Backend gera token JWT  
4. Token contém payload:

```json
{
  "user_id": 12,
  "role": "teacher",
  "school_id": 3
}
```

---

## 6.2 Uso do Token

Frontend envia:

`Authorization: Bearer <token>`

Backend:

- Decodifica token  
- Extrai payload  
- Usa school_id para filtrar dados  
- Usa role para autorizar ações  

---

## 6.3 Isolamento Entre Escolas

Mesmo que dois estudantes tenham o mesmo código:

- O token contém school_id  
- Toda query é filtrada por school_id  
- Não há acesso cruzado  

`Identidade efetiva = user_id + school_id.`

---

# 7. Perfis de Usuário e Responsabilidades

## 7.1 Admin do Sistema
- Cria escolas  
- Cria usuários da secretaria  
- Supervisiona estrutura  

## 7.2 Secretaria
- Registra estudantes  
- Atualiza dados  
- Cria turmas  
- Matricula estudantes  
- Registra professores  

## 7.3 Professor
- Visualiza turmas atribuídas  
- Lança notas por disciplina  
- Envia relatórios  

## 7.4 Diretor de Turma
- É um professor com responsabilidade adicional  
- Gere uma turma específica  
- Consolida relatórios  
- Acompanha situação global da turma  

## 7.5 Estudante
- Consulta notas  
- Consulta relatórios  
- Atualiza dados básicos (quando permitido)  

---

# 8. Modelagem de Dados e Estrutura Relacional

## Entidades Principais

School  
User  
Student  
Teacher  
Class  
Subject  
TeacherAssignment  
Enrollment  
Grade  
Report  

---

## TeacherAssignment

Resolve o problema de relação entre professor, disciplina e turma.

Conecta:

- Teacher  
- Class  
- Subject  
- School  

Permite saber:

Quem ensina o quê, em qual turma.

---

## Grade

Contém:

- student_id  
- subject_id  
- class_id  
- term  
- score  
- school_id  

Permite lançamento em lote (bulk).

---

# 9. Fluxos Operacionais Principais

## 9.1 Matrícula

Secretaria cria estudante → associa à turma → gera enrollment.

## 9.2 Atribuição de Professor

Admin ou secretaria cria TeacherAssignment.

## 9.3 Lançamento de Notas

Professor:
1. Seleciona turma  
2. Seleciona disciplina  
3. Sistema valida atribuição  
4. Envia notas em lote  
5. Backend salva  

## 9.4 Relatórios

Professores enviam relatórios → Diretor de turma consolida.

---

# 10. Rotas Essenciais do MVP

## Auth
`POST /auth/login` 
`GET /auth/me`  

## Schools
`POST /schools`  
`GET /schools`  

## Students
`POST /students` 
`GET /students` 
`GET /students/{id}`  
`PUT /students/{id}` 

## Classes
`POST /classes` 
`GET /classes`  

## TeacherAssignment
`POST /teacher-assignments`  
`GET /teacher-assignments` 

## Grades
`POST /grades/bulk`  
`GET /classes/{id}/grades`  

---

# 11. Levantamento Estatístico Escolar (Fase 03 de 03)

Antes das avaliações:

- Distribuição sexual  
- Distribuição etária  
- Órfãos  
- Deficiências  
- Situação familiar  

Funcionalidade essencial:

Atualização em massa (bulk update).

Exemplo:

Selecionar múltiplos estudantes → marcar todos como "deficiência auditiva".

Requer:

- Endpoint de atualização em lote  
- Interface com multi-select  

---

# 12. Dificuldades Técnicas e Desafios Arquiteturais

- Modelagem correta das relações  
- Controle fino de permissões  
- Garantir isolamento multitenant  
- Evitar excesso de rotas  
- Manter simplicidade no MVP  
- Lidar com resistência institucional  
- Gerenciar complexidade crescente  

A sensação de sobrecarga é normal. O sistema tem múltiplas camadas de responsabilidade.

---

# 13. Justificativas Arquiteturais e Estratégicas

As decisões foram baseadas em:

- Simplicidade inicial  
- Escalabilidade futura  
- Segurança  
- Baixo custo operacional  
- Adoção gradual  
- Estrutura preparada para expansão  

O foco foi construir uma base sólida antes de adicionar complexidade.

---

# 14. Conclusão e Direção Futura

O SGE é:

- Multitenant  
- Baseado em papéis  
- Seguro via JWT  
- Estruturado por escola  
- Preparado para relatórios  
- Preparado para estatística  
- Preparado para expansão  

