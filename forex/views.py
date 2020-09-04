import time
import selenium
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from .scrapt import scrape
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username,password,user)
        if user is not None:
            messages.success(request, 'Username or Password is in incorrect')
            return redirect('login')
        else:
            login(request, user)

            return redirect('dashboard')
    else:
        context = {}

        return render(request, 'login.html', context)


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.title = form.cleaned_data.get('title')

        user.profile.country = form.cleaned_data.get('country')
        user.profile.phonenumber = form.cleaned_data.get('phonenumber')
        user.is_active = False

        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        messages.success(request, 'Account was created for ' + username)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    profile = (Profile.objects.filter(user=request.user))
    profit = (list(profile.values('margin'))[0]['margin'])
    deposit = (list(profile.values('amount'))[0]['amount'])
    return render(request, 'dashboard.html', {'margin': profit, 'amount': deposit})


def corona(request):
    return render(request, 'coronavirus.html')

def pricelist(request):
    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument("--remote-debugging-port=9222")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_argument("--start-maximized")
    opt.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opt, 
    executable_path='./chromedriver')
    driver.get('https://www.ig.com/en/forex/markets-forex')


    timeout = 10

    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                "//div[@class='dynamic-table__cell']")
            )
        )
    except TimeoutException:
        print("Struggling to get the page....Have faith in this buggy script!")
        
    data = []

    while not data:
        for elm in driver.find_elements(By.CSS_SELECTOR, "span[data-field=V2-F-BID]"):
            if elm.text and elm.text != '-': # Maybe check on contains digit
                data.append(elm.text)
        time.sleep(7)

        
    tet =[]
    while not tet:
        for em in driver.find_elements(By.CSS_SELECTOR, "span[data-field=OFR]"):
            if em.text and em.text != '-': # Maybe check on contains digit
                tet.append(em.text)
        time.sleep(7)
    print(data)       


           
    context = {
        "price": 123,
        "mydata": data
    }

    return render(request, 'pricelist.html', context)





def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact-us.html')

def partnership(request):
    return render(request, 'partnership.html')