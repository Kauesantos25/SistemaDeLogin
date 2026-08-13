# ============================================================
# SISTEMA DE LOGIN E CADASTRO - CustomTkinter + SQLite3
# ============================================================
# Este programa cria uma interface gráfica (GUI) com duas telas:
#   1) Tela de Login
#   2) Tela de Cadastro
# Os dados dos usuários são armazenados em um banco de dados
# SQLite local (arquivo "Sistema_cadastros.db").
# ============================================================

# Importar a biblioteca tkinter
import customtkinter as ctk          # CustomTkinter: extensão do tkinter com widgets mais modernos e estilizados
from tkinter import *                 # Importa tudo do tkinter "puro" (ex: PhotoImage, END, etc.)
from tkinter import messagebox        # Módulo específico para exibir caixas de mensagem (erro, aviso, info)

# Importar o SQlite3
import sqlite3                        # Biblioteca padrão do Python para trabalhar com banco de dados SQLite


# ============================================================
# CLASSE BackEnd
# ------------------------------------------------------------
# Responsável por toda a lógica de banco de dados:
# conexão, criação de tabela, cadastro e verificação de login.
# Ela é usada como "mixin" (herança múltipla) na classe App.
# ============================================================
class BackEnd():

    def conecta_db(self):
        """Abre a conexão com o banco de dados SQLite e cria um cursor
        (objeto usado para executar comandos SQL)."""
        self.conn = sqlite3.connect("Sistema_cadastros.db")  # Cria/abre o arquivo do banco de dados
        self.cursor = self.conn.cursor()                     # Cursor permite executar comandos SQL
        print("Banco de dados conectado com sucesso!")

    def desconecta_db(self):
        """Fecha a conexão com o banco de dados.
        Importante para liberar o arquivo e evitar corrupção de dados."""
        self.conn.close()
        print("Banco de dados desconectado!")

    def cria_tabela(self):
        """Cria a tabela 'Usuarios' caso ela ainda não exista.
        É chamada uma vez, quando o app é iniciado (ver __init__ da classe App)."""
        self.conecta_db()  # Abre a conexão antes de qualquer operação no banco

        # IF NOT EXISTS evita erro caso a tabela já tenha sido criada anteriormente
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL
            );
        """)
        self.conn.commit()  # Salva (grava) a alteração no banco de dados
        print("Tabela criada com sucesso!")
        self.desconecta_db()  # Fecha a conexão após terminar a operação

    def cadastrar_usuario(self):
        """Lê os dados digitados no formulário de cadastro, valida os campos
        e insere o novo usuário no banco de dados."""

        # Captura o texto digitado em cada campo (Entry) do formulário de cadastro
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_entry.get()

        self.conecta_db()

        # ATENÇÃO (ponto de estudo/possível bug):
        # O INSERT é executado ANTES das validações abaixo (campos vazios,
        # tamanho mínimo, senhas iguais). Ou seja, mesmo que a validação
        # falhe depois, o registro já foi inserido no banco (via execute),
        # faltando apenas o commit() dentro do "else". Isso significa que
        # dados incompletos/incorretos podem ficar "pendentes" de forma
        # inconsistente. O ideal seria validar PRIMEIRO e só then executar
        # o INSERT dentro do bloco "else".
        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
            VALUES (?, ?, ?, ?)""", (self.username_cadastro, self.email_cadastro, self.senha_cadastro, 
                                     self.confirma_senha_cadastro ))
        # O uso de "?" como placeholder (em vez de concatenar strings) é uma
        # boa prática: evita SQL Injection.

        try:
            # Validação 1: verifica se algum campo está vazio
            if  (self.username_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""):
                messagebox.showerror(title = "Sistema de login", message= "ERRO! Por favor, preencha todos os campos!")

            # Validação 2: nome de usuário deve ter pelo menos 4 caracteres
            elif (len(self.username_cadastro ) < 4):
                messagebox.showwarning (title="Sistema de login", message = "O nome de usuário deve ser de pelo menos 4 caracteres!")

            # Validação 3: senha deve ter pelo menos 4 caracteres
            elif (len(self.senha_cadastro) < 4):
                messagebox.showwarning(title = "Sistema de login", message = "ERRO!!!\nA senha deve conter no mínimo 4 dígitos!")

            # Validação 4: senha e confirmação de senha devem ser iguais
            elif (self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title = "Sistema de login", message = "ERRO!!!\nAs senhas colocadas não são iguais, coloque senha iguais!")          

            else:
                # Só aqui os dados são de fato confirmados (commit) no banco
                self.conn.commit()
                messagebox.showinfo(title ="Sistema de login", message = f"Parabéns {self.username_cadastro}\nOs seus dados foram cadastrados com sucesso! ")

            self.desconecta_db()          # Fecha a conexão com o banco
            self.limpar_entry_cadastro()  # Limpa os campos do formulário

        except:
            # Captura qualquer erro inesperado durante o processo
            # OBS: usar "except:" genérico não é uma boa prática, pois
            # esconde o tipo real do erro. O ideal seria usar
            # "except Exception as e:" e exibir/registrar o erro (e).
            messagebox.showerror(title= "Sistema de login", message = "Erro no processamento do seu cadastro!\n Por favor, tente novamente!")
            self.desconecta_db()

    def verifica_login(self):
        """Lê usuário e senha digitados na tela de login e verifica
        se existem no banco de dados."""

        self.username_login = self.username_login_entry.get()
        self.senha_login = self.senha_login_entry.get()

        self.conecta_db()

        # Busca no banco um registro cujo Username e Senha coincidam
        # com os valores digitados
        self.cursor.execute('''                
            SELECT * FROM Usuarios
            WHERE (Username =? AND Senha =?) ''', 
            (self.username_login, self.senha_login)) # Verifica se o username e senha correspondem no Banco de dados

        # fetchone() retorna a primeira linha encontrada (tupla) ou None se não encontrar nada
        self.verifica_dados = self.cursor.fetchone()

        # Percorre a tabela usuário e verifica se o usuário e a senha estão corretos 
        if (self.username_login == "" or self.senha_login == ""):
                # Campos vazios
                messagebox.showwarning(title = "Sistem de Login", message = "Por favor preencha todos os campos!")

        elif (self.username_login in self.verifica_dados and self.senha_login in self.verifica_dados):
                # ATENÇÃO (ponto de estudo/possível bug):
                # 1) Se "verifica_dados" for None (usuário não encontrado),
                #    "in None" gera um TypeError, pois não é possível usar
                #    "in" em um objeto None. Isso quebraria o programa antes
                #    mesmo de cair no "else" abaixo.
                # 2) Usar "in" em uma tupla verifica se o valor existe em
                #    QUALQUER posição da tupla (id, username, email, senha,
                #    confirma_senha). Isso é menos seguro/preciso do que
                #    comparar diretamente verifica_dados[1] == username e
                #    verifica_dados[3] == senha, por exemplo.
                messagebox.showinfo(title = "Sistema de Login", message = f"Parabéns{self.username_login}\nLogin feito com sucesso!")
                self.limpar_entry_login()
                self.desconecta_db()

        else:
            # Usuário/senha não encontrados no banco
            messagebox.showerror(title ="Sistema de Login", message = "ERRO!!!\nDados não encontrados no sistema.\nPor favor, verifique os seus dados ou cadastre-se em nosso sistema!")
            self.desconecta_db()


