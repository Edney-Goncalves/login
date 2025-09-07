#vvv

print('Bem vindo à página de login')

#opções para o usuário
print('Login [ 1 ]')
print('Novo usuário [ 2 ]')
opcao = int(input('O que você deseja fazer? '))

# se ele digitar '1', será remetido para a página de login
if opcao == 1:
    print('Faça seu login')
    usuario = input('Usuário: ')
    senha = input('Senha: ')

#nesse laço de repetição, enquanto o usuário digitar um nome que não esteja no banco de dados,
#será barrado pelo algoritmo. O mesmo acontece caso a senha esteja incorreta.
    while True:
        if usuario != 'Edney' or senha != '123456':
            print('Usuário ou senha estão incorretos. Tente novamente.')
            usuario = input('Usuário: ')
            senha = input('Senha: ')
        else:
            break
    print('Bem vindo')
    
# caso digite a opção '2', será encaminhado para a página de criação de perfil.
elif opcao == 2:
    print('Crie seu usuário')
    novo_usuario = input('Nome do usuário: ')
    nova_senha = input('Crie sua senha: ')
    confirma_senha = input('Confirme sua senha: ')
    
#Enquanto for verdade que as senhas são diferentes uma da outra, o usuário continuará nesse laço.    
    while True:
        if confirma_senha != nova_senha:
            print('Senhas não coincidem. Digite novamente:')
            nova_senha = input('Crie sua senha: ')
            confirma_senha = input('Confirme sua senha: ')
        else:
            break