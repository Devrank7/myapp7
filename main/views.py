import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from hope_project.celery import app
from .forms import PhytonForm
from .models import Food
from .mongodb import get_nosql_database
from .tasks import sums
from celery.result import AsyncResult
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    alls = Food.objects.all()
    for food in alls:
        print(food)
    return HttpResponse("Hello, world. You're at the home view.")


class add_food(FormView):
    form_class = PhytonForm
    template_name = "add.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def perform_task(request):
    a = 2
    b = 5
    res = sums.apply_async(args=(a, b))
    # print(res.id)
    # task_id = res.id
    # result = AsyncResult(task_id, app=app)
    print(res.state)
    print(res.get())  # 7
    print(res.state)  # 'SUCCESS'
    return HttpResponse("Done")


def perform_task2(request):
    task_id = 'a0a42610-4e01-42ca-a341-cfe583729804'
    result = AsyncResult(task_id)
    print(result.state)
    print(result.get())
    print(result.state)
    return HttpResponse("Done 1")


def get_data(request, idd):
    try:
        db = get_nosql_database()
        clubs = db.food
        arrgs = {
            "_id": idd,
            "name": "Root",
            "price": 400,
            "category": ["boot", "coot"]
        }
        # clubs.insert_one(arrgs)
        # clubs.delete_one({"_id": idd})
        data = clubs.find_one({"_id": idd})
        print(data)
        return HttpResponse(json.dumps(data))

        # clubs.update_one({"_id": 2},
        #                 {"$set": {"category.0": "vegetables", "name": "Cucumber"}})

        print("Some OK")
    except Exception as e:
        print(e)
        print("Some Error")
    return HttpResponse("What nosql?")
