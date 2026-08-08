# importar biblioteca tkinter

import customtkinter as ctk
from tkinter import PhotoImage

# Chamar a classe ctk.CTk para criar a janela principal

class App (ctk.CTk): # chama a tela do tkinter dentro da classe App
    def __init__(self): # a função init (função inicial) determina o que vai acontecer quando a classe for chamada
        super().__init__() # super define que a função init vai ser chamada da classe pai (ctk.CTk)
        self.configuracoes_da_janela_inicial() # chama a função configuracoes_da_janela_inicial
        self.tela_de_login() # chama a função tela_de_login

    #Configurações da janela principal
    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400") # define o tamanho da janela
        self.title("Sistema de Login") # define o título da janela
        self.resizable(False, False) # define que a janela não pode ser redimensionada


    # Tela de Login
    def tela_de_login(self):
        # Trabalhando com as imagens
        self.img = PhotoImage(file="logi-img.png") # chama a imagem do arquivo logi-img.png
        self.img = self.img.subsample(6,6) # reduz o tamanho da imagem para 1/6 do tamanho original
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img) # cria um label para a imagem
        self.lb_img.grid(row=1, column = 0, padx = 10) # define a posição da imagem na tela


        # Trabalhando com o título
        self.title = ctk.CTkLabel(self, text="Faça o seu login ou Cadastre-se\nem nossa plataforma para acessar\nos nossos serviços!", font=("Century Gothic bold", 14)) # cria um label para o título
        self.title.grid (row=0, column=0, pady=10, padx=10) # define a posição do título na tela

    
        # Criar a Frame do formulário de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380) # cria um frame para o formulário de login
        self.frame_login.place(x= 350, y=10) # define a posição do frame na tela


        # Colocando Widgets dentro do frame - formulário de login
        self.lb_title = ctk.CTkLabel (self.frame_login, text="Faça o seu Login", font=("Century Gothic bold", 22)) # cria um label para o título do formulário de login
        self.lb_title.grid(row=0, column= 0,padx= 10, pady=10) # define a posição do título do formulário de login na tela

        # Criando os Entry para o formulário de login
        self.username_login_entry = ctk.CTkEntry (self.frame_login, width=300, placeholder_text=
        "Digite o seu nome de usuário:", font =("Century Gothic bold", 16), corner_radius=15) # cria um entry para o usuário
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10) # define a posição do entry do usuário na tela

        # Criando o Entry para a senha
        self.senha_login_entry = ctk.CTkEntry (self.frame_login, width=300, placeholder_text=
        "Digite o sua senha:", font =("Century Gothic bold", 16), corner_radius =15, show="*") # cria um entry para a senha
        self.senha_login_entry.grid(row=2, column=0, padx=10, pady=10) # define a posição do entry da senha na tela

        # Criando o checkbox para ver a senha   
        self.ver_senha = ctk.CTkCheckBox (self.frame_login, text="Clique para ver a senha", font =("Century Gothic bold", 12), corner_radius =20) # cria um checkbox para ver a senha
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10) # define a posição do checkbox na tela

        # Criando o botão de login
        self.btn_login_entry = ctk.CTkButton (self.frame_login, text="Fazer Login".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15) # cria um botão para o login
        self.btn_login_entry.grid(row=4, column=0, padx=10, pady=10) # define a posição do botão na tela

        # Criando o label para o texto de cadastro
        self.span = ctk.CTkLabel(self.frame_login, text="Se não possui uma conta, clique no\nbotão abaixo para se cadastrar!", font=("Century Gothic", 10)) # cria um label para o texto de cadastro
        self.span.grid(row=5, column=0, padx=10, pady=10) # define a posição do label na tela

        # Criando o botão de cadastro
        self.btn_cadastro = ctk.CTkButton (self.frame_login, text="Cadastrar".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15, command=self.tela_de_cadastro) # cria um botão para o cadastro
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=10) # define a posição do botão na tela




    # Tela de cadastro
    def tela_de_cadastro(self):
        # Remover a tela de login para abrir a tela de cadastro 
        self.frame_login.place_forget()


        # Criar a Frame do formulário de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380) 
        self.frame_cadastro.place(x= 350, y=10) 


         # Titulo 
        self.title = ctk.CTkLabel(self.frame_cadastro, text="Faça o seu Cadastro", font=("Century Gothic bold", 20)) # cria um label para o título
        self.title.grid (row=0, column=0, pady=10, padx=10)

        
        # Criando os Entry para o formulário de cadastro
        self.username_cadastro_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Digite o seu nome de usuário:", font =("Century Gothic bold", 16), corner_radius=15) 
        self.username_cadastro_entry.grid(row=1, column=0, padx=10, pady=5) 

        self.username_cadastro_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Digite o seu e-mail:", font =("Century Gothic bold", 16), corner_radius=15) 
        self.username_cadastro_entry.grid(row=2, column=0, padx=10, pady=5) 


        # Criando o Entry para a senha
        self.senha_cadastro_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Digite a sua senha:", font =("Century Gothic bold", 16), corner_radius =15, show="*") 
        self.senha_cadastro_entry.grid(row=3, column=0, padx=10, pady=5)

        self.confirma_senha_entry = ctk.CTkEntry (self.frame_cadastro, width=300, placeholder_text=
        "Confirme sua senha:", font =("Century Gothic bold", 16), corner_radius =15, show="*") 
        self.confirma_senha_entry.grid(row=4, column=0, padx=10, pady=5)



        # Criando o checkbox para ver a senha   
        self.ver_senha = ctk.CTkCheckBox (self.frame_cadastro, text="Clique para ver a senha", font =
        ("Century Gothic bold", 12), corner_radius =20) # cria um checkbox para ver a senha
        self.ver_senha.grid(row=5, column=0, pady=10) # define a posição do checkbox na tela


        # Criando o botão de cadastro
        self.btn_cadastrar_user = ctk.CTkButton (self.frame_cadastro, text="Fazer Cadastro".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15, command=self.tela_de_cadastro) # cria um botão para o cadastro
        self.btn_cadastrar_user.grid(row=6, column=0, padx=10, pady=10)


        # Criando o botão de Cadastro
        self.btn_login_back = ctk.CTkButton (self.frame_cadastro, text="Voltar ao login".upper(), font =
        ("Century Gothic bold", 14), corner_radius =15, fg_color="#444", hover_color="#333", command= self.tela_de_login) # cria um botão para o login
        self.btn_login_back.grid(row=7, column=0, padx=10, pady=10) # define a posição do botão na tela


    



if __name__ == "__main__": # se o arquivo for chamado diretamente, a função main será executada
    app = App() # cria uma instância da classe App
    app.mainloop() # chama o método mainloop da classe App para iniciar a aplicação     