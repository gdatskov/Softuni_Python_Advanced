from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    seniority_level = models.CharField(
        max_length=30,
        choices=((x, x) for x in ("Junior", "Regular", "Senior"))
    )

    @property
    def details(self):
        return f"{self.first_name} { self.last_name } - Seniority: {self.seniority_level}"

    # def get_absolute_url(self):
    #     pass