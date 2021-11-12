from django import forms


class Bmi_form(forms.Form):
    name = forms.CharField(max_length="30",label='Enter your name',widget=forms.TextInput(attrs={"placeholder": "your name",'class':'form-control'}))
    feet = forms.IntegerField(label='Enter your Height', widget=forms.NumberInput(attrs={"placeholder": "Feet",'class':'form-control'}))
    inch = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inches','class':'form-control'}))
    #height = forms.FloatField(label='Enter Height in Meter')
    weight = forms.FloatField(label='Enter weight in KG',widget=forms.NumberInput(attrs={"placeholder": "your weight",'class':'form-control'}))

class feet_meter(forms.Form):
    feet = forms.IntegerField(label='Enter your Height : ',widget=forms.NumberInput(attrs={'placeholder': 'Feet'}))
    inch = forms.IntegerField(label='Enter your Height : ',widget=forms.NumberInput(attrs={'placeholder': 'Inches'}))

