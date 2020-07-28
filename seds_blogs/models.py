from django.db import models

# Create your models here.

class categories(models.Model):
    categories=models.CharField(max_length=300)

    def __str__(self):
        return self.categories


class blog(models.Model):
    title=models.CharField(max_length=300)
    summary=models.TextField(default="summary mostly 200-250 words")
    img_link=models.CharField(max_length=300)
    blog_link=models.CharField(max_length=300)
    categories=models.ForeignKey(categories,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Trending_blog(models.Model):
    title=models.CharField(max_length=300,unique=True)
    summary=models.TextField(default="summary mostly 200-250 words")
    img_link=models.CharField(max_length=300)
    blog_link=models.CharField(max_length=300,unique=True)
    author=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class video_categories(models.Model):
    video_categories=models.CharField(max_length=300)

    def __str__(self):
        return self.video_categories


class vlog(models.Model):
    title=models.CharField(max_length=200)
    summary=models.TextField()
    link_video=models.CharField(max_length=350)
    video_categories=models.ForeignKey(video_categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class vlog_trending(models.Model):
    title=models.CharField(max_length=200)
    summary=models.TextField()
    link_video=models.CharField(max_length=350)


class Astrophotography_trending(models.Model):
    Astrophotography_link=models.CharField(max_length=400)


class categories_Astrophotography(models.Model):
    categories=models.CharField(max_length=150)

    def __str__(self):
        return self.categories

class Astrophotography(models.Model):
    title=models.CharField(max_length=150)
    Astrophotography_link=models.CharField(max_length=400)
    summary=models.TextField(max_length=350,default='350 words max ')
    date=models.DateField()
    categories=models.ForeignKey(categories_Astrophotography,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
