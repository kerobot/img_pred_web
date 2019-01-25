from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ImageForm
from .main import detect

class PredView(TemplateView):
   def __init__(self):
       self.params={'result_list': [],
                    'result_name': "",
                    'result_img': "",
                    'form': ImageForm()}

   def get(self, req):
       return render(req, 'idw/index.html', self.params)

   def post(self, req):
       form = ImageForm(req.POST, req.FILES)
       if not form.is_valid():
           raise ValueError('invalid form')

       image = form.cleaned_data['image']
       result = detect(image)
       self.params['result_list'], self.params['result_name'], self.params['result_img'] = result
       return render(req, 'idw/index.html', self.params)
