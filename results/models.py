from django.db import models
from main.models import Quiz
from django.contrib.auth.models import User

# Objekti i rezultateve

class Results(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.pk)