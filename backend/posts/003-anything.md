---
id: 3
title: Desenvolvimento vs Produção - os bugs que te pegam desprevenido
date: 18 de Janeiro de 2026
description: Entenda por que o que funciona na sua máquina de desenvolvimento nem sempre funciona em produção e por que os bugs aparecem nos piores momentos.
tags: [desenvolvimento, produção, bugs, engenharia, software]
---

## O paraíso do desenvolvimento

Quando estás a programar no teu computador, tudo parece fácil.  
O código roda, os erros aparecem claros, e tu consegues resolver rápido.  

É o **ambiente de desenvolvimento**: seguro, controlado, previsível.  
Parece que tens tudo na mão.

> Tipo quando cozinhamos em casa: todos os ingredientes estão prontos, a panela é nova, e a receita está à mão. Parece que não tem como falhar.

---

## A ilusão

No desenvolvimento, tens algumas vantagens:  
- o banco de dados está no teu PC, sem ninguém a encher com dados malucos  
- as imagens e ficheiros estão sempre no caminho certo  
- ninguém vai clicar em botões que tu nem imaginaste  

Tudo funciona como esperado. Dá até impressão que **controlas tudo**.  

Mas, bro, isso é só uma ilusão.

---

## Produção é outro mundo

Quando o código vai pra produção, a história muda.  
De repente:  
- chegam dados inesperados — nomes vazios, emails com símbolos estranhos  
- usuários clicam em botões que tu nem pensaste  
- o servidor fica lento ou cai  

Os bugs que antes eram simples agora são difíceis de apanhar.

> É como cozinhar para 100 pessoas num restaurante lotado: a panela de casa não ajuda, os ingredientes podem faltar, e alguém sempre vai pedir algo diferente.

---

## Por que bugs em produção são mais complicados

1. **Ambiente imprevisível**  
   Em produção, vários sistemas interagem e um erro pode aparecer de forma inesperada.

2. **Dados reais**  
   Usuários não seguem regras: escrevem “123abc” num campo que quer só números, ou deixam campos vazios.

3. **Escala**  
   No desenvolvimento testas com poucos registros.  
   Em produção tens milhares de utilizadores ao mesmo tempo.

4. **Pressão**  
   Bugs em produção custam dinheiro, stress e noites sem dormir.  
   Em desenvolvimento, é só frustração momentânea.

---

## Sobrevivendo aos bugs

Algumas dicas pra não te perder:  

- **Regista tudo**  
  Logs são essenciais pra saber o que aconteceu. Se não tiver logs, ficas às cegas.

- **Teste, mas não confies 100%**  
  Testes ajudam, mas não replicam o mundo real.

- **Prepara teu código pra falhar**  
  Sistemas robustos lidam melhor com erros; sistemas frágeis quebram com qualquer problema.

- **Humildade**  
  O que funciona na tua máquina não garante que funcione pra todos.

> Produção ensina rápido, e às vezes de forma dura.
> Entt, se tiveres uma cena no teu pc, faz deploy e complete o ciclo, mesmo que seja dificil.

---

## Resumo

- Desenvolvimento é seguro, previsível, mas ilusório.  
- Produção é imprevisível, cheia de dados reais e interações complicadas.  
- Bugs em produção são mais difíceis porque lidam com caos real.  
- Preparar teu código pra falhar é tão importante quanto fazê-lo funcionar.  

Se lembra: **“funciona na minha máquina” ≠ “funciona de verdade”**.  
Aprender a lidar com produção é o que faz a diferença entre um programador “kmk” e um engenheiro que sabe o que está a fazer.
