from django.db import models
import random

# LLojet e kuizeve sipas ne baze te veshtiresise

diff_choices = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
)

# Modeli i kuizit

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=diff_choices)

    def __str__(self):
        return self.name
    
    def get_question(self):
        questions = list(self.questions_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]