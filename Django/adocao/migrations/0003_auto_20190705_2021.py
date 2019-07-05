# Generated by Django 2.1.7 on 2019-07-05 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0002_auto_20190607_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Ex: vira-lata, beagle, pardal, persa', max_length=250, verbose_name='Descrição')),
                ('nome', models.CharField(blank=True, help_text='O animal tem nome?', max_length=50, null=True)),
                ('idade', models.DecimalField(decimal_places=1, help_text='Quantos anos, aproximadamente, o animal tem? Ex: 2,5', max_digits=3, null=True)),
                ('telefone', models.CharField(max_length=17)),
                ('cidade', models.ForeignKey(help_text='Onde o animal está?', on_delete=django.db.models.deletion.PROTECT, to='adocao.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Ex: vira-lata, beagle, pardal, persa', max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Raça',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Ex: gato, cachorro, pássarinho', max_length=50, verbose_name='Descrição')),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='cidade',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Raca', verbose_name='Raça'),
        ),
        migrations.AddField(
            model_name='animal',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Tipo'),
        ),
    ]
