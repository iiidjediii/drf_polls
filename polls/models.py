from django.db import models
from django.contrib.auth import get_user_model


class Question(models.Model):
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class Poll(models.Model):
    question = models.ManyToManyField(Question)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=4096)
    is_active = models.BooleanField(default=True)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField('expiration date')

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    poll = models.ManyToManyField(Poll)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll.title
