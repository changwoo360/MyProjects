from django.shortcuts import render, HttpResponse, redirect
from delicious_hometown import models
from django.views import View

from collections import Counter
from django.db.models import Sum, Count, Max, Min
import random
# Create your views here.

# 登陆
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.Account.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.pk

            return HttpResponse('登陆成功<br><a href="/index/">官网</a>')
    return render(request, 'login.html')

# 注销
def logout(request):
    request.session['user_id'] = None
    return HttpResponse('已成功注销<br><a href="/login/">登陆</a>')

# 主页
def index(request):
    user_id = request.session['user_id']
    user = models.User.objects.filter(account_id=user_id).first()
    return render(request, 'index.html', locals())

# 食材
def foodmaterial(request):
    food_material = models.FoodMaterial.objects.all()
    return render(request, 'foodmaterial.html', locals())

# 橱柜
def ambry(request):
    food_material_level_obj = models.FoodMaterialLevel.objects.all()
    level = request.GET.get('level')
    user_id = request.session['user_id']
    foodmaterial = models.Ambry.objects.filter(user_id__id=user_id).all()
    foodmaterial_count = models.Ambry.objects.filter(user_id__id=user_id).count()
    foodmaterial_list = [i.food_material_id for i in foodmaterial]
    foodmaterial_dic = {}
    food_material_level_1 = {}
    food_material_level_2 = {}
    food_material_level_3 = {}
    food_material_level_4 = {}
    food_material_level_5 = {}
    for key in foodmaterial_list:
        foodmaterial_dic[key] = foodmaterial_dic.get(key, 0) + 1
    #print(foodmaterial_list, foodmaterial_dic)
    for k, v in foodmaterial_dic.items():
        print(k,v)
        food_material_level = models.FoodMaterial.objects.filter(pk=k).first().food_material_level_id
        food_material = models.FoodMaterial.objects.filter(pk=k).first().food_material

        if food_material_level == 1:
            food_material_level_1[food_material] = v
        elif food_material_level == 2:
            food_material_level_2[food_material] = v
        elif food_material_level == 3:
            food_material_level_3[food_material] = v
        elif food_material_level == 4:
            food_material_level_4[food_material] = v
        elif food_material_level == 5:
            food_material_level_5[food_material] = v

    return render(request, 'ambry.html', locals())

# 圣地
def treasure(request):
    dig_num = request.GET.get('dig')
    user_id = request.session['user_id']
    user_obj = models.User.objects.filter(pk=user_id).first()
    energy = models.User.objects.filter(pk=user_id).first().energy
    if dig_num:
        if dig_num == '1':
            dig_energy = int(dig_num) * 3
            if energy < dig_energy:
                return HttpResponse('体力不足')
            else:
                energy = energy - dig_energy
                models.User.objects.filter(pk=user_id).update(energy=energy)
                dig_choice_count = models.FoodMaterial.objects.count()
                dig_choice_num = random.randint(1, dig_choice_count)
                dig_choice = models.FoodMaterial.objects.filter(pk=dig_choice_num).first()
                models.Ambry(food_material_id=dig_choice.pk, user_id=user_obj.pk).save()
                dig_choices = []

                dig_choices.append(dig_choice)
        if dig_num == '5':
            dig_energy = int(dig_num) * 3
            if energy < dig_energy:
                return HttpResponse('体力不足<br><a href="/treasure/">返回</a>')
            else:
                energy = energy - dig_energy
                models.User.objects.filter(pk=user_id).update(energy=energy)
                user_obj = models.User.objects.filter(pk=user_id).first()
                dig_choice_count = models.FoodMaterial.objects.count()
                dig_choice_list = [i for i in range(dig_choice_count)]
                dig_choice_num = random.sample(dig_choice_list, 5)
                dig_choices = []
                for dig_result in dig_choice_num:
                    dig_result_0 = models.FoodMaterial.objects.filter(pk=dig_result).first()
                    dig_choices.append(dig_result_0)
                for dig_choice in dig_choices:
                    models.Ambry(food_material_id=dig_choice.pk, user_id=user_obj.pk).save()
    else:
        return render(request, 'treasure.html', locals())
    return render(request, 'treasure.html', locals())

