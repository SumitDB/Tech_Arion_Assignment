from django.shortcuts import render , HttpResponseRedirect
from .forms import ProfileRegistration
from .models import Profile


# This function will add and show 
def add_show(request):
    if request.method == "POST":
        fm = ProfileRegistration(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['Name']
           bd= fm.cleaned_data['Date_of_birth']
           gd = fm.cleaned_data['Gender']
           ph= fm.cleaned_data['Phone_number']
           reg = Profile(name=nm, Date_of_birth=bd, Gender=gd)
           reg.save()
           fm = ProfileRegistration()
    else:
        fm = ProfileRegistration()
    prof= Profile.objects.all()
    return render(request,'addandshow.html', {"form":fm, 'pro':prof})


# This function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi= Profile.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# This function will update
def update_edit(request, id):
    if request.method == 'POST':
        pi=Profile.objects.get(pk=id)
        fm = ProfileRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi=Profile.objects.get(pk=id)
            fm = ProfileRegistration(instance=pi)        
    return render(request, 'site/updatestudent.html',{'form':fm})
