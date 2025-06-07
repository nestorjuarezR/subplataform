from django.db import models
from account.models import CustomUser



class Subscription(models.Model):
    subscriber_name = models.CharField(max_length=300)
    subscription_plan = models.CharField(max_length=255)
    subscription_cost = models.CharField(max_length=255)
    paypal_susbscription = models.CharField(max_length=300)
    is_activate = models.BooleanField(default=False)
    user = models.OneToOneField(CustomUser, max_length=10, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.subscriber_name} - {self.subscription_plan} - {self.subscription_cost} - {self.paypal_susbscription} - {self.is_activate}"
