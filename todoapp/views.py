from pyexpat import model
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, DetailView, DeleteView, CreateView, View
from todoapp.forms import TodoItemForm
from todoapp.models import TodoItemModel


# Create your views here.


# class TodoAppHomeView(TemplateView):
#     template_name = 'todoapp/todoapp.html'


# class TodoCreateView(CreateView):
#     template_name = 'todoapp/todo_create.html'
#     form_class = TodoItemForm
#     success_url = "/todoapp/create/"


class TodoUpdateView(UpdateView):
    template_name = 'todoapp/todo_update.html'
    model = TodoItemModel
    fields = ['title','is_completed']
    success_url = '/todoapp/list/'


class TodoListView(ListView):
    template_name = 'todoapp/todo_list.html'
    model = TodoItemModel

class TodoDetailView(DetailView):
    template_name = 'todoapp/todo_detail.html'
    model = TodoItemModel


class TodoDeleteView(DeleteView):
    model = TodoItemModel
    success_url = '/todoapp/list/'


class TodoAppHomeView(View):
    def get(self, request):
        template_name = 'todoapp/todoapp.html'
        context = {'title':"TodoApp"}
        return render(request,template_name,context=context)


class TodoCreateView(View):
    template_name = 'todoapp/todo_create.html'
    form_class = TodoItemForm

    context = {
        'title':'Todo',
        'form':form_class,
        'form_btn_text' : "Create"
        }

    def get(self, request):
        self.context['title'] = "Todo | Create"
        return render(request,self.template_name,context=self.context)
    
    def post(self, request):
        
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.valid_form(request, form)
        else:
            return self.invalid_form(request)

    def valid_form(self, request, form):
        """
        
        """
        form.save()
        return render(request,self.template_name,context=self.context)

    def invalid_form(self, request):
        """
        
        """
        return render(request,self.template_name,context=self.context)

