from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._estado = False
    
    def __str__(self):
        return f"Marca: {self._marca} | Modelo: {self._modelo} | Estado: {self.estado}"

    @property
    def estado(self):
        return 'Ligado' if self._estado else "Desligado"
    
    @abstractmethod
    def ligar(self):
        pass
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas, cor):
        super().__init__(marca, modelo)
        self._qtd_portas = qtd_portas
        self._cor = cor
        self._estado = False

    def __str__(self):
        return f"Marca: {self._marca} | Modelo: {self._modelo} | Estado: {self.estado} | Quantidade de portas: {self._qtd_portas} | Cor: {self._cor}"

    @property
    def estado(self):
        return 'Ligado' if self._estado else "Desligado"
    
    def ligar(self):
        pass
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
        self._estado = False

    def __str__(self):
        return f"Marca: {self._marca} | Modelo: {self._modelo} | Estado: {self.estado} | Quantidade de portas: {self._tipo}"

    @property
    def estado(self):
        return 'Ligado' if self._estado else "Desligado"
    
    def ligar(self):
        pass

# carro_1 = Veiculo('Chevrolet', 'Onix')
# print(carro_1)