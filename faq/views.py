from django.shortcuts import render,redirect
from django.views import View

from .models import Question,Answer,Reply

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context["questions"]    = Question.objects.all()

        return render(request,"faq/index.html",context)

index   = IndexView.as_view()


"""
class SingleView(View):
    def get(self, request, pk, *args, **kwargs):

        context = {}
        context["topic"]    = Topic.objects.filter(id=pk).first()
        context["replies"]  = TopicReply.objects.filter(topic=pk)

        return render(request,"faq/single.html",context)

    def post(self, request, pk, *args, **kwargs):

        print(request.POST)

        copied          = request.POST.copy()
        copied["topic"] = pk


        form    = TopicReplyForm(copied)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)

        return redirect("faq:single",pk)
single  = SingleView.as_view()

"""



