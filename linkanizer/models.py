from django.db import models, transaction
from django.db.models import F, Max
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from uuid import uuid4


# Special thanks to https://www.revsys.com/tidbits/keeping-django-model-objects-ordered/
class ListManager(models.Manager):
    def move(self, obj, new_order):
        qs = self.get_queryset()

        current_order = obj.order
        new_order = int(new_order)

        with transaction.atomic():
            if new_order < current_order:
                qs.filter(
                    owner=obj.owner, order__lt=current_order, order__gte=new_order
                ).exclude(pk=obj.pk).update(order=F("order") + 1)
            else:
                qs.filter(
                    owner=obj.owner, order__lte=new_order, order__gt=current_order,
                ).exclude(pk=obj.pk).update(order=F("order") - 1)

            obj.order = new_order
            obj.save()

    def create(self, **kwargs):
        instance = self.model(**kwargs)

        with transaction.atomic():
            # Get the current max order number
            results = self.filter(owner=instance.owner).aggregate(Max("order"))

            # Increment and use for new object
            current_order = results["order__max"]
            if current_order is None:
                current_order = 0

            value = current_order + 1
            instance.order = value
            instance.save()

            return instance


class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = AutoCreatedField()
    modified = AutoLastModifiedField()

    name = models.CharField(max_length=128)

    owner = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="lists"
    )

    order = models.IntegerField(default=1)

    objects = ListManager()

    def __str__(self):
        return f"<List - {self.name}>"


# Special thanks to https://www.revsys.com/tidbits/keeping-django-model-objects-ordered/
class LinkManager(models.Manager):
    def move(self, obj, new_order):
        qs = self.get_queryset()

        current_order = obj.order
        new_order = int(new_order)

        with transaction.atomic():
            if new_order < current_order:
                qs.filter(
                    list=obj.list, order__lt=current_order, order__gte=new_order
                ).exclude(pk=obj.pk).update(order=F("order") + 1)
            else:
                qs.filter(
                    list=obj.list, order__lte=new_order, order__gt=current_order,
                ).exclude(pk=obj.pk).update(order=F("order") - 1)

            obj.order = new_order
            obj.save()

    def create(self, **kwargs):
        instance = self.model(**kwargs)

        with transaction.atomic():
            # Get the current max order number
            results = self.filter(list=instance.list).aggregate(Max("order"))

            # Increment and use for new object
            current_order = results["order__max"]
            if current_order is None:
                current_order = 0

            value = current_order + 1
            instance.order = value
            instance.save()

            return instance


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = AutoCreatedField()
    modified = AutoLastModifiedField()

    title = models.CharField(max_length=128)
    url = models.URLField()

    order = models.IntegerField(default=1)

    objects = LinkManager()

    owner = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="links"
    )

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="links")

    class Meta:
        ordering = ("order",)
        index_together = ("list", "order")

    def __str__(self):
        return f"<Link - {self.title}>"
