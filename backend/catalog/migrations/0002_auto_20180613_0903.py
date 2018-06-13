from django.db import migrations
from django.conf import settings

def create_data(apps, schema_editor):
    Product = apps.get_model('catalog', 'Product')
    Product(sku='sku1',name='Product 1', description='Product 1', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=100).save()
    Product(sku='sku2',name='Product 2', description='Product 2', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=200).save()
    Product(sku='sku3',name='Product 3', description='Product 3', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=300).save()

    Product(sku='sku4',name='Product 4', description='Product 1', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=100).save()
    Product(sku='sku5',name='Product 5', description='Product 2', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=200).save()
    Product(sku='sku6',name='Product 6', description='Product 3', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=300).save()
    Product(sku='sku7',name='Product 7', description='Product 4', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=400).save()

    Product(sku='sku8',name='Product 8', description='Product 1', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=100).save()
    Product(sku='sku9',name='Product 9', description='Product 2', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=200).save()
    Product(sku='sku10',name='Product 10', description='Product 3', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=300).save()
    Product(sku='sku11',name='Product 11', description='Product 4', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=400).save()

    Product(sku='sku12',name='Product 12', description='Product 1', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=100).save()
    Product(sku='sku13',name='Product 13', description='Product 2', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=200).save()
    Product(sku='sku14',name='Product 14', description='Product 3', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=300).save()
    Product(sku='sku15',name='Product 15', description='Product 4', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=400).save()

    Product(sku='sku16',name='Product 16', description='Product 1', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=100).save()
    Product(sku='sku17',name='Product 17', description='Product 2', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=200).save()
    Product(sku='sku18',name='Product 18', description='Product 3', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=300).save()
    Product(sku='sku19',name='Product 19', description='Product 4', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=400).save()

    Product(sku='sku20',name='Product 20', description='Product 1', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=100).save()
    Product(sku='sku21',name='Product 21', description='Product 2', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=200).save()
    Product(sku='sku22',name='Product 22', description='Product 3', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=300).save()
    Product(sku='sku23',name='Product 23', description='Product 4', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=400).save()

class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]