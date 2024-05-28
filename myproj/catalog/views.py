from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import RESTAURANT, DISH
from .forms import AddRestaurantForm,AddDish
# # 导入模块
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
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


class RestaurantListView(generic.ListView):
    template_name = 'restaurant_list.html'
    context_object_name = 'searchresults'
    paginate_by = 1
    def get_queryset(self):
        searchway = self.request.GET.get('searchway')
        name = self.request.GET.get('name')
        
        if searchway == 'R':
            queryset = RESTAURANT.objects.all()
            if name:
                queryset = queryset.filter(resta_name__icontains=name)
        elif searchway == 'D':
            queryset = DISH.objects.all()
            if name:
                queryset = queryset.filter(dish_name__icontains=name)
        else:
            queryset = RESTAURANT.objects.all()
            if name:
                queryset = queryset.filter(resta_name__icontains=name)
                
        return queryset
    
    def get_template_names(self):
        '''
        searchway = self.request.GET.get('searchway')
        if searchway == 'D':
            return ['catalog/dish_list.html']
        '''
        return ['catalog/restaurant_list.html']


class DishListView(generic.ListView):
    model = DISH

class RestaurantDetailView(generic.DetailView):
    model = RESTAURANT

class DishDetailView(generic.DetailView):
    model = DISH



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
			
			return redirect('restaurants')
	
	else:
		print('ERROR3')
		return render(request, "login_fail.html")


def addrestaurant(request):
    """
    View function for renewing a specific BookInstance by librarian
    """

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST,request.FILES)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            form.save()  # 保存数据到数据库
            return redirect('index' )
            # redirect to a new URL:


    # If this is a GET (or any other method) create the default form.
    else:
        form = AddRestaurantForm
    return render(request, 'catalog/addrestaurant.html', {'form': form})

def adddish(request):

    if request.method == 'POST':
        form = AddDish(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('index' )
    else:
        form = AddDish
    return render(request, 'catalog/addrestaurant.html', {'form': form})