from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *
from .serializers import UserSerializer
import requests
from datetime import date
today = date.today()

# Api for searching the user and save the data in database and update duplicates
class Searchuser(View):
    def get(self,request):
        form = SearchForm()
        return render(request,'search_user.html',{'form':form})

    def post(self,request):
        username = request.POST['search']
        url = 'https://api.github.com/search/users?q=%s' % username
        response = requests.get(url)
        user = response.json()
        for i in range((len(user['items']))):
            serializer = UserSerializer(data=user['items'][i])
            if (serializer.is_valid()):
                serializer.save()

        return render(request, 'search_user.html', {'user': user})
        
# show all users
class ShowallUsers(View):
    def get(self,request):
        obj = github.objects.all()
        print (len(obj))
        return render(request, 'search_user.html', {'obj': obj})

# Report of the users on the basis of date(month,year,week)
class SearchUseremail(View):
    def get(self,request):
        obj1 = github.objects.filter(date__month=today.month)
        # obj1 = github.objects.filter(date__year=today.year)
        return render(request, 'search_user.html', {'obj1': obj1})


