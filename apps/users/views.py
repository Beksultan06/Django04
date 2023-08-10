from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from apps.users.serializers import UserSerializer, UserDetailSerializer
from rest_framework import generics
from apps.users.models import GeekUser
from apps.users.forms import UserRegistrationForm


class UserListAPIView(generics.ListAPIView):
    queryset = GeekUser.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = GeekUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "id"


# def register(request):

#     if request.method == "POST":
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data["password"])
#             new_user.save()
#             return render(request, "registration/register_done.html", {"user": new_user})
#     else:
#         user_form = UserRegistrationForm()

#     return render(request, "registration/register.html", {"form": user_form})

class UserRegisterView(generic.CreateView):
    template_name = 'registration/register_done.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
        return render(request, "registration/register.html", {"form": user_form})