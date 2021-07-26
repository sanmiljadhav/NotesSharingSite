from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date

# Create your views here.
def index(requests):
    return render(requests,'index.html')

def about(requests):
    return render(requests,'about.html')

def contact(requests):
    return render(requests,'contact.html')

def userlogin(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST['emailid']
        #Because User Table madhe username chya jagi email aahe
        pwd = request.POST['pwd']
        user = authenticate(username = uname,password = pwd)
        try:
            if user:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}

        

    
        
    return render(request,'userlogin.html',d)



def login_admin(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST['uname']
        pasw = request.POST['pwd']
        user = authenticate(username = uname,password = pasw)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'admin_login.html',d)

def register(request):
    error = ""
    if request.method == 'POST':
        print("hello sssss")
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        contact = request.POST['contact']
        email = request.POST['emailid']
        password = request.POST['password']
        branch = request.POST['branch']
        role = request.POST['role']
        print(role)
        try:
            myuser = User.objects.create_user(email,'',password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            #user save hot aahe user table madhe and contact,branch,role is saved in Register Table
            print('yes data saved to user model')
            regis = Register.objects.create(user=myuser,contact = contact,branch = branch,role = role)
            regis.save()
            print('yes data saved to register model')
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'register.html',d)

def admin_page(request):
    if not request.user.is_staff:
        return redirect('/admin_login')
    pending=Notes.objects.filter(status = 'Pending').count()
    accepted = Notes.objects.filter(status = 'Accepted').count()
    rejected = Notes.objects.filter(status = 'Rejected').count()
    allnotes = Notes.objects.all().count()
    d = {'pending':pending,'accepted':accepted,'rejected':rejected,'allnotes':allnotes}
    return render(request,'admin_page.html',d)

def logout_admin(request):
    logout(request)
    return redirect('notes-index')

def userprofile(request):
    if not request.user.is_authenticated:   #matlab agar login nahi kiya hai
        return redirect('/login')
    #kuch data of logged in User hume User model se milega
    user = User.objects.get(id = request.user.id)
    print(user)

    #kuch data of logged in User Hume Register model se milega
    data = Register.objects.get(user = user)
    print(data)
    d = {'data':data,'user':user}



    return render(request,'userprofile.html',d)


def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    error = ""
    if request.method == "POST":
        oldpass = request.POST['oldpassword']
        newpass = request.POST['newpassword']
        confirmpass = request.POST['confirmpassword']
        if newpass == confirmpass:
            u = User.objects.get(username__exact = request.user.username)
            print(u)
            u.set_password(newpass)
            u.save()
            error = "no"
        else:
            error="yes"
    d = {'error':error}


    return render(request,'changepassword.html',d)

def editprofile(request):
    if not request.user.is_authenticated:   #matlab agar login nahi kiya hai
        return redirect('/login')
    #kuch data of logged in User hume User model se milega
    user = User.objects.get(id = request.user.id)
    print(user)

    #kuch data of logged in User Hume Register model se milega
    data = Register.objects.get(user = user)
    print(data)

    #for update of the data
    error = False
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        contact = request.POST['contact']
        email = request.POST['emailid']
        branch = request.POST['branch']
        user.first_name = fname
        user.last_name = lname
        user.username = email
        print(user.username)
        
        data.contact = contact
        data.branch = branch
        user.save()
        data.save()
        error = True


    d = {'data':data,'user':user,'error':error}

    return render(request,'editprofile.html',d)

def uploadnotes(request):
    if not request.user.is_authenticated:   #matlab agar login nahi kiya hai
        return redirect('/login')
    error = ""
    if request.method == 'POST':
        branch = request.POST['branch']
        subject = request.POST['subject']
        notesfile = request.FILES['notesfile']
        filetype = request.POST['filetype']
        print("sanmil")
        print(filetype)
        print("sanmil")
        desc = request.POST['desc']
        u = User.objects.filter(username = request.user.username).first()
        try:
           Notes.objects.create(user = u,uploadingdate = date.today(),branch = branch,subject = subject,
           notesfile = notesfile,filetype = filetype,desc = desc,status = 'Pending')
           error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'uploadnotes.html',d)


def viewmynotes(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = User.objects.get(id = request.user.id)
    notes = Notes.objects.filter(user = user)
    print(notes)
    

    d = {'notes':notes}
    

    return render(request,'viewmynotes.html',d)

def deletemynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('/login')
    notes = Notes.objects.get(id = pid)
    notes.delete()
    return redirect('/viewmynotes')

def admin_viewusers(request):
    if not request.user.is_authenticated:
        return redirect('/login_admin')
    users = Register.objects.all()
    d = {'users':users}
    return render(request,'admin_viewusers.html',d)

def admin_delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('/login_admin')
    user = User.objects.get(id = pid)
    user.delete()
    return redirect('/admin_viewusers')

def pending_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login_admin')
    
    notes = Notes.objects.filter(status = "Pending")
    d = {'notes':notes}
    return render(request,'pending_notes.html',d)


def assign_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('/login_admin')
    notes = Notes.objects.get(id = pid)
    error = ""
    if request.method == 'POST':
        status = request.POST['status']
        try:
            notes.status = status
            notes.save()
            error = "no"
        except:
            error = "yes"
    
    d = {'notes':notes,'error':error}

    return render(request,'assign_status.html',d)

def accepted_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login_admin')
    notes = Notes.objects.filter(status = 'Accepted')
    d = {'notes':notes}
    return render(request,'accepted_notes.html',d)

def rejected_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login_admin')
    notes = Notes.objects.filter(status = 'Rejected')
    d = {'notes':notes}
    return render(request,'rejected_notes.html',d)


def all_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login_admin')
    notes = Notes.objects.all()
    d = {'notes':notes}
    return render(request,'all_notes.html',d)

def admin_delete_notes(request,pid):
    if not request.user.is_authenticated:
        return redirect('/login')
    notes = Notes.objects.get(id = pid)
    notes.delete()
    return redirect('/viewmynotes')


def user_all_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    notes = Notes.objects.filter(status = 'Accepted')
    d = {'notes':notes}
    return render(request,'user_all_notes.html',d)

