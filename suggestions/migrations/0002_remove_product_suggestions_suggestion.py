# Generated by Django 4.1.7 on 2023-07-22 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='suggestions',
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion_name', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to='suggestions.product')),
            ],
        ),
    ]
