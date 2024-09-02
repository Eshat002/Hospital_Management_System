from django.db import models


blood_types = [
    ("A+ve", "A+ve"),
    ("A-ve", "A-ve"),
    ("B+ve", "B+ve"),
    ("B-ve", "B-ve"),
    ("AB+ve", "AB+ve"),
    ("AB-ve", "AB-ve"),
    ("O+ve", "O+ve"),
    ("O-ve", "O-ve"),
]

genders = [
    ("male", "Male"),
    ("female", "Female"),
]


class Patient(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()
    blood_group = models.CharField(choices=blood_types, max_length=10)
    gender = models.CharField(choices=genders, max_length=10, default="male")
    phone = models.PositiveIntegerField()
    email = models.EmailField()

    class Meta:
        ordering = ["-id"]

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Patient - {self.first_name} {self.last_name}"
