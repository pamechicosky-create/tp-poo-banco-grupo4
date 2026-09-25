class CuentaBancaria:
    def __init__(self, titular, numero, saldo_inicial=0):
        self.titular = titular
        self.numero = numero
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0")
        self._saldo = self._saldo + monto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a 0")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo = self._saldo - monto

    def __str__(self):
        return f"Cuenta {self.numero} - {self.titular} - Saldo: ${self._saldo:.2f}"
