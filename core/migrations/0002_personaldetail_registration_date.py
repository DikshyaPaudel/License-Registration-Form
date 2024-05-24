

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, default='2021-04-10'),
            preserve_default=False,
        ),
    ]
