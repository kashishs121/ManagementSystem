from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .serializers import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.views import ObtainAuthToken
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
# from .forms import UserCreationForm, LoginForm,SignupFormStaff,LoginFormStaff,SignupForm
# from .forms import RegisterForm,LoginForm
# from .models import user
# Create your views here.
# s

# # def register(request):
# #     if request.method == 'GET':
# #         form  = RegisterForm()
# #         context = {'form': form}
# #         return render(request, 'register.html', context)
# #     if request.method == 'POST':
# #         form  = RegisterForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             user = form.cleaned_data.get('username')
# #             messages.success(request, 'Account was created for ' + user)
# #             return render(request,'login.html')
# #         else:
# #             print('Form is not valid')
# #             messages.error(request, 'Error Processing Your Request')
# #             context = {'form': form}
# #             return render(request, 'register.html', context)
# #     return render(request, 'register.html', {})


# # def sign_in(request):
# #     if request.method == 'GET':
# #         form = LoginForm()
# #         return render(request, 'login.html', {'form': form})
# #     if request.method == 'POST':
# #           username = request.POST['username']
# #           password = request.POST['password']
# #           staff_user = request.POST['staff_user']
# #           user = authenticate(username=username, password=password)
# #           if user is not None:
# #               if user.is_active:
# #                   login(request, user)
# #                   if staff_user == True:
# #                       return render(request,'index.html')
# #                   else:
# #                       return render(request,'register.html')        
# #     else:
# #         return render(request,'login.html', {})
    
# # if is_staff_user == True:
# #     return render('dex.htmll')

# # else:
# #     return render('register')

# def register(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         # staff_user = request.POST['staff_user']
#         # submit = request.POST['submit']
#         if password1==password2:
#             if user.objects.filter(username=username).exists():
#                 messages.info(request, 'Username is already taken')
#                 return render(request,'register.html')
#             else:
#                 users = user.objects.create(name=name,username=username, password1=password1, password2=password2,
#                                                  )
#                 users.save()
#                 return redirect('/login/')
#                 # else:
#                 #     return render(request,'index.html')
#         else:
#             messages.info(request, 'Both passwords are not matching')
#             return render(request,'register.html')
            

#     else:
#         return render(request, 'register.html')

# def signup(request):
#     return render(request,'register.html')

# def login(request):
#     if request.method == 'POST':
#         # name = request.POST['name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         # staff_user = request.POST['staff_user']
#         user = authenticate(username=username, password1=password1)
#         if user is not None:
#             if user.is_active:
#                 login(request,user)
#                 # if staff_user==True:
#                 return render(request,'index.html')
#                 # else:
#                 #     return render(request,'register.html')        
#     else:
#         return render(request,'login.html')
    
    



# Create your views here.
def index(request):
    return render(request, 'index.html')

# def user_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def user_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save() 
#             username = form.cleaned_data.get('username') 
#             messages.success(request, f'Account created for {username}!')
#             return redirect('/login/') 
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)    
#                 return redirect('/')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 return redirect('/')
#         else:
#             messages.info(request, 'Try again! username or password is incorrect')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form} )
# def user_logout(request):
#     logout(request)
#     return redirect('login')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save() 
#             username = form.cleaned_data.get('username') 
#             messages.success(request, f'Account created for {username}!')
#             return redirect('/signin/') 
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = LoginFormStaff(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 return render(request,'staff_index.html')
#         else:
#             messages.info(request, 'Try again! username or password is incorrect')
#     else:
#         form = LoginFormStaff()
#     return render(request, 'signin.html', {'form': form} )

# def staff_index(request):
#     return render(request,'staff_index.html')


# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 'success': True,
#                 # 'statusCode': status_code,
#                 'message': 'User successfully registered!',
#                 'user': serializer.data
#             }
#             return Response(response)
#         return Response(serializer.errors)
    
# @api_view(['POST'])
# def user_login(request):
    # if request.method == 'POST':
    #     username = request.data.get('username')
    #     password = request.data.get('password')

    #     user = None

    #     if not user:
    #         user = authenticate(username=username, password=password)

    #     if user:
    #         auth_login(request, user)
    #         token, _ = Token.objects.get_or_create(user=user)
    #         return Response({'token': token.key,'role':user.role}, status=status.HTTP_200_OK)  
    #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    # if request.method == 'POST':
    #     serializer = UserSerializer(data=request.data)
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     if serializer.is_valid():
    #         user = authenticate(username=username, password=password)
    #         serializer.save()
    #         response = {
    #             'success': True,
    #             # 'statusCode': status_code,
    #             'message': 'User successfully login!',
    #             'user': serializer.data,
    #             'authenticatedUser': {
    #                 'email': serializer.data['email'],
    #                 'role': serializer.data['role']
    #             }
            
    #         }
    #         auth_login(request,user)
    #         token, _ = Token.objects.get_or_create(user=user)
    #         return Response({'token': token.key},response)
    #     return Response(serializer.errors)
    

# class AuthUserRegistrationView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:
#             serializer.save()
#             status_code = status.HTTP_201_CREATED

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User successfully registered!',
#                 'user': serializer.data
#             }

#             return Response(response, status=status_code)
        
# class AuthUserLoginView(APIView):
#     # users = User.objects.all()
#     serializer_class = AuthUserLoginSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:
#             status_code = status.HTTP_200_OK

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User logged in successfully',
#                 'access': serializer.data['access'],
#                 'refresh': serializer.data['refresh'],
#                 'authenticatedUser': {
#                     'email': serializer.data['email'],
#                     'role': serializer.data['role']
#                 }
#             }

#             return Response(response, status=status_code)
# # 
# class CustomUserAdmin(UserAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser

# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

# Mixin that allows to create multiple objects from lists.
# s