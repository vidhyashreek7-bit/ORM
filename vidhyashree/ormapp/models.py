from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
    Car_Name=models.CharField(max_length=40)
    Number_plate=models.CharField(primary_key=True)
    Car_color=models.CharField(max_length=30) 
    Car_model=models.IntegerField()
    Car_capacity=models.IntegerField()
class Car_DBAdmin(admin.ModelAdmin):
    list_display=["Car_Name","Number_plate","Car_color","Car_model","Car_capacity"]
