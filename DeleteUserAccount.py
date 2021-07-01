"""  
Delete Registered User in Django 

"""



# From "Users/forms.py" forms for Delete Account 
  
from django import forms
from django.contrib.auth.models import User


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User   #this is model which is used in models.py
        fields = []    #Form has only submit button.  Empty "fields" list still necessary, though.
        
        
        
# From "Users/views.py "   views for Delete Account  


from .forms import UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def delete_user_profile(request):
    if request.method == 'POST':
        user = request.user.delete()
        return redirect('/signup/')
    else:
        form = UserDeleteForm(instance=request.user)
        return render(request, 'account/delete_account.html')
        
        
# From " Users/delete_account.html "   HTML file for Delete Account


<div class="container">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <h1 class="text-center text-info my-5">Delete Acccount</h1>
            <p>Are you sure you want to delete your account?  This will permanently delete your profile and any content you have created.</p>
            <form action="" method="post">
                {% csrf_token %}
                <button class="btn btn-danger" type="submit">Delete Account</button>
                <a class="btn btn-danger" href="{% url 'profile' %}">Cancel</a>
            </form>
        </div>
    </div>
</div>


# From " Users/urls.py "   urls for Delete Account

from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
  
    path('delete_account/', views.delete_user_profile, name='delete_account'),
]
