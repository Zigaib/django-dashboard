
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, ProfileForm, SignUpForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    msg = None
    success = False
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuário Criado - Por favor <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Formulário inválido!'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

@login_required
def update_profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = UserForm(instance=request.user.profile)
    if request.method == 'POST':        
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()

            messages.success(request, ('Perfil atualizado com sucesso!'))
        
        if profile_form.is_valid():
            if request.FILES:
                request.user.profile.avatar = request.FILES.get('avatar')
                request.user.profile.save()  
            profile_form.save()
            
            messages.success(request, ('Perfil atualizado com sucesso!'))

        else:
            messages.error(request, ('Por favor, corrigir informações.'))
        
        return redirect('/profile/')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })