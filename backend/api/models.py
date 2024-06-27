from django.db import models, transaction


class Task(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Назначена'),
        ('in_progress', 'Выполняется'),
        ('paused', 'Приостановлена'),
        ('completed', 'Завершена'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    performers = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    planned_effort = models.DurationField()
    actual_effort = models.DurationField()
    completion_date = models.DateTimeField(null=True, blank=True)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtasks')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        for subtask in self.subtasks.all():
            subtask.delete()
        super().delete(*args, **kwargs)

    @transaction.atomic
    def complete(self):
        if self.status != 'in_progress':
            raise ValueError('Task must be in progress to be completed')
        for subtask in self.subtasks.all():
            if subtask.status != 'completed':
                subtask.complete()
        self.status = 'completed'
        self.save()

    def pause(self):
        if self.status != 'in_progress':
            raise ValueError('Task must be in progress to be paused')
        self.status = 'paused'
        self.save()
