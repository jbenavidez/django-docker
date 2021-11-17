from django.db import models


class Portfolio(models.Model):
    name = models.TextField()
    description = models.TextField()
    img_url= models.TextField()


class Services(models.Model):
    name =  models.TextField()
    description = models.TextField()
    css_class= models.TextField()


class CompanyHistory(models.Model):
    name =   models.TextField()
    description = models.TextField()
    date = models.TextField()
    img_url = models.TextField()

class Team(models.Model):
    name =  models.TextField()
    title = models.TextField()
    img_url= models.TextField()