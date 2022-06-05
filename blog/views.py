from django.shortcuts import render
from . models import post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.




class postlistview(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2



class postdetailview(DetailView):
    model = post



class postcreateview(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)



class postupdateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post  = self.get_object()
        
        if self.request.user == post.author:
            return True
        return False




class postdeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post 
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')