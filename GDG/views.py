from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import  logout,login
from django.http import *
from .models import *
import random
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def member(request):
    return render(request,'index2.html')

def login2(request):
    return render(request,"login2.html")

def gallery2(request):
    return render(request,"gallery2.html")

def perks(request):
    return render(request,"perks.html")

def home(request):
    return render(request,"index2.html")

def a(request):
    return render(request,"a.html")

def contact(request):
    return render(request,"contact.html")

def registration(request):
    return render(request,"registration.html")

def after_login(request):
    return render(request,"after_login.html")

def quiz_instruction(request):
    return render(request,"quiz_instruction.html")

def about(request):
    return render(request,"about.html")

def user_logout(request):
    del request.session['email']
    return redirect("home") 

def registration_adding(request):
    if request.method == "POST":            
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')

        if password != cpassword:
            messages.error(request, "Passwords do not match!")
            return redirect("registration")  

        elif Registration.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("registration")  

        elif Registration.objects.filter(contact=contact).exists():
            messages.error(request, "Phone number already exists!")
            return redirect("registration") 

        else:
            user = Registration(name=name, contact=contact, email=email, password=password)
            user.save()
            messages.success(request, "Registration successful!")
            # return redirect("home")  

    return redirect("registration")  

            
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        request.session['email'] = email

        if Registration.objects.filter(email=email).exists():
            member = Registration.objects.get(email=email)
     

            if member.password == password:
               return redirect("after_login")

            else:
                 messages.error(request, "Invalid Password")
        else:
             messages.error(request, "Email does not exists ")

    return render(request, 'login2.html')
# def user_login(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         request.session['email'] = email

#         if Registration.objects.filter(email=email).exists():
#             member = Registration.objects.get(email=email)
     

#             if member.password == password:
#                return redirect("after_login")

#             else:
#                  messages.error(request, "Invalid Password")
#         else:
#              messages.error(request, "Email does not exists ")

#     return render(request, 'login2.html')


def kaggle(request):
    email = request.session.get('email')
    data=Registration.objects.get(email=email)
    if request.method == 'POST':
        email = request.session.get('email')
        data=Registration.objects.get(email=email)
        score = 0
        for question in kaggle_questions.objects.all():
                    selected_answer = request.POST.get('question' + str(question.id))
                    print("the selected answer is",selected_answer)
                    if selected_answer == question.answer:
                        score += 1
                    data.kaggle_result=score
                    data.save()
                    print("score is",data.kaggle_result)
    context={}
    questions =list(kaggle_questions.objects.all())
    print("the questions arre",questions)
    random.shuffle(questions)
    context = {
        'questions': questions
        }
    return render(request, 'quiz_template.html', context)
    
def quiz_view(request, quiz_name):
    email = request.session.get('email')
    data = Registration.objects.get(email=email)
    try:
        QuizModel = apps.get_model('GDG', f"{quiz_name}_questions")
    except LookupError:
        return render(request, 'error.html', {'message': 'Quiz not found'})

    if request.method == 'POST':
        score = 0
        for question in QuizModel.objects.all():
            selected_answer = request.POST.get(f'question{question.id}')
            if selected_answer == question.answer:
                score += 1
        
        setattr(data, f"{quiz_name}_result", score)  
        data.save()
        return redirect("after_login")
    
    questions = list(QuizModel.objects.all())
    random.shuffle(questions)

    context = {
        'questions': questions,
        'quiz_name': quiz_name,
    }
    return render(request, 'quiz_template.html', context)

def view_score(request):
    email=request.session['email']
    task=Registration.objects.get(email=email)
    context={
        'task':task,
    }
    return render(request,'view_score.html',context)
from django.shortcuts import render, redirect
from .models import Registration

def navbar2(request):
    # Check if the email exists in the session
    email = request.session.get('email')  # Use .get() to avoid KeyError

    if email:
        try:
            # Get the user based on email
            task = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
            task = None  # If user is not found, set task to None

        context = {
            'task': task,
        }
        print(task.kaggle_result)
        return render(request, "navbar2.html", context)

    # If email doesn't exist in session, redirect to login or home page
    return redirect('login2')  # or redirect to the home page



from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import io
import os
from django.conf import settings
from django.templatetags.static import static

import os
from django.conf import settings
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont

# def generate_certificate(request, student_name):
#     # Construct the correct absolute path
#     template_path = os.path.join(settings.BASE_DIR, 'GDG', 'static', 'img', 'certificate_template.jpg')

