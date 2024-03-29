# Generated by Django 4.2.2 on 2023-06-08 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0006_alter_libro_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('resume', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('copies', models.IntegerField()),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=250)),
                ('active', models.CharField(max_length=250)),
                ('books', models.ManyToManyField(to='proyecto_app.book')),
            ],
        ),
        migrations.CreateModel(
            name='Printing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('has_book', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto_app.book')),
            ],
        ),
        migrations.RemoveField(
            model_name='lector',
            name='libro_ocupado',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='id_imprenta',
        ),
        migrations.DeleteModel(
            name='Biblioteca',
        ),
        migrations.DeleteModel(
            name='Imprenta',
        ),
        migrations.DeleteModel(
            name='Lector',
        ),
        migrations.DeleteModel(
            name='libro',
        ),
        migrations.AddField(
            model_name='book',
            name='name_imprenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='proyecto_app.printing'),
        ),
    ]