# 商店
def shop(request):
    method = request.GET.get('method')
    buy = request.GET.get('buy')
    level = request.GET.get('level')
    '''
    if method:
        pass
    else:
        return redirect('/shop/')'''
    if buy:
        return HttpResponse('<button><a href="/shop/{}/?method=true">确定购买！</a></button>  <a href="/shop/">取消</a>'.format(buy))
    else:

        prop_level_obj = models.PropLevel.objects.all()
        prop_level_1 = models.Prop.objects.filter(prop_level_id=1).all()
        prop_level_2 = models.Prop.objects.filter(prop_level_id=2).all()
        prop_level_3 = models.Prop.objects.filter(prop_level_id=3).all()
        prop_level_4 = models.Prop.objects.filter(prop_level_id=4).all()
        prop_level_5 = models.Prop.objects.filter(prop_level_id=5).all()
        prop_level_6 = models.Prop.objects.filter(prop_level_id=6).all()
        prop_level_7 = models.Prop.objects.filter(prop_level_id=7).all()
        prop_level_8 = models.Prop.objects.filter(prop_level_id=8).all()
        return render(request, 'shop.html', locals())

# 商店购买确认
def shop_buy(request, buy_id):
    user_id = request.session.get('user_id')
    method = request.GET.get('method')
    if method == 'true':
        buy_obj = models.Prop.objects.filter(pk=buy_id).first()
        user_obj = models.User.objects.filter(pk=user_id).first()
        if buy_obj.price_class == 1:
            if user_obj.coin >= buy_obj.price:
                # 将用户的金币减去购买物品的价格
                new_coin = user_obj.coin - buy_obj.price
                user_coin = models.User.objects.get(pk=user_id)
                user_coin.coin = new_coin
                user_coin.save()
                #models.User(pk=user_id, wing=new_coin).save()
                models.Backpack(user_id=user_id, backpack_prop_id=buy_id).save()
                return HttpResponse('购买道具<{0}>成功,花费了{1}{2}<br><a href="/shop/">返回商店</a>'.format(buy_obj.name, buy_obj.price, buy_obj.get_price_class_display()))
            else:
                return HttpResponse('金币不足，购买失败<br><a href="/shop/">返回商店</a>')
        elif buy_obj.price_class == 2:
            if user_obj.wing >= buy_obj.price:
                # 将用户的元宝减去购买物品的价格
                new_wing = user_obj.wing - buy_obj.price
                user_wing = models.User.objects.get(pk=user_id)
                user_wing.wing = new_wing
                user_wing.save()
                models.Backpack(user_id=user_id, backpack_prop_id=buy_id).save()
                return HttpResponse('购买道具<{0}>成功,花费了{1}{2}<br><a href="/shop/">返回商店</a>'.format(buy_obj.name, buy_obj.price, buy_obj.get_price_class_display()))
            else:
                return HttpResponse('元宝不足，购买失败<br><a href="/shop/">返回商店</a>')
        else:
            return redirect('/shop/')
    else:
        return redirect('/shop/')

# 仓库
def backpack(request):
    level = request.GET.get('level')
    prop_level_obj = models.PropLevel.objects.all()
    user_id = request.session['user_id']
    backpack_obj_all = models.Backpack.objects.filter(user_id__id=user_id).all()
    backpack_obj_list = [i.backpack_prop_id for i in backpack_obj_all]
    prop_dic = {}
    prop_dic_1 = {}
    prop_dic_2 = {}
    prop_dic_3 = {}
    prop_dic_4 = {}
    prop_dic_5 = {}
    prop_dic_6 = {}
    prop_dic_7 = {}
    prop_dic_8 = {}
    for key in backpack_obj_list:
        prop_dic[key] = prop_dic.get(key, 0) + 1
    for k, v in prop_dic.items():
        prop_level_id = models.Prop.objects.filter(pk=k).first().prop_level_id
        prop_name = models.Prop.objects.filter(pk=k).first().name
        if prop_level_id == 1:
            prop_dic_1[prop_name] = v
        elif prop_level_id == 2:
            prop_dic_2[prop_name] = v
        elif prop_level_id == 3:
            prop_dic_3[prop_name] = v
        elif prop_level_id == 4:
            prop_dic_4[prop_name] = v
        elif prop_level_id == 5:
            prop_dic_5[prop_name] = v
        elif prop_level_id == 6:
            prop_dic_6[prop_name] = v
        elif prop_level_id == 7:
            prop_dic_7[prop_name] = v
        elif prop_level_id == 8:
            prop_dic_8[prop_name] = v
        print(prop_dic_1)
    return render(request, 'backpack.html', locals())

