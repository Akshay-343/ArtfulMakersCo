from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ArtisanForm, CustomerForm, ProductForm
def artisan_signup(request):
    if request.method == 'POST':
        form = ArtisanForm(request.POST)
        if form.is_valid():
            artisan = form.save()
            login(request, artisan.user)
            return redirect('home')
    else:
        form = ArtisanForm()
    return render(request, 'artisan_signup.html', {'form': form})

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer.user)
            return redirect('home')  # Redirect to the appropriate page
    else:
        form = CustomerForm()
    return render(request, 'customer_signup.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.artisan = request.user.artisan  # Assuming you have a one-to-one relationship between User and Artisan
            product.save()
            return redirect('home')  # Redirect to the appropriate page
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def homepage(request):
    return render(request, 'home.html')

def artisan_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.artisan is not None:
            login(request, user)
            return redirect('home')  # Redirect to the appropriate page
        else:
            # Handle invalid login credentials
            pass

    return render(request, 'artisan_login.html')

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.customer is not None:
            login(request, user)
            return redirect('home')  # Redirect to the appropriate page
        else:
            # Handle invalid login credentials
            pass

    return render(request, 'customer_login.html')
