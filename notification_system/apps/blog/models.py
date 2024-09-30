from django.db import models
from apps.account.models import Account


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Jańalıq'
        verbose_name_plural = "Jańalıqlar"



class Follow(models.Model):
    follower = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="follower"
    )
    following = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="following"
    )

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} follows {self.following}'
