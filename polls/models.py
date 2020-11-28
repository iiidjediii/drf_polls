from django.db import models
from django.contrib.auth import get_user_model


class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=4096)
    is_active = models.BooleanField(default=True)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField('expiration date')

    #question = models.ManyToManyField(Question, related_name='questions')

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.poll.title
