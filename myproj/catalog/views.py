from django.shortcuts import render

# Create your views here.
from .models import USER, RESTAURANT

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_users=USER.objects.all().count()
    # Available books (status = 'a')
    num_restaurants=RESTAURANT.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_users':num_users,'num_restaurants':num_restaurants},
    )

from django.views import generic

class RestaurantListView(generic.ListView):
    model = RESTAURANT

class RestaurantDetailView(generic.DetailView):
    model = RESTAURANT

# # 导入模块
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

def register(request):
	if request.method == 'GET':
		return render(
			request,
			'registration/register.html'
		)
	
	elif request.method == 'POST':
		# 获取参数
		user_name = request.POST.get('username')
		pwd = request.POST.get('password')
		
		if not user_name or not pwd:
			print('ERROR0')
			return render(request, "login_fail.html")

		# 用户已存在
		if User.objects.filter(username=user_name):
			print('ERROR1')
			return render(request, "login_fail.html")
		# 用户不存在
		else:
			# 使用User内置方法创建用户
			user = User.objects.create_user(
				username=user_name,
				password=pwd,
				email='123@qq.com',
				is_staff=0,
				is_active=1,
				is_superuser=0
			)
			user.save()
			
			return redirect('index')
	
	else:
		print('ERROR3')
		return render(request, "login_fail.html")


