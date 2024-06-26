

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(blank=True, max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=6, null=True)),
                ('b_group', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True)),
                ('education', models.CharField(max_length=100, null=True)),
                ('citizenship_no', models.IntegerField(null=True, unique=True)),
                ('citizenship_issue_district', models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Bhaktapur', 'Bhaktapur'), ('Lalitpur', 'Lalitpur'), ('Banepa', 'Banepa'), ('Bardia', 'Bardia')], max_length=10, null=True)),
                ('w_f_name', models.CharField(max_length=100, null=True)),
                ('w_m_name', models.CharField(blank=True, max_length=100)),
                ('w_l_name', models.CharField(max_length=100, null=True)),
                ('w_relationship', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Spouse', 'Spouse')], max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddressDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(choices=[('Bagmati', 'Bagmati'), ('Narayani', 'Narayani'), ('Lumbini', 'Lumbini'), ('Gandaki', 'Gandaki'), ('Janakpur', 'Janakpur')], max_length=10, null=True)),
                ('district', models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Bhaktapur', 'Bhaktapur'), ('Lalitpur', 'Lalitpur'), ('Banepa', 'Banepa'), ('Bardia', 'Bardia')], max_length=23, null=True)),
                ('village', models.CharField(max_length=100, null=True)),
                ('ward_no', models.IntegerField()),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('l_category', models.CharField(choices=[('A', 'A-Motercycle,Scooter,Moped'), ('C', 'C-Tempo,Autorickshaw'), ('D', 'D-Powertiler'), ('E', 'E-Tractor,Trailer'), ('K', 'K-Scooter,Moped')], max_length=26, null=True)),
                ('s_zone', models.CharField(choices=[('Bagmati', 'Bagmati')], max_length=10, null=True)),
                ('l_issue_office', models.CharField(choices=[('Bhaktapur', 'Jagati-Bhaktapur'), ('T_Kathmandu', 'Thulobharyand-Kathmandu'), ('C_Kathmandu', 'Chabahil-Kathmandu'), ('Lalitpur', 'Ekantakunna-Lalitpur')], max_length=23, null=True)),
                ('p_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.personaldetail')),
            ],
        ),
    ]
