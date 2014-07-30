from django.db import models
from django.utils.encoding import smart_text
from django.forms import ModelForm

# Create your models here.

class SignUp(models.Model):
    _id = models.CharField(max_length= 120, null = False, blank = False)
    _email = models.EmailField()
    _pw = models.CharField(max_length= 120, null = False, blank = False)

    def __unicode__(self):
        return smart_text(self._id)

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ['_id', '_email', '_pw']


#class