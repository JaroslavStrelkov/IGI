from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Review

def reviews_list(request):
    reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'reviews/index.html', {'reviews': reviews})

@login_required
def create_review(request):

    if request.method == 'POST':
        review = Review()
        review.user = request.user
        review.rating = request.POST.get('rating')
        review.text = request.POST.get('text')
        review.save()

        return HttpResponseRedirect('/reviews/')

    return render(request, 'reviews/create.html')

@login_required
def edit_review(request, id):

    try:
        review = Review.objects.get(id=id)

        if review.user != request.user and not request.user.is_superuser:
            return HttpResponseNotFound('<h2>Access denied</h2>')

        if request.method == 'POST':

            review.rating = request.POST.get('rating')
            review.text = request.POST.get('text')
            review.save()

            return HttpResponseRedirect('/reviews/')

        return render(request, 'reviews/edit.html', {'review': review})

    except Review.DoesNotExist:
        return HttpResponseNotFound('<h2>Отзыв не найден</h2>')

@login_required
def delete_review(request, id):

    try:
        review = Review.objects.get(id=id)

        if review.user != request.user and not request.user.is_superuser:
            return HttpResponseNotFound('<h2>Access denied</h2>')
        
        review.delete()

        return HttpResponseRedirect('/reviews/')

    except Review.DoesNotExist:
        return HttpResponseNotFound('<h2>Review not found</h2>')