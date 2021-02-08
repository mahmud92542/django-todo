from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from department.models import Company, CompanyDeptUser


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:  # password mathched
            try:
                # Getting username from the signup form and give the error if username is exist
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                # Create user storing username and password
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                # After creating user complete login and redirect to dashboard
                auth.login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

# Login method for the login


def login(request):
    if request.method == 'POST':
        # Get username and password from the login form mathched from the database by using authenticate method
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:  # Checked username and password is exist or not
            auth.login(request, user)  # Complete login by using login method
            return redirect('selcom')  # Redirect to company selection page
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')  # Show the login page


# Company Selection method
def selcom(request):
    allcomp = Company.objects.all()  # Getting all data from Company model
    # Getting company id for authenticated user which are given in the CompanyDeptUser model
    comdeptuser = CompanyDeptUser.objects.filter(user=request.user)
    compid = []  # List for authenticated user's company id
    for comp in comdeptuser:
        # Getting primery key of Company model for remove same company id filterd by authenticated user's company id
        compdata = Company.objects.filter(name=comp.compid).all()
        for c in compdata:
            # Append company model's primery key in the list of compid
            compid.append(c.id)
    scompid = set(compid)  # Remove same company id by using set method
    usercompid = list(scompid)  # Making a list of company id
    # Send the all company info and authenticated user's company id as a context
    context = {'allcomp': allcomp, 'usercompid': usercompid}
    # Show the select company page
    return render(request, 'accounts/select_company.html', context)


# Logout method for the logout
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')  # Show the login page
