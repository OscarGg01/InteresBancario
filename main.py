from InteresesBancaria import CuentaBancaria

saldo_inicial = float(input("Dame saldo actual: "))
cuenta = CuentaBancaria(saldo_inicial)
cuenta.actualizar_saldo()
cuenta.mostrar_saldo()