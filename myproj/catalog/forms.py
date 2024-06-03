from django import forms
from .models import RESTAURANT,DISH,MANAGER_REG

class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model =RESTAURANT
        fields = '__all__'  # 使用模型中的所有字段

class AddDish(forms.ModelForm):
    class Meta:
        model =DISH
        fields = '__all__'  # 使用模型中的所有字段
class ApplyRestaurantForm(forms.ModelForm):
    class Meta:
        model =MANAGER_REG
        fields = '__all__'  # 使用模型中的所有字段