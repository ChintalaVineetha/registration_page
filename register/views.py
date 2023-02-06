from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from django.contrib import messages

mydb = mysql.connector.connect(
    host='localhost', user='root', password='Cos90is0!', port='3306', database='userdetails')


def registration(request):
    return render(request, 'register.html')


def Home(request):
    return render(request, 'Home.html')


posts = []


def disp(request):
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
    print("hobbies", hobbies)
    hobbies1 = ','.join(map(str, hobbies))
    print("hobbies1", hobbies1)
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
list4=[]

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
    cursor.execute("select id from details")
    idlist = cursor.fetchall()
    print("idlist",idlist)
    print("desired  output in list ", output)
    print(request.POST.get('initial'))

    print("type of data",type(request.POST.get('initial')))
    if type(request.POST.get('initial')) == str:
        print(request.POST.get('initial'))
        print("stringtype")
        for i in output:
            if i[0] == request.POST.get('initial'):
                print("matched value", request.POST.get('initial'))
                detail.clear()
                print("cleared detail", detail)
                detail.update(
                    {'fname': i[0], 'lname': i[1], 'number': i[2], 'mail': i[3], 'radiooption': i[4], 'clgname': i[5],
                     'passedout': i[6], 'univ': i[7], 'percent': i[8], 'hobbies': i[9],'id':i[10]})
                print("detail", detail)
                list3.clear()
                list3.append(detail)
                print("detailsinlist", list3)
                context1 = {'list3': list3}
                return render(request, 'verify.html', context1)
            else:
                for i in output:
                    print("i[10]", i[10])
                    if i[10] ==      request.POST.get('initial'):
                        detail.clear()
                        print("id filtering", detail)
                        detail.update(
                            {'fname': i[0], 'lname': i[1], 'number': i[2], 'mail': i[3], 'radiooption': i[4],
                             'clgname': i[5],
                             'passedout': i[6], 'univ': i[7], 'percent': i[8], 'hobbies': i[9]})
                        print("detail", detail)
                        list4.clear()
                        list4.append(detail)
                        print("detailsinlist", list4)
                        context2 = {'list3': list4}
                        return render(request, 'verify.html', context2)
    else:
        return render(request, 'unknownuser.html')




