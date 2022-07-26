# from channels.auth import login, logout
from tkinter import filedialog
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import subprocess
from student_management_app.EmailBackEnd import EmailBackEnd
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Video


from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.urls import reverse_lazy, reverse


from .models import Event,EventMember
from .utils import Calendar
from .forms import EventForm, AddMemberForm




def back(request):
    return HttpResponseRedirect('/')


def graficos(request):
    return render(request, 'Graficos/dashboard.html')    

def graficosRandom(request): 
    return render(request, 'GrafphRandom/grafico/index.html')    

def contact(request):
    return render(request, 'index/contact.html')    

def teachers(request):
    return render(request, 'index/terchers.html')   

def about(request):
    return render(request, 'index/about.html')  

def live(request):
    return render(request, 'whiteboard/liveboard.html')

def home(request):
    return render(request, 'index/index.html')

def GMeet(request):
    #Meu aplicativo em GMeet Clone em  React 
    #output=os.system("start /wait cmd /c {command}")
  
    G= subprocess.call('npm start', shell=True, cwd='GmeetClone/')
    return HttpResponse(G)

def Formulario(request):
    #Meu aplicativo em GMeet Clone em  React 
    #output=os.system("start /wait cmd /c {command}")
  
    F= subprocess.call('npm start', shell=True, cwd='Formulario/')
    return HttpResponse(F) #verificar refresh

def Compilador(c):
    #Meu aplicativo em GMeet Clone em  React 
    #output=os.system("start /wait cmd /c {command}")
    c = subprocess.run('python MultiCompiler.py', shell=True,cwd='student_management_app/templates/Compilador')
    return redirect('admin_home')


def Brainstorming(request):
    #Meu aplicativo em BrainStorming em  React  
    B= subprocess.call('npm start', shell=True, cwd='Brainstorming/')
    return HttpResponse(B)
  
  
def loginPage(request): 
    #pagina login simples
    return render(request, 'login.html')

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            #definindo usuarios 
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
            #se for invalido redireciona para login
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')

def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


class Index(ListView):
    model= Video
    template_name= 'Videos/index.html'
    order_by='-date_posted'

def VideoIndex(request):
	return render(request, 'Videos/index.html')



class CreateVideo(CreateView):
	model = Video
	fields = ['title', 'description', 'video_file', 'thumbnail']
	template_name = 'Videos/create_video.html'

	def get_success_url(self):
		return reverse('video-detail', kwargs={'pk': self.object.pk})

class DetailVideo(DetailView):
	model = Video
	template_name = 'Videos/detail_video.html'

class UpdateVideo(UpdateView):
	model = Video
	fields = ['title', 'description']
	template_name = 'Videos/create_video.html'

	def get_success_url(self):
		return reverse('video-detail', kwargs={'pk': self.object.pk})

class DeleteVideo(DeleteView):
	model = Video
	template_name = 'Videos/delete_video.html'

	def get_success_url(self):
		return reverse('VideoIndex')


#calendar views

def calendario(request):
    return render(request, 'calendario/calendarapp/dashboard.html')


from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.urls import reverse_lazy, reverse
from .models import Event,EventMember
from .utils import Calendar
from .forms import EventForm, AddMemberForm
from django.views.generic import ListView
from .models import Event




class AllEventsListView(ListView):
    """ All event list views """

    template_name = "calendario/calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events()


class RunningEventsListView(ListView):
    """ Running events list view """

    template_name = "calendario/calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events()


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()



def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class CalendarView( generic.ListView):
    model = Event
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        Event.objects.get_or_create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendar"))
    return render(request, "event.html", {"form": form})


class EventEdit(generic.UpdateView):
    model = Event
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "event.html"


def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {"event": event, "eventmember": eventmember}
    return render(request, "calendario/event-details.html", context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == "POST":
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                EventMember.objects.create(event=event)
                return redirect("calendarapp:calendar")
            else:
                print("--------------User limit exceed!-----------------")
    context = {"form": forms}
    return render(request, "add_member.html", context)


class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = "calendario/event_delete.html"
    success_url = reverse_lazy("calendar")


class CalendarViewNew( generic.View):
    template_name = "calendario/calendarapp/calendar.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events()
        events_month = Event.objects.get_running_events()
        event_list = []
        # start: '2020-09-16T16:00:00'
        for event in events:
            event_list.append(
                {
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),

                }
            )
        context = {"form": forms, "events": event_list,
                   "events_month": events_month}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.save()
            return redirect("calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


from django.views.generic import View
from django.shortcuts import render

from .models import Event


def calendario(request):
    return render(request, 'calendario/calendarapp/dashboard.html')




class DashboardView(View):
   
    template_name = "calendario/calendarapp/dashboard.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.get_all_events()
        running_events = Event.objects.get_running_events()
        latest_events = Event.objects.filter().order_by("-id")[:10]
        context = {
            "total_event": events.count(),
            "running_events": running_events,
            "latest_events": latest_events,
        }
        return render(request, self.template_name, context)

from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage

from .forms import BookForm
from .models import Atividade

class Home(TemplateView):
    template_name = 'homework/home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'homework/upload.html', context)


def book_list(request):
    books = Atividade.objects.all()
    return render(request, 'homework/book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homework/book_list')
    else:
        form = BookForm()
    return render(request, 'homework/upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Atividade.objects.get(pk=pk)
        book.delete()
    return redirect('homework/book_list')


class BookListView(ListView):
    model = Atividade
    template_name = 'homework/class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Atividade
    form_class = BookForm
    success_url = reverse_lazy('homework/class_book_list')
    template_name = 'homework/upload_book.html'
