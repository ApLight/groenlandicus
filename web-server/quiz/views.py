from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
import csv, json

from .models import Quiz

def update_quizzes():
    with open("quiz/quizzes.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not Quiz.objects.filter(problem=row["problem"]).exists():
                Quiz.objects.create(problem=row["problem"], answer=row["answer"], explanation=row["explanation"])
        

def get_quizzes(request):
    quizzes = Quiz.objects.order_by("?")[:3]
    if len(quizzes) < 3:
        data = {"message": "Fail"}

    else:
        data = {
            "message": "Success",
            "quizzes": []
        }
        for quiz in quizzes:
            data["quizzes"].append(model_to_dict(quiz))

    return HttpResponse(json.dumps(data, ensure_ascii=False), "application/json")
