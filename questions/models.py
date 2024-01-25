from django.db import models
from main.models import Quiz

# Objekti i pyetjeve

class Questions(models.Model):
    text = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
    
    def get_answer(self):
        return self.anwser_set.all()

# Objekti i pergjgjjeve 

class Anwser(models.Model):
    text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question {self.question}, answer : {self.text}"