# Generated by Django 2.1 on 2018-09-14 13:21

from django.db import migrations
from base.models import Language


def create_basic_languages(apps, schema_editor):
    Language.objects.bulk_create([
        Language(title='Java'),
        Language(title='Python'),
        Language(title='Ruby'),
        Language(title='JavaScript'),
        Language(title='PHP'),
        Language(title='Perl'),
        Language(title='Go'),
        Language(title='Rust'),
        Language(title='C'),
        Language(title='C#'),
        Language(title='C++'),
        Language(title='R'),
        Language(title='Objective-C'),
        Language(title='Swift'),
        Language(title='Clojure'),
        Language(title='Haskell'),
        Language(title='Erlang'),
        Language(title='Bash'),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20180914_1321'),
    ]

    operations = [
        migrations.RunPython(create_basic_languages),
    ]
