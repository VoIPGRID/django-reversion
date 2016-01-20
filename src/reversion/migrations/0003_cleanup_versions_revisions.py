# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models  # noqa
from reversion.models import VERSION_DELETE


def remove_delete_revisions(apps, schema_editor):
    """
    Replaces south migration 0006, which removes delete revisions. See:
    https://github.com/etianen/django-reversion/blob/master/src/reversion/south_migrations/0006_remove_delete_revisions.py
    """
    Version = apps.get_model('reversion', 'Version')
    Revision = apps.get_model('reversion', 'Revision')

    print '\n\n  Removing %s obsolete Version objects with type VERSION_DELETE(%s)' % (
        Version.objects.filter(type=VERSION_DELETE).count(), VERSION_DELETE)
    Version.objects.filter(type=VERSION_DELETE).delete()

    print '  Removing %s obsolete Revision objects with version null\n' % (
        Revision.objects.filter(version__isnull=True).count())
    Revision.objects.filter(version__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0002_auto_20160120_1446'),
    ]

    operations = [
        migrations.RunPython(remove_delete_revisions, migrations.RunPython.noop)
    ]
