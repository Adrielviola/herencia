from .models import Notebook
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class NotebooksListView(ListView):
    model = Notebook
    template_name = "app/class_list.html"

class NotebooksDetailView(DetailView):
    model = Notebook
    template_name = "app/class_detail.html"

class NotebooksCreateView(CreateView):
    model = Notebook
    success_url = "app/Notebook_create.html"
    fields = ["marca" , "modelo"]

class NotebooksUpdateView(UpdateView):
    model = Notebook
    success_url = "app/Notebook_update.html"
    fields = ["marca"]

class NotebooksDeleteView(DeleteView):
    model = Notebook
    success_url = "app/Notebook_update.html"


