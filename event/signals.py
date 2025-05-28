from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Eventos, Inscricao

@receiver(post_save, sender=Eventos)
def expire_subscriptions_from_finished_events(send, instance, **kwargs):
    if instance.status == 0:
        Inscricao.objects.filter(id_evento=instance.id, status=0).update(status=2)