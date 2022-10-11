from sys import api_version
from django.shortcuts import render
import json
from utils.constant import USERNAME, PASSWORD
from django.views.generic import ListView
from django.views import View
from games.models import School, Courses

# Create your views here.


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods



def online_game(request):
    return HttpResponse("CS GO, DOTA, PUBG are some popular video games")

#Handle post request not get request
@require_http_methods(["POST"])
@csrf_exempt
def addition_numbers(request):
    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({"msg" : "Invalid parameters"}, status = 400) 
    if ("num1" not in data) or ("num2" not in data):
         return JsonResponse({"msg" : "Invalid parameters"}, status = 400) 
    sum_num = data["num1"] + data["num2"]
    multiply = data["num1"] * data["num2"]
    return JsonResponse({"sum" : sum_num, "multiply" : multiply})


#handle only get request and not post
@require_http_methods(["GET"])
@csrf_exempt
def get_addition_number(request, num1,num2):
    return JsonResponse({"sum" : num1+num2, "multiply" : num1*num2})


def substract_number(request):
    num1 = 10
    num2 = 20
    return JsonResponse({"data" : num2-num1})


@require_http_methods(["POST"])
@csrf_exempt
def login(request):
    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({"msg" : "Invalid parameters"}, status = 400) 
    if ("username" not in data) or ("password" not in data):
         return JsonResponse({"msg" : "Username or password is missing"}, status = 400) 
    username = data["username"]
    password = data["password"]
    if username != USERNAME:
        return JsonResponse({"msg" : "Invalid username"}, status = 400) 
    if password != PASSWORD:
        return JsonResponse({"msg" : "Invalid password"}, status = 400) 
    return JsonResponse({"data" : "Login successfully"})


class LoginView(View):
    success_msg = "Login successfully"
    invalid_params = "Invalid Parameter"
    invalid_args = "Missing username or password"
    username_password_err = "Invalid username or password"
    error_status = 400


    def post(self, request):
        if not self.validate_payload(request):
            return JsonResponse({"msg" : self.invalid_params}, status = self.error_status)
        data = json.loads(request.body)
        if not self.validate_username_password(data):
            return JsonResponse({"msg" : self.invalid_args}, status = self.error_status)
        if not self.validate_values(data):
            return JsonResponse({"msg" : self.username_password_err}, status = self.error_status)
        return JsonResponse({"data" : self.success_msg})

    def validate_payload(self, request):
        try:
            data = json.loads(request.body)
            return True
        except Exception:
            return False
    
    def validate_username_password(self, data): 
        if ("email" not in data) or ("password" not in data):
            return False
        return True
    
    def validate_values(self, data):
        if data["email"] != USERNAME:
            return False
        if data["password"] != PASSWORD:
            return False
        return True













class StrCount(View):

    def post(self, request):
        data = json.loads(request.body)
        name_data = data["entries"]
        print(name_data)
        resp = []
        for i in name_data:
            resp.append({"entry_name" : i, "length" : len(i), "vowels_count" : self.find_vowels(i)})
        return JsonResponse({"data" : resp})

    
    def find_vowels(self, val):
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        for i in val:
            if i in vowels:
                count+=1
        return count



class AddSchool(View):

    # CRUD

    def post(self, request):
        user_data = json.loads(request.body)
        school_name = user_data.get("school_name")
        address = user_data.get("address")
        contact = user_data.get("contact")
        print("ghdfsagdasdfsagf")
        school_qs = School.objects.create(name = school_name, address = address, contact_number = contact)
        print(school_qs.id)
        return JsonResponse({"id" : school_qs.id, "name" : school_qs.name})
    
    def get(self, request):
        school_qs = School.objects.all()
        resp = []
        for data in school_qs:
            resp.append({"id" : data.id, "name" : data.name,"address" : data.address})
        return JsonResponse({"data" : resp})


class UpdateSchool(View):

    # CRUD

    def put(self, request, school_id):
        user_data = json.loads(request.body)
        school_name = user_data.get("school_name", None)
        address = user_data.get("address",None)
        contact = user_data.get("contact", None)
        if school_name:
            School.objects.filter(id = school_id).update(name=school_name)
        if address:
            School.objects.filter(id = school_id).update(address=address)
        if contact:
            School.objects.filter(id = school_id).update(contact_number=contact)
        return JsonResponse({"data" : "Successfully updated"})
    
    def delete(self, request, school_id):
        School.objects.filter(id = school_id).delete()
        return JsonResponse({"data" : "Deleted successfully"})


class AddCourses(View):

    # CRUD

    def post(self, request, school_id):
        user_data = json.loads(request.body)
        name = user_data.get("name", None)
        strength = user_data.get("strength",None)
        duration = user_data.get("duration", None)
        qs = Courses.objects.create(name = name, strength= strength, duration = duration, school_id = school_id)
        return JsonResponse({"id" : qs.id, "name" : qs.name})
    
    def get(self, request, school_id):
        qs = Courses.objects.filter(school_id = school_id)
        resp = []
        for data in qs:
            resp.append({"id" : data.id, "name" : data.name, "duration" : data.duration, "strength" : data.strength})
        return JsonResponse({"data" : resp})