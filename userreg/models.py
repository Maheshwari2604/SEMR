from django.db import models

# Create your models here.


class register_model(models.Model):
    Name = models.CharField(max_length=250, help_text='Required')
    email = models.EmailField(max_length=250, help_text='Required')
    slug = models.SlugField(unique=True, null=True)
    password = models.CharField(max_length=100)
    Confirm_password = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['firstname', 'lastname']

    '''def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})'''

    def __str__(self):
        return str(self.id)


class address(models.Model):
    user = models.ForeignKey(register_model, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    service_area = models.CharField(max_length=100)
    local_address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=120, null=True)
    pin = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):  
        return str(self.user)

