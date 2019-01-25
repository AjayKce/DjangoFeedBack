from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import (
    IndexView,
    RegisterView,
    StudentFeedbackCreateVeiw,
    FeedBackDetailVeiw,
    FacultyFeedbackCreateVeiw,
    designation,
    AdminStudentDetails,
    AdminFacultyDetails,
    AdminFacultyFilterDetails,
    AdminStudentFilterDetails,
    listuser,
    deleteuser,
    UpdateUser
)

urlpatterns = [
    url(r'^$', IndexView, name="home"),
    url(r'^feed/register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(template_name='feed/registration/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^student/create', StudentFeedbackCreateVeiw.as_view(), name="studentfeedbackcreate"),
    url(r'^faculty/create', FacultyFeedbackCreateVeiw.as_view(), name="facultyfeedbackcreate"),

    url(r'^feedback/detail', FeedBackDetailVeiw, name="feedbackdetail"),
    url(r'^res/$', listuser, name='userview'),
    url(r'res/(?P<pk>[0-9]+)/$', deleteuser, name='deleteuser'),
    url(r'res/update/(?P<pk>[0-9]+)/$', UpdateUser.as_view(), name='updateuser'),

    url(r'designation/', designation, name='designation'),

    url(r'^adminstudentdetails$', AdminStudentDetails, name='adminstudents'),
    url(r'^adminfacultydetails$', AdminFacultyDetails, name='adminfaculty'),

    url(r'^adminstudentdetailsfilter', AdminStudentFilterDetails, name='adminstudentfilter'),
    url(r'^adminfacultydetailsfilter', AdminFacultyFilterDetails, name='adminfacultyfilter'),

]
