import pytest

from banco.modelos.conta import Conta


@pytest.fixture
def conta_valida():
    return Conta(333, 444)

def test_validando_atributo_numero_conta(conta_valida):
    assert conta_valida.numero_conta == 333

def test_validando_atributo_agencia(conta_valida):
    assert conta_valida.agencia == 444

def test_depositar_valor_positivo(conta_valida):
    conta_valida.depositar(100)
    assert conta_valida.saldo == 100

def test_sacar_valor_positivo_com_saldo_suficiente(conta_valida):
    conta_valida.depositar(200)  
    conta_valida.sacar(50)
    assert conta_valida.saldo == 150  


    












