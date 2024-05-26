from django.shortcuts import render
from django.http import HttpResponse
from webserver.models import Diet, Food
from django.http import JsonResponse
from django.db import connection, transaction

# Create your views here.


def webserver(request):
    myvalue = {}
    data = Food.objects.all()
    food_list = []
    food_json = {"request": "webserver"}
    for line in data:
        food ={
            "Name": line.Name,
            "Calories": line.Calories,
            "Carbohydrats": line.Carbohydrates,
            "Proteins": line.Proteins,
            "Fat": line.Fat,
            "Fiber": line.Fiber
        }
        food_list.append(food)

    
    food_json["data"] =food_list
    print(food_json)

    if request.method == "POST":
        user_name = request.POST["Name"]
        


    return render(request, "webserver.html", food_json)


def webserver_json(request):
    pass

def database(request):
    value = {}
    if request.method == "POST":
        name = request.POST["Name"]
        cals = request.POST["Calories"]
        carbo = request.POST["Carbohydrates"]
        protein = request.POST["Protein"]
        fat = request.POST["Fat"]
        fiber = request.POST["Fiber"]

        new_food = Food(Name= name, Calories= cals ,Carbohydrates= carbo, Proteins= protein,Fat= fat, Fiber= fiber)
        new_food.save()


    return render(request, "database.html")



def get_dropdown_data(request):
    data = list(Food.objects.all().values(
    "Name", 
    "Calories", 
    "Carbohydrates",
    "Proteins",
    "Fat",
    "Fiber"))
    return JsonResponse(data, safe=False)

def databasedell(request):
    response = {}
    if request.method == "POST":
       

        name = Food.objects.filter(Name=f'{request.POST["Name"]}').delete()
        response["name"] = name

        

    return render(request, "databasedell.html", response)