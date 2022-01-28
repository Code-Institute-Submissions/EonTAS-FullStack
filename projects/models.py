from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    class  Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.friendly_name

class Project(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    name = models.CharField(max_length=254)
    description = models.TextField()
    
    price = models.DecimalField(max_digits=6, decimal_places=2)

    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)

    image = models.ImageField(null=True, blank=True, upload_to="media/submitted")

    suggester = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    payed_for = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    item = models.ForeignKey('Project', null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length=30)
    body = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment "{self.body}" by {self.owner}'
        
class Update(models.Model): #associated with account, account views all they have funded + able to see updates specifically for those ones in a special view
    project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.SET_NULL)

    header = models.CharField(max_length=30)
    body = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    #def __new__(self):
        #project.commission.user.sendemail()
        #send email

    def __str__(self):
        return f'{self.project} update {self.created_on}'