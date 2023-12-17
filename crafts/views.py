from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ArtisanUserForm, ArtisanForm, CustomerUserForm, CustomerForm, ProductForm, ArtisanLoginForm, CustomerLoginForm

def homepage(request):
    return render(request, 'home.html')



def artisan_signup(request):
    if request.method == 'POST':
        user_form = ArtisanUserForm(request.POST)
        artisan_form = ArtisanForm(request.POST, request.FILES)

        if user_form.is_valid() and artisan_form.is_valid():
            user = user_form.save(commit=False)



            user.set_password(user_form.cleaned_data['password'])
            user.save()

            artisan = artisan_form.save(commit=False)
            artisan.user = user
            artisan.save()

            # Log the user in after registration
            login(request, user)

            return redirect('home')  # Replace 'success_page' with your actual success page URL

    else:
        user_form = ArtisanUserForm()
        artisan_form = ArtisanForm()

    return render(request, 'artisan_signup.html', {'user_form': user_form, 'artisan_form': artisan_form})


def customer_signup(request):
    if request.method == 'POST':
        user_form = CustomerUserForm(request.POST)
        customer_form = CustomerForm(request.POST, request.FILES)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

            # Log the user in after registration
            login(request, user)

            return redirect('home')  # Replace 'success_page' with your actual success page URL

    else:
        user_form = CustomerUserForm()
        customer_form = CustomerForm()

    return render(request, 'customer_signup.html', {'user_form': user_form, 'customer_form': customer_form})


from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Assuming the logged-in user is an artisan
            artisan = request.user.artisan
            product = form.save(commit=False)

            # Assign the artisan to the product before saving
            product.artisan = artisan
            product.save()

            return redirect('home')  # Replace 'success_page' with your actual success page URL

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def artisan_login(request):
    if request.method == 'POST':
        form = ArtisanLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if hasattr(user, 'artisan') and user.artisan is not None:
                    login(request, user)
                    return redirect('home')  # Redirect to the appropriate page
                else:
                    error = 'User has no artisan profile.'
            else:
                error = 'Invalid login credentials'
        else:
            error = 'Invalid form data'
    else:
        form = ArtisanLoginForm()
        error = None

    return render(request, 'artisan_login.html', {'form': form, 'error': error})


def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.customer is not None:
                login(request, user)
                return redirect('home')  # Redirect to the appropriate page
            else:
                error = 'Invalid login credentials'
        else:
            error = 'Invalid form data'
    else:
        form = CustomerLoginForm()
        error = None

    return render(request, 'customer_login.html', {'form': form, 'error': error})