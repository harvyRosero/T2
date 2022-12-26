# Generated by Django 3.0.8 on 2022-12-25 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20221225_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='images_adicionales')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Product')),
            ],
        ),
    ]