# 仓库道具操作
def backpack_option(request, option_name):
    user_id = request.session.get('user_id')
    backpack_option_method = request.GET.get('method')
    if backpack_option_method == 'used':
        option_pk = models.Prop.objects.filter(name=option_name).first().pk
        models.Backpack.objects.filter(user_id=user_id, backpack_prop_id=option_pk).delete()
        return HttpResponse('使用成功<br><a href="/backpack/">返回仓库</a>')
    elif backpack_option_method == 'view':
        return HttpResponse('查看成功')
    elif backpack_option_method == 'sell':
        option_pk = models.Prop.objects.filter(name=option_name).first().pk
        models.Backpack.objects.filter(user_id=user_id, backpack_prop_id=option_pk).first().delete()
        return HttpResponse('出售成功<br><a href="/backpack/">返回仓库</a>')
    else:
        return redirect('/backpack/')

# 充值
def buy_money(request):
    buy = request.GET.get('buy')
    user_id = request.session.get('user_id')
    user_obj = models.User.objects.filter(pk=user_id).first()
    if buy:
        return HttpResponse('<button><a href="/buy_money/{}/?method=true">确定购买！</a></button>  <a href="/buy_money/">取消</a>'.format(buy))
    else:
        return render(request, 'buy_money.html', locals())

# 充值确认
def buy_money_buy(request, buy_id):
    user_id = request.session.get('user_id')
    user_obj = models.User.objects.get(pk=user_id)
    method = request.GET.get('method')
    if method == 'true':
        if buy_id == 'a6':
            user_obj.wing = user_obj.wing + 600
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(600, user_obj.wing))
        elif buy_id == 'a25':
            user_obj.wing = user_obj.wing + 2500
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(2500, user_obj.wing))
        elif buy_id == 'a50':
            user_obj.wing = user_obj.wing + 5000
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(5000, user_obj.wing))
        elif buy_id == 'a98':
            user_obj.wing = user_obj.wing + 9800
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(9800, user_obj.wing))
        elif buy_id == 'a128':
            user_obj.wing = user_obj.wing + 12800
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(12800, user_obj.wing))
        elif buy_id == 'a198':
            user_obj.wing = user_obj.wing + 19800
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(19800, user_obj.wing))
        elif buy_id == 'a328':
            user_obj.wing = user_obj.wing + 32800
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(32800, user_obj.wing))
        elif buy_id == 'a648':
            user_obj.wing = user_obj.wing + 64800
            user_obj.save()
            return HttpResponse('充值{0}元宝成功，当前元宝总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(64800, user_obj.wing))

        elif buy_id == 'b6':
            user_obj.coin = user_obj.coin + 60000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(60000, user_obj.coin))
        elif buy_id == 'b25':
            user_obj.coin = user_obj.coin + 250000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(250000, user_obj.coin))
        elif buy_id == 'b50':
            user_obj.coin = user_obj.coin + 500000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(500000, user_obj.coin))
        elif buy_id == 'b98':
            user_obj.coin = user_obj.coin + 980000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(980000, user_obj.coin))
        elif buy_id == 'b128':
            user_obj.wing = user_obj.wing + 1280000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(1280000, user_obj.coin))
        elif buy_id == 'b198':
            user_obj.coin = user_obj.coin + 1980000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(1980000, user_obj.coin))
        elif buy_id == 'b328':
            user_obj.coin = user_obj.coin + 3280000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(3280000, user_obj.coin))
        elif buy_id == 'b648':
            user_obj.coin = user_obj.coin + 6480000
            user_obj.save()
            return HttpResponse('充值{0}金币成功，当前金币总额为{1} <br><a href="/buy_money/">返回充值中心</a>'.format(6480000, user_obj.coin))



        return HttpResponse('233333')
    else:
        return redirect('/buy_money/')

