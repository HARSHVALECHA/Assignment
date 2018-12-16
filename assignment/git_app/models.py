from django.db import models
import datetime
# Create your models here.
class github(models.Model):
    login= models.CharField(max_length=42)
    id= models.IntegerField(primary_key=True)
    node_id= models.CharField(max_length=42)
    date = models.DateField(("Date"), default=datetime.date.today)
    avatar_url= models.URLField(max_length=200, null=True, blank=True)
    gravatar_id= models.URLField(max_length=200, null=True, blank=True)
    url= models.URLField(max_length=200, null=True, blank=True)
    html_url= models.URLField(max_length=200, null=True, blank=True)
    followers_url= models.URLField(max_length=200, null=True, blank=True)
    following_url= models.URLField(max_length=200, null=True, blank=True)
    gists_url= models.URLField(max_length=200, null=True, blank=True)
    starred_url= models.URLField(max_length=200, null=True, blank=True)
    subscriptions_url= models.URLField(max_length=200, null=True, blank=True)
    organizations_url= models.URLField(max_length=200, null=True, blank=True)
    repos_url= models.URLField(max_length=200, null=True, blank=True)
    events_url= models.URLField(max_length=200, null=True, blank=True)
    received_events_url= models.URLField(max_length=200, null=True, blank=True)
    type= models.CharField(max_length=42)
    site_admin= models.CharField(max_length=42)
    score= models.IntegerField(default=0)
    image= models.FileField(upload_to='images',blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'git_data'