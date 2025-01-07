from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Task
from .tasks import log_message

@receiver(post_save, sender=Task)
def log_to_terminal(sender, instance: Task, **kwargs):
    message = ["A new task with an id of:", str(instance.id),
               "and a tile of:", instance.title,
               "has been created at", instance.created_at.isoformat(),
               "by the user named:", instance.user.get_full_name()
               ]
    
    log_message.delay(' '.join(message))

    
