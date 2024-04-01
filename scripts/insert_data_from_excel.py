import pandas as pd
import os
import django
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))

project_directory = os.path.abspath(os.path.join(current_directory, '..'))

sys.path.append(project_directory)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from calculator.models import Consumer, DiscountRules

excel_file = os.path.join(os.path.dirname(__file__), '..', 'consumers.xlsx')

def import_data_from_excel():
    df = pd.read_excel(excel_file)
    
    for index, row in df.iterrows():
        name = row['Nome']
        document = row['Documento']
        city = row['Cidade']
        state = row['Estado']
        consumption = row['Consumo(kWh)']
        distributor_tax = row['Tarifa da Distribuidora']

        consumer_type = row['Tipo']
        cover_value = row['Cobertura(%)']

        try:
          consumption_range = "< 10.000 kWh"
          percentage_discount = ""
          parse_consumption_to_float = float(consumption)
          parse_distributor_tax_to_float = float(distributor_tax)
          discount_value = 20000.00

          if(parse_consumption_to_float < 10000):
            if(consumer_type == 'Residencial'):
               discount_value = parse_distributor_tax_to_float * (100 - 18) / 100
               percentage_discount = "18%"
            if(consumer_type == 'Comercial'):
               discount_value = parse_distributor_tax_to_float * (100 - 22) / 100
               percentage_discount = "22%"
            if(consumer_type == 'Industrial'):
               discount_value = parse_distributor_tax_to_float * (100 - 25) / 100
               percentage_discount = "25%"
          if(parse_consumption_to_float >= 10000 and parse_consumption_to_float <= 20000):
            consumption_range = ">= 10.000 kWh e <= 20.000 kWh"

            if(consumer_type == 'Residencial'):
               discount_value = parse_distributor_tax_to_float * (100 - 16) / 100
               percentage_discount = "16%"
            if(consumer_type == 'Comercial'):
               discount_value = parse_distributor_tax_to_float * (100 - 18) / 100
               percentage_discount = "18%"
            if(consumer_type == 'Industrial'):
               discount_value = parse_distributor_tax_to_float * (100 - 22) / 100
               percentage_discount = "22%"

          if(parse_consumption_to_float > 20000):
            consumption_range = "> 20.000 kWh"

            if(consumer_type == 'Residencial'):
               discount_value = parse_distributor_tax_to_float * (100 - 12) / 100
               percentage_discount = "12%"
            if(consumer_type == 'Comercial'):
               discount_value = parse_distributor_tax_to_float * (100 - 15) / 100
               percentage_discount = "15%"
            if(consumer_type == 'Industrial'):
               discount_value = parse_distributor_tax_to_float * (100 - 28) / 100
               percentage_discount = "28%"


          discount_rules = DiscountRules(
              consumer_type=consumer_type,
              cover_value=cover_value,
              consumption_range=consumption_range,
              percentage_discount=percentage_discount,
              discount_value=discount_value
          )

          discount_rules.save()

          consumer = Consumer(
                name=name,
                document=document,
                city=city,
                state=state,
                consumption=consumption,
                distributor_tax=distributor_tax,
                discount_rule=discount_rules
            )
          
          consumer.save()

        except Exception as e:
            print(f"Erro ao salvar o Consumer {name}: {str(e)}")
        
if __name__ == "__main__":
    import_data_from_excel()