def recipe(request):
    level = request.GET.get('level')
    recipe_class_obj = models.RecipeClass.objects.all()
    recipe_class_1 = models.RecipeName.objects.filter(recipe_class__id=1).all()
    recipe_class_2 = models.RecipeName.objects.filter(recipe_class__id=2).all()
    recipe_class_3 = models.RecipeName.objects.filter(recipe_class__id=3).all()
    recipe_class_4 = models.RecipeName.objects.filter(recipe_class__id=4).all()
    recipe_class_5 = models.RecipeName.objects.filter(recipe_class__id=5).all()
    recipe_class_6 = models.RecipeName.objects.filter(recipe_class__id=6).all()
    recipe_class_7 = models.RecipeName.objects.filter(recipe_class__id=7).all()
    recipe_class_8 = models.RecipeName.objects.filter(recipe_class__id=8).all()
    recipe_class_9 = models.RecipeName.objects.filter(recipe_class__id=9).all()
    recipe_class_10 = models.RecipeName.objects.filter(recipe_class__id=10).all()
    return render(request, 'recipe.html', locals())

def recipe_view(request, view_id):
    recipe_object = models.RecipeName.objects.filter(pk=view_id).first()
    recipe_view_obj = models.RecipeLevel.objects.filter(recipe_name_id__pk=recipe_object.pk).all()
    recipe_level = []
    for num in range(1, 6):
        view_level = models.RecipeLevel.objects.filter(recipe_name_id__pk=recipe_object.pk, level=num).all()
        for view in view_level:
            ss_obj = models.RecipeMaterial.objects.filter(level_id=view.pk).all()
            recipe_level_1 = []
            for s in ss_obj:
                material = models.FoodMaterial.objects.filter(pk=s.material_id).first().food_material
                recipe_level_1.append(material)
        recipe_level.append(recipe_level_1)

    return render(request, 'recipe_view.html', locals())

def recipe_study(request):
    user_id = request.session.get('user_id')
    recipe_id = request.GET.get('recipe')
    level_id = request.GET.get('level')
    material_id = models.RecipeLevel.objects.filter(recipe_name_id=recipe_id, level=level_id).first().pk
    level_material_all = models.RecipeMaterial.objects.filter(level=material_id).all()
    material_dic = {}
    for level_material in level_material_all:
        material_list = []
        material_name = level_material.material.food_material
        material_id = level_material.material_id
        material_count = models.Ambry.objects.filter(user_id=user_id, food_material_id=material_id).count()
        material_list.append(material_name)
        material_list.append(material_count)
        material_dic[material_id] = material_list
    return render(request, 'recipe_study.html', locals())

