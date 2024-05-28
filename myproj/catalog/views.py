from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import RESTAURANT, DISH, COMMENT, REPLY

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_users=0
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

class DishListView(generic.ListView):
    model = DISH

class RestaurantDetailView(generic.DetailView):
    model = RESTAURANT
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 获取相关信息
        context['restaurant_dishes'] = DISH.objects.filter(resta_ID = self.object.resta_ID)
        context['restaurant_comments_and_replies'] = COMMENT.objects.filter(resta_ID = self.object.resta_ID).prefetch_related('replies')
        return context

class DishDetailView(generic.DetailView):
    model = DISH

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 获取相关信息
        context['dish_comments_and_replies'] = COMMENT.objects.filter(dish_ID = self.object.dish_ID).prefetch_related('replies')
        return context

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
	

from django.urls import reverse

def adddishes_form(request):
    if request.method == 'POST':
        resta_ID = request.POST.get('resta_ID')
        # 重定向到表单页面并传递主码
        return redirect(reverse('adddishes') + f'?resta_ID={resta_ID}')
    return render(request, 'catalog/restaurant_detail.html')

def adddishes(request):
    if request.method == 'POST':
        resta_ID = request.POST.get('resta_ID')
        dish_name = request.POST.get('dishname')
        price_c = request.POST.get('price')
        more_Info = request.POST.get('moreinfo')
        image = request.FILES.get('image')

        # 处理表单数据
        if not resta_ID or not dish_name:
            print('ERROR0: Missing required fields')
            return render(request, "login_fail.html")

        # 用户已存在
        if DISH.objects.filter(resta_ID=resta_ID, dish_name=dish_name).exists():
            print('ERROR1: Dish already exists')
            return render(request, "login_fail.html")

        # 尝试保存新菜品
        if 1:
            restaurant = RESTAURANT.objects.get(resta_ID=resta_ID)
            price = float(price_c) if price_c else None

            dish = DISH(
                resta_ID=restaurant,
                dish_name=dish_name,
                price=price,
                more_Info=more_Info,
                image=image
            )
            dish.full_clean()  # 验证字段
            dish.save()
            return redirect('restaurant-detail', pk=resta_ID)  # 重定向到餐馆详情页面

    else:
        resta_ID = request.GET.get('resta_ID')
        return render(request, 'catalog/add_dishes.html', {'resta_ID': resta_ID})


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import RESTAURANT
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

@login_required
def editrestaurants(request, pk):
    restaurant = get_object_or_404(RESTAURANT, pk=pk)

    if request.method == 'POST':
        resta_name = request.POST.get('resta_name')
        location = request.POST.get('location')
        time_open = request.POST.get('time_open')
        time_close = request.POST.get('time_close')
        tag = request.POST.get('tag')
        more_Info = request.POST.get('more_Info')
        image = request.FILES.get('image') if 'image' in request.FILES else None
        isopen = request.POST.get('isopen') == 'on'

        # 更新餐厅信息
        restaurant.resta_name = resta_name
        restaurant.location = location
        restaurant.time_open = time_open
        restaurant.time_close = time_close
        restaurant.tag = tag
        restaurant.more_Info = more_Info
        if image:
            restaurant.image = image
        restaurant.isopen = isopen

        try:
            restaurant.full_clean()  # 验证字段
            restaurant.save()
            return redirect('restaurant-detail', pk=restaurant.resta_ID)
        except ValidationError as e:
            print(f'ERROR: Validation error - {e}')
            return render(request, "edit_restaurants.html", {'restaurant': restaurant, 'errors': e.messages})
        except IntegrityError as e:
            print(f'ERROR: Integrity error - {e}')
            return render(request, "edit_restaurants.html", {'restaurant': restaurant, 'errors': [str(e)]})
        except Exception as e:
            print(f'ERROR: {e}')
            return render(request, "edit_restaurants.html", {'restaurant': restaurant, 'errors': [str(e)]})

    return render(request, 'catalog/edit_restaurants.html', {'restaurant': restaurant})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import RESTAURANT, DISH, COMMENT

@login_required
def add_comment(request, pk):
    restaurant = get_object_or_404(RESTAURANT, pk=pk)
    dishes = DISH.objects.filter(resta_ID=restaurant)

    if request.method == 'POST':
        grade = request.POST.get('grade')
        content = request.POST.get('content')
        dish_id = request.POST.get('dish_ID')

        # Check for valid inputs
        if not grade or not content:
            return render(request, 'catalog/add_comment.html', {'restaurant': restaurant, 'dishes': dishes, 'error': 'Grade and content are required.'})

        # Create and save the comment
        comment = COMMENT(
            user_ID=request.user,
            resta_ID=restaurant,
            dish_ID=DISH.objects.get(pk=dish_id) if dish_id else None,
            grade=grade,
            content=content
        )
        comment.save()
        return redirect('restaurant-detail', pk=restaurant.pk)

    return render(request, 'catalog/add_comment.html', {'restaurant': restaurant, 'dishes': dishes})
