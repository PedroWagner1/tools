print('Bem vindo ao validador de cpf, pressione qualquer tecla para continuar\n', end='')
input('')

cpf_insert = input('Digite um CPF (no formato: xxx.xxx.xxx-xx).\n\n> ')

# Checa se o CPF foi escrito no formato correto: 

tam_cpf_insert = len(cpf_insert)

for i, event in enumerate(cpf_insert):

    if tam_cpf_insert != 14:
        print('\nVocê não digitou o CPF em um formato válido. Saindo do programa.\n')
        exit()
    if i == 0 or i == 1 or i == 2 or i == 4 or i == 5 or i == 6 or i == 8 or i == 9 or i == 10:
        if event != '0' and event != '1' and event != '2' and event != '3' and event != '4' and event != '5' and event != '6' and event != '7' and event != '8' and event != '9':
            print('\nVocê não digitou números em seus respectivos lugares, saindo do programa.')
            exit()
    if i == 3 or i == 7:
        if event != '.':
            print('\nVocê não digitou o CPF no formato correspondente, saindo do programa.\n')
            exit()
    if i == 11:
        if event != '-':
            print('\nVocê não digitou o CPF no formato correspondente, saindo do programa.\n')
            exit()
    if i == 12 or i == 13:
        if event != '0' and event != '1' and event != '2' and event != '3' and event != '4' and event != '5' and event != '6' and event != '7' and event != '8' and event != '9':
            print('\nVocê não digitou números em seus respectivos lugares, saindo do programa.')
            exit()

# -------------------------------------------

number_1 = int(cpf_insert[0])
number_2 = int(cpf_insert[1])
number_3 = int(cpf_insert[2])
number_4 = int(cpf_insert[4])
number_5 = int(cpf_insert[5])
number_6 = int(cpf_insert[6])
number_7 = int(cpf_insert[8])
number_8 = int(cpf_insert[9])
number_9 = int(cpf_insert[10])

digit_1_calc1 = (number_1 * 10) + (number_2 * 9) + (number_3 * 8) + (number_4 * 7) + (number_5 * 6) + (number_6 * 5) + (number_7 * 4) + (number_8 * 3) + (number_9 * 2)
digit_1_calc2 = 11 - (digit_1_calc1 % 11)

if digit_1_calc2 > 9:
    digit_1 = 0
    if cpf_insert[12] != '0':
        print('\n-----CPF inválido!-----\n')
        exit()
else:
    digit_1 = digit_1_calc2


digit_2_calc1 = (number_1 * 11) + (number_2 * 10) + (number_3 * 9) + (number_4 * 8) + (number_5 * 7) + (number_6 * 6) + (number_7 * 5) + (number_8 * 4) + (number_9 * 3) + (digit_1 * 2)
digit_2_calc2 = 11 - (digit_2_calc1 % 11)
digit_2 = digit_2_calc2

if cpf_insert[13] != str(digit_2):
    print('-----CPF inválido!-----')
    exit()

print('\n\n-----Parabéns, seu CPF é válido!-----\n')