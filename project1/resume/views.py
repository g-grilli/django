from django.template.response import TemplateResponse
from django import forms
from django import http
from django.core.mail import send_mail

import datetime

def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})
# Create your views here.

def photos (request):
  return TemplateResponse(request, 'photos.html', {})
def food (request):
  return TemplateResponse(request, 'food.html', {})
def thanks (request):
  return TemplateResponse(request, 'thanks.html', {})


def contact (request):
  form  = NameForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      print(form.cleaned_data['first_name'])
      send_mail(
      	form.cleaned_data['first_name'],
      	form.cleaned_data['email'] + "\n\n" + form.cleaned_data['question'],
      	'gene@grilli.tech',
      	['gene@grilli.tech'],
      	fail_silently=False,
      	)
      return http.HttpResponseRedirect('/thanks')
    else:
    	print(form.errors)
  context = {'form': form}
  return TemplateResponse(request, 'contact.html', {})

class NameForm (forms.Form):
  first_name = forms.CharField(
    label='First name', max_length=100)
  last_name = forms.CharField(
    label='Last name', max_length=100)
  email = forms.CharField(
    label='Email', max_length=100)
  question = forms.CharField(
    label='Question', max_length=100)
