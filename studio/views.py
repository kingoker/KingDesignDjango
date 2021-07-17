from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProneNumberForm
from django.contrib.auth import login, logout

from .models import Project, Author


# Отображение проектов
class ProjectView(ListView):
    model = Project
    queryset = Project.objects.filter(publicate=True)
    template_name = "studio/portfolio.html"


# Полное отображение проектов
class ProjectDetailView(DetailView):
    model = Project
    slug_field = "url"
    template_name = "studio/project-detail.html"


# Главная страница
class MainPageView(ListView):
    model = Project
    queryset = Project.objects.order_by('-id')
    template_name = "studio/index.html"


# Список услуг
def services(request):
    error = ''
    success = ''
    if request.method == 'POST':
        form = ProneNumberForm(request.POST)
        if form.is_valid():
            form.save()
            success = 'Спасибо, мы скоро позвоним'
        else:
            error = 'Телефон не верный =('

    form = ProneNumberForm()

    date = {
        'form': form,
        'error': error,
        'success': success,
    }

    return render(request, 'studio/services.html', date)


# Студия
class StudioView(ListView):
    model = Project
    queryset = Project.objects.order_by('-id')
    template_name = "studio/studio.html"


# Поиск проектов
def Search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        project_list = Project.objects.filter(title__icontains=searched)
        return render(request, 'studio/search.html', {'searched': searched, 'project_list': project_list})
    else:
        return render(request, 'studio/search.html', {})


class SignInView(ListView):
    model = Project
    queryset = Project.objects.order_by('-id')
    template_name = "studio/signin.html"


class Profile(ListView):
    model = Project
    template_name = "studio/profile.html"


class StudioView(ListView):
    model = Author
    template_name = "studio/studio.html"


class AuthorDetailView(DetailView):
    model = Author
    slug_field = "url"
    template_name = "studio/author-detail.html"
    allow_empty = False


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'studio/registration.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'studio/signin.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('/')
