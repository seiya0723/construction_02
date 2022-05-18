from django.contrib import admin

from .models import Question,Answer,Reply,QuestionUser,AnswerUser


class QuestionAdmin(admin.ModelAdmin):
    list_display    = ["title","dt","content","accept_dt","user",]


class AnswerAdmin(admin.ModelAdmin):
    list_display    = ["dt","content","question","user",]


class ReplyAdmin(admin.ModelAdmin):
    list_display    = ["dt","content","answer","user",]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Reply,ReplyAdmin)

admin.site.register(QuestionUser)
admin.site.register(AnswerUser)
