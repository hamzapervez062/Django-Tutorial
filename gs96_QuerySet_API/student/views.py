from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Student , Teacher
from django.db.models import Q, Max, Min, Avg, Sum, Count

# Create your views here.


def home(request):  
    # students = Student.objects.all() 
    # students = Student.objects.order_by("-name")   
    # students = Student.objects.order_by("name").first() 
    # students = Student.objects.order_by("id").reverse()[:2]  
    # students = Student.objects.values('id','name') #give data in dict
    # students = Student.objects.values_list('id', 'name', 'roll', named=True) #give data in tubles
    # students = Student.objects.using('default') #
    # students = Student.objects.dates('pass_date', 'month')

    ######UNION######## 
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # students = qs2.union(qs1)
    # students = qs1.intersection(qs2)
    # students = qs1.difference(qs2)


    ########### AND OR Operator ###########
    # fetch data where id=5 and roll=1

    # students = Student.objects.filter(id=5) & Student.objects.filter(roll=1)
    # students = Student.objects.filter(id=5, roll =1)
    # students = Student.objects.filter(id=5) | Student.objects.filter(roll=33)

    ###########  ###########

    # students = Student.objects.create(name = 'Ali', roll = 182, city= "d", marks=33, pass_date = '2020-3-3' )

    #get if data avialable , otherwise create it
    # students = Student.objects.get_or_create(name = 'Ali hamza', roll = 192, city= "d", marks=33, pass_date = '2020-3-3' )

    # students = Student.objects.filter(id=2).update(name='Lariab', marks = 999)
    # students = Student.objects.filter(marks=33).update(city='Khusi')
    # students = Student.objects.update_or_create(name='Lariab', marks = 99 , defaults={'name': 'Maham'})


    ########### Bulk create ###########
    # objs = [
    #     Student(name = 'Ahamza', roll = 92, city= "dd", marks=343, pass_date = '2020-3-3'),
    #     Student(name = 'Ahamzaali', roll = 822, city= "ddd", marks=903, pass_date = '2020-4-3')
    # ]
    # students = Student.objects.bulk_create(objs)

    #update bulk
    # dat = Student.objects.all()
    # for s in dat:
    #     s.city = 'KH'
    # students = Student.objects.bulk_update(dat, ['city'])
    # students = Student.objects.filter(marks=33).delete()

    ########### Fields Lookups(where clause)###########

    # students = Student.objects.filter(marks= 111) #queryset
    # student = Student.objects.get(marks= 111) #object 

    # students = Student.objects.filter(name__exact= 'saira') 
    # students = Student.objects.filter(name__iexact= 'Saira') 
    # students = Student.objects.filter(name__contains= 's') 
    # students = Student.objects.filter(id__in = [1,2,5]) 
    # students = Student.objects.filter(marks__gte = 300) 
    # students = Student.objects.filter(marks__lte = 300) 
    # students = Student.objects.filter(name__startswith = 's') 
    # students = Student.objects.filter(name__istartswith = 'S') 
    # students = Student.objects.filter(name__endswith = 's') 
    # students = Student.objects.filter(name__iendswith = 'S')
    # students = Student.objects.filter(name__range = ('saira', 'saira'))  # between 
    # students = Student.objects.filter(name__isnull = True)    # is null

    ########### Q object ###########
    # students = Student.objects.filter(Q(id=1) & Q(roll=12)) #AND
    # students = Student.objects.filter(Q(id=1) | Q(roll=12)) #OR
    # students = Student.objects.filter(~Q(id=1))

    ########### Aggregate ###########
    # student = Student.objects.all() 
    # students = student.aggregate(Max('marks'))

    ####### Limiting QuerySet ########
    # students = Student.objects.all()[:2] #limit
    # students = Student.objects.all()[2:4] #start, end
    # students = Student.objects.all()[2:4:2] #start, end, step	



    print("S: ", students)
    # print(Student)
    # print('query', students.query)
    return render(request, 'student/home.html', {'students': students})