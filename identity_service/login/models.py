from django.db import models

class Users(models.Model):
    """This class represents the users model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False, unique=True)

    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)