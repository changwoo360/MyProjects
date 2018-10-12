"""test_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from delicious_hometown import views
urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^login/', views.login),
    url(r'^logout/', views.logout),

    url(r'^index/', views.index),
    url(r'^foodmaterial', views.foodmaterial),
    url(r'^ambry/', views.ambry),
    url(r'^treasure/', views.treasure),
    url(r'^shop/(\d+)/$', views.shop_buy),
    url(r'^shop/', views.shop),
    url(r'^backpack/option/(.*?)/$', views.backpack_option),
    url(r'^backpack/', views.backpack),
    url(r'^buy_money/(.\d+)/$', views.buy_money_buy),
    url(r'^buy_money/$', views.buy_money),
    #url(r'^recipe/(\d+)/study/$', views.recipe_study),
    url(r'^recipe/(\d+)/$', views.recipe_view),
    url(r'^recipe/', views.recipe),
    url(r'^my_recipe/', views.my_recipe),
    url(r'^study_confirm/(\d+)/$', views.recipe_study_confirm),
    url(r'^recipe_study/', views.recipe_study),

    url(r'^market/',views.market),


    url(r'^gift/', views.Gift.as_view()),
    url(r'^friend/', views.friend),



    # 临时填充页面
    url('^test_1/', views.test_1),
    url('^test_2/', views.test_2),
    url('^test_3/', views.test_3),
    url('^home_address/', views.home_address),

]
