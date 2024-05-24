

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_personaldetail_registration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetail',
            name='registration_date',
        ),
    ]
