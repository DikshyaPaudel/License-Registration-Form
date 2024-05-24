
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_personaldetail_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='register_date',
            field=models.DateField(auto_now_add=True, default='2021-04-10'),
            preserve_default=False,
        ),
    ]
