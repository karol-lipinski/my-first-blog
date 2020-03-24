# Generated by Django 2.2.9 on 2020-01-09 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_dictimmovables_dictusing'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DictUsing',
            new_name='SlAkcja',
        ),
        migrations.RenameModel(
            old_name='DictImmovables',
            new_name='SlNieruchomosci',
        ),
        migrations.AlterModelOptions(
            name='slakcja',
            options={'verbose_name': 'Sposób nabycia/wykorzystania', 'verbose_name_plural': 'Sposoby nabycia/wykorzystania'},
        ),
        migrations.AlterModelOptions(
            name='slnieruchomosci',
            options={'verbose_name': 'Typ nieruchomości', 'verbose_name_plural': 'Typy nieruchomości'},
        ),
        migrations.RenameField(
            model_name='slakcja',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='slnieruchomosci',
            old_name='name',
            new_name='nazwa',
        ),
    ]
