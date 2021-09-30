# Esse script foi feito para realizar o desafio do módulo final do Bootcamp Programador de Software Iniciante do IGTI
# Eu utilizei o terminal pelo powershell para passar informações pelos inputs e rodar a aplicação com o commando - python folhaDePagamento.py
# ATENÇÃO: Os calculos desse script fazem referência a tabela de valores de 2020, disponibilizados pelo IGTI

def menu():
    opcao = int(input("Escolha uma das opções a seguir: \n1)Cadastrar Funcionario: \n2)Imprimir contracheque: \n3)Sair do pograma: "))
    return opcao
opcao = int(input("Escolha uma das opções a seguir: \n1)Cadastrar Funcionario: \n2)Imprimir contracheque: \n3)Sair do pograma: "))
empresa = []
while opcao != 3:
    if opcao == 1:
        funcionarios = []
        nome = str(input("Digite o nome do funcionario: "))
        salario = float(input("Digite o salario bruto: "))
        funcionarios.append(nome)
        funcionarios.append(salario)
        empresa.append(funcionarios)
        opcao = menu()
    if opcao == 2:
        indice = int(input("Digite o indice do funcionario que deseja imprimir o contracheque:"))
        salario = empresa[indice][1]
        #Calculo do salario com o desconto do INSS 
        if salario <= 1045.00:
            Inss = salario * 0.075
            salarioInss = salario - Inss
        elif salario > 1045.00 and salario <= 2089.60:
            Inss = (salario - 1045.01) * 0.09 + 94.01
            salarioInss = salario - Inss
        elif salario > 2089.60 and salario <= 3134.40:
            Inss = (salario - 2089.61) * 0.12 + 172.39
            salarioInss = salario - Inss
        elif salario > 3134.40 and salario <= 6101.06:
            Inss = (salario - 3134.41) * 0.14 + 297.77
            salarioInss = salario - Inss
        elif salario > 6101.06:
            salarioInss = salario - 713.10
        #Calculo do desconto do IRRF
        if salarioInss <= 1903.98:
            Irrf = 0
            salarioLiquido = salarioInss
        elif salarioInss >= 1903.99 and salarioInss <= 2826.65:
            Irrf = salarioInss * 0.075 - 142.80
            salarioLiquido = salarioInss - Irrf
        elif salarioInss > 2826.65 and salarioInss <= 3751.05:
            Irrf = salarioInss * 0.15 - 354.80
            salarioLiquido = salarioInss - Irrf
        elif salarioInss > 3751.05 and salarioInss <= 4664.68:
            Irrf = salarioInss * 0.225 - 636.13
            salarioLiquido = salarioInss - Irrf
        else:
            Irrf = salarioInss * 0.275 - 869.36
            salarioLiquido = salarioInss - Irrf
        print(f'O funcionário {empresa[indice][0]} de salário {salario} terá:\nDesconto INSS: {Inss:.2f}\nDesconto IRRF: {Irrf:.2f}\nSalario Liquido: {salarioLiquido:.2f}')
        opcao = menu()
print("Volte Sempre")