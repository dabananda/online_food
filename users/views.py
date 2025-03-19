from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}, your account has been created successfully!')
            return redirect('login')

    form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


@login_required
def profile_page(request):
    return render(request, 'users/profile.html')
