from django.db import models

# Create your models here.

# 食材等级表
class FoodMaterialLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='食材等级', max_length=12)
    class Meta:
        db_table = 'FoodMaterialLevel'

# 食材表
class FoodMaterial(models.Model):
    food_material = models.CharField(max_length=12)
    food_material_level = models.ForeignKey(FoodMaterialLevel, null=True)
    class Meta:
        db_table = 'FoodMaterial'

# 账户表
class Account(models.Model):
    username = models.CharField(verbose_name='账户', max_length=12)
    password = models.CharField(verbose_name='密码', max_length=12)
    email = models.EmailField(verbose_name='邮箱', null=True)
    phone = models.CharField(verbose_name='手机号', max_length=11, null=True)

    class Meta:
        db_table = 'Account'

# 玩家表
class User(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=12)
    energy = models.IntegerField(verbose_name='体力', )
    level = models.IntegerField(verbose_name='等级', )
    coin = models.IntegerField(verbose_name='金币', default=0)
    wing = models.IntegerField(verbose_name='元宝', default=0)
    street_choices = (
        (1, '湖南街'),
        (2, '广东街'),
        (3, '四川街'),
        (4, '福建街'),
        (5, '山东街'),
        (6, '浙江街'),
        (7, '江苏街'),
        (8, '安徽街'),
        (9, '情侣街'),
    )
    street = models.IntegerField(verbose_name='街道', choices=street_choices, null=True)
    account = models.ForeignKey(to='Account')
    class Meta:
        db_table = 'User'

# 个人橱柜表
class Ambry(models.Model):
    user = models.ForeignKey(to='User')
    food_material = models.ForeignKey(to='FoodMaterial')

    class Meta:
        db_table = 'Ambry'

# 物品表
class Prop(models.Model):
    name = models.CharField(verbose_name='道具名称', max_length=16)
    introdutions = models.CharField(verbose_name='道具介绍', max_length=128)
    price = models.IntegerField(verbose_name='价格')
    price_choices = (
        (1, '金币'),
        (2, '元宝'),
    )
    price_class = models.IntegerField(verbose_name='需要的货币', choices=price_choices)

    prop_level = models.ForeignKey(to='PropLevel')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Prop'

# 物品等级表
class PropLevel(models.Model):
    name = models.CharField(verbose_name='道具类别', max_length=16)
    class Meta:
        db_table = 'PropLevel'

# 个人仓库表
class Backpack(models.Model):
    user = models.ForeignKey(to='User')
    backpack_prop = models.ForeignKey(to='Prop')
    class Meta:
        db_table = 'Backpack'

# 个人菜谱表(多对多)
class UserRecipe(models.Model):
    user = models.ForeignKey(to='User')
    recipe_level = models.ForeignKey(to='RecipeLevel')
    class Meta:
        db_table = 'UserRecipe'

#
class RecipeMaterial(models.Model):
    level = models.ForeignKey(to='RecipeLevel', null=True)
    material = models.ForeignKey(to='FoodMaterial', null=True)
    class Meta:
        db_table = 'RecipeMaterial'

# 菜谱等级表
class RecipeLevel(models.Model):
    level_choices = (
        (1, '普通'),
        (2, '上品'),
        (3, '极品'),
        (4, '银牌'),
        (5, '金牌'),
    )
    level = models.IntegerField(verbose_name='菜谱等级', choices=level_choices)
    price = models.IntegerField(verbose_name='售价')
    oil_used = models.IntegerField(verbose_name='耗油量')
    experience = models.IntegerField(verbose_name='获得经验')
    recipe_name = models.ForeignKey(to='RecipeName')

    class Meta:
        db_table = 'RecipeLevel'

# 菜谱名称(一对多)
class RecipeName(models.Model):
    name = models.CharField(verbose_name='菜谱名称', max_length=16)
    introduce = models.CharField(verbose_name='详细做法', max_length=1024, null=True)
    recipe_class = models.ForeignKey(verbose_name='菜系', to='RecipeClass')
    class Meta:
        db_table = 'RecipeName'

# 菜系表(一对多)
class RecipeClass(models.Model):
    name = models.CharField(verbose_name='菜系名称', max_length=16)
    class Meta:
        db_table = 'RecipeClass'

'''
class RecipeStudy(models.Model):
    user = models.ForeignKey(to='User')
    study = models.ForeignKey(to='RecipeLevel')

    class Meta:
        db_table = 'RecipeStudy'
        '''

class ChoiceMarket(models.Model):
    test = models.IntegerField(default=1)
    market_material = models.ForeignKey(to='FoodMaterial')
    class Meta:
        db_table = 'ChoiceMarket'

class FoodMaterialLevelPrice(models.Model):
    price = models.IntegerField()
    food_material_level = models.ForeignKey(to='FoodMaterialLevel')

    class Meta:
        db_table = 'FoodMaterialLevelPrice'
