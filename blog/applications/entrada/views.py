from django.views.generic import ListView, DetailView

from applications.entrada.models import Entry
from applications.entrada.models import Category


class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context
    
    
    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        categoria = self.request.GET.get('categoria', '')
        # consulta de busquedad
        resultado = Entry.objects.buscar_entradas(kword, categoria)
        return resultado
    

class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"
