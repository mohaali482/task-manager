from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', _("Pending")
        IN_PROGRESS = 'in_progress', _("In Progress")
        COMPLETED = 'completed', _("Completed")

    user = models.ForeignKey("auth.User", verbose_name=_("User"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    status = models.CharField(_("Status"), max_length=50, choices=StatusChoices.choices,
                              default=StatusChoices.PENDING)
    
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

    def __str__(self):
        return self.title
