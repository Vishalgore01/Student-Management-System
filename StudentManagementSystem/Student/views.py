from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from Student.models import Student_Details, Admission_Details, Marks, Feedback

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def view_hello(request):
    return render(request, 'hello.html', {})

def signupPage(request):
    if request.method=='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(pass1!=pass2):
            return HttpResponse('Password Not Matched')
        else:
            my_user = User.objects.create_user(name,email,pass1)
            my_user.save()
            
            return redirect('login')
    
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password Incorrect")
        
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@csrf_exempt
def Homepage(request):
    return render(request,'home.html')

@login_required(login_url='login')
def student(request):
    try:
        if request.method == 'POST':
            Student_Name = request.POST.get('Student_Name')
            Reg_no = request.POST.get('Reg_no')
            Address = request.POST.get('Address')
            Taluka = request.POST.get('Taluka')
            District = request.POST.get('District')
            State = request.POST.get('State')
            pincode = request.POST.get('pincode')
            info=Student_Details(Student_Name=Student_Name,Reg_no=Reg_no,Address=Address,Taluka=Taluka,District=District,State=State,pincode=pincode)
            info.save()
            
            return redirect('studentinfo.html')
        
    except:
        return HttpResponse("You are Not Registered!!!")
    
    return render(request, "studentinfo.html")


@login_required(login_url='login')
def admission(request):
    
    if request.method == 'POST':
        Reg_no = request.POST.get('Reg_no')
        S_name = request.POST.get('S_name')
        Class_name = request.POST.get('Class_name')
        Branch = request.POST.get('Branch')
        year = request.POST.get('year')
        Date_of_Admission = request.POST.get('Date_of_Admission')
        Semester = request.POST.get('Semester')
        
        info2=Admission_Details(Reg_no=Student_Details.objects.get(Reg_no=Reg_no),S_name=S_name,Class_name=Class_name,Branch=Branch,year=year,Date_of_Admission=Date_of_Admission,Semester=Semester)
        info2.save()
        
    return render(request, "admissioninfo.html")  


@login_required(login_url='login')
def marks(request):
    
    dict={}
    if request.method == "POST":
        Reg_no = request.POST.get('Reg_no')
        Subject = request.POST.get('Subject')
        marks = request.POST.get('marks')
        Semester = request.POST.get('Semester')
        year = request.POST.get('year')
        info3=Marks(Reg_no=Student_Details.objects.filter(Reg_no=Reg_no).first(),Subject=Subject,marks=marks,Semester=Semester,year=year)
        info3.save()
        
    
    return render(request,"marksinfo.html")


@login_required(login_url='login')
def feedback(request):
    context={}
    adm = Student_Details.objects.all()
    m = Marks.objects.all()
    a = Admission_Details.objects.all()
    context = {
        'data': adm,
        'mdata': m,
        'adata': a
    }
    return render(request, "feedback.html",context)

          
