# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date and time this revision was created.', verbose_name='date created', db_index=True),
        ),
        migrations.AlterField(
            model_name='revision',
            name='manager_slug',
            field=models.CharField(default='default', max_length=191, db_index=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='type',
            field=models.PositiveSmallIntegerField(default=1, null=True, db_index=True, choices=[(0, 'Addition'), (1, 'Change'), (2, 'Deletion')]),
        ),
    ]
