# Yo, Mauricio Alejandro Chávez Funes, confirmo que este trabajo fue realizado 100% por mí. 
# # No utilicé ninguna herramienta de inteligencia artificial (como ChatGPT), # ni copié código de internet o compañeros. Acepto que si se detecta plagio, 
# # mi calificación será automáticamente 0 para toda la clase.

#pseudo código:
#declarar la variable de la contraseña real
#declarar una variable que contenga el abecedario
#declarar una variable con un string vacio para guardar la contraseña adivinada
#hacer un bucle for que itere cada caracter la contraseña.
#   poner un bucle for que itere los caracteres del abecedario
#       hacer un condicional que compare la letra del abecedario con la letra de la contraseña
#           si se cumple, concatenar la letra al string donde adivinamos la contraseña
# imprimir la contraseña 

password = 'holapipipipipi'
abc = 'abcdefghijklmnñopqrstuvwxyz'
adivinada = ''
for character in password:
    for letter in abc:
        if letter == character:
            adivinada += letter
print('hola, la contrasenia es:',adivinada)