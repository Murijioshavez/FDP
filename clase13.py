subtotal = float(input('Ingrese el subtotal de la cuenta'))
propina = subtotal *0.1
total = subtotal + propina
print(f'Subtotal: ${subtotal:.2f}\nPropina: ${propina:.2f}\nTotal de la cuenta: ${total:.2f}')