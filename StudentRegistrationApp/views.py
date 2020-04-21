from django.shortcuts import render
from .models import StudentModel

# Create your views here.
def student_registration_View(request):
    if request.method == 'POST':
        roll = request.POST.get('roll', '')
        sname = request.POST.get('sname', '')
        mobile = request.POST.get('mobile', '')
        fee = request.POST.get('fee', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        course = request.POST.get('course', '')
        institute = request.POST.get('institute', '')
        data = StudentModel(
            Roll_Number=roll,
            Student_Name=sname,
            Mobile=mobile,
            Fee=fee,
            Email=email,
            Address=address,
            DateOfBirth=dob,
            Gender=gender,
            Course=course,
            InstituteName=institute,
        )
        data.save()
        return render(request, 'StudentRegForm.html')
    return render(request, 'StudentRegForm.html')
