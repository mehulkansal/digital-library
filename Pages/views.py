from django.shortcuts import render,redirect
from Book.models import Book,Issue
from django.contrib.auth.models import User 
import datetime 
# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"home.html")
def about_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"about.html")

def contact_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"contact.html")

def signin_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"signin.html")
    
def signup_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"signup.html")

def welcome_view(request,*args,**kwargs):
    print(request.user)
    books=Book.objects.all()
    print(books)
    try:
        username=request.user.username
        user = User.objects.get(username=username)
        issue = Issue.objects.filter(user=user)
        print(issue)
        today = datetime.date.today()
        today = str(today)
        year = today[0:4]
        month = today[5:7]
        date = today[8:]
        today = str(date) + str('-') + str(month) + str('-') + str(year)
        print(issue[0].returndate, today)

        d={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        latedays = 0
        remaining = 0
        if issue[0].returndate[6:] == today[6:]:
            if issue[0].returndate[3:5] == today[3:5]:
                if int(today[0:2]) - int(issue[0].returndate[0:2]) > 0:
                    latedays = int(today[0:2]) - int(issue[0].returndate[0:2]) 
                else:
                    latedays = 0
                    remaining = int(issue[0].returndate[0:2]) - int(today[0:2])  
            else:
                if int(today[0:2]) - int(issue[0].returndate[0:2]) > 0:
                    latemonth = int(today[3:5]) - int(issue[0].returndate[3:5]) 
                    latedays = int(today[0:2])+d[int(issue[0].returndate[3:5])]*latemonth - int(issue[0].returndate[0:2]) 
                else:
                    latedays = -(int(today[0:2]) - int(issue[0].returndate[0:2]))
        else:
            pass
        print(latedays)
        issue2=Issue.objects.get(user=user)
        
        print(issue2)
        issue2.fine=int(latedays)*15
        issue2.save()
        return render(request,"welcome.html",{'books':books, 'latedays':-(latedays-15), 'issuebooks':issue})

    except Exception as e:
        print(e)

    
    return render(request,"welcome.html",{'books':books})

def select_view(request,*args,**kwargs):
    if request.method=="POST":

        try:
            username=request.user.username
            user=User.objects.get(username=username)
            bookname=request.POST['bookname']
            print(bookname)
            book=Book.objects.get(Name=bookname)
            if book.Status==True:
                newissue=Issue.objects.create(user=user,book=book)
                today = datetime.date.today()
                today = str(today)
                d={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                year = today[0:4]
                month = today[5:7]
                date = today[8:]
                if int(date) + 15 >= 30:
                    if int(month) != 12:
                        month = int(month) + 1
                        monthdays = d[int(month)]
                        date = int(date)+15-monthdays
                    else:
                        year += int(year)+1
                        month = 1
                        date = int(date)+15-31
                else:
                    date = int(date)+15
                today = str(date) + str('-') + str(month) + str('-') + str(year)
                newissue.returndate = today
                
                newissue.save()
                book.Quantity-=1
                if book.Quantity==0:
                    book.Status=False
                book.save()
                print("book issued")
            else:
                print("book not available")
        except Exception as e:
            print(e,"error")
    return redirect('welcome')

def bookreturn(request):
    if request.method=="POST":
        print('postmethod')
        try:
            username = request.user.username
            user = User.objects.get(username=username)
            bookname = request.POST['bookname']
            print(bookname)
            book = Book.objects.get(Name=bookname)
            print(book)
            try:
	            issue = Issue.objects.get(user=user)
	            issue.delete()
	            if book.Quantity == 0:
		            book.Status = True
	            book.Quantity += 1
                
            except:
	            print('no book is issued with this id')
            book.save()
           
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('welcome')  
            
