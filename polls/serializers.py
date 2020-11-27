from rest_framework import serializers
from .models import Answer, Question, Poll


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['pk', 'title', 'is_active', 'date_start', 'date_finish', 'question', ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'title', ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['pk', 'poll', 'created', ]






