from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order

from .helpers import send_email
from .models import Robot


@receiver(post_save, sender=Robot)
def create_new_robot(sender, instance, created, **kwargs):
    if created:
        unique_robot = Robot.objects.filter(serial=instance.serial).count()
        if unique_robot == 1:
            orders = Order.objects.all()
            for order in orders:
                if order.robot_serial == instance.serial:
                    send_email(
                        to_email=order.customer.email,
                        model=order.robot_serial[:2],
                        version=order.robot_serial[-2:],
                    )
