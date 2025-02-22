from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from postapp.dacorators import post_ownership_required
from postapp.forms import PostCreationForm
from postapp.models import Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'postapp/create.html'

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk':self.object.pk})



class PostDetailView(DetailView, FormMixin):
    model = Post
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'postapp/detail.html'


@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'target_post'
    form_class = PostCreationForm
    template_name = 'postapp/update.html'


    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk':self.object.pk})




@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'target_post'
    template_name = 'postapp/delete.html'
    success_url = reverse_lazy('postapp:list')


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'postapp/list.html'
    paginate_by = 10

def delete(request):
    print('실행!')
    print(request.GET['post'])
    Post.objects.filter(pk=request.GET['post']).delete()
    return JsonResponse(data={})


def delete_comment(request):
    print('실행!')
    print(request.GET['comment'])
    Comment.objects.filter(pk=request.GET['comment']).delete()
    return JsonResponse(data={})
