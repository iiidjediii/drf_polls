from django.contrib import admin
from .models import Question, Answer, Poll

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Answer)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#     )
#
#
# class PollAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'description',
#         'date_start',
#         'date_finish',
#         'is_active',
#     )
#     list_filter = ('question',)
#
#
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = (
#         'user',
#         'created',
#     )
#     list_filter = ('user',)


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Poll, PollAdmin)
# admin.site.register(Answer, AnswerAdmin)