def recipe_study_confirm(request, confirm_id):
    level = request.GET.get('level')
    user_id = request.session.get('user_id')
    method = request.GET.get('method')
    if method == 'true':
        study_dic = {}
        level_id = models.RecipeLevel.objects.filter(recipe_name_id=confirm_id, level=int(level)).first().pk
        study_all_id = models.RecipeMaterial.objects.filter(level_id=level_id).all()
        for study_id in study_all_id:
            study_count = models.Ambry.objects.filter(user_id=user_id, food_material_id=study_id.material_id).count()
            study_dic[study_id.material.food_material] = study_count
        # print(study_dic) # {'面粉': 4, '甜面酱': 5, '鸡蛋': 3}
        if level == '1':
            study_dic_len = len(study_dic)
            i = 0
            study_list = []
            for study_name, study_used in study_dic.items():
                study_list.append(study_name)
                if study_used > 1:
                    i += 1
                else:
                    return HttpResponse('材料不足，学习失败<br><a href="/recipe/{0}/">返回菜谱详细页</a>'.format(confirm_id))
            if i == study_dic_len:
                study_name_main = models.RecipeName.objects.filter(pk=confirm_id).first().name
                # 该在modesl中删除数据和增加食谱了，另外还要判断level的数量
                if len(study_list) == 2:
                    models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[0]).first().delete()
                    models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[1]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse('学习【{0}】成功，共耗费食材{1}1份 {2}1份<br><a href="/recipe/{3}/">返回菜谱详细页</a>'.format(study_name_main, study_list[0], study_list[1], confirm_id))
                elif len(study_list) == 3:
                    models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[0]).first().delete()
                    models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[1]).first().delete()
                    models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[2]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse('学习【{0}】成功<br>共耗费食材:<br>{1}1份 <br>{2}1份 <br>{3}1份<br><a href="/recipe/{4}/">返回菜谱详细页</a>'.format(study_name_main, study_list[0], study_list[1], study_list[2], confirm_id))
                else:
                    pass

        elif level == '2':
            study_dic_len = len(study_dic)
            i = 0
            study_list = []
            for study_name, study_used in study_dic.items():
                study_list.append(study_name)
                if study_used > 10:  # 第二次升级需要的材料数量
                    i += 1
                else:
                    return HttpResponse('材料不足，学习失败<br><a href="/recipe/{0}/">返回菜谱详细页</a>'.format(confirm_id))
            if i == study_dic_len:
                study_name_main = models.RecipeName.objects.filter(pk=confirm_id).first().name
                # 该在modesl中删除数据和增加食谱了，另外还要判断level的数量
                if len(study_list) == 2:
                    for x in range(10):
                        models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[1]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse('学习【{0}】成功，共耗费食材{1}10份 {2}10份<br><a href="/recipe/{3}/">返回菜谱详细页</a>'.format(study_name_main, study_list[0], study_list[1], confirm_id))
                elif len(study_list) == 3:
                    for x in range(10):
                        models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[1]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id, food_material__food_material=study_list[2]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse('学习【{0}】成功<br>共耗费食材:<br>{1}10份 <br>{2}10份 <br>{3}10份<br><a href="/recipe/{4}/">返回菜谱详细页</a>'.format(study_name_main, study_list[0], study_list[1], study_list[2], confirm_id))
                else:
                    pass

        elif level == '3':
            study_dic_len = len(study_dic)
            i = 0
            study_list = []
            for study_name, study_used in study_dic.items():
                study_list.append(study_name)
                if study_used > 30:
                    i += 1
                else:
                    return HttpResponse('材料不足，学习失败<br><a href="/recipe/{0}/">返回菜谱详细页</a>'.format(confirm_id))
            if i == study_dic_len:
                study_name_main = models.RecipeName.objects.filter(pk=confirm_id).first().name
                # 该在modesl中删除数据和增加食谱了，另外还要判断level的数量
                if len(study_list) == 2:
                    for x in range(30):
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[1]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse(
                        '学习【{0}】成功，共耗费食材{1}30份 {2}30份<br><a href="/recipe/{3}/">返回菜谱详细页</a>'.format(study_name_main, study_list[0], study_list[1], confirm_id))
                elif len(study_list) == 3:
                    for x in range(30):
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[1]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[2]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse(
                        '学习【{0}】成功<br>共耗费食材:<br>{1}30份 <br>{2}30份 <br>{3}30份<br><a href="/recipe/{4}/">返回菜谱详细页</a>'.format(
                            study_name_main, study_list[0], study_list[1], study_list[2], confirm_id))
                else:
                    pass

        elif level == '4':
            study_dic_len = len(study_dic)
            i = 0
            study_list = []
            for study_name, study_used in study_dic.items():
                study_list.append(study_name)
                if study_used > 50:
                    i += 1
                else:
                    return HttpResponse('材料不足，学习失败<br><a href="/recipe/{0}/">返回菜谱详细页</a>'.format(confirm_id))
            if i == study_dic_len:
                study_name_main = models.RecipeName.objects.filter(pk=confirm_id).first().name
                # 该在modesl中删除数据和增加食谱了，另外还要判断level的数量
                if len(study_list) == 2:
                    for x in range(50):
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[1]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse(
                        '学习【{0}】成功，共耗费食材{1}50份 {2}50份<br><a href="/recipe/{3}/">返回菜谱详细页</a>'.format(study_name_main, study_list[0], study_list[1], confirm_id))
                elif len(study_list) == 3:
                    for x in range(50):
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[1]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[2]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse(
                        '学习【{0}】成功<br>共耗费食材:<br>{1}50份 <br>{2}50份 <br>{3}1份<br><a href="/recipe/{4}/">返回菜谱详细页</a>'.format(
                            study_name_main, study_list[0], study_list[1], study_list[2], confirm_id))
                else:
                    pass

        elif level == '5':
            study_dic_len = len(study_dic)
            i = 0
            study_list = []
            for study_name, study_used in study_dic.items():
                study_list.append(study_name)
                if study_used > 80:
                    i += 1
                else:
                    return HttpResponse('材料不足，学习失败<br><a href="/recipe/{0}/">返回菜谱详细页</a>'.format(confirm_id))
            if i == study_dic_len:
                study_name_main = models.RecipeName.objects.filter(pk=confirm_id).first().name
                # 该在modesl中删除数据和增加食谱了，另外还要判断level的数量
                if len(study_list) == 2:
                    for x in range(80):
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[1]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse(
                        '学习【{0}】成功，共耗费食材{1}80份 {2}80份<br><a href="/recipe/{3}/">返回菜谱详细页</a>'.format(study_name_main, study_list[0], study_list[1], confirm_id))
                elif len(study_list) == 3:
                    for x in range(80):
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[0]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[1]).first().delete()
                        models.Ambry.objects.filter(user_id=user_id,
                                                    food_material__food_material=study_list[2]).first().delete()
                    models.UserRecipe(user_id=user_id, recipe_level_id=level_id).save()
                    return HttpResponse(
                        '学习【{0}】成功<br>共耗费食材:<br>{1}80份 <br>{2}80份 <br>{3}80份<br><a href="/recipe/{4}/">返回菜谱详细页</a>'.format(
                            study_name_main, study_list[0], study_list[1], study_list[2], confirm_id))
                else:
                    pass
        else:
            pass
    else:
        return redirect('/recipe_study/')

