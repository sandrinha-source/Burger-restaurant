print("1 - Hambúrguer Simples - R$12.00")
print("2 - X-Salada - R$15.50")
print("3 - Batata-frita - R$9.00")
print("4 - Refrigerante - R$6.50")

item = int(input("Digite qual item você deseja: "))
quantidade=int(input("Digite a quantidade: "))

if item == 1:
    cobrar = quantidade*12.00
elif item == 2:
    cobrar = quantidade*15.50
elif item == 3:
    cobrar = quantidade*9.00
else:
    cobrar = quantidade*6.50
print("Olá," "você deverá pagar R$: ", cobrar)
