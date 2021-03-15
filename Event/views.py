from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import EventsForm
from .models import Events
# Create your views here.
ACTION_1 = "create.html"
def home(request):
    e=Events.objects.all()
    return render(request,"home.html",{"e":e})

def create(request):
    if request.method == "POST":
        form=EventsForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,ACTION_1,{"obj":obj})  
    else:
        form=EventsForm()    
        return render(request,ACTION_1,{"form":form})
    return HttpResponseRedirect('/')    

def index(request):
    return render(request,ACTION_1)

def base(request):
    return render(request,"base.html")

def liked(request):
    e=Events.objects.all()
    return render(request,'liked.html',{'e':e})

def likedevent(request):
    if request.method == "GET":
        events_id = request.GET['i_id']
        e= Events.objects.get(id = events_id )
        if e.is_liked:
            e.is_liked=False
        else:
            e.is_liked=True
        e.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")
