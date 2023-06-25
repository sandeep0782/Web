from calendar import calendar
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import *


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'


class CalenderForm(ModelForm):
    class Meta:
        model = Calender
        fields = '__all__'

class SeasonForm(ModelForm):
    class Meta:
        model = Season
        fields = '__all__'

class DropForm(ModelForm):
    class Meta:
        model = Drop
        fields = '__all__'

class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'

class OTBForm(ModelForm):
    class Meta:
        model = OTB
        fields = '__all__'

class ATForm(ModelForm):
    class Meta:
        model = Article_Type
        fields = '__all__'
    
class AssortmentForm(ModelForm):
    class Meta:
        model = Assortment
        fields = ('assortment_date','season','drop','brand','article_type','gender','options','quantity','domimp','onoff','wwnww','order_type','inward_month','fabric_type','content1','content2','content3')
        

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class GenderForm(ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'

class TechpackForm(ModelForm):
    class Meta:
        model = Assortment
        fields = ('techpack',)