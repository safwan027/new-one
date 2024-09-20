from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from . models import book,comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def admin_home(request):
    data = book.objects.all() 
    return render(request,'admin_home.html',{"data":data})

@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        temp_title = request.POST.get("title")
        temp_author = request.POST.get("author")
        temp_price = request.POST.get('price')
        temp_category = request.POST.get('type')
        temp_image = request.FILES.get('image')
        temp_description = request.POST.get('description')
        book.objects.create(
            title = temp_title,
            author = temp_author,
            price = temp_price,
            category = temp_category,
            image = temp_image,
            description = temp_description,
        )
        return redirect('adminhome')
    return render(request,'add_book.html')

@login_required(login_url='login')
def edit_book(request,id):
    data = book.objects.get(id=id)
    if request.method == 'POST':
        temp_title = request.POST.get("title")
        temp_author = request.POST.get("author")
        temp_price = request.POST.get('price')
        temp_description = request.POST.get('description')
        temp_category = request.POST.get('category')
        data.title = temp_title
        data.author = temp_author
        data.price = temp_price
        data.description = temp_description
        data.category = temp_category
        data.save()
        return redirect('adminhome')
    return render(request,'edit_book.html',{"data":data})  

@login_required(login_url='login')
def delete_book(request,id):
    data = book.objects.filter(id=id)
    data.delete()
    return redirect('adminhome')



@login_required(login_url='login')
def user_home(request):
    data = book.objects.all()
    if request.method == 'POST':
        temp_title = request.POST.get('title1')
        temp_category = request.POST.get('type')
        if  temp_title:
            data = book.objects.filter(title=temp_title)
        if temp_category:
            data = book.objects.filter(category=temp_category)
    return render(request,'user_home.html',{'data':data})

@login_required(login_url='login')
def book_details(request,id):
    current_user = request.user
    data = book.objects.get(id=id)
    comment_data = comment.objects.filter(fk_book=id)
    if request.method == 'POST':
        temp_comment = request.POST.get("comment")
        comment.objects.create(
            fk_user = current_user,
            fk_book = data,
            comment = temp_comment,
        )
        return redirect('bookdetails',id=data.id)
    return render(request,"book_details.html",{"data":data,"comment_data":comment_data})


def edit_comment(request,id):
    data = comment.objects.filter(id=id)
    if request.method == 'POST':
        temp_comment = request.POST.get("comment")
        data.comment = temp_comment
        data.save()
        return redirect('bookdetails',id=data.fk_book.id)
    return render(request,"edit_comment.html",{"data":data})

def delete_comment(request,id):
    data = comment.objects.filter(id=id)
    data.delete()
    return redirect('bookdetails',id=data.fk_book.id)


@login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        temp_usrname = request.POST.get("username")
        temp_pass = request.POST.get("password")
        temp_confrm_pass = request.POST.get("cnfrm_pass")
        if temp_pass == temp_confrm_pass:
            User.objects.create_user(
                username = temp_usrname,
                password = temp_pass,
            )
            return redirect('login')
        return HttpResponse('not match')
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwrd = request.POST.get("password")
        user = authenticate(username = uname,password = pwrd)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminhome')
            return redirect ('userhome')
        return HttpResponse('Invalid Credentials')
    return render(request,'login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')


