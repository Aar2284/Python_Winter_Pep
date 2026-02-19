from django.shortcuts import render

def home1(request):
    return render(request, 'app1.html')

def greet(request, name):
    return render(request, 'hello.html', {'name': name})

def student_view(request, name):
    context = {'student_name': name}
    return render(request, 'student.html', context)
