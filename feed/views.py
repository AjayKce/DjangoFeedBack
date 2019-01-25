from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView
from django.http import Http404

from .forms import RegisterForm, StudentsFeedbackCreateForm, FacultyFeedbackCreateForm
from .models import StudentsFeedback, FacultyFeedback


def listuser(request):
    if request.user.is_superuser:
        users = User.objects.all()
        context = {'all': users}
        return render(request, 'feed/userview.html', context)
    else:
        return redirect("/feed/")



def deleteuser(request, pk):
    wat = User.objects.filter(id=pk)
    wat.delete()
    users = User.objects.all()
    context = {'all': users}
    return render(request, 'feed/userview.html', context)


def IndexView(request):
    return render(request, 'feed/index.html')


class UpdateUser(UpdateView):
    form_class = RegisterForm
    template_name = 'feed/updateuser.html'
    success_url = "/res/"

    def get_queryset(self, *args, **kwargs):
        return User.objects.filter(id=self.kwargs['pk'])


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'feed/registration/register.html'
    success_url = '/feed'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return super(RegisterView, self).dispatch(*args, **kwargs)
        else:
            if self.request.user.is_authenticated:
                return redirect("/feed/login")
            return super(RegisterView, self).dispatch(*args, **kwargs)


class StudentFeedbackCreateVeiw(LoginRequiredMixin, CreateView):
    form_class = StudentsFeedbackCreateForm
    template_name = 'feed/studentFeedbackForm.html'
    success_url = '/feed/'

    # login_url = '/userlogin/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(StudentFeedbackCreateVeiw, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(StudentFeedbackCreateVeiw, self).get_context_data(*args, **kwargs)
        context['title'] = 'ADD Student'
        return context


class FacultyFeedbackCreateVeiw(LoginRequiredMixin, CreateView):
    form_class = FacultyFeedbackCreateForm
    template_name = 'feed/facultyFeedbackForm.html'
    success_url = '/feed/'

    # login_url = '/userlogin/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(FacultyFeedbackCreateVeiw, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(FacultyFeedbackCreateVeiw, self).get_context_data(*args, **kwargs)
        context['title'] = 'ADD Faculty'
        return context


def FeedBackDetailVeiw(request):
    if request.user.is_authenticated:
        queryset1 = StudentsFeedback.objects.filter(owner=request.user)
        queryset2 = FacultyFeedback.objects.filter(owner=request.user)
        context = {
            'objects': queryset1,
            'object1': queryset2
        }
        return render(request, 'feed/feedbackdetail.html', context)
    else:
        return redirect("/")


def designation(request):
    return render(request, 'feed/designation.html')


cse1y1s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
cse1y2s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
cse2y3s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
cse2y4s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
cse3y5s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
cse3y6s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
cse4y7s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
cse4y8s = StudentsFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

it1y1s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
it1y2s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
it2y3s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
it2y4s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
it3y5s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
it3y6s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
it4y7s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
it4y8s = StudentsFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

eee1y1s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
eee1y2s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
eee2y3s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
eee2y4s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
eee3y5s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
eee3y6s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
eee4y7s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
eee4y8s = StudentsFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

ece1y1s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
ece1y2s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
ece2y3s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
ece2y4s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
ece3y5s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
ece3y6s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
ece4y7s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
ece4y8s = StudentsFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

eie1y1s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
eie1y2s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
eie2y3s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
eie2y4s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
eie3y5s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
eie3y6s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
eie4y7s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
eie4y8s = StudentsFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

ete1y1s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
ete1y2s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
ete2y3s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
ete2y4s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
ete3y5s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
ete3y6s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
ete4y7s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
ete4y8s = StudentsFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

mech1y1s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
mech1y2s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
mech2y3s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
mech2y4s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
mech3y5s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
mech3y6s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
mech4y7s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
mech4y8s = StudentsFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

auto1y1s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
auto1y2s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
auto2y3s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
auto2y4s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
auto3y5s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
auto3y6s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
auto4y7s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
auto4y8s = StudentsFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

civil1y1s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
civil1y2s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
civil2y3s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
civil2y4s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
civil3y5s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
civil3y6s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
civil4y7s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
civil4y8s = StudentsFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

# faculty filtering

