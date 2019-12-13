from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from uuid import uuid4


class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = AutoCreatedField()
    modified = AutoLastModifiedField()

    name = models.CharField(max_length=128)

    owner = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="lists"
    )

    def __str__(self):
        return f"<List - {self.name}>"


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = AutoCreatedField()
    modified = AutoLastModifiedField()

    title = models.CharField(max_length=128)
    url = models.URLField()

    owner = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="links"
    )

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f"<Link - {self.title}>"