#     # Check if the file exists
#     if not os.path.exists(template_path):
#         return HttpResponse("Certificate template not found.", status=404)

#     # Open the certificate template
#     img = Image.open(template_path)
#     draw = ImageDraw.Draw(img)

#     # Define font properties
#     font_path = os.path.join(settings.BASE_DIR, 'GDG', 'static', 'fonts', 'dejavu-sans.book.ttf')
#     # font_path = os.path.join(settings.BASE_DIR, 'GDG', 'static', 'fonts', 'Arial.ttf')  # Adjust if needed
#     font = ImageFont.truetype(font_path, 60)  # Adjust font size if necessary

#     # Position the student's name
#     name_position = (500, 920)  # Adjust position if needed
#     draw.text(name_position, student_name, fill="black", font=font)

#     # Return as an image response
#     response = HttpResponse(content_type="image/png")
#     img.save(response, "PNG")
#     return response


import os
from django.conf import settings
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont

def certificate_form(request):
    """ Renders the certificate form page """
    return render(request, 'certificate_form.html')
from PIL import Image, ImageDraw, ImageFont
import os
from django.http import HttpResponse
from django.conf import settings
from .models import Registration

def generate_certificate(request):
    email = request.session.get('email')
    member = Registration.objects.get(email=email)
    student_name = member.name
   
        # Path to certificate template
    template_path = os.path.join(settings.BASE_DIR, 'GDG', 'static', 'img', 'certificate_template2.jpg')
    if not os.path.exists(template_path):
        return HttpResponse("Certificate template not found.", status=404)
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    font_path = os.path.join(settings.BASE_DIR, 'GDG', 'static', 'fonts', 'dejavu-sans.book.ttf')
    font = ImageFont.truetype(font_path, 60)
    # Measure the text width using textbbox
    bbox = draw.textbbox((0, 0), student_name, font=font)
    text_width = bbox[2] - bbox[0]
    image_width = img.width
    x_position = (image_width - text_width) // 2
    y_position = 425  # Keep as per your design
    # Draw name on certificate
    draw.text((x_position, y_position), student_name, fill="black", font=font)
    response = HttpResponse(content_type="image/png")
    response['Content-Disposition'] = f'attachment; filename="{student_name}_certificate.png"'
    img.save(response, "PNG")
    return response


# def generate_certificate(request):
#     # Get student's name from the GET request
#     student_name = request.GET.get('student_name', 'Your Name')  # Default value if name is not provided

#     # Path to certificate template
#     template_path = os.path.join(settings.BASE_DIR, 'GDG', 'static', 'img', 'certificate_template.jpg')

#     if not os.path.exists(template_path):
#         return HttpResponse("Certificate template not found.", status=404)

#     # Open and edit the template
#     img = Image.open(template_path)
#     draw = ImageDraw.Draw(img)

#     # Load font
#     font_path = os.path.join(settings.BASE_DIR, 'GDG', 'static', 'fonts', 'dejavu-sans.book.ttf')
#     font = ImageFont.truetype(font_path, 60)

#     # Position student's name
#     name_position = (600, 920)
#     draw.text(name_position, student_name, fill="black", font=font)

#     # Return as a downloadable file
#     response = HttpResponse(content_type="image/png")
#     response['Content-Disposition'] = f'attachment; filename="{student_name}_certificate.png"'
#     img.save(response, "PNG")

#     return response

from django.core.mail import send_mail


from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        recipient_list = ['ayyappaswamypragada@gmail.com']  # Must be a list

        # Plain text fallback message
        text_message = f"""
        Name: {name}
        Phone: {phone}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        # HTML-styled email message
        html_message = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f8f9fa; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background: white; padding: 20px; 
                        border-radius: 8px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                <h2 style="color: #007bff; text-align: center;">New Contact Form Submission</h2>
                <hr style="border: 1px solid #ddd;">
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Subject:</strong> {subject}</p>
                <p><strong>Message:</strong></p>
                <p style="background: #f1f1f1; padding: 10px; border-radius: 5px;">{message}</p>
                <hr style="border: 1px solid #ddd;">
               
            </div>
        </body>
        </html>
        """

        send_mail(
            subject,
            text_message,  # Fallback plain text message
            'from@example.com',  # Change this to your sender email
            recipient_list,
            fail_silently=False,
            html_message=html_message  # Send HTML email
        )

        messages.success(request, "Email sent successfully!")

    return render(request, 'contact.html')


