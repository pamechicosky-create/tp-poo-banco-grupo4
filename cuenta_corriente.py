from cuenta_bancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, numero, saldo_inicial=0, limite_descubierto=2000):
        super().__init__(titular, numero, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a 0")
        if self._saldo - monto < -self.limite_descubierto:
            raise ValueError("Se supera el límite de descubierto")
        self._saldo = self._saldo - monto
