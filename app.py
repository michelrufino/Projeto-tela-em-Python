import customtkinter as ctk

#Configuração aparencia
ctk.set_appearance_mode("dark")

#Criação das funções de funcionalidades
def validar_Login():
    usuario = campo_usuario.get()
    senha = campo_Senha.get()

    #verifica se o usuário e senha estão corretos
    if usuario =="Michel" and senha =="123456":
        resultado_login.configure(text="Login bem-sucedido!", text_color="green")
    else:
        resultado_login.configure(text="Usuário ou senha incorretos.", text_color="red")


#Criação da Janela Principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

#Label e campo de usuário
label_usuario =ctk.CTkLabel(app,text="Usuário:")
label_usuario.pack(pady=10)

#entrada de texto para o usuário
campo_usuario =ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

#Label e campo da Senha
label_Senha =ctk.CTkLabel(app,text="Senha:")
label_Senha.pack(pady=10)

#entrada de texto para o Senha
campo_Senha=ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
campo_Senha.pack(pady=10)

#button de login
botao_login =ctk.CTkButton(app,text="Login",command=validar_Login)
botao_login.pack(pady=10)


#Campo feedback de Login
resultado_login = ctk.CTkLabel(app,text="")
resultado_login.pack(pady=10)




app.mainloop()