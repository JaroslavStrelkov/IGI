from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
import logging

logger = logging.getLogger(__name__)



def register_view(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            logger.info(f'New user is sign in: {user.username}')
            login(request, user)
            return redirect('profile')
        
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f'User is login: {user.username}')
            return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('login')


@login_required
def profile_view(request):
    profile = request.user.profile
    orders = request.user.customer_orders.all()

    return render(request, 'accounts/profile.html', {'profile': profile, 'orders': orders,})