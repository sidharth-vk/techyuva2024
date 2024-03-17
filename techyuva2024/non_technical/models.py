from django.db import models
from ckeditor.fields import RichTextField 
from django.utils.text import slugify
import uuid
import random
import string





# Create your models here.
class non_tech_event(models.Model):

    

    
    
    name = models.CharField(("Event Name"), max_length=250)
    img = models.ImageField(("banner 500 * 341"), upload_to='event/banner')
    dec = RichTextField()
    fc = models.CharField(("Faculty Cordinator"), max_length=50)
    fcph = models.CharField(("Faculty Cordinator Phono"), max_length=50)
    ec1 = models.CharField(("Event Cordinator 1"), max_length=50)
    ec1ph = models.CharField(("Event Cordinator 1 phone number"), max_length=50)
    ec2= models.CharField(("Event Cordinator 2"), max_length=50)
    ec2ph= models.CharField(("Event Cordinator 2 phono number"), max_length=50)
    venue = models.CharField(("Venue"), max_length=50)
    ef = models.CharField(("Entry Fee"), max_length=50)
    prize1st = models.CharField(("Price 1st"), max_length=50)
    prize2nd = models.CharField(("Price 2nd"), max_length=50)
    slug = models.SlugField(max_length=400, unique=True,blank=True)


    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    



def generate_unique_id():
    prefix = 'suiet-'
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return prefix + suffix

def generate_unique_id_with_check():
        unique_id = generate_unique_id()
        while non_tech_event_register.objects.filter(id=unique_id).exists():
            unique_id = generate_unique_id()
        return unique_id


class non_tech_event_register(models.Model):
    id = models.CharField(primary_key=True, max_length=12, default=generate_unique_id_with_check, editable=False)
    name = models.CharField(("Name"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    ph = models.CharField(("Phone number"), max_length=250)
    collegename = models.CharField(("College Name"), max_length=250)
    usn = models.CharField(("USN"), max_length=250)
    event = models.ForeignKey("non_tech_event", verbose_name=("Event Name"), on_delete=models.SET_NULL, null=True)
    paymentproof = models.ImageField(("Payment Proof"), upload_to='event/PaymentProof')

    slug = models.SlugField(max_length=400, unique=True,blank=True)



    

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_unique_id_with_check()
        if not self.slug:
            self.slug = slugify(self.id)
        
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
