# Generated by Django 4.0.4 on 2022-09-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('heading', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]
