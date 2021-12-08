# Generated by Django 3.1.13 on 2021-11-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memovocab', '0004_vocab1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocab2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocab', models.CharField(max_length=20)),
                ('meaning_vocab', models.CharField(max_length=200)),
                ('vocab_all', models.CharField(choices=[('VE', 'Verb'), ('NO', 'Noun'), ('AD', 'Adj'), ('AV', 'Adv')], default='VE', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Vocab1',
        ),
    ]
