from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.timezone import now
from apps.accounts.utils import employee_required
from .models import PromoCode
from .forms import PromoCodeForm

def promo_list(request):
    active_promos = PromoCode.objects.filter(is_active=True, valid_until__gte=now().date())
    archive_promos = PromoCode.objects.filter(is_active=False)

    return render(request, 'promo/index.html', {'active_promos': active_promos, 'archive_promos': archive_promos,})

@employee_required
def create_promo(request):
    if request.method == 'POST':
        form = PromoCodeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Промокод успешно создан!')
            return redirect('/promo/')
    else:
        form = PromoCodeForm()

    return render(request, 'promo/create.html', {'form': form})

@employee_required
def edit_promo(request, id):
    promo = get_object_or_404(PromoCode, id=id)

    if request.method == 'POST':
        form = PromoCodeForm(request.POST, instance=promo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Промокод успешно обновлён!')
            return redirect('/promo/')
    else:
        form = PromoCodeForm(instance=promo)

    return render(request, 'promo/edit.html', {'form': form, 'promo': promo})

@employee_required
def delete_promo(request, id):
    promo = get_object_or_404(PromoCode, id=id)
    promo.delete()
    messages.success(request, 'Промокод удалён!')
    
    return redirect('/promo/')