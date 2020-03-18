from django.db import models


# Create your models here.


class Question(models.Model):
    qno = models.CharField(max_length=100, null=True)
    option=models.CharField(max_length=100,null=True)

    def __str__(self):
        return '{}'.format(self.qno)


# class Answer(models.Model):
#     question_relation = models.ForeignKey(Question, on_delete=models.CASCADE)
#     option = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return '{}'.format(self.option)
