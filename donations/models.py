from django.db import models
from django.db.models import Sum
from django.conf import settings


from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    original_bag = models.TextField(null=False, blank=False, default='')
    total = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=False,
                                default=0)
    stripe_pid = models.CharField(max_length=254,
                                  null=False,
                                  blank=False,
                                  default='')

    def __str__(self):
        return self.full_name

    def update_total(self):
        """
        Update total each time a line item is added,
        accounting for delivery costs.
        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()
