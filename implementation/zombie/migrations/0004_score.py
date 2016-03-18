# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombie', '0003_auto_20160318_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('days_survived', models.IntegerField()),
                ('zombie_kills', models.IntegerField()),
                ('most_survivors', models.IntegerField()),
                ('user', models.ForeignKey(to='zombie.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
