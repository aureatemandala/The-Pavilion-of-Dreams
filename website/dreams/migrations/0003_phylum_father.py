# Generated by Django 3.0.8 on 2020-08-25 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dreams', '0002_article_kingdom_phylum'),
    ]

    operations = [
        migrations.AddField(
            model_name='phylum',
            name='FATHER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='dreams.Kingdom', verbose_name='父类别'),
            preserve_default=False,
        ),
    ]
