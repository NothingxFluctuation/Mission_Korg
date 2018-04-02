from django.db import models

# Create your models here.

    
class Code(models.Model):
    code = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.is_read)
    
