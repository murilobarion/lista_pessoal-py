import time

lista_usuario = []

print('Bem vindo as opções da SUA LISTA!\n')
time.sleep(1)

quer = int(input('Quer entrar na sua lista? Digite 1 para entrar: '))
time.sleep(1)


if quer == 1:
    while True:
        print('\n[1] - Inserir um novo item')
        time.sleep(0.7)
        print('[2] - Listar os itens da discórdia')
        time.sleep(0.7)
        print('[3] - Apagar o item')
        time.sleep(0.7)
        print('[4] - Sair (fechar a lista)\n')
        time.sleep(0.7)
        escolha_usuario = int(input('Digite o numero desejado aqui: '))
        time.sleep(1)
        
        if escolha_usuario == 1:
            while True:
                adicionar_item = input('\nDigite o item que deseja adicionar (x para sair): ')
                time.sleep(0.6)
                
                if adicionar_item == 'x'.lower():
                    time.sleep(0.2)
                    print('\nsaiu')
                    break
                lista_usuario.append(adicionar_item)
                print(f'\nO item {adicionar_item} foi adicionado a sua lista!')
                time.sleep(0.6)
                
        elif escolha_usuario == 2:
            print("\nAqui a sua lista\n")

            for indice, item in enumerate(lista_usuario):
             print(f"Item: {indice +1} | {item}")
             time.sleep(1)
                    

        elif escolha_usuario == 3:
            if not lista_usuario:
                print("\nSua lista está vazia!")
                time.sleep(1)
                continue

            else:
                remover_item = input('\nDigite o item que deseja remover: ')
                time.sleep(0.6)
                lista_usuario.remove(remover_item)
                print(f'Item {remover_item} removido! essa é sua lista sem o item:\n')
                for indice, item in enumerate(lista_usuario):
                    print(f'  {indice + 1} - {item}')
                    time.sleep(2)
        

        elif escolha_usuario == 4:
            print('tu saiu da lista! ate mais')
            quit()
            

        else:
            print('Escolha oq foi pedido')
            continue
            

else:
  print('Ok, você não quer')
  quit()