fcse1y1s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
fcse1y2s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
fcse2y3s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
fcse2y4s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
fcse3y5s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
fcse3y6s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
fcse4y7s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
fcse4y8s = FacultyFeedback.objects \
    .filter(department__iexact='cse') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

fit1y1s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
fit1y2s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
fit2y3s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
fit2y4s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
fit3y5s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
fit3y6s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
fit4y7s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
fit4y8s = FacultyFeedback.objects \
    .filter(department__iexact='it') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

feee1y1s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
feee1y2s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
feee2y3s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
feee2y4s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
feee3y5s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
feee3y6s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
feee4y7s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
feee4y8s = FacultyFeedback.objects \
    .filter(department__iexact='eee') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

fece1y1s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
fece1y2s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
fece2y3s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
fece2y4s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
fece3y5s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
fece3y6s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
fece4y7s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
fece4y8s = FacultyFeedback.objects \
    .filter(department__iexact='ece') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

feie1y1s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
feie1y2s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
feie2y3s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
feie2y4s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
feie3y5s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
feie3y6s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
feie4y7s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
feie4y8s = FacultyFeedback.objects \
    .filter(department__iexact='eie') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

fete1y1s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
fete1y2s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
fete2y3s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
fete2y4s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
fete3y5s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
fete3y6s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
fete4y7s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
fete4y8s = FacultyFeedback.objects \
    .filter(department__iexact='ete') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

fmech1y1s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
fmech1y2s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
fmech2y3s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
fmech2y4s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
fmech3y5s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
fmech3y6s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
fmech4y7s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
fmech4y8s = FacultyFeedback.objects \
    .filter(department__iexact='mech') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

fauto1y1s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
fauto1y2s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
fauto2y3s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
fauto2y4s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
fauto3y5s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
fauto3y6s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
fauto4y7s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
fauto4y8s = FacultyFeedback.objects \
    .filter(department__iexact='auto') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')

fcivil1y1s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='1')
fcivil1y2s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='1') \
    .filter(semester__iexact='2')
fcivil2y3s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='3')
fcivil2y4s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='2') \
    .filter(semester__iexact='4')
fcivil3y5s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='5')
fcivil3y6s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='3') \
    .filter(semester__iexact='6')
fcivil4y7s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='7')
fcivil4y8s = FacultyFeedback.objects \
    .filter(department__iexact='civil') \
    .filter(year__iexact='4') \
    .filter(semester__iexact='8')


def AdminStudentDetails(request):
    queryset = StudentsFeedback.objects.all()
    context = {
        'all': queryset,
        'cse1y1s': cse1y1s,
        'cse1y2s': cse1y2s,
        'cse2y3s': cse2y3s,
        'cse2y4s': cse2y4s,
        'cse3y5s': cse3y5s,
        'cse3y6s': cse3y6s,
        'cse4y7s': cse4y7s,
        'cse4y8s': cse4y8s,

        'it1y1s': it1y1s,
        'it1y2s': it1y2s,
        'it2y3s': it2y3s,
        'it2y4s': it2y4s,
        'it3y5s': it3y5s,
        'it3y6s': it3y6s,
        'it4y7s': it4y7s,
        'it4y8s': it4y8s,

        'eee1y1s': eee1y1s,
        'eee1y2s': eee1y2s,
        'eee2y3s': eee2y3s,
        'eee2y4s': eee2y4s,
        'eee3y5s': eee3y5s,
        'eee3y6s': eee3y6s,
        'eee4y7s': eee4y7s,
        'eee4y8s': eee4y8s,

        'ece1y1s': ece1y1s,
        'ece1y2s': ece1y2s,
        'ece2y3s': ece2y3s,
        'ece2y4s': ece2y4s,
        'ece3y5s': ece3y5s,
        'ece3y6s': ece3y6s,
        'ece4y7s': ece4y7s,
        'ece4y8s': ece4y8s,

        'eie1y1s': eie1y1s,
        'eie1y2s': eie1y2s,
        'eie2y3s': eie2y3s,
        'eie2y4s': eie2y4s,
        'eie3y5s': eie3y5s,
        'eie3y6s': eie3y6s,
        'eie4y7s': eie4y7s,
        'eie4y8s': eie4y8s,

        'ete1y1s': ete1y1s,
        'ete1y2s': ete1y2s,
        'ete2y3s': ete2y3s,
        'ete2y4s': ete2y4s,
        'ete3y5s': ete3y5s,
        'ete3y6s': ete3y6s,
        'ete4y7s': ete4y7s,
        'ete4y8s': ete4y8s,

        'mech1y1s': mech1y1s,
        'mech1y2s': mech1y2s,
        'mech2y3s': mech2y3s,
        'mech2y4s': mech2y4s,
        'mech3y5s': mech3y5s,
        'mech3y6s': mech3y6s,
        'mech4y7s': mech4y7s,
        'mech4y8s': mech4y8s,

        'auto1y1s': auto1y1s,
        'auto1y2s': auto1y2s,
        'auto2y3s': auto2y3s,
        'auto2y4s': auto2y4s,
        'auto3y5s': auto3y5s,
        'auto3y6s': auto3y6s,
        'auto4y7s': auto4y7s,
        'auto4y8s': auto4y8s,

        'civil1y1s': civil1y1s,
        'civil1y2s': civil1y2s,
        'civil2y3s': civil2y3s,
        'civil2y4s': civil2y4s,
        'civil3y5s': civil3y5s,
        'civil3y6s': civil3y6s,
        'civil4y7s': civil4y7s,
        'civil4y8s': civil4y8s,
    }
    if request.user.is_superuser:
        return render(request, 'feed/adminstudentfeedbackdetails.html', context)
    else:
        return redirect('/')


