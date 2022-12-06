from django.db import models

# Create your models here.

class Machine(models.Model):
	machine_no=models.CharField(max_length=100)



class Process(models.Model):
	machine=models.ForeignKey(Machine,null=True,blank=True,on_delete=models.CASCADE)
	process_name=models.CharField(null=True,blank=True,max_length=100)


class Productdetail(models.Model):
	machine=models.ForeignKey(Machine,null=True,blank=True,on_delete=models.CASCADE)
	process=models.ForeignKey(Process,null=True,blank=True,on_delete=models.CASCADE)
	name=models.CharField(null=True,blank=True,max_length=100)
	starttime=models.CharField(null=True,blank=True,max_length=100)
	endtime=models.CharField(null=True,blank=True,max_length=100)
	cycletime=models.CharField(null=True,blank=True,max_length=100)
	width=models.IntegerField(null=True,blank=True)
	thickness=models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=5)
	weight=models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=5)
