from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Eventos, Inscricao

@receiver(post_save, sender=Eventos)
def expire_subscriptions_from_finished_events(sender, instance, **kwargs):
    if instance.data < now().date():  # Verifica se a data do evento já passou
        Inscricao.objects.filter(id_evento=instance.id, status=0).update(status=2)