from django.db import models
class Products(models.Model):
	image=models.ImageField(upload_to='owner/images/')
	title=models.CharField(max_length=50)
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
class Comment(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

   