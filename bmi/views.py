from django.shortcuts import render
from bmi.forms import Bmi_form 
import math

# Create your views here.
def home(request):
    if request.method == "POST":
        form = Bmi_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            feet = form.cleaned_data["feet"]
            inch = form.cleaned_data["inch"]
            weight = form.cleaned_data["weight"]
            height = (feet * 0.3048 + inch * 0.0254)
            bmi1 = weight/height**2

            bmi = '{:.2f}'.format(weight/height**2)

            if bmi1 < 18.5:
                ans = "you are Underweight "
            elif bmi1 >= 18.5 and bmi1 <= 24.5:
                ans = "you have Healthyweight "
            elif bmi1 >= 25.0 and bmi1 <= 29.5:
                ans = "you are Overweight "
            elif bmi1 >= 30.0 :
                ans = "you are suffering from Obesity"
            
            form = Bmi_form()

            return render(request, "home.html", {"form": form, "bmi":bmi, "name":name,"height":height,"ans":ans})
    else:
        form = Bmi_form()
    return render(request, "home.html", {"form": form})

'''def home(request):

  #  form = Bmi_form(request.POST, request.FILES)

    if request.method == 'POST':
        form = Bmi_form(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']

            bmi = weight/height

            result={
                'name':name,
                'bmi':bmi,
            }
            return render(request,'home.html',{'form':form},result)
    else:
        form = Bmi_form()
        return render(request,'home.html',{'form':form})

'''
