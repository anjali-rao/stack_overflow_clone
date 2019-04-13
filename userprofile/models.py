from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class UserReputation(models.Model):
    '''
    Stores User reputation counter which gets incremented for
    every question and upvoted answer
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reputation = models.IntegerField()

class ReadItems(models.Model):
    '''
    Marks an item as read by a particular user.
    The item can be a question, answer or a comment.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    r_item = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="r_item")
    item_id = models.PositiveIntegerField()
    item_object = GenericForeignKey('r_item', 'item_id')

    read_status = models.BooleanField(default=False)

class Favorites(models.Model):
    '''
    Marks any item as item as favorite for a given user.
    The item can be a question, answer or a comment.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    f_item = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="f_item")
    item_id = models.PositiveIntegerField()
    item_object = GenericForeignKey('f_item', 'item_id')

    fav_status = models.BooleanField(default=False)
