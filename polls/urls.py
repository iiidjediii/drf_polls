from django.urls import path
from rest_framework import viewsets
from .views import QuestionViewSet, PollViewSet, AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('/questions', QuestionViewSet)
router.register('/polls', PollViewSet)
router.register('/answers', AnswerViewSet)
urlpatterns = router.urls

