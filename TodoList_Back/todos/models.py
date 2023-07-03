from django.db import models


class Todo(models.Model):
    value = models.CharField('Todo', max_length=500, blank=True, default='')
    checked = models.BooleanField('status', default=False)    
    code = models.TextField()
    
    def __str__(self):
        return self.value 
        