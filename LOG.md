# Project Log

## Environment
python = 3.11.4

## Version = 5.20.18lrz
### Modifications
1. 增加 templates/registration/register.html 文件，用于注册（注意在 html 页面中部分位置将register写为login，不是bug无需修改，仅因css是抄的，渲染方便）
2. 增加 static/css/reg_style.html 文件，用于渲染 register.html
3. 补写 urls.py (line 8) 和 views.py (line 30-75), 但注意失败弹窗等还未具体完成
4. 改写 static/css/style.html 用于界面的风格统一
### Additional Features
1. 可实现顾客注册功能（可以写入数据库）
2. 改进了 UI 界面，仍待继续改进
### Directory
> myproj/
    >> 1. manage.py
    >> 2. catalog/
        >>> 1. models.py (建立模型，目前只建立了RESTAURANT，且暂未处理图片，修改后需运行 manage.py makemigration 和 manage.py migrate)
        >>> 2. urls.py (实现网址和views的对接，参数name是干什么的？)
        >>> 3. views.py (和前端html对接)
        >>> 4. static/
            >>>> 1. css/
                >>>>> 1. style.css (第一版，可随时修改)
                >>>>> 2. reg_style.html (可与style.css合并)
            >>>> 2. image/
        >>> 5. templates/
            >>>> 1. base_generic.html (通用页面模板，可随时修改)
            >>>> 2. index.html (主页，待完善)
            >>>> 3. catalog/
                >>>>> 1. base_generic_cata.html (给catalog目录下的模板，非必须，可能依靠bug运行)
                >>>>> 2. restaurant_detail.html (餐厅详情页，待完善)
                >>>>> 3. restaurant_list.html (餐厅列表，待完善)
            >>>> 4. registration/
                >>>>> 1. login.html (登陆界面，目前渲染疑似存在问题)
                >>>>> 2. logged_out.html (登出)
                >>>>> 3. password_reset_xxx.html (修改密码系列，直接从教程复制，暂未修改)
                >>>>> 4. register.html (注册界面)
    >> 3. myproj/ (目前暂无需要频繁修改的文件)
### Urls
1. 'catalog/', name='index', 主页
2. 'catalog/restaurants/', name='restaurants', 餐厅列表
3. 'catalog/restaurants/<int:pk>', name='restaurant-detail', 餐厅详情页
4. 'catalog/register', name='Registration', 注册页面

            
            