def AdminFacultyDetails(request):
    queryset = FacultyFeedback.objects.all()
    context = {
        'all': queryset,
        'fcse1y1s': fcse1y1s,
        'fcse1y2s': fcse1y2s,
        'fcse2y3s': fcse2y3s,
        'fcse2y4s': fcse2y4s,
        'fcse3y5s': fcse3y5s,
        'fcse3y6s': fcse3y6s,
        'fcse4y7s': fcse4y7s,
        'fcse4y8s': fcse4y8s,

        'fit1y1s': fit1y1s,
        'fit1y2s': fit1y2s,
        'fit2y3s': fit2y3s,
        'fit2y4s': fit2y4s,
        'fit3y5s': fit3y5s,
        'fit3y6s': fit3y6s,
        'fit4y7s': fit4y7s,
        'fit4y8s': fit4y8s,

        'feee1y1s': feee1y1s,
        'feee1y2s': feee1y2s,
        'feee2y3s': feee2y3s,
        'feee2y4s': feee2y4s,
        'feee3y5s': feee3y5s,
        'feee3y6s': feee3y6s,
        'feee4y7s': feee4y7s,
        'feee4y8s': feee4y8s,

        'fece1y1s': fece1y1s,
        'fece1y2s': fece1y2s,
        'fece2y3s': fece2y3s,
        'fece2y4s': fece2y4s,
        'fece3y5s': fece3y5s,
        'fece3y6s': fece3y6s,
        'fece4y7s': fece4y7s,
        'fece4y8s': fece4y8s,

        'feie1y1s': feie1y1s,
        'feie1y2s': feie1y2s,
        'feie2y3s': feie2y3s,
        'feie2y4s': feie2y4s,
        'feie3y5s': feie3y5s,
        'feie3y6s': feie3y6s,
        'feie4y7s': feie4y7s,
        'feie4y8s': feie4y8s,

        'fete1y1s': fete1y1s,
        'fete1y2s': fete1y2s,
        'fete2y3s': fete2y3s,
        'fete2y4s': fete2y4s,
        'fete3y5s': fete3y5s,
        'fete3y6s': fete3y6s,
        'fete4y7s': fete4y7s,
        'fete4y8s': fete4y8s,

        'fmech1y1s': fmech1y1s,
        'fmech1y2s': fmech1y2s,
        'fmech2y3s': fmech2y3s,
        'fmech2y4s': fmech2y4s,
        'fmech3y5s': fmech3y5s,
        'fmech3y6s': fmech3y6s,
        'fmech4y7s': fmech4y7s,
        'fmech4y8s': fmech4y8s,

        'fauto1y1s': fauto1y1s,
        'fauto1y2s': fauto1y2s,
        'fauto2y3s': fauto2y3s,
        'fauto2y4s': fauto2y4s,
        'fauto3y5s': fauto3y5s,
        'fauto3y6s': fauto3y6s,
        'fauto4y7s': fauto4y7s,
        'fauto4y8s': fauto4y8s,

        'fcivil1y1s': fcivil1y1s,
        'fcivil1y2s': fcivil1y2s,
        'fcivil2y3s': fcivil2y3s,
        'fcivil2y4s': fcivil2y4s,
        'fcivil3y5s': fcivil3y5s,
        'fcivil3y6s': fcivil3y6s,
        'fcivil4y7s': fcivil4y7s,
        'fcivil4y8s': fcivil4y8s,
    }
    if request.user.is_superuser:
        return render(request, 'feed/adminfacultyfeedbackdetails.html', context)
    else:
        return redirect('/')


