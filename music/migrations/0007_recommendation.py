<<<<<<< HEAD
# Generated by Django 2.1.5 on 2019-01-27 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0006_auto_20190126_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_by', to=settings.AUTH_USER_MODEL)),
                ('recommended_song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Song')),
                ('recommended_to', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
=======
# Generated by Django 2.1.5 on 2019-01-27 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0006_auto_20190126_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_by', to=settings.AUTH_USER_MODEL)),
                ('recommended_song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Song')),
                ('recommended_to', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
>>>>>>> 1dec1ff361299080e76c8789214accf677b3fef6
