from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name # This will display the first name of the user in the admin panel
        return self.last_name # This will display the last name of the user in the admin panel
        return self.email # This will display the email of the user in the admin panel
        return self.password # This will display the password of the user in the admin panel