def AdminFacultyFilterDetails(request):
    import datetime
    if request.method == "POST":
        start = datetime.datetime.strptime(request.POST['date1'], "%Y-%m-%d").date()
        end = datetime.datetime.strptime(request.POST['date2'], "%Y-%m-%d").date()
        queryset = FacultyFeedback.objects.filter(timestamp__range=[start, end])
        fcse1y1s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        fcse1y2s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        fcse2y3s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        fcse2y4s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        fcse3y5s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        fcse3y6s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        fcse4y7s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        fcse4y8s = FacultyFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        fit1y1s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        fit1y2s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        fit2y3s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        fit2y4s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        fit3y5s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        fit3y6s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        fit4y7s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        fit4y8s = FacultyFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        feee1y1s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        feee1y2s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        feee2y3s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        feee2y4s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        feee3y5s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        feee3y6s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        feee4y7s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        feee4y8s = FacultyFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        fece1y1s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        fece1y2s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        fece2y3s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        fece2y4s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        fece3y5s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        fece3y6s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        fece4y7s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        fece4y8s = FacultyFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        feie1y1s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        feie1y2s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        feie2y3s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        feie2y4s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        feie3y5s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        feie3y6s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        feie4y7s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        feie4y8s = FacultyFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        fete1y1s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        fete1y2s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        fete2y3s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        fete2y4s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        fete3y5s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        fete3y6s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        fete4y7s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        fete4y8s = FacultyFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        fmech1y1s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        fmech1y2s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        fmech2y3s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        fmech2y4s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        fmech3y5s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        fmech3y6s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        fmech4y7s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        fmech4y8s = FacultyFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        fauto1y1s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        fauto1y2s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        fauto2y3s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        fauto2y4s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        fauto3y5s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        fauto3y6s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        fauto4y7s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        fauto4y8s = FacultyFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        fcivil1y1s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        fcivil1y2s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        fcivil2y3s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        fcivil2y4s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        fcivil3y5s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        fcivil3y6s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        fcivil4y7s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        fcivil4y8s = FacultyFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])
        context = {
            'all': queryset,
            'fcse1y1s': fcse1y1s,
            'fcse1y2s': fcse1y2s,
            'fcse2y3s': fcse2y3s,
            'fcse2y4s': fcse2y4s,
            'fcse3y5s': fcse3y5s,
            'fcse3y6s': fcse3y6s,
            'fcse4y7s': fcse4y7s,
            'fcse4y8s': fcse4y8s,

            'fit1y1s': fit1y1s,
            'fit1y2s': fit1y2s,
            'fit2y3s': fit2y3s,
            'fit2y4s': fit2y4s,
            'fit3y5s': fit3y5s,
            'fit3y6s': fit3y6s,
            'fit4y7s': fit4y7s,
            'fit4y8s': fit4y8s,

            'feee1y1s': feee1y1s,
            'feee1y2s': feee1y2s,
            'feee2y3s': feee2y3s,
            'feee2y4s': feee2y4s,
            'feee3y5s': feee3y5s,
            'feee3y6s': feee3y6s,
            'feee4y7s': feee4y7s,
            'feee4y8s': feee4y8s,

            'fece1y1s': fece1y1s,
            'fece1y2s': fece1y2s,
            'fece2y3s': fece2y3s,
            'fece2y4s': fece2y4s,
            'fece3y5s': fece3y5s,
            'fece3y6s': fece3y6s,
            'fece4y7s': fece4y7s,
            'fece4y8s': fece4y8s,

            'feie1y1s': feie1y1s,
            'feie1y2s': feie1y2s,
            'feie2y3s': feie2y3s,
            'feie2y4s': feie2y4s,
            'feie3y5s': feie3y5s,
            'feie3y6s': feie3y6s,
            'feie4y7s': feie4y7s,
            'feie4y8s': feie4y8s,

            'fete1y1s': fete1y1s,
            'fete1y2s': fete1y2s,
            'fete2y3s': fete2y3s,
            'fete2y4s': fete2y4s,
            'fete3y5s': fete3y5s,
            'fete3y6s': fete3y6s,
            'fete4y7s': fete4y7s,
            'fete4y8s': fete4y8s,

            'fmech1y1s': fmech1y1s,
            'fmech1y2s': fmech1y2s,
            'fmech2y3s': fmech2y3s,
            'fmech2y4s': fmech2y4s,
            'fmech3y5s': fmech3y5s,
            'fmech3y6s': fmech3y6s,
            'fmech4y7s': fmech4y7s,
            'fmech4y8s': fmech4y8s,

            'fauto1y1s': fauto1y1s,
            'fauto1y2s': fauto1y2s,
            'fauto2y3s': fauto2y3s,
            'fauto2y4s': fauto2y4s,
            'fauto3y5s': fauto3y5s,
            'fauto3y6s': fauto3y6s,
            'fauto4y7s': fauto4y7s,
            'fauto4y8s': fauto4y8s,

            'fcivil1y1s': fcivil1y1s,
            'fcivil1y2s': fcivil1y2s,
            'fcivil2y3s': fcivil2y3s,
            'fcivil2y4s': fcivil2y4s,
            'fcivil3y5s': fcivil3y5s,
            'fcivil3y6s': fcivil3y6s,
            'fcivil4y7s': fcivil4y7s,
            'fcivil4y8s': fcivil4y8s,
        }
        if request.user.is_superuser:
            return render(request, 'feed/adminfacultyfeedbackdetails.html', context)
        else:
            return redirect('/')


