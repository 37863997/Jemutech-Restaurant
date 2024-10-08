# Generated by Django 5.1 on 2024-08-08 21:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sales', models.IntegerField()),
                ('expenses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('course', models.CharField(choices=[('Negros Best Food', 'Negros Best Food'), ('Manila Best Food', 'Manila Best Food'), ('Cebu Best Food', 'Cebu Best Food'), ('Iloilo Best Food', 'Iloilo Best Food'), ('Aklan Food', 'Aklan Food')], max_length=50)),
                ('status', models.CharField(choices=[('Disabled', 'Disabled'), ('Enabled', 'Enabled')], max_length=50)),
                ('content_description', models.TextField()),
                ('base_price', models.FloatField()),
                ('sale_price', models.FloatField(default=models.FloatField())),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('num_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=10)),
                ('orders', models.IntegerField(default=0)),
                ('total_sale', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.food')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_timestamp', models.CharField(blank=True, max_length=100)),
                ('delivery_timestamp', models.CharField(blank=True, max_length=100)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100)),
                ('delivery_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100)),
                ('if_cancelled', models.BooleanField(default=False)),
                ('total_amount', models.IntegerField()),
                ('payment_method', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Card Payment', 'Card Payment'), ('UPI Payment', 'UPI Payment')], max_length=100)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.order')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=10)),
                ('salary', models.IntegerField()),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Chef', 'Chef'), ('Delivery Boy', 'Delivery Boy')], max_length=30)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_boy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.staff'),
        ),
        migrations.CreateModel(
            name='DeliveryBoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.order')),
                ('delivery_boy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.staff')),
            ],
        ),
    ]
