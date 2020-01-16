import stripe
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, UserStripe
from django.contrib.auth.signals import user_logged_in
from orders.models import Order
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRETE_KEY


def get_or_create_stripe(sender, user, *args, **kwargs):
    try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
            email=str(user.email)
        )
        new_user_stripe = UserStripe.objects.create(
            user=user,
            stripe_id=customer.id
        )
    except:
        pass


user_logged_in.connect(get_or_create_stripe)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

