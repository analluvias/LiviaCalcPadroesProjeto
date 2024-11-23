class LiviaCalc:
    def soma(self, n1, n2):
        return n1 + n2

    def subtracao(self, n1, n2):
        return n1 - n2

    def divisao(self, n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            return "Erro: Divisão por zero não é permitida."

    def multiplicacao(self, n1, n2):
        return n1 * n2
