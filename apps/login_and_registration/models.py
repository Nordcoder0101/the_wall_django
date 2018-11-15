from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def basic_validation(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        filter_to_check_for_unique_email = User.objects.filter(email = postData['email'])

        if len(postData['first_name']) < 2:
            errors['first_name'] = "Please provide a valid first name"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Please provide a valid last name"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please provide a valid email"
        if len(filter_to_check_for_unique_email) > 0:
            errors['email_not_unique'] = "Email already in use, try again"
        if not postData['password'] == postData['vpassword']:
            errors['password'] = "Passwords do not match"
        return errors
    
    def login_validation(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if len(user) == 0:
            errors['email_validate'] = "Invalid login Information"
        if bcrypt.checkpw(postData['password'].encode(), user[0].p_hash.encode()):
            return errors
        else:
            errors['email_validate'] = "Invalid login Information"
        return errors

class User(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  p_hash = models.CharField(max_length=90)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
