# 🔐 Sistema de Login e Cadastro

Sistema de login e cadastro desenvolvido em **Python**, com interface gráfica utilizando **CustomTkinter** e banco de dados **SQLite3**.

O projeto foi desenvolvido com finalidade **acadêmica e de estudo**, buscando praticar conceitos de programação orientada a objetos, interfaces gráficas, manipulação de banco de dados e operações SQL.

---

## 📌 Sobre o Projeto

O **SistemaDeLogin** permite que o usuário:

* 🔑 Realize login utilizando nome de usuário e senha;
* 📝 Cadastre novos usuários;
* 📧 Informe um e-mail durante o cadastro;
* 🔒 Cadastre e confirme uma senha;
* 👁️ Mostre ou oculte a senha digitada;
* 🗄️ Armazene os dados em um banco de dados SQLite;
* ⚠️ Receba mensagens de erro e avisos durante o preenchimento dos formulários.

O programa possui duas telas principais: **Tela de Login** e **Tela de Cadastro**.

---

## 🖥️ Tecnologias Utilizadas

| Tecnologia       | Utilização                               |
| ---------------- | ---------------------------------------- |
| 🐍 Python        | Linguagem principal                      |
| 🎨 CustomTkinter | Interface gráfica                        |
| 🖼️ Tkinter      | Componentes adicionais da interface      |
| 🗄️ SQLite3      | Banco de dados                           |
| 💾 SQL           | Criação e consulta da tabela de usuários |

O SQLite é utilizado através da biblioteca `sqlite3`, disponível na biblioteca padrão do Python.

---

## 📂 Estrutura do Projeto

```text
SistemaDeLogin/
│
├── app.py
├── Sistema_cadastros.db
├── logi-img.png
└── README.md
```

### `app.py`

Arquivo principal responsável pela execução do sistema.

Nele estão implementadas as classes, funções, telas, validações e operações com o banco de dados.

### `Sistema_cadastros.db`

Banco de dados SQLite responsável pelo armazenamento dos usuários cadastrados.

A aplicação cria ou abre esse arquivo automaticamente através da conexão SQLite.

### `logi-img.png`

Imagem utilizada na interface da tela de login. O código espera que ela esteja na mesma pasta do arquivo Python.

---

## ⚙️ Funcionamento

### 🔑 1. Tela de Login

Na tela inicial, o usuário informa:

* Nome de usuário;
* Senha.

Depois, pode clicar em **Fazer Login**.

O sistema realiza uma consulta no banco de dados procurando um registro correspondente ao nome de usuário e à senha informados.

Também existe a opção:

> 👁️ Clique para ver a senha

Essa opção permite alternar entre senha oculta (`*`) e senha visível.

---

### 📝 2. Tela de Cadastro

O usuário pode realizar um novo cadastro informando:

* Nome de usuário;
* E-mail;
* Senha;
* Confirmação da senha.

O sistema possui validações para verificar:

* Se os campos foram preenchidos;
* Se o nome de usuário possui pelo menos 4 caracteres;
* Se a senha possui pelo menos 4 caracteres;
* Se a senha e a confirmação são iguais.

---

## 🗄️ Banco de Dados

O projeto utiliza uma tabela chamada `Usuarios`.

Sua estrutura possui:

```text
Usuarios
│
├── id
├── Username
├── Email
├── Senha
└── Confirma_Senha
```

O campo `id` utiliza `INTEGER PRIMARY KEY AUTOINCREMENT`, permitindo que o SQLite gere automaticamente os identificadores dos usuários.

---

## 🧩 Estrutura do Código

O projeto utiliza duas classes principais.

### `BackEnd`

Responsável pela parte relacionada ao banco de dados e às regras do sistema.

Entre suas principais funções estão:

```python
conecta_db()
desconecta_db()
cria_tabela()
cadastrar_usuario()
verifica_login()
```

A classe concentra as operações de conexão, criação da tabela, cadastro e verificação de login.

### `App`

É a classe responsável pela interface gráfica.

Ela herda de:

```python
class App(ctk.CTk, BackEnd):
```

Dessa forma, a aplicação reúne a interface do **CustomTkinter** com as funcionalidades de banco de dados implementadas na classe `BackEnd`.