def my_recipe(request):
    level = request.GET.get('level')
    recipe_class_obj = models.RecipeClass.objects.all()
    user_id = request.session.get('user_id')
    study_all = models.UserRecipe.objects.filter(user_id=user_id).all()
    recipe_class_1 = []
    recipe_class_2 = []
    recipe_class_3 = []
    recipe_class_4 = []
    recipe_class_5 = []
    recipe_class_6 = []
    recipe_class_7 = []
    recipe_class_8 = []
    recipe_class_9 = []
    recipe_class_10 = []
    max_level_all = models.UserRecipe.objects.filter(user_id=user_id).values('recipe_level__recipe_name').annotate(Max('recipe_level__level'))
    study_id_list = []
    study_level_list = []
    for max_level in max_level_all:
        #print(max_level['recipe_level__recipe_name'])
        #print(max_level['recipe_level__level__max'])
        study_id_list.append(max_level['recipe_level__recipe_name'])
        study_level_list.append(max_level['recipe_level__level__max'])
    study_zip = zip(study_id_list, study_level_list)
    for study in study_zip:
        study_obj = models.RecipeLevel.objects.filter(level=study[1], recipe_name_id=study[0]).first()
        if study_obj.recipe_name.recipe_class_id == 1:
            recipe_class_1.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 2:
            recipe_class_2.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 3:
            recipe_class_3.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 4:
            recipe_class_4.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 5:
            recipe_class_5.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 6:
            recipe_class_6.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 7:
            recipe_class_7.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 8:
            recipe_class_8.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 9:
            recipe_class_9.append(study_obj)
        elif study_obj.recipe_name.recipe_class_id == 10:
            recipe_class_10.append(study_obj)
        else:
            pass
    return render(request, 'my_recipe.html', locals())

class Gift(View):
    def get(self, request):
        return render(request, 'gift.html')
    def post(self, request):
        return HttpResponse('礼包码有误')

def friend(request):
    user_obj = models.User.objects.all()
    return render(request, 'friend.html', locals())

def market(request):
    user_id = request.session.get('user_id')
    choice_list = models.ChoiceMarket.objects.all()
    buy = request.GET.get('buy')
    if buy:
        foodmaterial = models.ChoiceMarket.objects.filter(pk=int(buy)).first()
        price_1 = models.ChoiceMarket.objects.filter(pk=int(buy)).first().market_material.food_material_level_id
        user = models.User.objects.filter(pk=user_id).first()
        if user.coin >= price_1*price_1*5000:
            new_coin = user.coin - price_1*price_1*5000
            models.Ambry(user_id=user_id, food_material_id=foodmaterial.market_material_id).save()
            models.User.objects.filter(pk=user_id).update(coin=new_coin)
            return HttpResponse('购买{0}成功,共花费{1}金币，<br>剩余{2}金币<br><a href="/market/">返回菜场</a>'.format(foodmaterial.market_material.food_material, price_1*price_1*5000, new_coin))


    return render(request, 'market.html', locals())




def test_1(request):
    return render(request, 'test_1.html')
def test_2(request):
    return render(request, 'test_2.html')
def test_3(request):
    return render(request, 'test_3.html')
def home_address(request):
    address = request.GET.get('address')
    if address:
        user_id = request.session.get('user_id')
        models.User.objects.filter(pk=user_id).update(street=address)
        return HttpResponse('搬家成功,<a href="/index/">返回首页</a>')
    return render(request, 'home_address.html', locals())


