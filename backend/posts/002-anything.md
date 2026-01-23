---
id: 2
title: HTML e suas parvoices
date: 2026-01-20
description: HTMX permite construir interfaces modernas sem frameworks pesados. Convenhamos que HTML e uma das coisas mais horriveis que alguem pode trabalhar com. Em 2007, ano mais felis da minha vida eu passe por algumas situacoes nada nobres sobre como lidar com a ansiedade.  

tags: [html, frontend]
---


<p id="introducao">HTML (HyperText Markup Language) é a linguagem fundamental da web, usada para estruturar conteúdo e dar significado semântico aos elementos de uma página. Neste post vamos explorar algumas das tags mais comuns, como organizar conteúdo e criar uma navegação interna usando links de índice.</p>


## Tags HTML Comuns
<p id="tags-html">Existem diversas tags em HTML. Algumas das mais utilizadas incluem:</p>

- _`<h1>`_ a _`<h6>`_ → Títulos e subtítulos, com níveis hierárquicos
- _`<p>`_ → Parágrafos de texto
- _`<div>`_ → Containers genéricos para agrupar conteúdo
- _`<section>`_ → Divisão semântica de uma página
- _`<header>`_ / _`<footer>`_ → Cabeçalho e rodapé
- _`<article>`_ → Artigo ou bloco de conteúdo independente

## Listas e Estruturas
<p id="listas">HTML permite criar listas ordenadas e não ordenadas para organizar informações:</p>

```html
<ul>
  <li>Item de lista não ordenada 1</li>
  <li>Item de lista não ordenada 2</li>
</ul>

<ol>
  <li>Primeiro item</li>
  <li>Segundo item</li>
</ol>
```

Também podemos aninhar listas para criar hierarquias complexas.

## Links e Imagens
Para navegar e ilustrar páginas usamos links e imagens:

```html
<a href="https://example.com">Visite o Example.com</a>
<img src="imagem.png" alt="Descrição da imagem">
```

* O atributo `href` define o destino do link  
* `alt` descreve a imagem para acessibilidade  

## Formulários
<p id="formularios">Formulários permitem capturar dados do usuário:</p>

```html
<form action="/enviar" method="post">
  <label for="nome">Nome:</label>
  <input type="text" id="nome" name="nome">
  <button type="submit">Enviar</button>
</form>
```

- Cada `input` deve ter `name` para enviar dados  
- `button type="submit"` envia o formulário  

## Blocos de Código
<p id="codigo">Para mostrar código em páginas, usamos:</p>

Com Markdown, podemos usar a sintaxe de blocos de código:

```javascript
function soma(a, b):
    return a + b
```

O CSS pode estilizar esses blocos com `codehilite`.

## Conclusão
HTML é simples de aprender, mas extremamente poderoso. Usando tags semânticas, listas, links internos, imagens e blocos de código, você consegue criar páginas estruturadas, navegáveis e acessíveis. Combinado com CSS e JavaScript, torna-se a base de qualquer site moderno.
