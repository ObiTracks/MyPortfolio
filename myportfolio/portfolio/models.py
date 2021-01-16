from django.db import models

class IntroContent(models.Model):
    salutation = models.CharField(max_length=2500, null=False, blank=False, unique=False)
    title = models.CharField(max_length=2500, null=False, blank=False, unique=False)
    about =  models.TextField(max_length=2500, null=True, blank=True, unique=False)
    email = models.CharField(max_length=2500, null=True, blank=True, unique=False)
    btn1link = models.CharField(max_length=2500, null=True, blank=True, unique=False)
    btn2link = models.CharField(max_length=2500, null=True, blank=True, unique=False)
    btn3link = models.CharField(max_length=2500, null=True, blank=True, unique=False)
    profile_image = models.ImageField()


class Tag(models.Model):
    tag_title = models.CharField(max_length=2500, null=False, blank=False, unique=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Tag:{}".format(self.tag_title)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, unique=False, blank=False)
    desc = models.TextField(max_length=2500, null=True, blank=True, unique=False)
    desc_short = models.TextField(max_length=1500, null=True, blank=True, unique=False)
    desc_design = models.TextField(max_length=2500, null=True, blank=True, unique=False)
    # Details
    client = models.CharField(max_length=100, null=True, blank=True, unique=False)
    date = models.CharField(max_length=100, null=True, blank=True, unique=False)
    basedin = models.CharField(max_length=100, null=True, blank=True, unique=False)
    website = models.CharField(max_length=500, null=True, blank=True, unique=False)
    github = models.CharField(max_length=500, null=True, blank=True, unique=False)
    #Tags
    tags = models.ManyToManyField(Tag)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return "Project: {}".format(self.name)

def get_image_filename(instance, filename):
    id = instance.project.id
    return "post_images/%s" % (id)  
    
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, related_name="image_set")
    # image = models.FileField(upload_to='images/', verbose_name='Image')
    image = models.FileField(upload_to='media/images', verbose_name='Image')
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return "Image: {}".format(self.image.name)


