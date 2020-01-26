from django.db import models
from django.utils import timezone

State = (
    ('Free','Free'),
    ('Blocked','Blocked'),
)

class Token(models.Model):
    key = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    last_alive = models.DateTimeField(default=timezone.now)
    state = models.CharField(max_length=20,default='Free',choices=State)

    def __str__(self):
        return self.key
