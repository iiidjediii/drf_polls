from rest_framework import serializers
from .models import Answer, Question, Poll
from django.forms import ValidationError


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'title', ]


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set', )

    class Meta:
        model = Poll
        fields = ['pk', 'title', 'is_active', 'date_start', 'date_finish', 'questions', ]


class AnswerSerializer(serializers.ModelSerializer):
    answers = serializers.JSONField()

    class Meta:
        model = Answer
        fields = ['pk', 'poll', 'created', 'question', 'answers', ]


    # def validate_answers(self, answers):
    #     if not answers:
    #         raise serializers.Validationerror("Answers must be not null.")
    #     return answers

    # def save(self):
    #     answers = self.data['answers']
    #     user = self.context.user
    #     for poll_id in answers:
    #         poll = Poll.objects.get(pk=poll_id)
    #         question = answers[poll_id]
    #         for question_id in questions:
    #             question = Question.objects.get(pk=question_id)
    #             Answer(user=user, poll=poll, question=question).save()
    #             user.is_answer = True
    #             user.save()


