# Generated by Django 4.0.4 on 2022-04-24 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, verbose_name='Текст:')),
                ('is_public', models.BooleanField(default=False, verbose_name='Публичная статья:')),
            ],
        ),
    ]
