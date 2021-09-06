from conta import Conta


def test_saca_com_sucesso():
    conta = Conta(1, 'Fulano', 1000, 500)
    resultado = conta.saca(300)
    esperado = 700
    assert resultado == esperado


def test_saca_saldo_insuficiente():
    conta = Conta(1, 'Fulano', 1000, 500)
    resultado = conta.saca(1100)
    esperado = 1000
    assert resultado == esperado


def test_depositar_valor_negativo():
    conta = Conta(1, 'Fulano', 1000, 500)
    resultado = conta.deposita(-100)
    esperado = 1000
    assert resultado == esperado 


def test_depositar_com_sucesso():
    conta = Conta(1, 'Fulano', 1000, 500)
    resultado = conta.deposita(500)
    esperado = 1500
    assert resultado == esperado


def test_trasferencia_com_sucesso():
    conta1 = Conta(1, 'Fulano', 1000, 500)
    conta2 = Conta(2, 'Ciclano', 400, 300)
    resultado1, resultado2 = conta1.transfere(400, conta2)
    esperado1 = 600
    esperado2 = 800
    assert resultado1 == esperado1 and resultado2 == esperado2

def test_transferencia_com_saldo_negativo():
    conta1 = Conta(1, 'Fulano', 0, 500)
    conta2 = Conta(2, 'Ciclano', 400, 300)
    resultado1, resultado2 = conta1.transfere(200, conta2)
    esperado1 = 0
    esperado2 = 400
    assert resultado1 == esperado1 and resultado2 == esperado2




