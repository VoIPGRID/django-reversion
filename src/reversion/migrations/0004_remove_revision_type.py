# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0003_cleanup_versions_revisions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='type',
        ),
    ]
