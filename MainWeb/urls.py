from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_view,name='home'),
    path('home/',views.home_view,name='home'),
    path('GeneralUniversity/',views.General_University,name='GeneralUniversity'),
    path('MedicalCollege/',views.Medical_College,name='MedicalCollege'),
    path('ScienceAndTechnology/',views.ScienceAndTechnology,name='ScienceAndTechnology'),
    path('EngineeringUniversity/',views.Engineering_University,name='EngineeringUniversity'),
    path('index/',views.findGeneralUniversity,name='findUni'),



]
