def mdc(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# Exemplo de uso
num1 = 1680
num2 = 640
resultado = mdc(num1, num2)
print("O MDC de", num1, "e", num2, "é:", resultado)
