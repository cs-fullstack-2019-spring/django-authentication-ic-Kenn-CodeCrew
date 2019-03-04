from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# ID number, state, and issuedDate
class DMVModel(models.Model):
    IDNumber = models.CharField(max_length=200, default="")
    stateAbbr = models.CharField(max_length=2, default="")
    issueDate = models.DateField(default = "")
    userTableForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "ID number is: " + self.IDNumber
