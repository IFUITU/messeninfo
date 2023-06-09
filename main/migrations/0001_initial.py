# Generated by Django 4.1.3 on 2023-03-24 17:56

from django.db import migrations, models
import messeninfo.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('cnsort', models.CharField(blank=True, max_length=10, null=True)),
                ('messe_text', models.CharField(max_length=255)),
                ('beschreibung', models.TextField(blank=True, null=True)),
                ('google', models.IntegerField(blank=True, null=True)),
                ('small_img', models.ImageField(blank=True, null=True, upload_to=messeninfo.helpers.upload_file_name)),
                ('big_img', models.ImageField(blank=True, null=True, upload_to=messeninfo.helpers.upload_file_name)),
            ],
            options={
                'db_table': 'branchen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('languages_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=2)),
                ('site_domain', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/lang_img')),
                ('directory', models.CharField(blank=True, max_length=32, null=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('language_charset', models.TextField()),
            ],
            options={
                'db_table': 'languages',
                'managed': False,
            },
        ),
    ]