---

## 🔄 Fluxo do Sistema

```text
                 ┌─────────────────┐
                 │   Iniciar App   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Tela Login    │
                 └───────┬─────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       ┌─────────────┐       ┌─────────────┐
       │ Fazer Login │       │  Cadastrar  │
       └──────┬──────┘       └──────┬──────┘
              │                     │
              ▼                     ▼
       ┌─────────────┐       ┌─────────────┐
       │ Consulta DB │       │ Validações  │
       └──────┬──────┘       └──────┬──────┘
              │                     │
              ▼                     ▼
       ┌─────────────┐       ┌─────────────┐
       │ Login OK?   │       │ Salva no DB │
       └─────────────┘       └─────────────┘
```

---

## 🛡️ SQL Injection

No cadastro, o projeto utiliza `?` como placeholder para inserir os valores no SQL:

```python
INSERT INTO Usuarios
(Username, Email, Senha, Confirma_Senha)
VALUES (?, ?, ?, ?)
```

Essa abordagem é uma boa prática porque evita a concatenação direta dos valores fornecidos pelo usuário na instrução SQL.

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta

```bash
cd SistemaDeLogin
```

### 3. Instale o CustomTkinter

```bash
pip install customtkinter
```

> O `tkinter` e o `sqlite3` normalmente fazem parte da instalação do Python.

### 4. Execute o programa

```bash
python app.py
```

Ao iniciar, o programa cria a janela do sistema, configura a interface, cria a tabela do banco de dados e inicia o loop principal da aplicação.

---

## 📚 Objetivos de Estudo

Este projeto foi desenvolvido para praticar conceitos importantes de programação, como:

* 🐍 Fundamentos de Python;
* 🧱 Classes e objetos;
* 🔗 Herança múltipla;
* 🖥️ Desenvolvimento de interfaces gráficas;
* 🗄️ Banco de dados SQLite;
* 🔎 Consultas SQL;
* ✅ Validação de dados;
* 🔐 Sistemas de autenticação;
* 🧩 Organização de código;
* 🐞 Identificação e correção de possíveis bugs.

---

## 🔧 Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Criptografar as senhas antes de armazená-las;
* [ ] Impedir cadastro de nomes de usuário duplicados;
* [ ] Impedir cadastro de e-mails duplicados;
* [ ] Validar formato do e-mail;
* [ ] Melhorar o tratamento de exceções;
* [ ] Corrigir a validação do login quando o usuário não existe;
* [ ] Validar os campos antes de executar o `INSERT`;
* [ ] Adicionar recuperação de senha;
* [ ] Criar uma tela inicial após o login;
* [ ] Adicionar botão de logout;
* [ ] Melhorar a organização das classes;
* [ ] Criar uma interface mais responsiva.

---

## ⚠️ Pontos de Estudo Encontrados no Código

O projeto também contém alguns pontos interessantes para estudar e melhorar.

### Validação antes do INSERT

Atualmente, o `INSERT` é executado antes das validações do cadastro. O próprio código identifica esse comportamento como um possível problema. O ideal é realizar todas as validações primeiro e somente depois inserir os dados no banco.

### Verificação do Login

A consulta utiliza `fetchone()`, que pode retornar `None` quando nenhum usuário é encontrado. O código atual tenta utilizar `in` sobre esse resultado, o que pode gerar `TypeError` quando não existe registro correspondente.

### Senhas

Atualmente, o projeto armazena a senha diretamente no banco de dados. Para uma aplicação real, seria necessário utilizar um mecanismo apropriado de **hash de senhas**, em vez de armazená-las em texto puro.

---

## 👨‍💻 Projeto Acadêmico

Este projeto foi desenvolvido como parte dos estudos de **Engenharia de Software**, com foco na prática de desenvolvimento em Python, interfaces gráficas, banco de dados e sistemas de autenticação.

---

## 📌 Status

🟢 **Projeto finalizado para fins de estudo**

O sistema está funcional como uma aplicação básica de login e cadastro, mas possui pontos que podem ser aprimorados para aproximá-lo de uma aplicação de produção.

---

⭐ **Se este projeto foi útil para seus estudos, considere deixar uma estrela no repositório!**
