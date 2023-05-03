# Generated by Django 4.2 on 2023-05-03 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_ticektbooking_options_advertisment_comapnyname'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='balance',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='TicketBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatcount', models.IntegerField()),
                ('totalprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bookingDate', models.DateTimeField(auto_now_add=True)),
                ('eventName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.event')),
                ('seat', models.ManyToManyField(to='mainapp.seatcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.attendee')),
            ],
        ),
    ]