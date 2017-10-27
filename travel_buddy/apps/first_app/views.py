from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import User, Trip
from django.contrib import messages
def index(request):
    return render(request, "login.html")
def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Logged in!!")
    return redirect("/success")

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    
    return redirect('/dash')
def dash(request):
    this_user = User.objects.get(id = request.session['user_id']) 
    context = {
        'users': User.objects.get(id=request.session['user_id']),
        'all_users': Trip.objects.exclude(user = this_user),
        'trips': Trip.objects.filter(user = this_user),
    }
    return render(request, 'dashboard.html', context)
def add_trip(request):
    this_user = User.objects.get(id = request.session['user_id'])
    this_trip = Trip.objects.create(destination_name = request.POST
    ['destination'], description = request.POST['description'], travel_from = request.POST['travel_from'], travel_to = request.POST['travel_to'])
    this_trip.user.add(this_user)
    return redirect('/dash')
def adddestination(request, id):
    this_trip = Trip.objects.get(id=id)
    this_user = User.objects.get(id = request.session['user_id'])
    this_trip.user.add(this_user)
    return redirect("/dash")
def destination(request, id):
    return render(request, "destination.html")
