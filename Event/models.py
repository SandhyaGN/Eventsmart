from django.db import models

# Create your models here.
class Events(models.Model):
    event_name= models.CharField(max_length=100,default='',null=False)
    date= models.DateField(default='',null=False)
    time= models.TimeField()
    location= models.CharField(max_length=100,default='',null=False)
    image= models.ImageField(upload_to='static/%y')
    is_liked= models.BooleanField(default=False)

    def __str__(self):
        return self.event_name+"\n"+ str(self.date)+"\n"+ str(self.time) +"\n"+self.location