# Generated by Django 4.1 on 2023-03-02 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("grace", "0003_church_event_church_event_gallery_church_gallery_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="image2",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="image3",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="image4",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="image5",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="image6",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="title2",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="title3",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="title4",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="title5",
        ),
        migrations.RemoveField(
            model_name="church_event_gallery",
            name="title6",
        ),
        migrations.RemoveField(
            model_name="church_gallery",
            name="image2",
        ),
        migrations.RemoveField(
            model_name="church_gallery",
            name="image3",
        ),
        migrations.RemoveField(
            model_name="church_gallery",
            name="image4",
        ),
        migrations.RemoveField(
            model_name="church_gallery",
            name="image5",
        ),
        migrations.RemoveField(
            model_name="church_gallery",
            name="image6",
        ),
    ]
