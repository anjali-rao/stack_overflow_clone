from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Question(models.Model):
    '''
    Stores question asked by a user.
    The title explains the main question,
    the body gives more information about the title
    and the tags make it easier for searching and categorizing the question.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    body = models.TextField()
    _tags = models.TextField()

    #returns list of _tags
    @property
    def tags(self):
        return [x.strip('[]') for x in self._tags.split(',') if x.strip('[]')]

class Answer(models.Model):
    '''
    stores answers to questions given by each user
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

class Vote(models.Model):
    '''
    Stores upvotes/downvotes for an item like question, answer and comment.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    v_item = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="v_item")
    item_id = models.PositiveIntegerField()
    item_object = GenericForeignKey('v_item', 'item_id')

    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

class Comment(models.Model):
    '''
    Stores comments to a question/answer by a user
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    c_item = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="c_item")
    item_id = models.PositiveIntegerField()
    item_object = GenericForeignKey('c_item', 'item_id')

    comment = models.TextField()
