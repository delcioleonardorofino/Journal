---
id: 1
title: Dia 1 | As motivações e a arquitetura
date: 11 de Fevereiro de 2026
description: Qualquer bom sistema deve ser pensado e bem planejado desde o início. Por isso, na fase de desenvolvimento de uma ideia, o primeiro passo é arquitetar.
---



## A ideia e o motivo 

Enquanto lia a mensagem de meu irmão me contando eufórico sobre o desempenho académico de meu sobrinho, pensei no quão seria útil ter um sistema de gestão escolar.
Inspirado nas utilidades dos sistemas de gestão universitária, porquê não expandir a ideia de digitalização do processo académico-administrativo para o sector do ensino fundamental?

Ter as notas de nossos educandos para ver/consultar sempre que possível, de modo estruturado e seguindo uma lógica bem definida seria algo de extrema utilidade.

>Por isso decidí construir um eu mesmo.

## Planejamento

O planejamento é uma fase que deixa todo dev preguiçoso. Somos às vezes convecidos pelos nossos egos que a melhor e mais importante parte do desenvolvimento de software é na escrita do código. Cuspir linhas de código e sentir a nostalgia por ter decorado uma sintaxe inteira. Feliz ou infelizmente, a parte mais importante de tudo isso é arquitectar, traduzir o desejo abstrato em regras de negócio bem definidas, porque no final de tudo escrever código é mais ferramental do que objectivo.

>Tendemos a objectivar o código, nos esquecendo que é parte de uma vasta gama de ferramentas que se usam para atingir um produto que no fim não é código, mas um serviço ou uma infraestrutura.

A sensação de ver o terminal rodar é viciante, mas construir sem arquitetura é como levantar um prédio sem planta: na primeira alteração estrutural, tudo desaba.  

​Um Sistema de Gestão Escolar (SGE) Multi-Tenant é um desafio arquitetural fascinante porque exige um isolamento rigoroso de dados entre escolas (Tenants) enquanto partilham a mesma infraestrutura.


​Aqui está uma proposta de estruturação para o MVP, focada no equilíbrio entre utilidade real e viabilidade técnica.  

## Arquitetura Multi-Tenant


​Antes das funcionalidades, precisamos decidir como os dados serão separados. Para um MVP escalável, encontrei a possibilidade de seguir por uma das duas abordagens:

* ​**Database-per-tenant:** Cada escola tem o seu próprio banco de dados. Máxima segurança, mas maior custo de manutenção (Pior para uma só pessoa, praticamente inviável a longo prazo).

* **​Shared Database (Discriminator Column):** Todas as escolas na mesma tabela, diferenciadas por um `school_id`. É a forma mais rápida de validar o MVP e mais barata de hospedar.


## ​Levantamento de Requisitos (MVP)


​Para que o sistema seja funcional logo no "Dia 1", ele precisa cobrir o triângulo básico: `Administração, Académico e Financeiro`.  
Decidí que o financeiro podia ser o último bloco a ser implementado (tudo que tem a ver com dinheiro deve ser feito com toda a serenidade e sem pressa).

 
​**Core Administrativo (O "Cérebro")**

_Gestão de Tenants:_ Cadastro de escolas, períodos letivos e turmas.

_Controle de Acesso (RBAC):_ Diferenciar o que o Diretor, o Professor, o Aluno e o Encarregado de Educação podem ver.


​**Gestão Académica (O "Coração")**

_Matrículas e Entrâncias:_ Cadastro de alunos e alocação em turmas.

_Diário de Classe Digital:_ Registo de faltas e sumários.

_Avaliações e Notas:_ Lançamento de notas e cálculo automático de médias.


​**Financeiro Essencial (A "Sobrevivência")**

* _Gestão de Propinas/Mensalidades:_ Emissão de faturas e controlo de pagamentos (quem pagou e quem deve).