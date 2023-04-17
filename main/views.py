from django.shortcuts import render
from .models import Ipl
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse

# Create your views here.
def index(request):
    teams = Ipl.objects.filter().all()
    context = {'teams' : teams}
    return render(request,"index.html", context)



class AuthorCreateView(CreateView):
    model = Ipl
    template_name = "create.html"
    fields = ["team_name","wins", "losses"]
    success_url =  "/"
    # def get_success_url(self):
    #     return reverse('index')


class AuthorUpdateView(UpdateView):
    model = Ipl
    template_name = "create.html"
    template_name_suffix = "_update_form"
    fields = ["team_name","wins", "losses"]
    success_url =  "/"
    

class AuthorDeleteView(DeleteView):
    model = Ipl
    template_name = "delete.html"
    success_url =  "/"