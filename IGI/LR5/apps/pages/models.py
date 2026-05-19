from django.db import models

class AboutCompany(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    history = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.question

class EmployeeContact(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='employees/', blank=True, null=True)

    def str(self):
        return self.full_name


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title