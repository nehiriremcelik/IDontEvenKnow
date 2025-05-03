from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.TextField()
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


