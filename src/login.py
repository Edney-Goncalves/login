import json
import os

ARQUIVO_USUARIOS = "data/usuarios.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        try:
            with open(ARQUIVO_USUARIOS, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return{}
    return{}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=4)
        

def main():
    usuarios = carregar_usuarios()
    
    print('Bem vindo à página de login')
    #opções para o usuário
    print('Login [ 1 ]')
    print('Novo usuário [ 2 ]')
    opcao = input('O que você deseja fazer? ')

    # se ele digitar '1', será remetido para a página de login
    if opcao == "1":
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        if usuarios.get(usuario) == senha:
            print(f'Bem vindo, {usuario}!')
        else:
            print(f'Usuário ou senha incorretos.')
            
    
    # caso digite a opção '2', será encaminhado para a página de criação de perfil.
    elif opcao == "2":
        novo_usuario = input('Nome do usuário: ')
        
        # caso o nome digitado em novo_usuario já estiver em usuarios:
        if novo_usuario in usuarios:
            print('Usuário já cadastrado.')
            return
        
        nova_senha = input('Crie sua senha: ')
        confirma_senha = input('Confirme sua senha: ')
        
        if nova_senha != confirma_senha:
            print('Senhas não coincidem. Digite novamente: ')
            
        usuarios[novo_usuario] = nova_senha
        salvar_usuarios(usuarios)
        print('Usuário criado com sucesso.')            

if __name__== "__main__":
    main()