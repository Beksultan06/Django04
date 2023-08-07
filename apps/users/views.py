from django.shortcuts import render
from apps.users.forms import UserReqistrationForm
from django.views import View

# def reqister(request):
#     if request.method == "Post":
#         user_form = UserReqistrationFrom(request.Post)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.clean_password2())
#             new_user.save()
#             return render(request, "registration/register_done.html", {"user": new_user})

#     else:
#         user_from = UserReqistrationFrom()
#     return render(request, "registration/register.html", {"form": user_form})



class RegisterView(View):
    def get(self, request):
        user_form = UserReqistrationForm()
        return render(request, "registration/register.html", {"form": user_form})

    def post(self, request):
        user_form = UserReqistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data.get('password2'))
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
        return render(request, "registration/register.html", {"form": user_form})
