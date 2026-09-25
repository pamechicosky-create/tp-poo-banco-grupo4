from cuenta_bancaria import CuentaBancaria


class CajaDeAhorro(CuentaBancaria):
    def __init__(self, titular, numero, saldo_inicial=0, tasa_interes=0.05):
        super().__init__(titular, numero, saldo_inicial)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self._saldo * self.tasa_interes
        self._saldo = self._saldo + interes
