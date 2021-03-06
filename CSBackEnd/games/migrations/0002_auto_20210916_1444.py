# Generated by Django 3.2.7 on 2021-09-16 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='team_Two_Name',
            new_name='away_Team',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='team_Two_ML',
            new_name='away_Team_ML',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='team_Two_Spread',
            new_name='away_Team_Spread',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='team_One_Name',
            new_name='home_Team',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='team_One_ML',
            new_name='home_Team_ML',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='team_One_Spread',
            new_name='home_Team_Spread',
        ),
        migrations.AddField(
            model_name='game',
            name='sports_Book',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
