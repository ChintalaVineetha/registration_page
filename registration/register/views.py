from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from django.contrib import messages

mydb = mysql.connector.connect(
    host='localhost', user='root', password='', port='', database='')


def registration(request):
    detail = {}
    list = []
    detail.update(
        {'fname': '', 'lname': '', 'number': '', 'mail': '', 'radiooption': '', 'clgname': '',
         'passedout': '', 'univ': '', 'percent': '', 'hobbies': ''})
    list.append(detail)
    context1 = {'list': list}
    return render(request, 'register.html', context1)


def Home(request):
    return render(request, 'Home.html')

posts = []

def disp(request):
    print("fnameprint", request.POST.get('FirstName'))
    firstname = request.POST.get('FirstName')
    lastname = request.POST.get('LastName')
    number = request.POST.get('MobileNumber')
    mail = request.POST.get('MailId')
    radiooption = request.POST.get('Gender')
    clgname = request.POST.get('CollegeName')
    passedout = request.POST.get('Passedoutyear')
    univ = request.POST.get('University')
    percent = request.POST.get('Percentage')
    hobbies = request.POST.getlist('game')
    hobbies1 = ','.join(map(str, hobbies))
    posts = [{'firstname1': firstname, 'lastname1': lastname, 'number1': number, 'mail1': mail,
              'radiooption1': radiooption, 'clgname1': clgname, 'passedout1': passedout, 'univ1': univ,
              'percent1': percent,
              'hobbies': hobbies1}]
    context = {'posts': posts}
    list1 = posts[0].values()
    list2 = []
    for i in list1:
        list2.append(i)
    cursor = mydb.cursor()
    cursor.execute(
        "insert INTO details(firstname,lastname,number,mail,gender,clgname,passedout,univ,percent,hobbies) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        list2)
    mydb.commit()
    return render(request, 'extractvalues.html', context)

list3 = []
list4 = []
def verify(request):
    return render(request, 'verify.html')


def viewdetails(request):
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='Cos90is0!', port='3306', database='userdetails')
    cursor = mydb.cursor()
    cursor.execute("select * from details")
    output = cursor.fetchall()
    detail = {}
    for i in output:
        if i[0] == request.POST.get('initial1'):
            detail.clear()
            detail.update(
                {'fname': i[0], 'lname': i[1], 'number': i[2], 'mail': i[3], 'radiooption': i[4], 'clgname': i[5],
                 'passedout': i[6], 'univ': i[7], 'percent': i[8], 'hobbies': i[9]})
            list3.clear()
            list3.append(detail)
            context1 = {'list3': list3}
            return render(request, 'verify.html', context1)
        elif str(i[10]) == request.POST.get('initial2'):
            detail.clear()
            detail.update(
                {'fname': i[0], 'lname': i[1], 'number': i[2], 'mail': i[3], 'radiooption': i[4],
                 'clgname': i[5],
                 'passedout': i[6], 'univ': i[7], 'percent': i[8], 'hobbies': i[9]})
            list3.clear()
            list3.append(detail)
            context2 = {'list3': list3}
            return render(request, 'verify.html', context2)
    else:
        return render(request, 'unknownuser.html')


def edit(request):
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='Cos90is0!', port='3306', database='userdetails')
    cursor = mydb.cursor()
    cursor.execute("select * from details")
    output = cursor.fetchall()
    detail = {}
    list6 = []
    genderlist = []
    hobbieslist = []
    for i in output:
        if i[3] == request.POST.get('mailcorr'):
            detail.clear()
            hobbieslist.append(i[9])
            fullhobbylist = ['cricket', 'Hockey', 'Tv', 'Online Games', 'Browsing']
            hobbies = hobbieslist[0].split(',')
            diffhobbies = list(set(fullhobbylist) - set(hobbies))
            detail.update(
                {'fname': i[0], 'lname': i[1], 'number': i[2], 'mail': i[3], 'radiooption': i[4], 'clgname': i[5],
                 'passedout': i[6], 'univ': i[7], 'percent': i[8], 'hobbies': hobbies, 'hobbies2': diffhobbies})
            list6.clear()
            list6.append(detail)
            context1 = {'list6': list6}
            return render(request, 'register.html', context1)
