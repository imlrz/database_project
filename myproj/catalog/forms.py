from django import forms
from .models import RESTAURANT,DISH

class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model =RESTAURANT
        fields = ['resta_ID', 'resta_name','time_open','time_close','tag','AVG_grade','location','image','more_Info']

class AddDish(forms.ModelForm):
    class Meta:
        model =DISH
        fields = '__all__'  # 使用模型中的所有字段