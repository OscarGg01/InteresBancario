class CuentaBancaria:
    def __init__(self, saldo_actual):
        self.saldo = saldo_actual

    def actualizar_saldo(self):
        if self.saldo < 10000.00:
            self.saldo *= (1 + 0.03)
        else:
            self.saldo *= (1 + 0.04)

    def mostrar_saldo(self):
        print(f"Saldo final es {self.saldo:.2f}")