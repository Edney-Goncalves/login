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
    
    os.makedirs(os.path.dirname(ARQUIVO_USUARIOS), exist_ok=True)
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=4)
        

def main():
    usuarios = carregar_usuarios()
    
    while True:
        print('Login [ 1 ]')
        print('Cadastre-se [ 2 ]')
        opcao = input(' ')

        # se ele digitar '1', será remetido para a página de login;
        # Enquanto Usuário/Senha não estiver no banco de dados ou for digitado 
        # incorretamente, ficará nesse laço
        if opcao == "1":
            usuario = input('Usuário: ')
            senha = input('Senha: ')
            if usuarios.get(usuario) == senha:
                print(f'Bem vindo, {usuario}!')
                print("FIM DE PROGRAMA")
                break
            else:
                print(f'Usuário ou senha incorretos.')
                
        
        # caso digite a opção '2', será encaminhado para a página de criação de perfil.
        elif opcao == "2":
            novo_usuario = input('Nome do usuário: ').strip
            
            if not novo_usuario:
                print("Nome de usuário está vazio.")
                continue
            # caso o nome digitado em novo_usuario já estiver em usuarios:
            elif novo_usuario in usuarios:
                print('Usuário já cadastrado.')
                continue
            
            nova_senha = input('Crie sua senha: ')
            confirma_senha = input('Confirme sua senha: ')
            
            if nova_senha != confirma_senha:
                print('Senhas não coincidem. Digite novamente: ')
                nova_senha = input('Crie sua senha: ')
                confirma_senha = input('Confirme sua senha: ')
                continue
        
            
            usuarios[novo_usuario] = nova_senha
            salvar_usuarios(usuarios)
            print('Usuário criado com sucesso.')            

if __name__== "__main__":
    main()