from django.db import models

class DiscountRules(models.Model):
    CHOICES_CONSUMER = (
        ('COMERCIAL', 'Comercial'),
        ('RESIDENCIAL', 'Residencial'),
        ('INDUSTRIAL', 'Industrial'),
    )

    CHOICES_COVER = (
        ('90%', '90%'),
        ('95%', '95%'),
        ('99%', '99%'),
    )

    CHOICES_CONSUMPTION_RANGE = (
        ('< 10.000 kWh', '< 10.000 kWh'),
        ('>= 10.000 kWh e <= 20.000 kWh', '>= 10.000 kWh e <= 20.000 kWh'),
        ('> 20.000 kWh', '> 20.000 kWh'),
    )

    consumer_type = models.CharField("Tipo de Consumidor", choices=CHOICES_CONSUMER, max_length=128)
    consumption_range = models.CharField("Faixa de Consumo", choices=CHOICES_CONSUMPTION_RANGE, max_length=128)
    cover_value = models.CharField("Cobertura", choices=CHOICES_COVER, max_length=128)
    discount_value = models.FloatField("Desconto")

class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
    discount_rule = models.OneToOneField(DiscountRules, on_delete=models.CASCADE, related_name="discount_rule")
    #  create the foreign key for discount rule model here

# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
