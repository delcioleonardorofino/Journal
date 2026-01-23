---
id: 1
title: Introdução ao HTMX
date: 13 de Dezembro de 2025
description: Aprenda os conceitos básicos do HTMX e como ele permite criar interações dinâmicas em suas páginas HTML sem precisar de JavaScript pesado. Ideal para simplificar a atualização de conteúdo, carregamento de partes de página e navegação assíncrona.
tags: [htmx, flask, frontend]
---

## Por que HTMX?

HTMX permite construir interfaces modernas sem frameworks pesados.  
Convenhamos que HTML e uma das coisas mais horriveis que alguem pode trabalhar com.  
Em 2007, ano mais felis da minha vida eu passe por algumas situacoes nada nobres sobre como lidar com a ansiedade.  


## Que diabos e HTML?
**HTML (HyperText Markup Language)** é a linguagem base da web, usada para estruturar conteúdo. Cada pedaço de informação é marcado usando tags, que dizem ao navegador como renderizar o conteúdo. Por exemplo, _`<h1>`_ representa um título principal, enquanto _`<p>`_ é usado para parágrafos. Para listas, podemos usar _`<ul>`_ ou _`<ol>`_, com cada item dentro de _`<li>`_. Links são criados com _`<a href="...">`_, imagens com _`<img src="..." alt="...">`_ e blocos de código com _`<pre><code>...</code></pre>`_.

Outras tags importantes incluem _`<header>`_ e _`<footer>`_ para topo e rodapé da página, _`<section>`_ para divisões semânticas, e _`<div>`_ para agrupamentos genéricos. Estilos são aplicados com atributos ou via CSS externo, enquanto scripts usam _`<script>`_. Tags podem ter atributos como class, id, src, alt e href, permitindo identificação, estilo e comportamento.

>Nenhuma tag vai ser autoexplicativa. Voce precisa saber quando usar lendo a documentacao do html.
>HTML e uma daquelas tecnologias que nao precisa de tutorial em video. Tem boa documentacao e basta uma boa leitura para entender.

Em páginas modernas, usamos `<nav>` para menus, `<article>` para posts ou notícias, `<aside>` para conteúdos secundários, e `<main>` para o conteúdo principal. Juntas, essas tags tornam a página semântica, acessível e fácil de estilizar.




<h3 id='secao-2'>Tags nao sao tuas inimigas</h3>
