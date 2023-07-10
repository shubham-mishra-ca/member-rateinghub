
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader



def index_view(request):
  template = loader.get_template('template.html')
  context = {

  }

  return HttpResponse(template.render(context, request))

def delete_view(request, id):

  # The reverse function looks up the available urls.
  return HttpResponseRedirect(reverse('index'))


def update_view(request, id):
  # need to create a new view to obtain the update data
  template = loader.get_template('template.html')
  context = {

  }
  return HttpResponse(template.render(context, request))
  
def update(request, id):
  name = request.POST['name']
  rating = request.POST['rating']
  
  return HttpResponseRedirect(reverse('index'))

# For practice and capstone tasks
def reg_view(request):
  template = loader.get_template('register.html')
  
  context = {
    
  }
  if request.POST:
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    uid = request.POST['uid']
    
  return HttpResponse(template.render(context, request))