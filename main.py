from cuenta_bancaria import CuentaBancaria
from caja_de_ahorro import CajaDeAhorro
from cuenta_corriente import CuentaCorriente
from banco import Banco

# 1) Demostración del programa
banco = Banco("Banco POO")
banco.agregar_cuenta(CajaDeAhorro("Ana", "001", 1000))
banco.agregar_cuenta(CuentaCorriente("Luis", "002", 200, 1000))
banco.transferir("002", "001", 700)   # Luis queda en negativo (permitido)
banco.listar_cuentas()
print("Total en el banco:", banco.total_depositado())
print()

# 2) Pruebas automáticas
def probar(condicion, mensaje):
    assert condicion, mensaje

# --- CuentaBancaria ---
c = CuentaBancaria("Test", "T1", 100)
probar(c.saldo == 100, "El saldo inicial no es correcto")
c.depositar(50)
probar(c.saldo == 150, "depositar no suma bien")
c.extraer(30)
probar(c.saldo == 120, "extraer no resta bien")
for malo in (lambda: c.depositar(-10), lambda: c.extraer(0), lambda: c.extraer(10_000)):
    try:
        malo()
        probar(False, "Falta validar montos inválidos o saldo insuficiente")
    except ValueError:
        pass
probar("T1" in str(c) and "Test" in str(c), "__str__ debe mostrar número y titular")

# --- CajaDeAhorro ---
a = CajaDeAhorro("Test", "T2", 1000, 0.10)
probar(isinstance(a, CuentaBancaria), "CajaDeAhorro debe heredar de CuentaBancaria")
a.aplicar_interes()
probar(abs(a.saldo - 1100) < 0.01, "aplicar_interes no calcula bien")

# --- CuentaCorriente ---
cc = CuentaCorriente("Test", "T3", 500, 2000)
cc.extraer(2500)
probar(cc.saldo == -2000, "CuentaCorriente debe permitir descubierto hasta el límite")
try:
    cc.extraer(1)
    probar(False, "CuentaCorriente no debe superar el límite de descubierto")
except ValueError:
    pass

# --- Banco ---
b = Banco("Test")
b.agregar_cuenta(CajaDeAhorro("A", "X1", 1000))
b.agregar_cuenta(CuentaCorriente("B", "X2", 0, 500))
try:
    b.agregar_cuenta(CuentaBancaria("C", "X1"))
    probar(False, "No se deben permitir números de cuenta repetidos")
except ValueError:
    pass
probar(b.buscar_cuenta("NOEXISTE") is None, "buscar_cuenta debe devolver None si no existe")
b.transferir("X2", "X1", 300)
probar(b.buscar_cuenta("X1").saldo == 1300, "transferir no deposita bien en el destino")
probar(b.buscar_cuenta("X2").saldo == -300, "transferir no extrae bien del origen")
probar(b.total_depositado() == 1000, "total_depositado no suma bien")

print("¡Todas las pruebas pasaron!")
