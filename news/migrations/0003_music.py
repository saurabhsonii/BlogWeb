# Generated by Django 3.2.6 on 2022-09-26 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_blogcategory_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.FileField(upload_to='music')),
                ('mid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.blog')),
            ],
        ),
    ]
