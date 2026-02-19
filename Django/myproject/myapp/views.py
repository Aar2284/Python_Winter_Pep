from django.shortcuts import redirect, render
from myapp.models import Student


def student_detail(request, student_name):
    context = {
        'student_name': student_name,
    }
    return render(request, 'student_detail.html', context)


def add_student(request):
    return render(request, 'form.html')


def submit_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        branch = request.POST.get('branch')
        image = request.FILES.get('image')

        student = Student(
            name=name,
            email=email,
            age=age,
            branch=branch,
            image=image
        )
        student.save()

        context = {
            'name': name,
            'email': email,
            'age': age,
            'branch': branch,
        }

        return redirect('students_list')

    return redirect('add_student')

from .models import Student

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})
