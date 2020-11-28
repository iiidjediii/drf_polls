from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.filter(is_active=True, )
    serializer_class = serializers.PollSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
