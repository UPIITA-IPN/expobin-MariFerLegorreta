#expobin

def expobin(M, e, n):

    e_bin = bin(e)[2:]
    k = len(e_bin)
    C = 1

    print("\n k | e | Ca | Cb")
    print("-------------------------")


    for i, bit in enumerate(e_bin):

        k_actual = k - i - 1

        Ca = (C * C) % n
        if bit == '1':
            C = (Ca * M) % n
            Cb = C
        else:
            C = Ca
            Cb = "-"
        print(f"{k_actual:2} | {bit} | {Ca:3} | {Cb}")

    return C

base = int(input("Ingrese la base M: "))
exponente = int(input("Ingrese el exponente e: "))
modulo = int(input("Ingrese el módulo n: "))

resultado = expobin(base, exponente, modulo)

print("\nResultado:", resultado)