from django.shortcuts import render
from . import models
from .models import Question
# from .models import Answer

# Create your views here.
def home(request):


    return render(request,'index.html')
def sheet(request):
    # print("im here")
    Question.objects.all().delete()
    noq=request.POST.get('noq')
    context = {
        'noq':list(range(1,int(noq)+1))
    }

    return render(request,'./qna/sheet.html',context)
def result(request):





    for i in request.POST:


        if i!='csrfmiddlewaretoken':
            x=models.Question.objects.create(qno=i,option=request.POST.get(str(i)))
    context = {'ans': Question.objects.all()}

    return render(request, './qna/result.html', context)




