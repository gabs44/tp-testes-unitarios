class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo
    
    def deposita(self, valor):
        self.__saldo += valor
        return self.__saldo

    def saca(self, valor):
        self.__saldo -= valor
        return self.__saldo
    
    def transfere(self, valor, contaDestino):
        self.saca(valor)
        contaDestino.deposita(valor)
        return self.__saldo, contaDestino.get_saldo()

    def extrato(self):
        print(self.__saldo)

