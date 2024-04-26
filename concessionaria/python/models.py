from django.db import models

# Definição do modelo Carro
class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    # Método para representação textual do objeto Carro
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

# Definição do modelo Venda
class Venda(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente_nome = models.CharField(max_length=200)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)

    # Método para representação textual do objeto Venda
    def __str__(self):
        return f"Venda de {self.carro} para {self.cliente_nome}"
