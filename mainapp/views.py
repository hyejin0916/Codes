from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from commentapp.models import Comment
from mainapp.forms import AccountUpdateForm
from postapp.models import Post
from upracticeapp.models import Upractice
from practiceapp.models import Presult


def main_page(request):
    return render(request, 'mainapp/mainpage.html')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('mainapp:mainpage')
    template_name = 'mainapp/signup.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'mainapp/detail.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(writer=self.get_object())
        object_list = object_list[::-1]
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('mainapp:mainpage')
    template_name = 'mainapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('mainapp:login')
    template_name = 'mainapp/delete.html'


def practice_result(request,pk):
    print(pk)
    print(type(pk))
    user = User.objects.get(pk=pk)
    print(user)
    result_list = Presult.objects.filter(user_id=user.pk)
    print(result_list)
    context = {'user': user, 'result_list': result_list}
    return render(request, 'mainapp/user_result.html', context)

def page_not_found(request, exception):
    """
    404 Page not found
    """
    print(exception)
    return render(request, 'error/404.html', {})