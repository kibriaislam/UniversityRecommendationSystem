from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import General_University,General_University_requirement,Medical_College,Science_And_Technology
from .models import Engineering_University,Science_And_Technology_requirement, General_University_requirement
# Create your views here.
def home_view(request):
    return render(request,'home.html')


def General_University(request):
    return render(request,'General_University.html')

def findGeneralUniversity(request):
    data = []
    if request.method=="POST":
        background = request.POST.get('Background')
        passingyear=request.POST.get('Passingyear')
        gpahsc=request.POST.get('GpaHsc')
        gpassc=request.POST.get('GpaSsc')
        totalgpa=int(gpahsc)+int(gpassc)
        data = General_University_requirement.objects.filter(
            requireGpa__lte=totalgpa,
            background=background,
            passingyear=passingyear,
        )
        print(data)
    return render(request, 'Recommended_University.html', {'data': data})

def Engineering_University(request):
    return render(request,'Engineering_University.html')


def Medical_College(request):
    return render(request,'Medical_College.html')

def ScienceAndTechnology(request):
    return render(request,'Science_and_Technology.html')
