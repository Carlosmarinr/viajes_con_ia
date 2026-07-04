from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm, DestinationForm, SignupForm
from .models import Destination, Vote


def home(request):
    featured_destinations = Destination.objects.filter(featured=True)[:3]
    latest_destinations = Destination.objects.all()[:6]
    return render(request, 'blog/home.html', {
        'featured_destinations': featured_destinations,
        'latest_destinations': latest_destinations,
    })


def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'blog/destination_list.html', {'destinations': destinations})


@login_required
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.author = request.user
            if not request.user.is_staff and not request.user.is_superuser:
                destination.image = None
            destination.save()
            return redirect('destination_detail', slug=destination.slug)
    else:
        form = DestinationForm(user=request.user)
    return render(request, 'blog/destination_form.html', {'form': form, 'title': 'Crear destino'})


@login_required
def destination_update(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    if destination.author != request.user and not request.user.is_staff and not request.user.is_superuser:
        return redirect('destination_detail', slug=destination.slug)

    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination, user=request.user)
        if form.is_valid():
            if not request.user.is_staff and not request.user.is_superuser:
                destination.image = None
            form.save()
            return redirect('destination_detail', slug=destination.slug)
    else:
        form = DestinationForm(instance=destination, user=request.user)
    return render(request, 'blog/destination_form.html', {'form': form, 'title': 'Editar destino'})


@login_required
def destination_delete(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    if destination.author != request.user and not request.user.is_staff and not request.user.is_superuser:
        return redirect('destination_detail', slug=destination.slug)

    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')
    return render(request, 'blog/delete_confirm.html', {'destination': destination})


def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    comments = destination.comments.all()
    comment_form = CommentForm()
    user_vote = None
    if request.user.is_authenticated:
        user_vote = destination.votes.filter(user=request.user).first()

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.destination = destination
            comment.user = request.user
            comment.save()
            return redirect('destination_detail', slug=destination.slug)

    return render(request, 'blog/destination_detail.html', {
        'destination': destination,
        'comments': comments,
        'comment_form': comment_form,
        'user_vote': user_vote,
    })


@login_required
@require_POST
def vote_destination(request, slug, vote_type):
    destination = get_object_or_404(Destination, slug=slug)
    if vote_type not in {'like', 'dislike'}:
        return redirect('destination_detail', slug=destination.slug)

    vote = destination.votes.filter(user=request.user).first()
    if vote:
        if vote.vote_type == vote_type:
            vote.delete()
        else:
            vote.vote_type = vote_type
            vote.save()
    else:
        Vote.objects.create(destination=destination, user=request.user, vote_type=vote_type)
    return redirect('destination_detail', slug=destination.slug)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'blog/auth_form.html', {'form': form, 'title': 'Registrarse'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/auth_form.html', {'form': form, 'title': 'Iniciar sesión'})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
