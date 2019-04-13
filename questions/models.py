from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    '''
    Stores question asked by a user.
    The title explains the main question,
    the body gives more information about the title
    and the tags make it easier for searching and categorizing the question.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    body = models.CharField(max_length=30000)
    _tags = models.CharField(max_length=500)

    #returns list of _tags
    @property
    def tags(self):
        return [int(x.strip('[]')) for x in self._tags.split(',') if x.strip('[]')]

class Answer(models.Model):
    '''
    stores answers to questions given by each user
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=30000)

class Vote(models.Model):
    '''
    Stores upvotes/downvotes for an item like question, answer and comment.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    item = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="item")
    item_id = models.PositiveIntegerField()
    item_object = GenericForeignKey('item', 'item_id')

    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

class Comment(models.Model):
    '''
    Stores comments to a question/answer by a user
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    item = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="item")
    item_id = models.PositiveIntegerField()
    item_object = GenericForeignKey('item', 'item_id')

    comment = models.CharField(max_length=30000)
