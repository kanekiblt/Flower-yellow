def validar_clave():
    clave_correcta = "1508" 
    intentos = 3  

    while intentos > 0:
        clave_ingresada = input("Ingrese la clave: ")

        if clave_ingresada == clave_correcta:
            print("Acceso permitido")
            return clave_correcta  
        else:
            intentos -= 1
            print(f"Clave incorrecta, intentos restantes: {intentos}")

            clave_correcta = generar_nueva_clave()

    print("Acceso dengado.")
    return None  

def generar_nueva_clave():
    import random
    import string

    nueva_clave = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(f"La clave nueva es: {nueva_clave}")
    return nueva_clave

if __name__ == "__main__":
    clave_final = validar_clave()
    if clave_final:
        print(f"La clave final es: {clave_final}")
    else:
        print("Clve invalida.")













