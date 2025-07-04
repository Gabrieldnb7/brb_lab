# Generated by Django 5.2.2 on 2025-06-28 14:56

import uuid
from django.db import migrations, models

def generate_events_checkin_code(apps, schema_editor):
    Events = apps.get_model('event', 'Eventos')

    for evento in Events.objects.all():
        evento.checkin_code = uuid.uuid4()
        evento.save()

def change_inscription_status(apps, schema_editor):
    Inscricao = apps.get_model('event', 'Inscricao')
    status = ['ativa', 'cancelada', 'validada', 'expirada']

    for insc in Inscricao.objects.all():
        insc.status = status[insc.status-1]

class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_eventos_checkin_code_alter_eventos_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='checkin_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RunPython(generate_events_checkin_code),
        migrations.RunPython(change_inscription_status),
    ]
