from django.db import models

# Create blog models here.
# add blog app to the settings
#create a migrations
#migrate
#add to the admin

class Blog(models.Model):
    #title
    title=models.CharField(max_length=255)
    #data
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self): #to change the name of the blog in database
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')