# ============================================================
# CLASSE App
# ------------------------------------------------------------
# Herda de ctk.CTk (janela principal do CustomTkinter) e de
# BackEnd (lógica de banco de dados). É a classe principal que
# monta e controla toda a interface gráfica.
# ============================================================
class App (ctk.CTk, BackEnd): # chama a tela do tkinter dentro da classe App
    def __init__(self): # a função init (função inicial) determina o que vai acontecer quando a classe for chamada
        super().__init__() # super define que a função init vai ser chamada da classe pai (ctk.CTk)
        self.configuracoes_da_janela_inicial() # chama a função configuracoes_da_janela_inicial
        self.tela_de_login() # chama a função tela_de_login
        self.cria_tabela() # chama a função de criar tabela
        # OBS: a ordem de chamada aqui não afeta a montagem da tela (a tabela
        # só precisa existir antes do usuário clicar em login/cadastro),
        # mas seria mais intuitivo criar a tabela antes de montar a tela.


    # ------------------------------------------------------------
    # Configurações da janela principal
    # ------------------------------------------------------------
    def configuracoes_da_janela_inicial(self):
        """Define tamanho, título e comportamento de redimensionamento
        da janela principal da aplicação."""
        self.geometry("700x400") # define o tamanho da janela (largura x altura)
        self.title("Sistema de Login") # define o título exibido na barra da janela
        self.resizable(False, False) # impede que a janela seja redimensionada (largura, altura)


    # ------------------------------------------------------------
    # Tela de Login
    # ------------------------------------------------------------
    def tela_de_login(self):
        """Monta todos os widgets (imagem, título, campos de entrada e
        botões) da tela de login."""

        # Trabalhando com as imagens
        self.img = PhotoImage(file="logi-img.png") # carrega a imagem do arquivo logi-img.png (deve estar na mesma pasta do script)
        self.img = self.img.subsample(6,6) # reduz a imagem para 1/6 do tamanho original (subsample reduz resolução)
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img) # cria um label (rótulo) apenas para exibir a imagem
        self.lb_img.grid(row=1, column = 0, padx = 10) # posiciona a imagem na grade (grid) da janela


        # Trabalhando com o título
        self.title = ctk.CTkLabel(self, text="Faça o seu login ou Cadastre-se\nem nossa plataforma para acessar\nos nossos serviços!", font=("Century Gothic bold", 14)) # texto de boas-vindas
        self.title.grid (row=0, column=0, pady=10, padx=10) # posiciona o título acima da imagem
        # OBS: "self.title" aqui SOBRESCREVE o método/atributo "title" herdado
        # de ctk.CTk (usado para definir o título da janela). Isso funciona
        # porque em Python não há erro de sobrescrita, mas é uma prática de
        # nomenclatura arriscada — o ideal seria usar outro nome, como
        # "self.lb_title_principal".


        # Criar a Frame do formulário de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380) # cria um "container" (frame) para agrupar os widgets do login
        self.frame_login.place(x= 350, y=10) # posiciona o frame usando coordenadas absolutas (x, y)


        # Colocando Widgets dentro do frame - formulário de login
        self.lb_title = ctk.CTkLabel (self.frame_login, text="Faça o seu Login", font=("Century Gothic bold", 22)) # título do formulário
        self.lb_title.grid(row=0, column= 0,padx= 10, pady=10) # posiciona o título dentro do frame


        # Criando os Entry para o formulário de login
        self.username_login_entry = ctk.CTkEntry (self.frame_login, width=300, placeholder_text=
        "Digite o seu nome de usuário:", font =("Century Gothic bold", 16), corner_radius=15) # campo de texto para o usuário digitar o username
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10) # posiciona o campo na tela


        # Criando o Entry para a senha
        self.senha_login_entry = ctk.CTkEntry (self.frame_login, width=300, placeholder_text=
        "Digite o sua senha:", font =("Century Gothic bold", 16), corner_radius =15, show="*") # show="*" esconde os caracteres digitados (senha)
        self.senha_login_entry.grid(row=2, column=0, padx=10, pady=10)


        # Criando o checkbox para ver a senha   
        self.ver_senha = ctk.CTkCheckBox (self.frame_login, text="Clique para ver a senha", font =("Century Gothic bold", 12), corner_radius =20, command=self.mostrar_senha_login) # ao marcar/desmarcar, chama mostrar_senha_login
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10)


        # Criando o botão de login
        self.btn_login_entry = ctk.CTkButton (self.frame_login, text="Fazer Login".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15, command = self.verifica_login) # ao clicar, executa a função verifica_login (herdada de BackEnd)
        self.btn_login_entry.grid(row=4, column=0, padx=10, pady=10)


        # Criando o label para o texto de cadastro
        self.span = ctk.CTkLabel(self.frame_login, text="Se não possui uma conta, clique no\nbotão abaixo para se cadastrar!", font=("Century Gothic", 10)) # texto explicativo
        self.span.grid(row=5, column=0, padx=10, pady=10)


        # Criando o botão de cadastro
        self.btn_cadastro = ctk.CTkButton (self.frame_login, text="Cadastrar".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15, command=self.tela_de_cadastro) # ao clicar, troca para a tela de cadastro
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=10)


    # ------------------------------------------------------------
    # Tela de cadastro
    # ------------------------------------------------------------
    def tela_de_cadastro(self):
        """Remove (esconde) a tela de login e monta a tela de cadastro
        de novos usuários."""

        # Remover a tela de login para abrir a tela de cadastro 
        self.frame_login.place_forget() # esconde o frame de login (não destrói, apenas remove da exibição)


        # Criar a Frame do formulário de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380) 
        self.frame_cadastro.place(x= 350, y=10) 


         # Titulo 
        self.title = ctk.CTkLabel(self.frame_cadastro, text="Faça o seu Cadastro", font=("Century Gothic bold", 20))
        self.title.grid (row=0, column=0, pady=10, padx=10)

        
        # Criando os Entry para o formulário de cadastro
        self.username_cadastro_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Digite o seu nome de usuário:", font =("Century Gothic bold", 16), corner_radius=15) 
        self.username_cadastro_entry.grid(row=1, column=0, padx=10, pady=5) 


        self.email_cadastro_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Digite o seu e-mail:", font =("Century Gothic bold", 16), corner_radius=15) 
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=5) 


        # Criando o Entry para a senha
        self.senha_cadastro_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Digite a sua senha:", font =("Century Gothic bold", 16), corner_radius =15, show="*") 
        self.senha_cadastro_entry.grid(row=3, column=0, padx=10, pady=5)

        self.confirma_senha_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Confirme sua senha:", font =("Century Gothic bold", 16), corner_radius =15, show="*") 
        self.confirma_senha_entry.grid(row=4, column=0, padx=10, pady=5)


        # Criando o checkbox para ver a senha   
        self.ver_senha = ctk.CTkCheckBox (self.frame_cadastro, text="Clique para ver a senha", font =
        ("Century Gothic bold", 12), corner_radius =20, command=self.mostrar_senha_cadastro) # ao marcar, mostra as duas senhas em texto plano
        self.ver_senha.grid(row=5, column=0, pady=10)
        # OBS: este checkbox reutiliza o mesmo nome de atributo
        # "self.ver_senha" usado na tela de login. Como só existe uma tela
        # visível por vez, isso não causa erro, mas sobrescreve a
        # referência ao checkbox da tela de login.


        # Criando o botão de cadastro
        self.btn_cadastrar_user = ctk.CTkButton (self.frame_cadastro, text="Fazer Cadastro".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15, command=self.cadastrar_usuario) # ao clicar, executa cadastrar_usuario (herdada de BackEnd)
        self.btn_cadastrar_user.grid(row=6, column=0, padx=10, pady=10)


        # Criando o botão de Cadastro
        self.btn_login_back = ctk.CTkButton (self.frame_cadastro, text="Voltar ao login".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15, fg_color="#444", hover_color="#333", command= self.tela_de_login) # ao clicar, volta para a tela de login
        self.btn_login_back.grid(row=7, column=0, padx=10, pady=10)
        # OBS: ao voltar, tela_de_login() é chamada novamente e recria TODOS
        # os widgets de login do zero (inclusive um novo frame_login), em vez
        # de apenas reexibir o frame já existente. Funciona, mas gera
        # widgets "duplicados" na memória a cada ida e volta entre as telas.


    # ---------------------
    # Funções auxiliares 
    # ---------------------

    # Limpeza de campos
    def limpar_entry_cadastro(self):
        """Apaga o conteúdo de todos os campos do formulário de cadastro
        após o cadastro ser concluído."""
        self.username_cadastro_entry.delete(0, END) # apaga do caractere 0 até o final (END)
        self.email_cadastro_entry.delete(0, END) 
        self.senha_cadastro_entry.delete(0, END) 
        self.confirma_senha_entry.delete(0, END) 

    def limpar_entry_login(self):
        """Apaga o conteúdo dos campos do formulário de login após
        um login bem-sucedido."""
        self.username_login_entry.delete(0 , END)
        self.senha_login_entry.delete(0, END)


