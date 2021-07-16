
from django.forms import ModelForm
from .models import Cars
from ckeditor.fields import RichTextField

class CarForm(ModelForm):
	class Meta:
		model = Cars
		fields = '__all__'
