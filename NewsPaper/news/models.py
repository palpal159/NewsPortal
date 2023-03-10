from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    rating_author = models.FloatField(default=0.0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        self.rating_author = 0
        posts = Post.objects.filter(author=self)
        for post in posts:
            self.rating_author += post.rating_post * 3
            comments = Comment.objects.filter(post=post)
            for comment in comments:
                self.rating_author += comment.rating_comment
            own_comments = Comment.objects.filter(user=self.user)
            for own_comment in own_comments:
                self.rating_author += own_comment.rating_comment

        self.save()

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    NEWS = 'NE'
    ARTICLE = 'AR'
    POST = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    ]
    post = models.CharField(max_length=2, choices=POST, default=NEWS)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    header_post = models.CharField(max_length=255)
    text_post = models.TextField()
    category = models.ManyToManyField(Category, through='PostCategory')
    post_date = models.DateTimeField(auto_now_add=True)
    rating_post = models.FloatField(default=0.0)

    def like_post(self):
        self.rating_post += 1
        self.save()

    def dislike_post(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[:144] + '...'

    def __str__(self):
        return self.header_post

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_text = models.TextField(default="Текст комментария")
    comment_date = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like_comment(self):
        self.rating_comment += 1
        self.save()

    def dislike_comment(self):
        self.rating_comment -= 1
        self.save()





