from django.db import models


class Todo(models.Model):
    value = models.CharField('todo point', max_length=500, blank=True, default='')
    checked = models.BooleanField('status', default=False)    
    
    def __str__(self):
        return self.value 
        