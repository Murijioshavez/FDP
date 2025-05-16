# Yo, Mauricio Alejandro Chávez Funes, confirmo que este trabajo fue realizado 100% por mí. 
# # No utilicé ninguna herramienta de inteligencia artificial (como ChatGPT), # ni copié código de internet o compañeros. Acepto que si se detecta plagio, 
# # mi calificación será automáticamente 0 para toda la clase.

#pseudo código:
#declarar la variable de la contraseña real
#declarar una lista con las contraseñas más comunes, estas las he sacado de https://nordpass.com/es/most-common-passwords-list/ (son 200)
#hacer un bucle for que itere la lista.
#   poner un condicional que compare la contra con la contraseña comun en la iteracion
#       imprimir la contraseña y hacer break
#   si no, compararla con la contraseña comun en todo minuscula
#       imprimir la contraseña y hacer break
#   si no, compararla con la contraseña comun en todo mayuscula
#       imprimir la contraseña y hacer break
#   si no, compararla con la contraseña comun con solo la primera letra mayuscula
#       imprimir la contraseña y hacer break
#   si no, compararla con la contraseña comun pero esta vez si las mayusculas fueran minusculas y vicebersa
#       imprimir la contraseña y hacer break
#   caso contrario a todo, imprimir un mensaje que diga que no se pudo encontrar la contraseña.

contra_real = 'Contrasenia'
#las 200 contras mas comunes segun https://nordpass.com/es/most-common-passwords-list/ y otras que aniadi yo
common_passwords = ["123456", "admin", "12345678", "123456789", "1234", "12345", "password",
    "123", "Aa123456.", "1234567890", "UNKNOWN", "1234567", "qwerty", "abc123",
    "111111", "123123", "123321", "password1", "123qwe", "000000", "1q2w3e",
    "iloveyou", "7777777", "1qaz2wsx", "sunshine", "qwerty123", "qwe123",
    "654321", "superman", "asdfghjkl", "147258369", "zxcvbnm", "88888888",
    "dragon", "monkey", "nicole", "jessica", "welcome", "princess", "football",
    "michael", "batman", "pokemon", "baseball", "qwertyuiop", "charlie", "daniel",
    "shadow", "ashley", "hannah", "lovely", "maggie", "cheese", "pepper", "secret",
    "jordan", "ginger", "letmein", "tigger", "thomas", "summer", "buster", "soccer",
    "harley", "silver", "cookie", "amanda", "justin", "killer", "snoopy", "ginger1",
    "andrew", "michelle", "corona", "love", "flower", "purple", "taylor", "internet",
    "angel", "samsung", "banana", "hockey", "matrix", "naruto", "master", "pokemon1",
    "internet1", "monkey1", "cookie1", "starwars", "barbie", "michael1", "jesus",
    "bailey", "chocolate", "abc123456", "monica", "jennifer", "112233", "a123456",
    "789456123", "samantha", "qazwsx", "soccer1", "pepper1", "nathan", "123abc",
    "dragon1", "superman1", "batman1", "tiger", "joseph", "passw0rd", "jordan23",
    "killer1", "heather", "george", "chelsea", "buster1", "andrea", "michelle1",
    "princess1", "pass123", "ashley1", "qwerty1", "pass1234", "hello", "computer",
    "qweasdzxc", "asdfgh", "zxcvbn", "asdf1234", "987654321", "123456a", "7654321",
    "123456789a", "999999", "michael123", "thomas1", "charlie1", "qwerty12",
    "password123", "football1", "test123", "12344321", "hunter", "baseball1",
    "shadow1", "loveme", "trustno1", "admin123", "donald", "qazwsxedc", "123456q",
    "marina", "hello123", "julia", "liverpool", "qwe123456", "alexander", "password!",
    "london", "qweasd", "fuckyou", "daniel1", "iloveyou1", "poop", "kitty", "ginger123",
    "secret1", "merlin", "spiderman", "peanut", "internet123", "flower123", "iloveme",
    "789456", "hello1", "666666", "letmein1", "cookie123", "samsung123", "fuckoff",
    "biteme", "america", "yankees", "tinkerbell", "qazxsw", "12345678910", "welcome1",
    "asdf123", "computer1", "test1", "batman123", "football123", "hello1234", 'contrasenia',
    "soccer123", "summer1", "taylor1", "jesus1", "starwars1", "princess123", "hunter1",
    "dragon123", "iloveyou2", "flower1", "chocolate1", "trustno1!", "lucky", "kitty1",
    "shadow123", "donald1", "qwerty1234", "zxcvbn123", "cheese1", "hannah1", "contraseña", "a", "b"
    "c", 'd','e','f','g', 'h', 'i', 'j', 'k', 'l','m','n',"ñ",'o','p','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9']

