# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddrObj',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('aoguid', models.UUIDField(primary_key=True, serialize=False)),
                ('parentguid', models.UUIDField(db_index=True, blank=True, null=True)),
                ('aoid', models.UUIDField(unique=True, db_index=True)),
                ('previd', models.UUIDField(null=True, blank=True)),
                ('nextid', models.UUIDField(null=True, blank=True)),
                ('formalname', models.CharField(db_index=True, max_length=120)),
                ('offname', models.CharField(null=True, blank=True, max_length=120)),
                ('shortname', models.CharField(db_index=True, max_length=10)),
                ('aolevel', models.PositiveSmallIntegerField(db_index=True)),
                ('regioncode', models.CharField(max_length=2)),
                ('autocode', models.CharField(max_length=1)),
                ('areacode', models.CharField(max_length=3)),
                ('citycode', models.CharField(max_length=3)),
                ('ctarcode', models.CharField(max_length=3)),
                ('placecode', models.CharField(max_length=3)),
                ('streetcode', models.CharField(max_length=4)),
                ('extrcode', models.CharField(max_length=4)),
                ('sextcode', models.CharField(max_length=3)),
                ('code', models.CharField(null=True, blank=True, max_length=17)),
                ('plaincode', models.CharField(null=True, blank=True, max_length=15)),
                ('actstatus', models.BooleanField(default=False)),
                ('centstatus', models.PositiveSmallIntegerField()),
                ('operstatus', models.PositiveSmallIntegerField()),
                ('currstatus', models.PositiveSmallIntegerField()),
                ('livestatus', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['aolevel', 'formalname'],
            },
        ),
        migrations.CreateModel(
            name='AddrObjIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aoguid', models.UUIDField()),
                ('aolevel', models.PositiveSmallIntegerField()),
                ('scname', models.TextField()),
                ('fullname', models.TextField()),
                ('item_weight', models.PositiveSmallIntegerField(default=64)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('aoguid', models.UUIDField()),
                ('housenum', models.CharField(null=True, blank=True, max_length=20)),
                ('eststatus', models.PositiveSmallIntegerField(default=0)),
                ('buildnum', models.CharField(null=True, blank=True, max_length=10)),
                ('strucnum', models.CharField(null=True, blank=True, max_length=10)),
                ('strstatus', models.PositiveSmallIntegerField()),
                ('houseguid', models.UUIDField(primary_key=True, serialize=False)),
                ('houseid', models.UUIDField()),
                ('statstatus', models.PositiveSmallIntegerField()),
                ('counter', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseInt',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('houseintid', models.UUIDField()),
                ('intguid', models.UUIDField(primary_key=True, serialize=False)),
                ('aoguid', models.UUIDField()),
                ('intstart', models.PositiveIntegerField()),
                ('intend', models.PositiveIntegerField()),
                ('intstatus', models.PositiveIntegerField()),
                ('counter', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LandMark',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('landid', models.UUIDField()),
                ('landguid', models.UUIDField(primary_key=True, serialize=False)),
                ('aoguid', models.UUIDField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NormDoc',
            fields=[
                ('normdocid', models.UUIDField(primary_key=True, serialize=False)),
                ('docname', models.TextField(null=True, blank=True)),
                ('docdate', models.DateField(null=True, blank=True)),
                ('docnum', models.CharField(null=True, blank=True, max_length=20)),
                ('doctype', models.PositiveIntegerField()),
                ('docimgid', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocrBase',
            fields=[
                ('level', models.PositiveSmallIntegerField(verbose_name='level')),
                ('scname', models.CharField(max_length=10, default=' ')),
                ('socrname', models.CharField(max_length=50, default=' ')),
                ('kod_t_st', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('item_weight', models.PositiveSmallIntegerField(default=64)),
            ],
            options={
                'ordering': ['level', 'scname'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('table', models.CharField(primary_key=True, max_length=15, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('ver', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True, blank=True, db_index=True)),
                ('dumpdate', models.DateField(db_index=True)),
                ('complete_xml_url', models.CharField(max_length=255)),
                ('complete_dbf_url', models.CharField(max_length=255)),
                ('delta_xml_url', models.CharField(null=True, blank=True, max_length=255)),
                ('delta_dbf_url', models.CharField(null=True, blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='ver',
            field=models.ForeignKey(to='fias.Version'),
        ),
        migrations.AlterIndexTogether(
            name='socrbase',
            index_together=set([('level', 'scname')]),
        ),
        migrations.AlterIndexTogether(
            name='addrobj',
            index_together=set([('aolevel', 'shortname'), ('shortname', 'formalname')]),
        ),
    ]
