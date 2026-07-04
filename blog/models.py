from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Destination(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def likes(self):
        return self.votes.filter(vote_type='like').count()

    @property
    def dislikes(self):
        return self.votes.filter(vote_type='dislike').count()


class Vote(models.Model):
    VOTE_CHOICES = [('like', 'Like'), ('dislike', 'Dislike')]
    destination = models.ForeignKey(Destination, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=10, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('destination', 'user')


class Comment(models.Model):
    destination = models.ForeignKey(Destination, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.user.username}: {self.body[:30]}'
