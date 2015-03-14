# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.CharField(max_length=50)),
                ('reg_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('qualifications', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=50)),
                ('sub_speciality', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
