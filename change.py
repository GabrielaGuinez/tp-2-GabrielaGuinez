def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido:")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    pesos = money-expense
    print(int(pesos))
    print("Centavos:")
    centavos= (money-expense-int(pesos))*100
    print(int(centavos))

change()
