from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length = 30)
    emailID = models.EmailField(max_length = 30)
    desc = models.TextField(max_length = 50)
    phone = models.IntegerField() 

    def __str__(self):
        return self.name
    

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default=' ')
    sub_category = models.CharField(max_length=100, default=' ')
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length = 500)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name


class orders(models.Model):
    oid = models.AutoField
    item_json = models.CharField(max_length = 300)
    amount = models.IntegerField()
    name = models.CharField(max_length = 300)
    address1 = models.TextField(max_length = 300)
    address2 = models.TextField(max_length = 300)
    city = models.CharField(max_length = 300)
    state = models.CharField(max_length = 300)
    zipcode = models.IntegerField()
    paymentdetails = models.IntegerField()
    phonenumber = models.IntegerField()

    def _str_(self):
        return self.name
    
class orderupdate(models.Model):
    updateID = models.AutoField
    oid = models.IntegerField()
    update_desc = models.CharField(max_length = 300)
    delivered = models.BooleanField()
    timestamp = models.DateField()

    def _str_(self):
        return self.oid