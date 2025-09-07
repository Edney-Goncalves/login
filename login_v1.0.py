#Essa é a primeira versão do meu cógigo de login. A ideia é simular a lógica de uma página de login,
#com um pequeno tratamento de erros.

#usuário deve entrar com nome e senha.
usuario = input('Usuário: ')
senha = input('Senha: ')

#nesse laço de repetição, enquanto o usuário digitar o nome que foi previamente definido,
#será barrado pelo algoritmo. O mesmo acontece caso a senha esteja incorreta.
while True:
    if usuario != 'Edney' or senha != '123456':
        print('Usuário ou senha estão incorretos. Tente novamente.')
        usuario = input('Usuário: ')
        senha = input('Senha: ')
    else:
        break
print('Bem vindo')