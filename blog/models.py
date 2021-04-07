from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=511, default='GIVE ME DESCRIPTION')
    content = models.TextField(default='Type something creative')
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' % self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments', default=0)
    author = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text
    class Meta:
        ordering = ('-date',)

