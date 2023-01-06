# Generated by Django 4.1.4 on 2023-01-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='productapp/images')),
                ('productName', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('unit', models.CharField(choices=[('kg', 'KG'), ('mtr', 'Mtr'), ('ltr', 'Ltr')], max_length=200)),
            ],
        ),
    ]