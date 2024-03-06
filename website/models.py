from django.db import models

class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)
    partner_name = models.CharField(max_length=50)
    hours_worked1_partner_user = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    hours_worked_main_user = models.IntegerField()
    number_of_spots = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    number_of_boitier = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    raccordement = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    description = models.TextField(max_length=500, default='N/A')
    observation = models.TextField(max_length=500, default='N/A')


    def __str__(self):
        return(f"{self.user_name} {self.created_at}")
    

class Customer(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return(f"{self.company} {self.title}")
    

class Product(models.Model):
    item = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    description = models.TextField(max_length=200)