# Exibição de senha

    def mostrar_senha_login(self):
        """Alterna a visibilidade da senha no formulário de login,
        de acordo com o estado do checkbox 'ver_senha'."""
        if self.ver_senha.get(): # get() retorna 1 se marcado, 0 se desmarcado
            self.senha_login_entry.configure(show="")   # show="" exibe o texto normalmente
        else:
            self.senha_login_entry.configure(show="*")  # show="*" volta a esconder a senha


    def mostrar_senha_cadastro(self):
        """Alterna a visibilidade da senha e da confirmação de senha
        no formulário de cadastro."""
        if self.ver_senha.get():
            self.senha_cadastro_entry.configure(show="")
            self.confirma_senha_entry.configure(show="")
        else:
            self.senha_cadastro_entry.configure(show="*")
            self.confirma_senha_entry.configure(show="*")


# ============================================================
# PONTO DE ENTRADA DO PROGRAMA
# ------------------------------------------------------------
# Este bloco só é executado quando o arquivo é rodado diretamente
# (não quando é importado como módulo em outro script).
# ============================================================
if __name__ == "__main__": # se o arquivo for chamado diretamente, o código abaixo será executado
    app = App() # cria uma instância da classe App (isso já monta toda a interface, ver __init__)
    app.mainloop() # inicia o loop principal do tkinter, que "escuta" eventos (cliques, digitação, etc.) e mantém a janela aberta