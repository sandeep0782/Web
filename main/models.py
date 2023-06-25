from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)


class Gender(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Ok #
class Article_Type(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #

class Width(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Ok #
class Buyer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Ok #
class Drop(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #

# Ok #
class Department(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #

# Ok #
class Designation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #


# Ok #
class Domimp(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #


class Fabric_Type(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Onoff(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Order_Type(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Wwnww(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Ok #
class Activity(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    department_name = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #

# Ok #
class Calender(models.Model):
    activity_name = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.activity_name
    # Ok #

# Ok #
class Assortment(models.Model):
    options = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    inward_month = models.CharField(max_length=100, null=True, blank=True)
    content1 = models.CharField(max_length=100, null=True, blank=True)
    content2 = models.CharField(max_length=100, null=True, blank=True)
    content3 = models.CharField(max_length=100, null=True, blank=True)
    article_type = models.ForeignKey(Article_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    brand = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    domimp = models.ForeignKey(Domimp, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    fabric_type = models.ForeignKey(Fabric_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, null=True, blank=True)
    onoff = models.ForeignKey(Onoff, on_delete=models.DO_NOTHING, null=True, blank=True)
    order_type = models.ForeignKey(Order_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    wwnww = models.ForeignKey(Wwnww, on_delete=models.DO_NOTHING, null=True, blank=True)
    assortment_date = models.DateField(null=True, blank=True)
    techpack = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.options
    # Ok #


class Travel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class OTB(models.Model):
    brand = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    article_type = models.ForeignKey(Article_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    otb_value = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Project_created_by')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Project_updated_by')
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Order_Management(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)