def AdminStudentFilterDetails(request):
    import datetime
    if request.method == "POST":
        start = datetime.datetime.strptime(request.POST['datef'], "%Y-%m-%d").date()
        end = datetime.datetime.strptime(request.POST['datet'], "%Y-%m-%d").date()
        queryset = StudentsFeedback.objects.filter(timestamp__range=[start, end])
        cse1y1s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        cse1y2s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        cse2y3s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        cse2y4s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        cse3y5s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        cse3y6s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        cse4y7s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        cse4y8s = StudentsFeedback.objects \
            .filter(department__iexact='cse') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        it1y1s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        it1y2s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        it2y3s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        it2y4s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        it3y5s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        it3y6s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        it4y7s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        it4y8s = StudentsFeedback.objects \
            .filter(department__iexact='it') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        eee1y1s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        eee1y2s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        eee2y3s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        eee2y4s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        eee3y5s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        eee3y6s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        eee4y7s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        eee4y8s = StudentsFeedback.objects \
            .filter(department__iexact='eee') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        ece1y1s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        ece1y2s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        ece2y3s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        ece2y4s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        ece3y5s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        ece3y6s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        ece4y7s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        ece4y8s = StudentsFeedback.objects \
            .filter(department__iexact='ece') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        eie1y1s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        eie1y2s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        eie2y3s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        eie2y4s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        eie3y5s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        eie3y6s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        eie4y7s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        eie4y8s = StudentsFeedback.objects \
            .filter(department__iexact='eie') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        ete1y1s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        ete1y2s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        ete2y3s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        ete2y4s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        ete3y5s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        ete3y6s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        ete4y7s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        ete4y8s = StudentsFeedback.objects \
            .filter(department__iexact='ete') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        mech1y1s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        mech1y2s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        mech2y3s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        mech2y4s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        mech3y5s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        mech3y6s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        mech4y7s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        mech4y8s = StudentsFeedback.objects \
            .filter(department__iexact='mech') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        auto1y1s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        auto1y2s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        auto2y3s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        auto2y4s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        auto3y5s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        auto3y6s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        auto4y7s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        auto4y8s = StudentsFeedback.objects \
            .filter(department__iexact='auto') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])

        civil1y1s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='1') \
            .filter(timestamp__range=[start, end])
        civil1y2s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='1') \
            .filter(semester__iexact='2') \
            .filter(timestamp__range=[start, end])
        civil2y3s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='3') \
            .filter(timestamp__range=[start, end])
        civil2y4s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='2') \
            .filter(semester__iexact='4') \
            .filter(timestamp__range=[start, end])
        civil3y5s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='5') \
            .filter(timestamp__range=[start, end])
        civil3y6s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='3') \
            .filter(semester__iexact='6') \
            .filter(timestamp__range=[start, end])
        civil4y7s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='7') \
            .filter(timestamp__range=[start, end])
        civil4y8s = StudentsFeedback.objects \
            .filter(department__iexact='civil') \
            .filter(year__iexact='4') \
            .filter(semester__iexact='8') \
            .filter(timestamp__range=[start, end])
        context = {
            'all': queryset,
            'cse1y1s': cse1y1s,
            'cse1y2s': cse1y2s,
            'cse2y3s': cse2y3s,
            'cse2y4s': cse2y4s,
            'cse3y5s': cse3y5s,
            'cse3y6s': cse3y6s,
            'cse4y7s': cse4y7s,
            'cse4y8s': cse4y8s,

            'it1y1s': it1y1s,
            'it1y2s': it1y2s,
            'it2y3s': it2y3s,
            'it2y4s': it2y4s,
            'it3y5s': it3y5s,
            'it3y6s': it3y6s,
            'it4y7s': it4y7s,
            'it4y8s': it4y8s,

            'eee1y1s': eee1y1s,
            'eee1y2s': eee1y2s,
            'eee2y3s': eee2y3s,
            'eee2y4s': eee2y4s,
            'eee3y5s': eee3y5s,
            'eee3y6s': eee3y6s,
            'eee4y7s': eee4y7s,
            'eee4y8s': eee4y8s,

            'ece1y1s': ece1y1s,
            'ece1y2s': ece1y2s,
            'ece2y3s': ece2y3s,
            'ece2y4s': ece2y4s,
            'ece3y5s': ece3y5s,
            'ece3y6s': ece3y6s,
            'ece4y7s': ece4y7s,
            'ece4y8s': ece4y8s,

            'eie1y1s': eie1y1s,
            'eie1y2s': eie1y2s,
            'eie2y3s': eie2y3s,
            'eie2y4s': eie2y4s,
            'eie3y5s': eie3y5s,
            'eie3y6s': eie3y6s,
            'eie4y7s': eie4y7s,
            'eie4y8s': eie4y8s,

            'ete1y1s': ete1y1s,
            'ete1y2s': ete1y2s,
            'ete2y3s': ete2y3s,
            'ete2y4s': ete2y4s,
            'ete3y5s': ete3y5s,
            'ete3y6s': ete3y6s,
            'ete4y7s': ete4y7s,
            'ete4y8s': ete4y8s,

            'mech1y1s': mech1y1s,
            'mech1y2s': mech1y2s,
            'mech2y3s': mech2y3s,
            'mech2y4s': mech2y4s,
            'mech3y5s': mech3y5s,
            'mech3y6s': mech3y6s,
            'mech4y7s': mech4y7s,
            'mech4y8s': mech4y8s,

            'auto1y1s': auto1y1s,
            'auto1y2s': auto1y2s,
            'auto2y3s': auto2y3s,
            'auto2y4s': auto2y4s,
            'auto3y5s': auto3y5s,
            'auto3y6s': auto3y6s,
            'auto4y7s': auto4y7s,
            'auto4y8s': auto4y8s,

            'civil1y1s': civil1y1s,
            'civil1y2s': civil1y2s,
            'civil2y3s': civil2y3s,
            'civil2y4s': civil2y4s,
            'civil3y5s': civil3y5s,
            'civil3y6s': civil3y6s,
            'civil4y7s': civil4y7s,
            'civil4y8s': civil4y8s,
        }
        if request.user.is_superuser:
            return render(request, 'feed/adminstudentfeedbackdetails.html', context)
        else:
            return redirect('/')
