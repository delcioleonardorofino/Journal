---
id: 2
title: Dia 2 | Segurança e Permissões 
date: 12 de Fevereiro de 2026
description: Veja a documentacao do processo de construncao de um sistema de gestao escolar multi-tenant.
---


## 1. Introdução

Quando decidi construir este Sistema de Gestão Escolar, percebi rapidamente que segurança não poderia ser um detalhe técnico. Eu não estou lidando apenas com tabelas e registros. Estou lidando com:

- Dados pessoais de estudantes  
- Notas escolares  
- Relatórios pedagógicos  
- Informações sensíveis (órfãos, deficiências, situação familiar)  
- Estrutura institucional da escola  

Por isso, tratei a segurança como um dos pilares centrais do sistema. Minha arquitetura de segurança é baseada em:

- FastAPI como framework backend  
- JWT para autenticação stateless  
- Hash seguro de senhas  
- Isolamento multitenant rigoroso  

---

# 2. Escolha da Stack de Segurança

## 2.1 FastAPI

Escolhi o FastAPI porque ele me oferece:

- Alto desempenho  
- Tipagem forte  
- Validação automática com Pydantic  
- Sistema de dependências elegante  
- Organização clara da autenticação  

A injeção de dependências do FastAPI me permite centralizar a lógica de autenticação e autorização, evitando código repetido e vulnerável espalhado pelo projeto.

---

## 2.2 Hash de Senha

Eu nunca armazeno senhas em texto puro. Para isso uso `passlib` com bcrypt:

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Exemplo de uso
senha = "MeuSegredo123"
hash_da_senha = hash_password(senha)
assert verify_password("MeuSegredo123", hash_da_senha)  # True
```

> O hash garante que mesmo que o banco seja vazado, ninguém consegue descobrir a senha original.

---

## 2.3 JWT para Autenticação

Quando o usuário faz login, eu gero um **JWT** que contém informações essenciais: `user_id`, `role` e `school_id`.

```python
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "uma_chave_muito_segura_aleatoria"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

payload = {"user_id": 12, "role": "teacher", "school_id": 3}
token = create_access_token(payload)
print(token)
```

> Esse token será enviado ao frontend e usado em todas as requisições protegidas.

---

## 2.4 Decodificação e Validação do JWT

No backend, uso dependências do FastAPI para decodificar e validar o token:

```python
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        role: str = payload.get("role")
        school_id: int = payload.get("school_id")
        if user_id is None or role is None or school_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )
        return {"user_id": user_id, "role": role, "school_id": school_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )
```

> Qualquer rota que precise de autenticação apenas injeta `current_user`. O filtro `school_id` garante que o usuário só acesse dados da sua escola.

---

## 2.5 Criação de Usuários com Hash

Quando crio usuários, aplico hash à senha antes de salvar:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

def create_user(user_data: UserCreate):
    hashed_pw = hash_password(user_data.password)
    user_record = {
        "username": user_data.username,
        "hashed_password": hashed_pw,
        "role": user_data.role
    }
    # db.save(user_record)
    return user_record

novo_user = UserCreate(username="joao.professor", password="12345", role="teacher")
user_criado = create_user(novo_user)
print(user_criado)
```

---

## 2.6 Controle de Acesso por Papel (RBAC) e Tenant

```python
from fastapi import Depends, HTTPException

def require_teacher(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "teacher":
        raise HTTPException(status_code=403, detail="Acesso negado")
    return current_user

@app.get("/minhas-turmas")
def minhas_turmas(current_user: dict = Depends(require_teacher)):
    school_id = current_user["school_id"]
    # turmas = db.query(Turma).filter(Turma.school_id == school_id)
    return {"school_id": school_id, "message": "Você só acessa suas turmas"}
```

> Assim, qualquer tentativa de acessar dados de outra escola é bloqueada. Mesmo IDs duplicados entre escolas não permitem vazamento.

---

# 3. Fluxo Completo

1. Usuário envia login  
2. Backend verifica hash da senha  
3. Backend gera JWT com `user_id`, `role` e `school_id`  
4. Frontend envia token nas requisições  
5. Backend valida token, role e school_id antes de devolver dados  
6. Qualquer tentativa de violação é barrada  

---

# 4. Conclusão

Implementar segurança no SGE envolveu combinar:

- **Hash seguro** para senhas  
- **JWT** para autenticação stateless  
- **Controle de papel (RBAC)**  
- **Isolamento multitenant (school_id)**  

Cada escolha foi feita pensando em proteger os dados sensíveis de estudantes e escolas, mantendo a arquitetura escalável e simples para o MVP.  

A segurança é uma camada ética, não apenas técnica — estou protegendo pessoas, não apenas dados.

