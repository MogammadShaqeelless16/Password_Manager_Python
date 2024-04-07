from django.db import models

    
class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    account_name = models.CharField(max_length=100)

    user_name = models.CharField(max_length=100)

    email = models.CharField(max_length=255)

    password = models.CharField(max_length=20)

    link = models.CharField(max_length=300)


    def __str__(self):

        return self.account_name
    















