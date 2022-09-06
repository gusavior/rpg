import dado
d = []
while True:
    print('--- Menu de dados ---')
    print('| 1. D20  (1 - 20)  |')
    print('| 2. D12  (1 - 12)  |')
    print('| 3. D10  (0 -  9)  |')
    print('| 4. D8   (1 -  8)  |')
    print('| 5. D6   (1 -  6)  |')
    print('| 6. D4   (1 -  4)  |')
    print('| 0. ---> SAIR <--- |')
    print('-' * 21)
    opc = input('Escolha uma opção: ').strip()
    if opc.isnumeric():
        opc = int(opc)
        if opc == 1:
            d = dado.d20()
        elif opc == 2:
            d = dado.d12()
        elif opc == 3:
            d = dado.d10()
        elif opc == 4:
            d = dado.d8()
        elif opc == 5:
            d = dado.d6()
        elif opc == 6:
            d = dado.d4()
        elif opc == 0:
            exit()
        else:
            print('Opção inválida, tente novamente!')
        if 0 <= opc <= 6:
            for i in range(len(d)):
                print(f'O {i + 1}º dado rolou: {d[i]}')
            s = True
            while s:
                ctn = input('Voltar ao menu de dados? \n1.Sim 2.Não: ').strip()
                if ctn.isnumeric():
                    ctn = int(ctn)
                    if ctn == 1:
                        s = False
                    elif ctn == 2:
                        exit()
                    else:
                        print('Opção inválida!')
    else:
        print('Opção inválida! \nUse apenas números para escolher a opção!')
