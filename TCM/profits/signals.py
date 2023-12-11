from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profit
from sales.models import Sales

@receiver(post_save, sender=Sales)
def create_profit(sender, instance, created, **kwargs):
    print(f"Created: {created}, Completed: {instance.completed}")
    if created:
        print("Creating Profit...")
        Profit.objects.create(
            quantity=instance.amount * instance.service.price,
            date=instance.date,
            fk_sale=instance
        )