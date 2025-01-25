from django.db import models


# Create your models here.
class Chicken(models.Model):
    name=models.CharField(max_length=50)
    age= models.IntegerField()
    breed= models.CharField(max_length=50)
    health_status=models.CharField(max_length=50)

class Egg(models.Model):
    quantity=models.IntegerField()
    date_collected=models.DateField()
    chicken=models.ForeignKey(Chicken, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.quantity) + "eggs collected" + str(self.date_collected) + " given by "+ self.chicken.name

