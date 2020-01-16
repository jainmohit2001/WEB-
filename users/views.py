from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from orders.forms import CheckoutForm
from .models import Address


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now Log In!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

@login_required
def new_address(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            address = Address()
            address.user = request.user
            address.zip = form.cleaned_data['zip']
            address.house_no = form.cleaned_data['house_no']
            address.area = form.cleaned_data['area']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.landmark = form.cleaned_data['landmark']
            address.name = form.cleaned_data['name']
            address.mobile_no = form.cleaned_data['mobile_no']
            address.alternate_no = form.cleaned_data['alternate_no']
            address.zip = form.cleaned_data['zip']
            address.address_type = form.cleaned_data['address_type']
            address.save()
            return redirect('checkout')
    else:
        form = CheckoutForm()
    context = {
        'user': request.user,
        'form': form,
    }
    template = 'users/address.html'
    return render(request, template, context)

def edit_address(request, id):
    if request.method == "POST":
        address = Address.objects.get(id=id)
        form = CheckoutForm(request.POST, instance=address)
        if form.is_valid():
            address.zip = form.cleaned_data['zip']
            address.house_no = form.cleaned_data['house_no']
            address.area = form.cleaned_data['area']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.landmark = form.cleaned_data['landmark']
            address.name = form.cleaned_data['name']
            address.mobile_no = form.cleaned_data['mobile_no']
            address.alternate_no = form.cleaned_data['alternate_no']
            address.zip = form.cleaned_data['zip']
            address.address_type = form.cleaned_data['address_type']
            address.save()
            messages.success(request, f'Address edited successfully')
            return redirect('checkout')
    else:
        address = Address.objects.get(id=id)
        form = CheckoutForm(instance=address)
    template = "users/edit_address.html"
    context = {
        'user': request.user,
        'form': form,
        'address': address,
    }
    return render(request, template, context)


def remove_address(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    messages.success(request, f'address removed successfully')
    return redirect('checkout')