from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    TAG_CHOICES = [
    ('daily_life', 'Daily Life'),
    ('sports', 'Sports'),
    ('hobbies', 'Hobbies'),
    ('technology', 'Technology'),
    ('education_career', 'Education and Career'),
    ('health_fitness', 'Health and Fitness'),
    ('travel', 'Travel'),
    ('entertainment', 'Entertainment'),
    ('food_cooking', 'Food and Cooking'),
    ('music_arts', 'Music and Arts'),
    ('books_literature', 'Books and Literature'),
    ('relationships', 'Relationships'),
    ('gaming', 'Gaming'),
    ('science_nature', 'Science and Nature'),
    ('other', 'Other'),
]

    question_text = models.TextField()
    tag = models.CharField(max_length=30, choices=TAG_CHOICES)
    pub_date = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.question_text


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer_text[:50]