for intento in common_passwords:
    if contra_real == intento:
        print('La contra es:', intento)
        break
    elif contra_real == intento.lower():
        print('La contra es:', intento.lower())
        break
    elif contra_real == intento.upper():
        print('La contra es', intento.upper())
        break
    elif contra_real == intento.capitalize():
        print('La contra es:', intento.capitalize())
        break
    elif contra_real == intento.swapcase():
        print('La contra es:', intento.swapcase())
        break
    else:
        #funcion index sacada de: https://www.geeksforgeeks.org/python-list-index/
        print(f'La contrasenia {intento}, en el indice "{common_passwords.index(intento)}" no funciono, tal vez la siguiente funciona.', contra_real)
        
        
        
#Como extra dejo las cosas que se me ocurrieron el dia que hicimos el pseudo codigo en la pizarra en grupos:
# FORMA 1
# 1. Definir la variable contraseña y su valor será la contraseña
# 2. Definir una variable (con el nombre adivinada por ejemplo) con un string vacío
# 3. Con un bucle for recorremos la variable contraseña.
# 4. En el bucle for concatenamos la letra de la variable del bucle a la variable del string vacío

# FORMA 2
# 1. Definir la variable contraseña y su valor será la contraseña
# 2. Definir una variable cuya valor es una lista vacía
# 3. Con un bucle for recorremos la variable contraseña.
# 4. En el bucle for, añadiremos cada letra de la contraseña a la lista
# 5. Unimos los elementos de la lista en un solo string ya que la contraseña es un string. Esto puede ser con otro bucle for o usando una función para ellos si el lenguaje ya trae para hacerlo (.join() en python por ejemplo)
# FORMA 3 (bien fumada y mal optimizada como hicmod en clase
# 1. Definir la variable contraseña y su valor será la contraseña.
# 2. Definir una variable abecedario. Su valor será todo el abecedario en español en lowercase.
# 3. Declarar una variable que sea una lista vacía, en mi caso la llamaré adivinada.
# 4. Hacer un bucle for que recorra cada letra de la contraseña.
# 5.    En el bucle for, encontraremos el índice correspondiente a la letra en la iteración, luego, vamos a validar si es mayúscula o minúscula
# 6. Vamos a añadir una lista de dos elementos a la lista antes definida, el primero será el índice de la letra en la iteración y el segundo un indicativo para saber si es mayúscula o minúscula ("U" o "L" por ejemplo) de tal manera que quedará de esta forma: [índice, "mayus/mimus"].
# 7. Declarar un string vacío
# 8. Hacer un bucle for el cual va a recorrer nuestra lista llamada adivinada
# 9. En el bucle for vamos a declarar una variable y su valor será el de el primer elemento de la lista pequeña que estamos recorriendo
# 10. Vamos a usar un condicional y compararemos si la letra es mayúscula, de ser así, transformaremos la letra en mayúscula, caso contrario la dejaremos tal cual (recordemos que el abecedaro por default está en lowercase)
# 11. Al final del bucle añadiremos la letra al string vacío