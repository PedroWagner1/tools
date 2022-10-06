# Início do código

print('\nOlá, seja bem vindo a calculadora, para continuar, pressione qualquer tecla ')
input('')

print('Certo, agora, informe o tipo de operação que deseja realizar:\n\n+ -> Adição\n- -> Subtração\n* -> Multiplicação\n/ -> Divisão\n** -> Potenciação\n\n> ', end='')
tipo = input('')
if tipo != '+' and tipo != '-' and tipo != '/' and tipo != '*' and tipo != '**':
    print('\nVocê não digitou uma opção válida, saindo do programa.')
    exit()

print('\n\nCerto, agora, informe o primeiro número no qual deseja realizar a operação\n\n> ', end='')
num1 = input('')

print('\n\nAgora, informe o segundo número no qual deseja realizar a operação\n\n> ', end='')
num2 = input('')

try:
    num1 = float(num1)
    num2 = float(num2)
except:
    print('\n+ Houve um problema ao tentar validar os valores, verifique se indicou valores válidos\n')
    exit()

if tipo == '+':
    print(f'\n\nOperação: {num1} + {num2}\nResultado: {num1 + num2}\n')
elif tipo == '-':
    print(f'\n\nOperação: {num1} - {num2}\nResultado: {num1 - num2}\n')
elif tipo == '*':
    print(f'\n\nOperação: {num1} * {num2}\nResultado: {num1 * num2}\n')
elif tipo == '/':
    print(f'\n\nOperação: {num1} / {num2}\nResultado: {num1 / num2}\n')
elif tipo == '**':
    print(f'\n\nOperação: {num1} ** {num2}\nResultado: {num1 ** num2}\n')