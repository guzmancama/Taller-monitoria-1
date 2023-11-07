#2 Taller Sierra ej 2
# Elaborado por:Ivan david galeano, nicole camila hoyos, juan jose guzman camacho, Jerson stiven gonzalez.
def buscar_tarjeta(numero_tarjeta, tarjetas):
    for tarjeta in tarjetas:
        if tarjeta[0] == numero_tarjeta:
            return tarjeta
    return None

def verificar_clave(tarjeta, clave):
    return tarjeta[1] == clave

def retirar_dinero(tarjeta, monto):
    if monto <= tarjeta[2]:
        tarjeta[2] -= monto
        return True
    return False

def main():
    tarjetas = [
        ["1234567890", "1234", 10000],
        ["0987654321", "4321", 5000],
        ["5678901234", "5678", 20000]
    ]

    numero_tarjeta = input("Ingrese el numero de tarjeta: ")
    tarjeta_valida = buscar_tarjeta(numero_tarjeta, tarjetas)

    if tarjeta_valida is not None:
        clave = input("Ingrese la clave: ")

        if verificar_clave(tarjeta_valida, clave):
            if tarjeta_valida[2] >= 10000:
                monto_a_retirar = int(input("Ingrese el monto a retirar: "))

                if retirar_dinero(tarjeta_valida, monto_a_retirar):
                    print(f"Retire su dinero: ${monto_a_retirar}")
                    print(f"Saldo restante en la tarjeta: ${tarjeta_valida[2]}")
                else:
                    print("El monto a retirar es mayor que el saldo disponible.")
            else:
                print("El saldo en la tarjeta es insuficiente para realizar un retiro de $10,000.")
        else:
            print("La clave ingresada no es válida.")
    else:
        print("El número de tarjeta no es válido")

if __name__ == "__main__":
    main()


