from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import folium
from .models import app1




# Create your views here.
@login_required(login_url='login')
def findyourbus(request):
     if request.method=='POST':
         return redirect('route')
     
     return render (request,'findyourbus.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('findyourbus')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def route(request):
    import pandas as pd
    df = pd.read_csv(r'c:\Users\user\Documents\busroute2.csv')

    data = pd.DataFrame.from_records(df[1:])
    m = folium.Map(location=[22.4934288,88.2871806],
               zoom_start=13)
    place_lat = data['latitude'].astype(float).tolist()

    place_lng = data['longitude'].astype(float).tolist()    
    points = []
    for i in range(len(place_lat)):
     points.append([place_lat[i], place_lng[i]])
    
    for index,lat in enumerate(place_lat):
     folium.Marker([lat, 
                   place_lng[index]],
                  popup=('route'.format(index))
                  ,icon = folium.Icon(color='blue',icon_color='white',prefix='fa', icon='bus')
                  ).add_to(m)
    
    folium.PolyLine(points, color='blue',dash_array='5',opacity ='.85',
                tooltip ='Transit Route 101'
                ).add_to(m)

    m.save('route.html')
    #fetching data from database
    #from django.core import serializers
    #table = serializers.serialize('python',app1.objects.all())
    
    #context= {
     #   'table':table,
    #}
    app=app1.objects.all()
    return render(request,'route.html', {'app': app})

    