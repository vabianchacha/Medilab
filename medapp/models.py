from django.db import models

# Create your models here.
class patient(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    massage = models.TextField()


    def __str__(self):
        return self.full_name



class doctor(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField()
    status =models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=50)


    def __str__(self):
        return self.name



class staff(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=10)
    email = models.EmailField()
    hire_date = models.DateField()

    def __str__(self):
        return self.firstname
        return self.lastname


class ward(models.Model):
    name = models.CharField(max_length=50)
    totalbeds = models.IntegerField()
    availablebeds = models.IntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()


    def __str__(self):
        return self.name

