class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def maior_numero(self):
        return max(self.num1, self.num2)

    def soma(self):
        return self.num1 + self.num2

    def diferenca(self):
        return abs(self.num1 - self.num2)

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

calc = Calculadora(num1, num2)

print(f"O maior número é: {calc.maior_numero()}")
print(f"A soma dos números é: {calc.soma()}")
print(f"A diferença entre os números é: {calc.diferenca()}")
