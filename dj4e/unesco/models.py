from django.db import models

# Create your models here.
class Category(models.Model) :
	name = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self) :
		return self.name


class States(models.Model) :
	name = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self) :
		return self.name


class Region(models.Model) :
	name = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self) :
		return self.name

class ISO(models.Model) :
	name = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self) :
		return self.iso

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)
    justification = models.CharField(max_length=10000)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    states = models.ForeignKey(States, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    iso = models.ForeignKey(ISO, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self) :
        return self.name