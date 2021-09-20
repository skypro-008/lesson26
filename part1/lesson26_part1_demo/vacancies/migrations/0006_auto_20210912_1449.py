# Generated by Django 3.2.7 on 2021-09-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Навык', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.RemoveField(
            model_name='skill',
            name='vacancies',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ManyToManyField(to='vacancies.Skill'),
        ),
    ]
