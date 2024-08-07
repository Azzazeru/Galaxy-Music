# Generated by Django 5.0.6 on 2024-07-06 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id_artista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('total', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id_disco', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('fecha_lanzamiento', models.DateField(null=True)),
                ('tipo_disco', models.CharField(default='', max_length=100)),
                ('sello_discografico', models.CharField(default='', max_length=100)),
                ('genero_musical', models.CharField(default='', max_length=100)),
                ('artista', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EspecieInstrumento',
            fields=[
                ('id_especie_instrumento', models.AutoField(primary_key=True, serialize=False)),
                ('especie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GeneroMusical',
            fields=[
                ('id_genero_musical', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id_instrumento', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(default='', max_length=100)),
                ('tipo_instrumento', models.CharField(default='', max_length=100)),
                ('marca', models.CharField(default='', max_length=100)),
                ('especie', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MarcaInstrumento',
            fields=[
                ('id_marca_instrumento', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id_presupuesto', models.AutoField(primary_key=True, serialize=False)),
                ('presupuesto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SelloDiscografico',
            fields=[
                ('id_sello_discografico', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDisco',
            fields=[
                ('id_tipo_disco', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInstrumento',
            fields=[
                ('id_tipo_instrumento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField(default=0)),
                ('estado', models.BooleanField(default=False)),
                ('disco', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.disco')),
                ('instrumento', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.instrumento')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.boleta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producto')),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='productos',
            field=models.ManyToManyField(through='api.DetalleBoleta', to='api.producto'),
        ),
    ]
